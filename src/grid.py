# src/grid.py
from typing import Tuple, Generator, Optional, Set, List
import random

Coord = Tuple[int, int]
DIRECTIONS: List[Coord] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(coord: Coord, rows: int, cols: int) -> bool:
    r, c = coord
    return 0 <= r < rows and 0 <= c < cols

def neighbors(coord: Coord, rows: int, cols: int, blocked: Optional[Set[Coord]] = None) -> Generator[Coord, None, None]:
    if blocked is None:
        blocked = set()
    r, c = coord
    for dr, dc in DIRECTIONS:
        n = (r + dr, c + dc)
        if in_bounds(n, rows, cols) and n not in blocked:
            yield n

def all_cells(rows: int, cols: int) -> Generator[Coord, None, None]:
    for r in range(rows):
        for c in range(cols):
            yield (r, c)

def random_free_cell(rows: int, cols: int, blocked: Optional[Set[Coord]] = None, rng: Optional[random.Random] = None) -> Coord:
    if blocked is None:
        blocked = set()
    if rng is None:
        rng = random
    free = [cell for cell in all_cells(rows, cols) if cell not in blocked]
    if not free:
        raise ValueError("no free cells available")
    return rng.choice(free)
