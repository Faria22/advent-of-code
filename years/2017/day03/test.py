# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(1) == 0
    assert part_one(3) == 2
    assert part_one(9) == 2
    assert part_one(12) == 3
    assert part_one(13) == 4
    assert part_one(17) == 4
    assert part_one(23) == 2
    assert part_one(25) == 4
    assert part_one(26) == 5
    assert part_one(1024) == 31


def test_part_two_with_sample_input() -> None:
    assert part_two(800) == 806
    assert part_two(24) == 25
    assert part_two(3) == 4
    assert part_two(130) == 133
    assert part_two(315) == 330
    assert part_two(300) == 304
    assert part_two(50) == 54
