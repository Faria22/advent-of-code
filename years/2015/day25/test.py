# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import get_idx_for_row_col, part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_get_idx_for_row_col() -> None:
    assert get_idx_for_row_col(1, 1) == 1
    assert get_idx_for_row_col(2, 1) == 2
    assert get_idx_for_row_col(3, 1) == 4
    assert get_idx_for_row_col(4, 1) == 7
    assert get_idx_for_row_col(1, 2) == 3
    assert get_idx_for_row_col(1, 3) == 6
    assert get_idx_for_row_col(1, 4) == 10
    assert get_idx_for_row_col(1, 5) == 15
    assert get_idx_for_row_col(3, 3) == 13
    assert get_idx_for_row_col(4, 3) == 18


def test_part_one() -> None:
    assert part_one(1, 1) == 20151125
    assert part_one(2, 1) == 31916031
    assert part_one(3, 1) == 16080970
    assert part_one(1, 3) == 17289845
    assert part_one(3, 3) == 1601130
