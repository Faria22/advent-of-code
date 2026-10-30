# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 32
    assert part_one(DIR / 'sample_input2.txt') == 8317
    assert part_one(DIR / 'sample_input3.txt') == 146373
    assert part_one(DIR / 'sample_input4.txt') == 2764
    assert part_one(DIR / 'sample_input5.txt') == 54718
    assert part_one(DIR / 'sample_input6.txt') == 37305
