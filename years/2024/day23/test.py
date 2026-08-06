# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH) == 7


def test_part_two_with_sample_input() -> None:
    assert part_two(SAMPLE_PATH) == 'co,de,ka,ta'
