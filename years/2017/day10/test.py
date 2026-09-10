# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import get_knot_hash, get_sparse_hash, part_one, part_two, translate_input

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt', 5) == 12


def test_translate_input() -> None:
    assert translate_input(DIR / 'sample_input4.txt') == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]


def test_sparse_hash() -> None:
    elements = [0] * 256
    elements[:16] = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert get_sparse_hash(elements)[0] == 64


def test_knot_hash() -> None:
    assert get_knot_hash([64, 7, 255]) == '4007ff'


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert part_two(DIR / 'sample_input3.txt') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert part_two(DIR / 'sample_input4.txt') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert part_two(DIR / 'sample_input5.txt') == '63960835bcdc130f0b66d7ff4f6a5a8e'
