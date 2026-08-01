# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from aoc import Pos
from solution import Warehouse, part_one, part_two

DIR = Path(__file__).parent


def test_part_one_with_sample_input1() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 10092


def test_part_one_with_sample_input2() -> None:
    assert part_one(DIR / 'sample_input2.txt') == 2028


def test_part_two_with_sample_input1() -> None:
    assert part_two(DIR / 'sample_input1.txt') == 9021


def test_gps_coordinate() -> None:
    assert Warehouse.gps_coordinate(Pos(1, 4)) == 104
