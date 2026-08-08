from itertools import product
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'
NUM_HEIGHTS = 5
MAX_HEIGHT = 5

type Key = tuple[int, ...]
type Lock = tuple[int, ...]


def parse_heights(lines: list[str]) -> tuple[int, ...]:
    transposed_data = [[line[i] for line in lines] for i in range(NUM_HEIGHTS)]
    return tuple(line.count('#') for line in transposed_data)


def parse_data(input_path: Path) -> tuple[set[Key], set[Lock]]:
    keys = set()
    locks = set()
    lines = input_path.read_text().strip().split('\n')
    line_idx = 0
    while line_idx < len(lines):
        first_line = lines[line_idx]
        info_lines = lines[line_idx + 1 : line_idx + 6]
        if first_line.startswith('.'):
            keys.add(parse_heights(info_lines))
        else:
            locks.add(parse_heights(info_lines))

        line_idx += 8

    return keys, locks


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    keys, locks = parse_data(input_path)
    count = 0
    for key, lock in product(keys, locks):
        if all(k + l <= MAX_HEIGHT for k, l in zip(key, lock, strict=True)):
            count += 1
    return count


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)  # ruff: ignore[unused-variable]
    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
