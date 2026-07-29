# ruff: file-ignore[magic-value-comparison]  # ruff: ignore[unused-noqa]

from pathlib import Path

from solution import part_one, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'
data = SAMPLE_PATH.read_text().strip()


def test_part_one_with_sample_input() -> None:
    assert part_one(data) == 18


def test_part_two_with_sample_input() -> None:
    assert part_two(data) == 9
