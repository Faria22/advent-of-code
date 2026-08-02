# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

DIR = Path(__file__).parent


def test_part_one_with_sample_input1() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 7036


def test_part_one_with_sample_input2() -> None:
    assert part_one(DIR / 'sample_input2.txt') == 11048


def test_part_two_with_sample_input1() -> None:
    assert part_two(DIR / 'sample_input1.txt') == 45


def test_part_two_with_sample_input2() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 64
