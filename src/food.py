# src/food.py
from typing import Tuple, Optional, Set
import random
from .grid import random_free_cell, Coord

def place_food(rows: int, cols: int, blocked: Optional[Set[Coord]] = None, rng: Optional[random.Random] = None) -> Coord:
    """
    Return a random free cell not in blocked.
    Raises ValueError if no free cell exists.
    """
    return random_free_cell(rows, cols, blocked=blocked, rng=rng)
