# ruff: file-ignore[magic-value-comparison]

from pathlib import Path

from solution import part_one, part_two


def test_part_one_with_sample_input() -> None:
    sample_path = Path(__file__).parent / 'sample_input_1.txt'
    assert part_one(sample_path) == 161


def test_part_two_with_sample_input() -> None:
    sample_path = Path(__file__).parent / 'sample_input_2.txt'
    assert part_two(sample_path) == 48
