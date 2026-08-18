from itertools import combinations
from math import inf, prod
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[int]:
    return [int(line) for line in input_path.read_text().strip().split('\n')]


def get_package_combinations(packages: list[int], num_groups: int) -> list[tuple[int, ...]]:
    num_packages = len(packages)
    weight_in_group = sum(packages) // num_groups

    for i in range(1, num_packages - 1):
        if package_combinations := [
            combination for combination in combinations(packages, i) if sum(combination) == weight_in_group
        ]:
            return package_combinations

    return []


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    packages = parse_data(input_path)
    package_combinations = get_package_combinations(packages, 3)
    min_qe = inf
    for combination in package_combinations:
        min_qe = min(min_qe, prod(combination))

    return int(min_qe)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    packages = parse_data(input_path)
    package_combinations = get_package_combinations(packages, 4)
    min_qe = inf
    for combination in package_combinations:
        min_qe = min(min_qe, prod(combination))

    return int(min_qe)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
