# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH, 1) == 2
    assert part_one(SAMPLE_PATH, 2) == 2
    assert part_one(SAMPLE_PATH, 3) == 4
    assert part_one(SAMPLE_PATH, 4) == 6
    assert part_one(SAMPLE_PATH, 5) == 6
