import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

from src.game import Game
game = Game(rows=10, cols=10)
game.ai_enabled = True

steps = 0
while not game.game_over and steps < 2000:
    game.step_ai()
    steps += 1

print(f"Game over: {game.game_over}, Score: {game.score}, Steps: {steps}")
