# src/snake.py
from collections import deque
from typing import Deque, Iterable, List, Tuple, Set

Coord = Tuple[int, int]

class Snake:
    """
    Head is leftmost element of deque (index 0).
    Keep both deque and set in sync for O(1) membership checks.
    """
    def __init__(self, initial_body: Iterable[Coord]):
        self.body: Deque[Coord] = deque(initial_body)
        self.body_set: Set[Coord] = set(initial_body)
        self._debug_assert_sync()

    def _debug_assert_sync(self):
        assert set(self.body) == self.body_set, "body and body_set out of sync"

    def head(self) -> Coord:
        return self.body[0]

    def tail(self) -> Coord:
        return self.body[-1]

    def contains(self, coord: Coord) -> bool:
        return coord in self.body_set

    def move(self, next_coord: Coord, grow: bool = False):
        # add head
        self.body.appendleft(next_coord)
        self.body_set.add(next_coord)
        if not grow:
            old_tail = self.body.pop()
            self.body_set.remove(old_tail)
        self._debug_assert_sync()

    def get_body_list(self) -> List[Coord]:
        return list(self.body)

    def reset(self, initial_body: Iterable[Coord]):
        self.body = deque(initial_body)
        self.body_set = set(initial_body)
        self._debug_assert_sync()

    def __len__(self) -> int:
        return len(self.body)
