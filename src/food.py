from typing import Tuple, Optional, Set
import random
from .grid import random_free_cell, Coord

def place_food(rows: int, cols: int, blocked: Optional[Set[Coord]] = None, rng: Optional[random.Random] = None) -> Coord:
    """
    Returns a random free cell that isn't blocked.
    Raises ValueError when all the cells are blocked.
    """
    return random_free_cell(rows, cols, blocked=blocked, rng=rng)
