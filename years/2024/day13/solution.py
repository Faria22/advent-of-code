# ruff: file-ignore[non-lowercase-variable-in-function]
import re
from dataclasses import dataclass
from itertools import batched
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'

BUTTON_COST = (3, 1)


@dataclass
class Machine:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

    def solve(self) -> tuple[int, int] | None:
        # Get equation matrix
        a = np.array(self.a)
        b = np.array(self.b)
        A = np.column_stack((a, b))

        # Denominator for inverse matrix
        denominator = int(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])

        if denominator == 0:
            return None

        inv = np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])
        numerator = inv @ np.array(self.prize)

        for val in numerator:
            if int(val) % denominator != 0:
                return None

        sol = numerator / denominator
        return int(sol[0]), int(sol[1])

    def cost(self) -> int:
        solution = self.solve()
        if solution is None:
            return 0

        return sum(cost * sol for cost, sol in zip(BUTTON_COST, solution, strict=True))

    def shift_prize(self, shift: int) -> None:
        x, y = self.prize
        self.prize = (x + shift, y + shift)


def parse_line(line: str) -> tuple[int, int]:
    pattern = r'[^\d*,]'
    nums = re.sub(pattern, '', line)

    x, y = nums.split(',')
    return int(x), int(y)


def parse_data(input_path: Path) -> list[Machine]:
    lines = input_path.read_text().strip().split('\n')

    machines = []
    for batched_lines in batched(lines, 4):
        a_line, b_line, prize_line, *_ = batched_lines
        a = parse_line(a_line)
        b = parse_line(b_line)
        prize = parse_line(prize_line)
        machines.append(Machine(a, b, prize))

    return machines


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    machines = parse_data(input_path)

    return sum(machine.cost() for machine in machines)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    machines = parse_data(input_path)
    shift = 10000000000000

    cost = 0
    for machine in machines:
        machine.shift_prize(shift)
        cost += machine.cost()
    return cost


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
