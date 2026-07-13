# ruff: noqa: PLR2004

from solution import part_two


def test_part_two_single_range() -> None:
    assert part_two([(10, 21)]) == 11


def test_part_two_disjoint_ranges() -> None:
    assert part_two([(10, 21), (30, 41)]) == 22


def test_part_two_overlapping_ranges() -> None:
    assert part_two([(10, 21), (15, 31)]) == 21


def test_part_two_contained_range_does_not_shrink_outer_range() -> None:
    assert part_two([(1, 11), (2, 6), (8, 13)]) == 12


def test_part_two_handles_unsorted_ranges() -> None:
    assert part_two([(40, 51), (15, 31), (10, 21)]) == 32


def test_part_two_touching_ranges_do_not_double_count() -> None:
    assert part_two([(1, 6), (6, 11)]) == 10
