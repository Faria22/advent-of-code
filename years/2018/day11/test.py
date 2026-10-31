# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two, power_level

DIR = Path(__file__).parent


def test_power_level() -> None:
    assert power_level(3, 5, 8) == 4
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == '33,45'
    assert part_one(DIR / 'sample_input2.txt') == '21,61'


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input1.txt') == '90,269,16'
    assert part_two(DIR / 'sample_input2.txt') == '232,251,12'
