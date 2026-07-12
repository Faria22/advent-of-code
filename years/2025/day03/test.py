# ruff: noqa: PLR2004
from solution import best_test, parse_bank


def test_get_best_batteries() -> None:
    assert best_test(parse_bank('987654321111111'), 2) == 98
    assert best_test(parse_bank('811111111111119'), 2) == 89
    assert best_test(parse_bank('234234234234278'), 2) == 78
    assert best_test(parse_bank('818181911112111'), 2) == 92
    assert best_test(parse_bank('987654321111111'), 3) == 987
    assert best_test(parse_bank('811111111111119'), 3) == 819
    assert best_test(parse_bank('234234234234278'), 3) == 478
    assert best_test(parse_bank('818181911112111'), 3) == 921
