# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH, 11, 7) == 12
