# ruff: file-ignore[magic-value-comparison]  # ruff: ignore[unused-noqa]

from pathlib import Path

import pytest
from solution import Direction, Guard, part_one, part_two

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'
data = SAMPLE_PATH.read_text().strip()


def test_part_one_with_sample_input() -> None:
    assert part_one(data) == 41


def test_part_two_with_sample_input() -> None:
    assert part_two(data) == 6


def test_part_two_considers_obstacles_not_encountered_on_original_route() -> None:
    map_data = """\
..#..
..^.#
..#..
.....
...##"""

    assert part_two(map_data) == 0


def test_part_two_finds_loop_using_obstacle_not_encountered_on_original_route() -> None:
    map_data = """\
.....
...#.
..#^#
.....
....."""

    assert part_two(map_data) == 1


@pytest.mark.parametrize(
    ('direction', 'start', 'obstacle', 'expected_visited', 'expected_position', 'expected_direction'),
    [
        ('n', (5, 4), (2, 4), {(3, 4), (4, 4)}, (3, 4), 'e'),
        ('s', (2, 4), (5, 4), {(3, 4), (4, 4)}, (4, 4), 'w'),
        ('w', (4, 5), (4, 2), {(4, 3), (4, 4)}, (4, 3), 'n'),
        ('e', (4, 2), (4, 5), {(4, 3), (4, 4)}, (4, 4), 's'),
    ],
)
def test_guard_stops_before_obstacle_and_turns_right(
    direction: Direction,
    start: tuple[int, int],
    obstacle: tuple[int, int],
    expected_visited: set[tuple[int, int]],
    expected_position: tuple[int, int],
    expected_direction: Direction,
) -> None:
    guard = Guard(start, direction)

    visited, _ = guard.move({obstacle}, max_pos=(9, 9))

    assert visited == expected_visited
    assert guard.position == expected_position
    assert guard.direction == expected_direction


@pytest.mark.parametrize(
    ('direction', 'start', 'expected_visited'),
    [
        ('n', (2, 2), {(0, 2), (1, 2)}),
        ('s', (2, 2), {(3, 2), (4, 2)}),
        ('w', (2, 2), {(2, 0), (2, 1)}),
        ('e', (2, 2), {(2, 3), (2, 4)}),
    ],
)
def test_guard_moves_to_edge_then_leaves_map(
    direction: Direction,
    start: tuple[int, int],
    expected_visited: set[tuple[int, int]],
) -> None:
    guard = Guard(start, direction)

    visited, _ = guard.move(set(), max_pos=(4, 4))

    assert visited == expected_visited
    assert guard.position is None
    assert guard.direction == direction
