from pathlib import Path

from solution import allowed_password, part_one

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 'abcdffaa'
    assert part_one(DIR / 'sample_input2.txt') == 'ghjaabcc'


def test_allowed_password() -> None:
    assert not allowed_password([ord(p) for p in 'hijklmmn'])
    assert not allowed_password([ord(p) for p in 'abbceffg'])
    assert not allowed_password([ord(p) for p in 'abbcegjk'])
