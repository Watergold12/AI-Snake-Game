# src/main.py
import pygame
from typing import Tuple
from .game import Game
from .renderer import Renderer
from .grid import DIRECTIONS

# Config
ROWS = 20
COLS = 20
WIDTH = 600
HEIGHT = 600
TICKS_PER_SEC = 8  # snake moves per second
FPS = 60  # render cap

DIR_MAP = {
    pygame.K_UP: (-1, 0),
    pygame.K_DOWN: (1, 0),
    pygame.K_LEFT: (0, -1),
    pygame.K_RIGHT: (0, 1),
}

def main():
    game = Game(rows=ROWS, cols=COLS)
    renderer = Renderer(ROWS, COLS, WIDTH, HEIGHT, show_grid=False)
    paused = False

    # timing for fixed ticks
    clock = renderer.clock
    tick_interval_ms = 1000 // TICKS_PER_SEC
    acc = 0  # accumulator milliseconds

    running = True
    last_input_dir: Tuple[int, int] = game.current_direction

    while running:
        dt = clock.tick(FPS)  # ms since last frame, also caps FPS
        acc += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_r:
                    game.reset()
                    paused = False
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                elif event.key in DIR_MAP:
                    last_input_dir = DIR_MAP[event.key]
                elif event.key == pygame.K_a:
                    # toggle AI mode
                    game.ai_enabled = not game.ai_enabled

        # process ticks
        while acc >= tick_interval_ms:
            acc -= tick_interval_ms
            if not paused and not game.game_over:
                if game.ai_enabled:
                    game.step_ai()
                else:
                    game.step_manual(last_input_dir)

        # render
        renderer.clear()
        renderer.draw_grid_lines()
        renderer.draw_food(game.food)
        renderer.draw_snake(game.snake)
        renderer.draw_ui(game.score, game.ai_enabled, paused, game.game_over)
        renderer.present(FPS)

    renderer.quit()

if __name__ == "__main__":
    main()
