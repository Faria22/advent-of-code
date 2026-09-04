import heapq
from itertools import count
from math import inf
from pathlib import Path
from typing import NamedTuple

import numpy as np
from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

MAX_X = 36
MAX_Y = 24

sequence = count()


def parse_data(input_path: Path, max_x: int, max_y: int) -> tuple[np.ndarray, np.ndarray]:
    size_grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
    used_grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for line in input_path.read_text().strip().split('\n')[2:]:
        node_path, size_str, used_str, *_ = line.split()

        node_coordinates = node_path.split('-')[-2:]
        x, y = [int(node_coordinate[1:]) for node_coordinate in node_coordinates]
        size = int(size_str[:-1])
        used = int(used_str[:-1])

        size_grid[x, y] = size
        used_grid[x, y] = used

    return size_grid, used_grid


def part_one(input_path: Path, max_x: int = MAX_X, max_y: int = MAX_Y) -> int:
    """Return the answer to part one."""
    size_grid, used_grid = parse_data(input_path, max_x, max_y)
    avail_grid = size_grid - used_grid

    viable_pairs_count = 0
    for idx_a, used_a in np.ndenumerate(used_grid):
        if used_a == 0:
            continue

        for idx_b, avail_b in np.ndenumerate(avail_grid):
            if idx_a == idx_b:
                continue

            if used_a <= avail_b:
                viable_pairs_count += 1

    return viable_pairs_count


class State(NamedTuple):
    empty_pos: Pos
    goal_pos: Pos


def in_bounds(pos: Pos, max_x: int, max_y: int) -> bool:
    return all(0 <= d <= max_d for d, max_d in zip(pos, (max_x, max_y)))


def walk_maze(
    end: Pos,
    walls: set[Pos],
    visited: dict[State, int],
    queue: list[tuple[int, int, State]],
    max_x: int,
    max_y: int,
) -> int:
    while queue:
        cost, _, state = heapq.heappop(queue)
        if state.goal_pos == end:
            return cost

        if cost > visited.get(state, inf):
            continue

        cost += 1
        for neighbor in state.empty_pos.neighbors():
            if neighbor in walls or not in_bounds(neighbor, max_x, max_y):
                continue

            next_state = State(
                neighbor,
                state.goal_pos if neighbor != state.goal_pos else state.empty_pos,
            )

            prev_cost = visited.get(next_state, inf)
            if cost < prev_cost:
                visited[next_state] = cost
                heapq.heappush(queue, (cost, next(sequence), next_state))

    return -1


def part_two(input_path: Path, max_x: int = MAX_X, max_y: int = MAX_Y) -> int:
    """Return the answer to part two."""
    size_grid, used_grid = parse_data(input_path, max_x, max_y)

    empty_node_cords = np.argwhere(used_grid == 0)[0]
    empty_node = Pos(*empty_node_cords)
    goal_node = Pos(max_x, 0)

    empty_capacity = size_grid[tuple(empty_node)]

    # The logic is: if a node's used data is larger than the empty node can hold,
    # that data cannot move into the empty space, so the empty node cannot pass through it
    walls = {Pos(int(x), int(y)) for x, y in np.argwhere(used_grid > empty_capacity)}

    queue: list[tuple[int, int, State]] = []
    start_state = State(empty_node, goal_node)
    heapq.heappush(queue, (0, next(sequence), start_state))
    visited = {start_state: 0}
    return walk_maze(Pos(0, 0), walls, visited, queue, max_x, max_y)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
