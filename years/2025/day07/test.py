# ruff: noqa: PLR2004
from pathlib import Path

from solution import parse_data, part_one, part_two


def test_part_one_solution_against_example() -> None:
    input_path = Path(__file__).parent / 'puzzle_input.txt'
    grid = parse_data(input_path.read_text().rstrip('\n'))
    assert part_one(grid) == 21


def test_part_two_solution_against_example() -> None:
    input_path = Path(__file__).parent / 'puzzle_input.txt'
    grid = parse_data(input_path.read_text().rstrip('\n'))
    assert part_two(grid) == 40
