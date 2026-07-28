from collections.abc import Iterable
from itertools import product
from pathlib import Path
from typing import Literal, NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'

PLUS = '+'
MULT = '*'
CONC = '||'
type Operation = Literal['+', '*', '||']


class Test(NamedTuple):
    expected_value: int
    numbers: list[int]

    def solvable(self, operation_set: set[Operation]) -> bool:
        for operations in product(operation_set, repeat=len(self.numbers) - 1):
            if self.expected_value == solve_expression(self.numbers.copy(), operations):
                return True
        return False


def solve_expression(numbers: list[int], operations: Iterable[Operation]) -> int:
    total = numbers.pop(0)
    for number, operation in zip(numbers, operations, strict=True):
        if operation == PLUS:
            total += number
        elif operation == MULT:
            total *= number
        elif operation == CONC:
            total = int(str(total) + str(number))
        else:
            raise ValueError

    return total


def parse_data(input_path: Path) -> list[Test]:
    tests = []
    for line in input_path.read_text().strip().split('\n'):
        expected_value, numbers = line.split(': ')
        numbers = [int(number) for number in numbers.split()]
        tests.append(Test(int(expected_value), numbers))

    return tests


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    tests = parse_data(input_path)
    total = 0
    for test in tests:
        if test.solvable({PLUS, MULT}):
            total += test.expected_value
    return total


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    tests = parse_data(input_path)
    total = 0
    for test in tests:
        if test.solvable({PLUS, MULT, CONC}):
            total += test.expected_value
    return total


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
