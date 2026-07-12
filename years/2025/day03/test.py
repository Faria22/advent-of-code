# ruff: noqa: PLR2004
from solution import get_best_batteries, parse_bank


def test_get_best_batteries() -> None:
    assert get_best_batteries(parse_bank('987654321111111'), 2) == 98
    assert get_best_batteries(parse_bank('811111111111119'), 2) == 89
    assert get_best_batteries(parse_bank('234234234234278'), 2) == 78
    assert get_best_batteries(parse_bank('818181911112111'), 2) == 92
    assert get_best_batteries(parse_bank('987654321111111'), 3) == 987
    assert get_best_batteries(parse_bank('811111111111119'), 3) == 819
    assert get_best_batteries(parse_bank('234234234234278'), 3) == 478
    assert get_best_batteries(parse_bank('818181911112111'), 3) == 921
    assert get_best_batteries(parse_bank('987654321111111'), 12) == 987654321111
    assert get_best_batteries(parse_bank('811111111111119'), 12) == 811111111119
    assert get_best_batteries(parse_bank('234234234234278'), 12) == 434234234278
    assert get_best_batteries(parse_bank('818181911112111'), 12) == 888911112111
