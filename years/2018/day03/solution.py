import re
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_line(line: str) -> tuple[int, int, int, int]:
    return tuple(map(int, *re.findall(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', line)))  # ty: ignore[invalid-return-type]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    size = 1_000
    fabric = np.zeros((size, size), dtype=int)
    for line in lines:
        x, y, w, h = parse_line(line)
        fabric[x:x + w, y:y + h] += 1
    return int(np.count_nonzero(fabric > 1))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    size = 1_000
    fabric = np.zeros((size, size), dtype=int)
    for line in lines:
        x, y, w, h = parse_line(line)
        fabric[x:x + w, y:y + h] += 1

    for idx, line in enumerate(lines, 1):
        x, y, w, h = parse_line(line)
        if np.all(fabric[x:x + w, y:y + h] == 1):
            return idx
    return -1


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
