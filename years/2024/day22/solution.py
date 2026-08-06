from collections import defaultdict
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[int]:
    lines = input_path.read_text().strip().split('\n')
    return [int(line) for line in lines]


def process(secret_number: int, n: int = 1) -> int:
    for _ in range(n):
        number = secret_number * 64
        secret_number = (secret_number ^ number) % 16777216
        number = secret_number // 32
        secret_number = (secret_number ^ number) % 16777216
        number = secret_number * 2048
        secret_number = (secret_number ^ number) % 16777216
    return secret_number


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    total = 0
    for number in parse_data(input_path):
        total += process(number, 2000)
    return total


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    numbers = parse_data(input_path)
    prices = np.zeros((len(numbers), 2001), dtype=int)
    for i, num in enumerate(numbers):
        prices[i, 0] = num % 10
        cur_num = num
        for j in range(2000):
            cur_num = process(cur_num)
            prices[i, j + 1] = cur_num % 10

    price_diffs = np.diff(prices)
    print(price_diffs.shape)
    bananas_per_diff = defaultdict(int)
    for i in range(len(price_diffs)):
        seen_keys = set()
        for j in range(4, 2001):
            key = tuple(price_diffs[i, j - 4 : j].tolist())
            if key in seen_keys:
                continue

            seen_keys.add(key)
            bananas_per_diff[key] += int(prices[i, j])
    return max(bananas_per_diff.values())


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
