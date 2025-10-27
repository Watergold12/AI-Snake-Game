# tests/test_snake.py
from src.snake import Snake

def test_move_and_grow_and_contains():
    s = Snake([(2,2), (2,3)])   # head=(2,2), tail=(2,3)
    assert s.head() == (2,2)
    assert s.contains((2,3))
    s.move((1,2), grow=False)  # move up
    # new head (1,2), tail removed -> (2,3) removed
    assert s.head() == (1,2)
    assert not s.contains((2,3))
    assert s.contains((1,2))
    assert len(s) == 2

    # grow
    s.move((0,2), grow=True)
    assert len(s) == 3
    assert s.head() == (0,2)
