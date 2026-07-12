# ruff: noqa: PLR2004

from solution import is_invalid, parse_range


def test_parse_range() -> None:
    assert parse_range('11-22') == range(11, 23)


def test_is_invalid() -> None:
    assert is_invalid(55)
    assert is_invalid(1212)
    assert not is_invalid(1234)
    assert is_invalid(123123)
