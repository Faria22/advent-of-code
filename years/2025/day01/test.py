# ruff: noqa: PLR2004

from solution import INITIAL_DIAL_VALUE, move_dial_part_one, move_dial_part_two


def test_move_dial_one() -> None:
    assert move_dial_part_one(INITIAL_DIAL_VALUE, 10) == 60
    assert move_dial_part_one(INITIAL_DIAL_VALUE, -10) == 40
    assert move_dial_part_one(INITIAL_DIAL_VALUE, 60) == 10
    assert move_dial_part_one(INITIAL_DIAL_VALUE, -60) == 90
    assert move_dial_part_one(INITIAL_DIAL_VALUE, 160) == 10
    assert move_dial_part_one(INITIAL_DIAL_VALUE, -160) == 90
    assert move_dial_part_one(INITIAL_DIAL_VALUE, 50) == 0
    assert move_dial_part_one(INITIAL_DIAL_VALUE, -50) == 0


def test_move_dial_two() -> None:
    assert move_dial_part_two(INITIAL_DIAL_VALUE, 10) == (60, 0)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, -10) == (40, 0)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, 60) == (10, 1)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, -60) == (90, 1)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, -50) == (0, 1)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, 50) == (0, 1)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, 200) == (INITIAL_DIAL_VALUE, 2)
    assert move_dial_part_two(INITIAL_DIAL_VALUE, -200) == (INITIAL_DIAL_VALUE, 2)
    assert move_dial_part_two(0, -10) == (90, 0)


def test_move_dial_two_with_example() -> None:
    """Test with the example given in the puzzle"""
    initial = INITIAL_DIAL_VALUE
    movements = [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]
    expected_final_positions = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
    expected_zero_counts = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

    total_zero_count = 0
    for movement, e_f, e_z in zip(movements, expected_final_positions, expected_zero_counts, strict=True):
        initial, zero_count = move_dial_part_two(initial, movement)
        total_zero_count += zero_count

        assert (initial, zero_count) == (e_f, e_z)

    assert total_zero_count == sum(expected_zero_counts)
