import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Receiver:
    type: Literal['bot', 'output']
    idx: int


@dataclass
class Robot:
    idx: int
    chips: list[int]
    handoff: tuple[Receiver, Receiver]


class Robots:
    def __init__(self, robots: list[Robot]) -> None:
        self.robots = sorted(robots, key=lambda r: r.idx)
        self.outputs = [-1] * 3

    def __str__(self) -> str:
        return str(self.robots)

    def __getitem__(self, idx: int) -> Robot:
        for robot in self.robots:
            if robot.idx == idx:
                return robot
        raise IndexError

    def handoff(self) -> None:
        robots = (robot for robot in self.robots if len(robot.chips) == 2)  # ruff: ignore[magic-value-comparison]
        if robot := next(robots, None):
            min_chip, max_chip = sorted(robot.chips)
            for receiver, chip in zip(robot.handoff, (min_chip, max_chip), strict=True):
                if receiver.type == 'bot':
                    self[receiver.idx].chips.append(chip)
                elif receiver.type == 'output' and receiver.idx < 3:  # ruff: ignore[magic-value-comparison]
                    self.outputs[receiver.idx] = chip

            self.robots.remove(robot)

    def index_robot_compares_chips(self, a: int, b: int) -> int | None:
        for robot in self.robots:
            if a in robot.chips and b in robot.chips:
                return robot.idx

        return None

    def output_prod(self) -> int | None:
        if any(o == -1 for o in self.outputs):
            return None
        return math.prod(self.outputs)


def parse_data(input_path: Path) -> Robots:
    robots = []
    robot_values = defaultdict(list)
    for line in input_path.read_text().strip().split('\n'):
        parts = line.split()
        if parts[0] == 'value':
            robot_values[int(parts[-1])].append(int(parts[1]))
        else:
            idx = int(parts[1])
            low_receiver = Receiver(parts[5], int(parts[6]))  # ty: ignore[invalid-argument-type]
            high_receiver = Receiver(parts[-2], int(parts[-1]))  # ty: ignore[invalid-argument-type]
            robots.append(Robot(idx, [], (low_receiver, high_receiver)))

    robots = Robots(robots)
    for idx, values in robot_values.items():
        robots[idx].chips = values

    return robots


def part_one(input_path: Path, a: int = 61, b: int = 17) -> int:
    """Return the answer to part one."""
    robots = parse_data(input_path)
    while robots.robots:
        if (idx := robots.index_robot_compares_chips(a, b)) is not None:
            return idx
        robots.handoff()

    return -1


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    robots = parse_data(input_path)
    while robots.robots:
        if (prod := robots.output_prod()) is not None:
            return prod
        robots.handoff()

    return math.prod(robots.outputs)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
