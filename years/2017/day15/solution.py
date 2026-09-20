from pathlib import Path

from numba import njit

INPUT_PATH = Path(__file__).parent / 'input.txt'

DIVISOR = 2147483647


def parse_data(input_path: Path) -> list[int]:
    initial_values = []
    for line in input_path.read_text().strip().split('\n'):
        val = line.split()[-1]
        initial_values.append(int(val))

    return initial_values


@njit
def count_matches(val_a: int, val_b: int, multiples_a: int, multiples_b: int, num_iterations: int) -> int:
    factor_a = 16807
    factor_b = 48271

    num_of_equal_vals = 0
    for _ in range(num_iterations):
        while True:
            val_a = (val_a * factor_a) % DIVISOR
            if val_a % multiples_a == 0:
                break

        while True:
            val_b = (val_b * factor_b) % DIVISOR
            if val_b % multiples_b == 0:
                break

        if (val_a & 0xFFFF) == (val_b & 0xFFFF):
            num_of_equal_vals += 1

    return num_of_equal_vals


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    val_a, val_b = parse_data(input_path)
    return count_matches(val_a, val_b, 1, 1, 40_000_000)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    val_a, val_b = parse_data(input_path)
    return count_matches(val_a, val_b, 4, 8, 5_000_000)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
