from collections.abc import Iterator
from functools import cache
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Pos(NamedTuple):
    row: int
    col: int

    def __add__(self, other: 'Pos') -> 'Pos':
        return Pos(self.row + other.row, self.col + other.col)

    def __str__(self) -> str:
        return f'({self.row}, {self.col})'

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'


DIRECTIONS = {
    Pos(-1, 0),  # Up
    Pos(1, 0),  # Down
    Pos(0, -1),  # Left
    Pos(0, 1),  # Right
}

START_VALUE = 0
END_VALUE = 9


class Grid:
    def __init__(self, lines: list[str]) -> None:
        self.data = [[int(x) for x in line] for line in lines]
        self.shape = (len(self.data), len(self.data[0]))

    def __getitem__(self, pos: Pos) -> int:
        return self.data[pos.row][pos.col]

    def __iter__(self) -> Iterator:
        yield from self.data


def parse_data(input_path: Path) -> Grid:
    return Grid(input_path.read_text().strip().split('\n'))


@cache
def in_bounds(pos: Pos, grid: Grid) -> bool:
    return all(0 <= pos[i] < grid.shape[i] for i in range(2))


@cache
def walk_up(grid: Grid, pos: Pos, value: int) -> set[Pos]:
    found_ends: set[Pos] = set()  # All then ends that the current position found
    for direction in DIRECTIONS:
        new_pos = pos + direction
        if not in_bounds(new_pos, grid):
            continue

        new_pos_value = grid[new_pos]

        if new_pos_value != value:
            continue

        if new_pos_value == END_VALUE:
            found_ends.add(new_pos)
            continue

        found_ends |= walk_up(grid, new_pos, value + 1)

    return found_ends


@cache
def walk_up_count(grid: Grid, pos: Pos, value: int) -> int:
    count = 0
    for direction in DIRECTIONS:
        new_pos = pos + direction
        if not in_bounds(new_pos, grid):
            continue

        new_pos_value = grid[new_pos]

        if new_pos_value != value:
            continue

        if new_pos_value == END_VALUE:
            count += 1
            continue

        count += walk_up_count(grid, new_pos, value + 1)

    return count


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    grid = parse_data(input_path)

    starting_pos = [
        Pos(row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == START_VALUE
    ]

    count = 0
    for pos in starting_pos:
        count += len(walk_up(grid, pos, 1))
    return count


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    grid = parse_data(input_path)

    starting_pos = [
        Pos(row, col) for row, line in enumerate(grid) for col, cell in enumerate(line) if cell == START_VALUE
    ]

    count = 0
    for pos in starting_pos:
        count += walk_up_count(grid, pos, 1)
    return count


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
