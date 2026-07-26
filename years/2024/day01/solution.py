from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_file: Path) -> tuple[np.ndarray, np.ndarray]:
    lists = np.loadtxt(input_file, dtype=int)
    list_1 = np.sort(lists[:, 0].ravel())
    list_2 = np.sort(lists[:, 1].ravel())
    return list_1, list_2


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""

    list_1, list_2 = parse_data(input_path)

    diff = np.abs(list_1 - list_2)
    return np.sum(diff)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    list_1, list_2 = parse_data(input_path)

    matches = list_1[:, np.newaxis] == list_2
    occurrences = matches.sum(axis=1)

    return list_1 @ occurrences


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
