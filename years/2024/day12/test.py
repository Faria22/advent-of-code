# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

DIR = Path(__file__).parent


def test_part_one_with_sample_input1() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 140


def test_part_one_with_sample_input2() -> None:
    assert part_one(DIR / 'sample_input2.txt') == 772


def test_part_one_with_sample_input3() -> None:
    assert part_one(DIR / 'sample_input3.txt') == 1930


def test_part_two_with_sample_input1() -> None:
    assert part_two(DIR / 'sample_input1.txt') == 80


def test_part_two_with_sample_input2() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 436


def test_part_two_with_sample_input3() -> None:
    assert part_two(DIR / 'sample_input3.txt') == 1206


def test_part_two_with_sample_input4() -> None:
    assert part_two(DIR / 'sample_input4.txt') == 236


def test_part_two_with_sample_input5() -> None:
    assert part_two(DIR / 'sample_input5.txt') == 368
