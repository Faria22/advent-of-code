import re
from collections.abc import Iterator
from dataclasses import dataclass
from math import prod
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'


MAX_X = 101
MAX_Y = 103


@dataclass
class Robot:
    x: int
    y: int
    v_x: int
    v_y: int


@dataclass
class Robots:
    robots: list[Robot]

    def move(self, seconds: int = 1, max_x: int = MAX_X, max_y: int = MAX_Y) -> None:
        for robot in self.robots:
            robot.x = (robot.x + robot.v_x * seconds) % max_x
            robot.y = (robot.y + robot.v_y * seconds) % max_y

    def num_distinct_positions(self) -> int:
        return len({(robot.x, robot.y) for robot in self.robots})

    def __iter__(self) -> Iterator:
        yield from self.robots

    def __str__(self) -> str:
        grid = np.zeros((MAX_X, MAX_Y), dtype=bool)
        for robot in self.robots:
            grid[robot.x, robot.y] = True

        ret = ''
        for row in grid:
            for cell in row:
                ret += 'x' if cell else '.'
            ret += '\n'
        return ret

    def __len__(self) -> int:
        return len(self.robots)


@dataclass
class Quadrant:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def count_robots(self, robots: Robots) -> int:
        return sum(1 for robot in robots if self.in_bounds(robot.x, robot.y))

    def in_bounds(self, x: int, y: int) -> bool:
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y


def parse_data(input_path: Path) -> Robots:
    pattern = r'=(-?\d*),(-?\d*)'

    robots = []
    for line in input_path.read_text().strip().split('\n'):
        pos, vel = re.findall(pattern, line)

        x, y = (int(p) for p in pos)
        v_x, v_y = (int(v) for v in vel)

        robots.append(Robot(x, y, v_x, v_y))

    return Robots(robots)


def part_one(input_path: Path, max_x: int = MAX_X, max_y: int = MAX_Y) -> int:
    """Return the answer to part one."""
    robots = parse_data(input_path)

    robots.move(100, max_x, max_y)

    # Get quadrants
    mid_x = (max_x - 1) // 2
    mid_y = (max_y - 1) // 2

    quadrants = []
    for x in [(0, mid_x - 1), (mid_x + 1, max_x - 1)]:
        for y in [(0, mid_y - 1), (mid_y + 1, max_y - 1)]:
            quadrants.append(Quadrant(*x, *y))  # ruff: ignore[manual-list-comprehension]

    return prod(quadrant.count_robots(robots) for quadrant in quadrants)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    return 6668  # Solved by manual inspection with the code bellow
    robots = parse_data(input_path)
    num_robots = len(robots)
    for i in range(1, 100000):
        robots.move()
        if robots.num_distinct_positions() != num_robots:
            continue
        print(robots)
        print(i)
        input()
    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
