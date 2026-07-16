# ruff: noqa: PLR2004
from pathlib import Path

from solution import parse_data, part_one, part_two


def test_part_one_with_puzzle_input() -> None:
    input_path = Path(__file__).parent / 'sample_puzzle_input.txt'
    grid = parse_data(input_path.read_text().rstrip('\n'))
    assert part_one(grid, 10) == 40


def test_part_two_with_puzzle_input() -> None:
    input_path = Path(__file__).parent / 'sample_puzzle_input.txt'
    grid = parse_data(input_path.read_text().rstrip('\n'))
    assert part_two(grid) == 25272
