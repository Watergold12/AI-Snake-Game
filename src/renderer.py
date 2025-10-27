# src/renderer.py
import pygame
from typing import Tuple, List
from .grid import Coord
from .snake import Snake

# Colors (R,G,B)
BG_COLOR = (18, 18, 18)
GRID_COLOR = (40, 40, 40)
SNAKE_COLOR = (0, 180, 150)
SNAKE_HEAD_COLOR = (0, 255, 200)
FOOD_COLOR = (240, 80, 80)
TEXT_COLOR = (230, 230, 230)
OVERLAY_COLOR = (0, 0, 0, 160)

class Renderer:
    def __init__(self, rows: int, cols: int, width: int = 600, height: int = 600, show_grid: bool = False):
        pygame.init()
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("AI Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.big_font = pygame.font.SysFont(None, 48)
        self.show_grid = show_grid
        # compute cell sizes (integer)
        self.cell_w = max(1, width // cols)
        self.cell_h = max(1, height // rows)

    def cell_rect(self, coord: Coord) -> pygame.Rect:
        r, c = coord
        x = c * self.cell_w
        y = r * self.cell_h
        return pygame.Rect(x, y, self.cell_w, self.cell_h)

    def clear(self):
        self.screen.fill(BG_COLOR)

    def draw_grid_lines(self):
        if not self.show_grid:
            return
        for i in range(self.cols + 1):
            x = i * self.cell_w
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, self.height))
        for j in range(self.rows + 1):
            y = j * self.cell_h
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (self.width, y))

    def draw_snake(self, snake: Snake):
        body = snake.get_body_list()
        for i, coord in enumerate(body):
            rect = self.cell_rect(coord)
            color = SNAKE_HEAD_COLOR if i == 0 else SNAKE_COLOR
            pygame.draw.rect(self.screen, color, rect.inflate(-2, -2))  # small padding

    def draw_food(self, food_coord: Tuple[int, int]):
        if food_coord is None:
            return
        rect = self.cell_rect(food_coord)
        # draw circle centered in rect
        cx = rect.x + rect.w // 2
        cy = rect.y + rect.h // 2
        radius = min(rect.w, rect.h) // 3
        pygame.draw.circle(self.screen, FOOD_COLOR, (cx, cy), radius)

    def draw_ui(self, score: int, ai_enabled: bool, paused: bool, game_over: bool):
        # Score
        txt = self.font.render(f"Score: {score}", True, TEXT_COLOR)
        self.screen.blit(txt, (8, 8))
        ai_txt = self.font.render(f"AI: {'ON' if ai_enabled else 'OFF'}", True, TEXT_COLOR)
        self.screen.blit(ai_txt, (8, 30))
        if paused:
            overlay = self.big_font.render("PAUSED - Press P", True, TEXT_COLOR)
            self.screen.blit(overlay, overlay.get_rect(center=(self.width//2, self.height//2)))
        if game_over:
            go = self.big_font.render("GAME OVER - Press R", True, TEXT_COLOR)
            self.screen.blit(go, go.get_rect(center=(self.width//2, self.height//2)))

    def present(self, fps_cap: int = 60):
        pygame.display.flip()
        self.clock.tick(fps_cap)

    def quit(self):
        pygame.quit()
