import re
from math import prod
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


def part_one(data: str) -> int:
    """Return the answer to part one."""
    nums, ops = parse_data_part_one(data)
    column_totals = []
    for i, o in enumerate(ops):
        if o == '+':
            column_totals.append(np.sum(nums[:, i]))
        else:
            column_totals.append(np.prod(nums[:, i]))
    return sum(column_totals)


def part_two(data: str) -> int:
    nums, ops = parse_data_part_two(data)
    column_totals = []
    for i, o in enumerate(ops):
        if o == '+':
            column_totals.append(sum(nums[i]))
        else:
            column_totals.append(prod(nums[i]))
    return sum(column_totals)


def parse_data_part_one(data: str) -> tuple[np.ndarray, np.ndarray]:
    all_white_space = re.compile(r'[^\S\n]+')
    clean = re.sub(all_white_space, ',', data.strip())

    clean_path = Path('clean_input.txt')
    clean_path.write_text(clean)

    grid = np.loadtxt(clean_path, delimiter=',', dtype=object)
    nums = grid[:-1, :].astype(int)
    ops = grid[-1, :]
    return nums, ops


def parse_data_part_two(data: str) -> tuple[list[list[int]], list[str]]:
    # transpose nums
    nums = data.split('\n')[:-1]
    ops = [op.strip() for op in data.rsplit('\n', maxsplit=1)[-1].split() if op.strip()]

    len_nums = len(nums[0])  # number of number (counting spaces)
    transposed_nums = [''] * len_nums  # Creates a row for each column
    for i in range(len_nums):
        for row in nums:
            transposed_nums[i] += row[i]

    transposed_nums = [num.strip() for num in transposed_nums]
    transposed_grid = []
    col = []
    for num in transposed_nums:
        if num:
            col.append(int(num))
        else:
            transposed_grid.append(col)
            col = []
    transposed_grid.append(col)

    return transposed_grid, ops


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
