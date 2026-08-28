# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 'DDRRRD'
    assert part_one(DIR / 'sample_input2.txt') == 'DDUDRLRRUDRD'
    assert part_one(DIR / 'sample_input3.txt') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input1.txt') == 370
    assert part_two(DIR / 'sample_input2.txt') == 492
    assert part_two(DIR / 'sample_input3.txt') == 830
