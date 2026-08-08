import re
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'

GRID_SIZE = 1000


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)

    lines = parse_data(input_path)
    for line in lines:
        values = re.findall(r'\d+', line)
        start_x, start_y, end_x, end_y = [int(val) for val in values]
        sub_grid = grid[start_x : end_x + 1, start_y : end_y + 1]
        if 'on' in line:
            sub_grid[...] = True
        elif 'off' in line:
            sub_grid[...] = False
        else:
            sub_grid[...] = ~sub_grid
    return np.sum(grid)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    lines = parse_data(input_path)
    for line in lines:
        values = re.findall(r'\d+', line)
        start_x, start_y, end_x, end_y = [int(val) for val in values]
        sub_grid = grid[start_x : end_x + 1, start_y : end_y + 1]
        if 'on' in line:
            sub_grid += 1
        elif 'off' in line:
            sub_grid -= 1
            sub_grid[...] = np.where(sub_grid < 0, 0, sub_grid)
        else:
            sub_grid += 2
    return np.sum(grid)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
