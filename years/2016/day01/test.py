# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 12


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 4
