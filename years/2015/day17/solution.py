from itertools import combinations
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[int]:
    buckets = input_path.read_text().strip().split('\n')
    return [int(bucket) for bucket in buckets]


def part_one(input_path: Path, liters: int = 150) -> int:
    """Return the answer to part one."""
    buckets = parse_data(input_path)
    num_combinations = 0
    for num_used_buckets in range(2, len(buckets) + 1):
        for combination in combinations(buckets, num_used_buckets):
            if sum(combination) == liters:
                num_combinations += 1
    return num_combinations


def part_two(input_path: Path, liters: int = 150) -> int:
    """Return the answer to part two."""
    buckets = parse_data(input_path)
    num_combinations = 0
    for num_used_buckets in range(2, len(buckets) + 1):
        for combination in combinations(buckets, num_used_buckets):
            if sum(combination) == liters:
                num_combinations += 1
        if num_combinations > 0:
            return num_combinations
    return -1


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
