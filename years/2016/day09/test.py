# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two


def sample_path(n: int) -> Path:
    return Path(__file__).parent / f'sample_input{n}.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(sample_path(1)) == 7
    assert part_one(sample_path(2)) == 9
    assert part_one(sample_path(3)) == 11
    assert part_one(sample_path(4)) == 6
    assert part_one(sample_path(5)) == 18


def test_part_two_with_sample_input() -> None:
    assert part_two(sample_path(1)) == 7
    assert part_two(sample_path(5)) == 20
    assert part_two(sample_path(6)) == 241920
    assert part_two(sample_path(7)) == 445
