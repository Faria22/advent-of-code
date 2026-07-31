from functools import cache
from pathlib import Path

from aoc import Grid, Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


START_VALUE = 0
END_VALUE = 9


def parse_data(input_path: Path) -> Grid[int]:
    lines = input_path.read_text().strip().splitlines()
    return Grid([[int(cell) for cell in line] for line in lines])


@cache
def walk_up(grid: Grid[int], pos: Pos, value: int) -> set[Pos]:
    found_ends: set[Pos] = set()  # All then ends that the current position found
    for new_pos in pos.neighbors():
        if not grid.in_bounds(new_pos):
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
def walk_up_count(grid: Grid[int], pos: Pos, value: int) -> int:
    count = 0
    for new_pos in pos.neighbors():
        if not grid.in_bounds(new_pos):
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
