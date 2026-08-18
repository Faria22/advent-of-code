from array import array
from math import isqrt
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def sum_divisors(n: int) -> int:
    sum_divisors = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            sum_divisors += i + n // i
    return sum_divisors


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    min_presents = parse_data(input_path)

    limit = 1_000_000
    houses = array('Q', [10]) * (limit + 1)

    for elf in range(2, limit):
        house = elf
        while house < limit + 1:
            houses[house] += elf * 10
            house += elf

        if houses[elf] >= min_presents:
            return elf

    return 0


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    min_presents = parse_data(input_path)

    limit = 1_000_000
    houses = array('Q', [0]) * (limit + 1)

    for elf in range(1, limit):
        for house in range(elf, elf * 50 + 1, elf):
            if house < limit + 1:
                houses[house] += elf * 11

        if houses[elf] >= min_presents:
            return elf

    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
