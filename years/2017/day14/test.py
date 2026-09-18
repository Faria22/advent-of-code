# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import convert_hash_to_binary, part_one, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_convert_hash_to_binary() -> None:
    assert convert_hash_to_binary('a0c2017') == '1010000011000010000000010111'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH) == 8108


def test_part_two_with_sample_input() -> None:
    assert part_two(SAMPLE_PATH) == 1242
