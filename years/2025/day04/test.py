# ruff: noqa: PLR2004
import numpy as np
from solution import sum_surrounding


def test_sum_surrounding() -> None:
    grid = np.array([[True, False, True], [True, True, True], [False, False, False]])

    assert sum_surrounding(0, 0, grid) == 2
    assert sum_surrounding(0, 1, grid) == 5
    assert sum_surrounding(0, 2, grid) == 2
    assert sum_surrounding(1, 0, grid) == 2
    assert sum_surrounding(1, 1, grid) == 4
    assert sum_surrounding(1, 2, grid) == 2
    assert sum_surrounding(2, 0, grid) == 2
    assert sum_surrounding(2, 1, grid) == 3
    assert sum_surrounding(2, 2, grid) == 2
