# src/pathfinding.py
import heapq
from typing import Tuple, List, Dict, Optional, Set
from .grid import neighbors, Coord

def manhattan(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from: Dict[Coord, Coord], current: Coord) -> List[Coord]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def find_path(start: Coord, goal: Coord, rows: int, cols: int, blocked: Optional[Set[Coord]] = None, allow_tail: bool = True, tail: Optional[Coord] = None) -> Optional[List[Coord]]:
    """
    A* shortest path from start to goal on 4-neighbor grid.
    `blocked` is a set of blocked cells (e.g., snake body).
    If allow_tail is True and `tail` provided, we treat tail as free (since it may move).
    Returns list of coords from start to goal inclusive, or None if unreachable.
    """
    if blocked is None:
        blocked = set()

    # If allowed to treat tail as free, temporarily remove it from blocked
    if allow_tail and tail is not None and tail in blocked:
        blocked = set(blocked)
        blocked.remove(tail)

    open_heap = []
    heapq.heappush(open_heap, (manhattan(start, goal), 0, start))  # (f, g, coord)
    came_from: Dict[Coord, Coord] = {}
    g_score: Dict[Coord, int] = {start: 0}
    closed: Set[Coord] = set()

    while open_heap:
        f, g, current = heapq.heappop(open_heap)
        if current == goal:
            return reconstruct_path(came_from, current)
        if current in closed:
            continue
        closed.add(current)

        for nb in neighbors(current, rows, cols, blocked):
            tentative_g = g_score[current] + 1
            if nb in g_score and tentative_g >= g_score[nb]:
                continue
            came_from[nb] = current
            g_score[nb] = tentative_g
            heapq.heappush(open_heap, (tentative_g + manhattan(nb, goal), tentative_g, nb))

    return None
