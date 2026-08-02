import heapq
from collections.abc import Iterator
from dataclasses import dataclass
from itertools import count
from math import inf
from pathlib import Path
from typing import ClassVar

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'
sequence = count()


START_CHAR = 'S'
END_CHAR = 'E'
WALL_CHAR = '#'


@dataclass(frozen=True)
class Reindeer:
    pos: Pos
    direction: str

    OFFSETS: ClassVar[dict] = {
        'n': Pos(-1, 0),
        's': Pos(1, 0),
        'e': Pos(0, 1),
        'w': Pos(0, -1),
    }

    def foward(self) -> tuple['Reindeer', int]:
        return Reindeer(self.pos + self.OFFSETS[self.direction], self.direction), 1

    def left(self) -> tuple['Reindeer', int]:
        left = {
            'n': 'w',
            'w': 's',
            's': 'e',
            'e': 'n',
        }
        new_direction = left[self.direction]
        return Reindeer(self.pos + self.OFFSETS[new_direction], new_direction), 1000 + 1

    def right(self) -> tuple['Reindeer', int]:
        right = {
            'n': 'e',
            'e': 's',
            's': 'w',
            'w': 'n',
        }
        new_direction = right[self.direction]
        return Reindeer(self.pos + self.OFFSETS[new_direction], new_direction), 1000 + 1

    def neighbors(self) -> Iterator[tuple['Reindeer', int]]:
        yield self.foward()
        yield self.left()
        yield self.right()


def parse_data(input_path: Path) -> tuple[Reindeer, Pos, set[Pos]]:
    start, end, walls = None, None, set()
    for row, line in enumerate(input_path.read_text().strip().split('\n')):
        for col, char in enumerate(line):
            if char == WALL_CHAR:
                walls.add(Pos(row, col))
            elif char == START_CHAR:
                start = Pos(row, col)
            elif char == END_CHAR:
                end = Pos(row, col)

    assert start is not None
    assert end is not None

    return Reindeer(start, 'e'), end, walls


def walk_maze(
    end: Pos,
    walls: set[Pos],
    best_cost: dict[Reindeer, tuple[float, set[Reindeer]]],
    queue: list,
) -> float:
    cheapest_end = None
    while queue:
        cost, _, reindeer = heapq.heappop(queue)

        pos = reindeer.pos
        if pos == end and cheapest_end is None:
            cheapest_end = cost

        if cost > best_cost.get(reindeer, (inf, set()))[0]:
            continue

        for neighbor, move_cost in reindeer.neighbors():
            if neighbor.pos in walls:
                continue

            new_cost = cost + move_cost
            prev_cost, best_prev_states = best_cost.get(neighbor, (inf, set()))
            if new_cost < prev_cost:
                best_cost[neighbor] = (new_cost, {reindeer})
                heapq.heappush(queue, (new_cost, next(sequence), neighbor))
            elif new_cost == prev_cost:
                best_prev_states.add(reindeer)

    assert cheapest_end is not None
    return cheapest_end


def walk_backwards(starting_state: Reindeer, best_costs: dict[Reindeer, tuple[float, set[Reindeer]]]) -> set[Pos]:
    visited_pos = {starting_state.pos}
    _, prev_states = best_costs.get(starting_state, (inf, set()))
    for prev_state in prev_states:
        visited_pos |= walk_backwards(prev_state, best_costs)

    return visited_pos


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    start, end, walls = parse_data(input_path)

    queue: list[tuple[int, int, Reindeer]] = []

    heapq.heappush(queue, (0, next(sequence), start))
    best_cost: dict[Reindeer, tuple[float, set[Reindeer]]] = {start: (0, set())}
    return int(walk_maze(end, walls, best_cost, queue))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    start, end, walls = parse_data(input_path)

    queue: list[tuple[int, int, Reindeer]] = []

    heapq.heappush(queue, (0, next(sequence), start))
    best_cost: dict[Reindeer, tuple[float, set[Reindeer]]] = {start: (0, set())}
    cheapest_end = walk_maze(end, walls, best_cost, queue)

    starting_states = (
        state
        for direction in ('n', 'e', 'w', 's')
        if (state := Reindeer(end, direction)) in best_cost and best_cost[state][0] == cheapest_end
    )
    visited_pos: set[Pos] = set()
    for starting_state in starting_states:
        visited_pos |= walk_backwards(starting_state, best_cost)

    return len(visited_pos)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
