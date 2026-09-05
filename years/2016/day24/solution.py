import heapq
from collections.abc import Iterable
from functools import cache
from itertools import count, pairwise, permutations
from math import inf
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

sequence = count()


def parse_data(input_path: Path) -> tuple[frozenset[Pos], dict[int, Pos]]:
    walls = set()
    marked_locations = {}

    for row, line in enumerate(input_path.read_text().strip().split('\n')):
        for col, char in enumerate(line):
            match char:
                case '.':
                    continue
                case '#':
                    walls.add(Pos(row, col))
                case _:
                    marked_locations[int(char)] = Pos(row, col)

    return frozenset(walls), marked_locations


def walk_maze(
    end: Pos,
    walls: frozenset[Pos],
    visited: dict[Pos, int],
    queue: list[tuple[int, int, Pos]],
) -> int:
    while queue:
        cost, _, pos = heapq.heappop(queue)
        if pos == end:
            return cost

        if cost > visited.get(pos, inf):
            continue

        cost += 1
        for neighbor in pos.neighbors():
            if neighbor in walls:
                continue

            prev_cost = visited.get(neighbor, inf)
            if cost < prev_cost:
                visited[neighbor] = cost
                heapq.heappush(queue, (cost, next(sequence), neighbor))

    return -1


@cache
def walk_maze_start_to_end(start: Pos, end: Pos, walls: frozenset[Pos]) -> int:
    queue: list[tuple[int, int, Pos]] = []
    heapq.heappush(queue, (0, next(sequence), start))
    visited = {start: 0}
    return walk_maze(end, walls, visited, queue)


def find_shortest_path_given_order(
    order: Iterable[int],
    marked_locations: dict[int, Pos],
    walls: frozenset[Pos],
) -> int:
    total_cost = 0
    for start_idx, end_idx in pairwise(order):
        a, b = sorted((start_idx, end_idx))  # sorting allows us to cache a->b and b->a as the same thing
        start = marked_locations[a]
        end = marked_locations[b]
        total_cost += walk_maze_start_to_end(start, end, walls)
    return total_cost


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    walls, marked_locations = parse_data(input_path)

    start = 0
    other_locations = list(marked_locations.keys())
    other_locations.remove(start)

    return min(
        find_shortest_path_given_order([0, *order], marked_locations, walls) for order in permutations(other_locations)
    )


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    walls, marked_locations = parse_data(input_path)

    start = 0
    other_locations = list(marked_locations.keys())
    other_locations.remove(start)

    return min(
        find_shortest_path_given_order([0, *order, 0], marked_locations, walls)
        for order in permutations(other_locations)
    )


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
