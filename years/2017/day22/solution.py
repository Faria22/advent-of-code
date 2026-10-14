from enum import Enum
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Pos = tuple[int, int]


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def turn_left(self) -> 'Direction':
        turns = {
            Direction.UP: Direction.LEFT,
            Direction.DOWN: Direction.RIGHT,
            Direction.LEFT: Direction.DOWN,
            Direction.RIGHT: Direction.UP,
        }
        return turns[self]

    def turn_right(self) -> 'Direction':
        turns = {
            Direction.UP: Direction.RIGHT,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.RIGHT: Direction.DOWN,
        }
        return turns[self]

    def reverse(self) -> 'Direction':
        reverse = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        return reverse[self]


def move(pos: Pos, direction: Direction) -> Pos:
    x, y = pos
    dx, dy = direction.value
    return (x + dx, y + dy)


def parse_data(input_path: Path) -> set[Pos]:
    lines = input_path.read_text().strip().split('\n')
    dimension = len(lines)
    start_idx = -(dimension - 1) // 2
    infected = set()
    for row, line in enumerate(lines, start_idx):
        for col, cell in enumerate(line, start_idx):
            if cell == '#':
                infected.add((row, col))
    return infected


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    infected = parse_data(input_path)

    pos = (0, 0)
    direction = Direction.UP

    num_steps = 10_000
    num_infecting_steps = 0
    for _ in range(num_steps):
        if pos in infected:
            direction = direction.turn_right()
            infected.remove(pos)
        else:
            direction = direction.turn_left()
            infected.add(pos)
            num_infecting_steps += 1

        pos = move(pos, direction)

    return num_infecting_steps


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    infected = parse_data(input_path)
    weakened = set()
    flagged = set()

    pos = (0, 0)
    direction = Direction.UP

    num_steps = 10_000_000
    num_infecting_steps = 0
    for _ in range(num_steps):
        if pos in infected:
            direction = direction.turn_right()
            infected.remove(pos)
            flagged.add(pos)
        elif pos in flagged:
            direction = direction.reverse()
            flagged.remove(pos)
        elif pos in weakened:
            num_infecting_steps += 1
            weakened.remove(pos)
            infected.add(pos)
        else:
            direction = direction.turn_left()
            weakened.add(pos)

        pos = move(pos, direction)

    return num_infecting_steps


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
