from pathlib import Path

from solution import Password, part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH, 'abcde') == 'decab'


def test_reversed_rotate_on_letter() -> None:
    p = Password(list('decab'))
    p.rotate_on_letter_reversed('d')
    assert ''.join(p.password) == 'ecabd'

    p = Password(list('ecabd'))
    p.rotate_on_letter_reversed('b')
    assert ''.join(p.password) == 'abdec'
