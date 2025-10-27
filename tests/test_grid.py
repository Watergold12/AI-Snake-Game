import pytest
import random
from src.grid import in_bounds, neighbors, all_cells, random_free_cell

def test_neighbors_at_edges_and_center():
    n0 = set(neighbors((0, 0), 3, 3))
    assert n0 == {(1, 0), (0, 1)}

    n1 = set(neighbors((1, 1), 3, 3))
    assert n1 == {(0, 1), (2, 1), (1, 0), (1, 2)}

def test_all_cells_count_and_in_bounds_consistency():
    rows, cols = 4, 5
    cells = list(all_cells(rows, cols))
    assert len(cells) == rows * cols
    for coord in cells:
        assert in_bounds(coord, rows, cols)

def test_random_free_cell_and_no_free_cells():
    rows, cols = 3, 3
    blocked = {(r, c) for r in range(rows) for c in range(cols)}
    blocked.remove((2, 2))
    rng = random.Random(42)
    chosen = random_free_cell(rows, cols, blocked=blocked, rng=rng)
    assert chosen == (2, 2)

    with pytest.raises(ValueError):
        random_free_cell(rows, cols, blocked= {(r, c) for r in range(rows) for c in range(cols)})
