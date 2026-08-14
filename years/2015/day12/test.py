# ruff: file-ignore[magic-value-comparison]  # ruff: ignore[unused-noqa]
from pathlib import Path

from solution import get_sum, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert get_sum('[1,2,3]') == 6
    assert get_sum('{"a":2,"b":4}') == 6

    assert get_sum('[[[3]]]') == 3
    assert get_sum('{"a":{"b":4},"c":-1}') == 3

    assert get_sum('{"a":[-1,1]}') == 0
    assert get_sum('[-1,{"a":1}]') == 0

    assert get_sum('[]') == 0
    assert get_sum('{}') == 0


def test_part_two_with_sample_input() -> None:
    assert part_two(SAMPLE_PATH) == 0
