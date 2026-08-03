import heapq
from itertools import count
from math import inf
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'
sequence = count()


def parse_data(input_path: Path) -> list[Pos]:
    byte_positions = []
    for line in input_path.read_text().strip().split('\n'):
        x, y = line.split(',')
        byte_positions.append(Pos(int(x), int(y)))

    return byte_positions


def in_bounds(pos: Pos, side_len: int) -> bool:
    return all(0 <= pos[i] <= side_len for i in range(2))


def walk_maze(
    end: Pos,
    walls: set[Pos],
    visited: dict[Pos, int],
    queue: list[tuple[int, int, Pos]],
) -> int | None:
    while queue:
        cost, _, pos = heapq.heappop(queue)
        if pos == end:
            return cost

        if cost > visited.get(pos, inf):
            continue

        cost += 1
        for neighbor in pos.neighbors():
            if pos in walls:
                continue

            prev_cost = visited.get(neighbor, inf)
            if cost < prev_cost:
                visited[neighbor] = cost
                heapq.heappush(queue, (cost, next(sequence), neighbor))

    return visited.get(end)


def part_one(input_path: Path, side_len: int = 70, num_bytes: int = 1024) -> int:
    """Return the answer to part one."""
    byte_positions = parse_data(input_path)
    walls = {Pos(x, y) for x in (-1, side_len + 1) for y in range(side_len + 1)} | {
        Pos(x, y) for x in range(side_len + 1) for y in (-1, side_len + 1)
    }
    fallen_bytes = set(byte_positions[:num_bytes])

    start = Pos(0, 0)
    end = Pos(side_len, side_len)

    queue: list[tuple[int, int, Pos]] = []
    heapq.heappush(queue, (0, next(sequence), start))

    visited = {start: 0}

    output = walk_maze(end, walls | fallen_bytes, visited, queue)
    assert output is not None
    return output


def part_two(input_path: Path, side_len: int = 70, num_bytes: int = 1024) -> str:
    """Return the answer to part two."""
    byte_positions = parse_data(input_path)
    walls = {Pos(x, y) for x in (-1, side_len + 1) for y in range(side_len + 1)} | {
        Pos(x, y) for x in range(side_len + 1) for y in (-1, side_len + 1)
    }
    start = Pos(0, 0)
    end = Pos(side_len, side_len)

    fallen_bytes = set(byte_positions[:num_bytes])
    for next_byte in byte_positions[num_bytes:]:
        fallen_bytes.add(next_byte)
        queue: list[tuple[int, int, Pos]] = []
        heapq.heappush(queue, (0, next(sequence), start))
        visited = {start: 0}
        output = walk_maze(end, walls | fallen_bytes, visited, queue)
        if output is None:
            return f'{next_byte.row},{next_byte.col}'

    return ''


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
