from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


SIZE = 136


def parse_input(data: str) -> np.ndarray:
    grid = np.zeros((SIZE, SIZE), dtype=bool)
    for row_idx, row in enumerate(data.split('\n')):
        for roll_idx, roll in enumerate(row):
            if roll == '@':
                grid[row_idx, roll_idx] = True

    return grid


def sum_surrounding(row: np.intp, col: np.intp, grid: np.ndarray) -> int:
    left = col - 1
    right = col + 1
    up = row + 1
    down = row - 1

    # Get all surrounding indices
    inds = [(up, left), (row, left), (down, left), (up, col), (down, col), (up, right), (row, right), (down, right)]

    # Makes sure the indices are inbound
    inds = [ind for ind in inds if all(0 <= i < SIZE for i in ind)]

    rows, cols = zip(*inds, strict=True)
    return np.sum(grid[rows, cols])


def get_surrounding_rolls(grid: np.ndarray) -> np.ndarray:
    result = np.full_like(grid, -1, dtype=int)

    rows, cols = np.where(grid)  # only the (r, c) values where grid is True (where there is a roll)
    for r, c in zip(rows, cols, strict=True):
        result[r, c] = sum_surrounding(r, c, grid)
    return result


def part_one(grid: np.ndarray) -> np.intp:
    """Return the answer to part one."""
    return np.sum((grid < 4) & (grid >= 0))  # ruff:ignore[magic-value-comparison]


def part_two(grid: np.ndarray) -> np.intp:
    """Return the answer to part two."""
    return np.sum(np.where((grid < 4) & (grid >= 0)))  # ruff:ignore[magic-value-comparison]


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    grid = parse_input(data)
    grid = get_surrounding_rolls(grid)
    print(f'Part 1: {part_one(grid)}')
    print(f'Part 2: {part_two(grid)}')


if __name__ == '__main__':
    main()
