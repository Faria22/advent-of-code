# ruff: noqa: PLR2004
from pathlib import Path

from solution import part_one, part_two


def test_part_one_with_sample_input() -> None:
    sample_data = (Path(__file__).parent / 'sample_input_1.txt').read_text().rstrip('\n')
    assert part_one(sample_data) == 5


def test_part_two_with_sample_input() -> None:
    sample_data = (Path(__file__).parent / 'sample_input_2.txt').read_text().rstrip('\n')
    assert part_two(sample_data) == 2
