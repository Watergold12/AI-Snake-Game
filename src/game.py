# src/game.py
from typing import Tuple, Optional, Set
from .snake import Snake
from .grid import Coord
from .food import place_food
from .pathfinding import find_path

class Game:
    def __init__(self, rows: int = 20, cols: int = 20, rng=None):
        self.rows = rows
        self.cols = cols
        self.rng = rng
        self.reset()

    def reset(self):
        mid_r = self.rows // 2
        mid_c = self.cols // 2
        # initial snake: length 3 going left
        init = [(mid_r, mid_c), (mid_r, mid_c + 1), (mid_r, mid_c + 2)]
        self.snake = Snake(init)
        self.score = 0
        self.game_over = False
        self.ai_enabled = False
        self.current_direction = (0, -1)  # initial dir: left
        self.path = []
        # spawn food
        self.spawn_food()

    def spawn_food(self):
        blocked = set(self.snake.get_body_list())
        self.food = place_food(self.rows, self.cols, blocked=blocked, rng=self.rng)

    def step_manual(self, next_dir: Tuple[int, int]):
        """Advance one tick using manual direction (tuple dr,dc)."""
        if self.game_over:
            return
        # prevent reversing: new dir cannot be opposite of current if snake length > 1
        if len(self.snake) > 1:
            cur = self.current_direction
            if (next_dir[0] == -cur[0] and next_dir[1] == -cur[1]):
                next_dir = cur
        self.current_direction = next_dir
        head = self.snake.head()
        nr = head[0] + next_dir[0]
        nc = head[1] + next_dir[1]
        next_cell = (nr, nc)
        # check collisions
        if not (0 <= nr < self.rows and 0 <= nc < self.cols):
            self.game_over = True
            return
        # special-case: tail cell is considered free if we're not growing (will vacate)
        tail = self.snake.tail()
        blocked = set(self.snake.get_body_list())
        will_grow = (next_cell == self.food)
        if next_cell in blocked and not (next_cell == tail and not will_grow):
            # collided with body
            self.game_over = True
            return
        # move
        self.snake.move(next_cell, grow=will_grow)
        if will_grow:
            self.score += 1
            try:
                self.spawn_food()
            except ValueError:
                # no free cells -> win / game over
                self.game_over = True

    def step_ai(self):
        """Compute path to food with A* and step along it. If no path, try simple safe move."""
        if self.game_over:
            return
        start = self.snake.head()
        goal = self.food
        blocked = set(self.snake.get_body_list())
        tail = self.snake.tail()
        # ask A* to allow tail as free (common trick)
        path = find_path(start, goal, self.rows, self.cols, blocked=blocked, allow_tail=True, tail=tail)
        if path and len(path) >= 2:
            next_cell = path[1]
            # translate to direction
            dr = next_cell[0] - start[0]
            dc = next_cell[1] - start[1]
            self.step_manual((dr, dc))
            return
        # fallback: try any safe neighbor (order: up, down, left, right)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            candidate = (start[0] + dr, start[1] + dc)
            tail = self.snake.tail()
            blocked = set(self.snake.get_body_list())
            will_grow = (candidate == self.food)
            if 0 <= candidate[0] < self.rows and 0 <= candidate[1] < self.cols:
                if not (candidate in blocked and not (candidate == tail and not will_grow)):
                    self.step_manual((dr, dc))
                    return
        # no safe move -> game over
        self.game_over = True
