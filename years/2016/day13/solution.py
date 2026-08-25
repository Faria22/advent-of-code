import heapq
from itertools import count
from math import inf
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


sequence = count()


def is_wall(x: int, y: int, num: int) -> int:
    val = x * x + 3 * x + 2 * x * y + y + y * y + num
    return val.bit_count() % 2 == 1


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def walk_maze(
    end: Pos,
    walls: set[Pos],
    visited: dict[Pos, int],
    queue: list[tuple[int, int, Pos]],
) -> int:
    while queue:
        cost, _, pos = heapq.heappop(queue)
        if any(x < 0 for x in pos):
            continue

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

    return visited.get(end, -1)


def walk_maze_n_steps(
    walls: set[Pos],
    visited: dict[Pos, int],
    queue: list[tuple[int, int, Pos]],
    n: int,
) -> int:
    seen = set()
    while queue:
        cost, _, pos = heapq.heappop(queue)

        if cost <= n:
            seen.add(pos)

        if cost > visited.get(pos, inf):
            continue

        cost += 1
        for neighbor in pos.neighbors():
            if neighbor in walls or any(x < 0 for x in neighbor):
                continue

            prev_cost = visited.get(neighbor, inf)
            if cost < prev_cost:
                visited[neighbor] = cost
                heapq.heappush(queue, (cost, next(sequence), neighbor))

    return len(seen)


def part_one(input_path: Path, final_x: int = 31, final_y: int = 39) -> int:
    """Return the answer to part one."""
    num = parse_data(input_path)
    min_grid_size = 100
    walls = {Pos(x, y) for x in range(min_grid_size) for y in range(min_grid_size) if is_wall(x, y, num)}

    start = Pos(1, 1)
    end = Pos(final_x, final_y)

    queue: list[tuple[int, int, Pos]] = []
    heapq.heappush(queue, (0, next(sequence), start))

    visited = {start: 0}

    return walk_maze(end, walls, visited, queue)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    num = parse_data(input_path)
    min_grid_size = 60
    walls = {Pos(x, y) for x in range(min_grid_size) for y in range(min_grid_size) if is_wall(x, y, num)}

    start = Pos(1, 1)

    queue: list[tuple[int, int, Pos]] = []
    heapq.heappush(queue, (0, next(sequence), start))

    visited = {start: 0}

    return walk_maze_n_steps(walls, visited, queue, 50)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
