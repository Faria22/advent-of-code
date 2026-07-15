from copy import deepcopy
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


START_POINT = 'S'
LASER_CHAR = '|'
BLANK_CHAR = '.'
SPLITTER_CHAR = '^'

type Grid = list[list[str]]


def parse_data(data: str) -> Grid:
    grid = [list(line) for line in data.split('\n')]
    grid[0] = [cell.replace(START_POINT, LASER_CHAR) for cell in grid[0]]

    return grid


def part_one(grid: Grid) -> int:
    """Return the answer to part one."""
    split_times = 0
    for i, row in enumerate(grid[1:], 1):
        for j, cell in enumerate(row):
            # Do nothing if there is no laser in the previous row
            if grid[i - 1][j] != LASER_CHAR:
                continue

            if cell == BLANK_CHAR:
                grid[i][j] = LASER_CHAR
            elif cell == SPLITTER_CHAR:
                split_times += 1
                grid[i][j - 1] = LASER_CHAR
                grid[i][j + 1] = LASER_CHAR

    return split_times


def quantum_split(grid: Grid, current_row: int, cache: dict[tuple[int, int], int]) -> int:
    timeline_count = 0
    for i, row in enumerate(grid[current_row:], current_row):
        for j, cell in enumerate(row):
            # Do nothing if there is no laser in the previous row
            if grid[i - 1][j] != LASER_CHAR:
                continue

            if cell == BLANK_CHAR:
                grid[i][j] = LASER_CHAR
            elif cell == SPLITTER_CHAR:
                if (i, j) in cache:
                    return cache[i, j]

                left_split_grid = deepcopy(grid)
                left_split_grid[i][j - 1] = LASER_CHAR
                timeline_count += quantum_split(left_split_grid, i + 1, cache)

                right_split_grid = deepcopy(grid)
                right_split_grid[i][j + 1] = LASER_CHAR
                timeline_count += quantum_split(right_split_grid, i + 1, cache)

                # Caches answer if a bean hits the same splitter again
                cache[i, j] = timeline_count
                return timeline_count

    # Adds one for when it gets to the end
    # The idea is that if there were no splitters then
    # we would still have a single timeline
    return timeline_count + 1


def part_two(grid: Grid) -> int:
    """Return the answer to part two."""

    cache: dict[tuple[int, int], int] = {}
    return quantum_split(grid, 1, cache)


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    grid = parse_data(data)
    print(f'Part 1: {part_one(deepcopy(grid))}')
    print(f'Part 2: {part_two(deepcopy(grid))}')


if __name__ == '__main__':
    main()
