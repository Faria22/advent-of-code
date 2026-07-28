from collections.abc import Iterable
from itertools import islice
from pathlib import Path
from typing import Literal, get_args

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Pos = tuple[int, int]

Direction = Literal['n', 's', 'w', 'e']
DIRECTIONS = list(get_args(Direction))

OBSTACLE = '#'
GUARD_CHAR = '^'


def triowise(iterable: Iterable) -> Iterable:
    """Similar to pairwise but for three elements"""
    iterators = (islice(iterable, offset, None) for offset in range(3))
    return zip(*iterators, strict=False)


class Guard:
    def __init__(self, position: Pos, direction: Direction) -> None:
        self.position: Pos | None = position
        self.direction = direction

    @property
    def row(self) -> int | None:
        if self.position is None:
            return None
        return self.position[0]

    @property
    def col(self) -> int | None:
        if self.position is None:
            return None
        return self.position[1]

    def move(self, obstacles: set[Pos], max_pos: Pos) -> tuple[set[Pos], Pos | None]:
        assert self.row is not None
        assert self.col is not None

        # Check if there is an obstacle on the way
        found_obstacle = None
        try:  # ruff: ignore[too-many-statements-in-try-clause]
            match self.direction:
                case 'n':
                    found_obstacle = (
                        max(row for row, col in obstacles if col == self.col and row < self.row),
                        self.col,
                    )
                case 's':
                    found_obstacle = (
                        min(row for row, col in obstacles if col == self.col and row > self.row),
                        self.col,
                    )
                case 'w':
                    found_obstacle = (
                        self.row,
                        max(col for row, col in obstacles if row == self.row and col < self.col),
                    )
                case 'e':
                    found_obstacle = (
                        self.row,
                        min(col for row, col in obstacles if row == self.row and col > self.col),
                    )
        except ValueError:
            pass

        # if it found and obstacle
        if found_obstacle is not None:
            min_pos = (found_obstacle[0] + 1, found_obstacle[1] + 1)
            max_pos = (found_obstacle[0] - 1, found_obstacle[1] - 1)
        else:
            min_pos = (0, 0)

        match self.direction:
            case 'n':
                visited_pos = {(row, self.col) for row in range(min_pos[0], self.row)}
            case 's':
                visited_pos = {(row, self.col) for row in range(self.row + 1, max_pos[0] + 1)}
            case 'w':
                visited_pos = {(self.row, col) for col in range(min_pos[1], self.col)}
            case 'e':
                visited_pos = {(self.row, col) for col in range(self.col + 1, max_pos[1] + 1)}

        if found_obstacle is None:
            self.position = None
        else:
            match self.direction:
                case 'n':
                    self.position = (found_obstacle[0] + 1, found_obstacle[1])
                case 's':
                    self.position = (found_obstacle[0] - 1, found_obstacle[1])
                case 'w':
                    self.position = (found_obstacle[0], found_obstacle[1] + 1)
                case 'e':
                    self.position = (found_obstacle[0], found_obstacle[1] - 1)
            self.update_direction()

        return visited_pos, found_obstacle

    def update_direction(self) -> None:
        match self.direction:
            case 'n':
                self.direction = 'e'
            case 'e':
                self.direction = 's'
            case 's':
                self.direction = 'w'
            case 'w':
                self.direction = 'n'

    def looped(self, obstacles: set[Pos], max_pos: Pos) -> bool:
        found_states: set[tuple[Pos, Direction]] = set()
        while self.position is not None:
            obstacle = self.move(obstacles, max_pos)[1]
            if obstacle is not None:
                state = (obstacle, self.direction)
                if state in found_states:
                    return True
                found_states.add(state)  # pyright: ignore[reportArgumentType]

        return False


def parse_data(data: str) -> tuple[Guard, set[Pos], Pos]:
    guard = None
    obstacles: set[Pos] = set()
    for row, line in enumerate(data.split('\n')):
        for col, cell in enumerate(line):
            if cell == OBSTACLE:
                obstacles.add((row, col))
            elif cell == GUARD_CHAR:
                guard = Guard((row, col), 'n')

    assert guard is not None

    max_pos = (row, col)
    return guard, obstacles, max_pos


def part_one(data: str) -> int:
    """Return the answer to part one."""
    guard, obstacles, max_pos = parse_data(data)

    visited_positions = {guard.position}
    while guard.position is not None:
        visited_positions.update(guard.move(obstacles, max_pos)[0])

    return len(visited_positions)


def part_two(data: str) -> int:
    """Return the answer to part two."""
    guard, obstacles, max_pos = parse_data(data)
    assert guard.position is not None

    starting_position = guard.position
    visited_positions = {guard.position}
    while guard.position is not None:
        visited_positions.update(guard.move(obstacles, max_pos)[0])

    possible_positions = set()
    for pos in visited_positions:
        guard.position = starting_position
        guard.direction = 'n'
        if guard.looped(obstacles | {pos}, max_pos):
            possible_positions.add(pos)

    return len(possible_positions)


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
