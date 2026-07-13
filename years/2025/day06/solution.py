import re
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


def part_one(nums: np.ndarray, ops: np.ndarray) -> int:
    """Return the answer to part one."""
    ret = []
    for i, o in enumerate(ops):
        if o == '+':
            ret.append(np.sum(nums[:, i]))
        else:
            ret.append(np.prod(nums[:, i]))
    return sum(ret)


def part_two(data: str):
    """Return the answer to part two."""
    return


def parse_data(data: str) -> tuple[np.ndarray, ...]:
    all_white_space = re.compile(r'[^\S\n]+')
    clean = re.sub(all_white_space, ',', data.strip())

    clean_path = Path('clean_input.txt')
    clean_path.write_text(clean)

    grid = np.loadtxt(clean_path, delimiter=',', dtype=object)
    nums = grid[:-1, :].astype(int)
    ops = grid[-1, :]
    return nums, ops


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    nums, ops = parse_data(data)
    print(f'Part 1: {part_one(nums, ops)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
