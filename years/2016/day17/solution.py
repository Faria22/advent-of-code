import heapq
from collections.abc import Iterator
from itertools import count
from pathlib import Path

from aoc import Pos, get_hash

INPUT_PATH = Path(__file__).parent / 'input.txt'

VALID_CHARS = 'bcdef'
GRID_SIZE = 4

sequence = count()


def in_bounds(pos: Pos) -> bool:
    return all(0 <= coordinate < GRID_SIZE for coordinate in pos)


def next_moves(passcode: str, cur_moves: str, cur_pos: Pos) -> Iterator[tuple[Pos, str]]:
    cur_hash = get_hash(passcode + cur_moves)[:4]
    valid_moves = (char in VALID_CHARS for char in cur_hash)

    # valid moves and neighbors are in the same order, so we can zip them together
    for neighbor, valid_move, move_str in zip(cur_pos.neighbors(), valid_moves, 'UDLR'):
        if valid_move and in_bounds(neighbor):
            yield (neighbor, move_str)


def find_shortest(
    end: Pos,
    passcode: str,
    queue: list[tuple[int, int, str, Pos]],
) -> str:
    while queue:
        cost, _, cur_moves, pos = heapq.heappop(queue)
        if pos == end:
            return cur_moves

        for neighbor, move in next_moves(passcode, cur_moves, pos):
            heapq.heappush(queue, (cost + 1, next(sequence), cur_moves + move, neighbor))

    # Did not find the end
    raise RuntimeError


def find_longest(
    end: Pos,
    passcode: str,
    queue: list[tuple[int, int, str, Pos]],
) -> int:
    max_cost = 0
    while queue:
        cost, _, cur_moves, pos = heapq.heappop(queue)
        if pos == end:
            max_cost = max(max_cost, cost)
            continue

        for neighbor, move in next_moves(passcode, cur_moves, pos):
            heapq.heappush(queue, (cost + 1, next(sequence), cur_moves + move, neighbor))

    # Did not find the end
    return max_cost


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    passcode = parse_data(input_path)
    start = Pos(0, 0)
    queue: list[tuple[int, int, str, Pos]] = [
        (0, next(sequence), '', start),
    ]
    end = Pos(3, 3)
    return find_shortest(end, passcode, queue)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    passcode = parse_data(input_path)
    start = Pos(0, 0)
    queue: list[tuple[int, int, str, Pos]] = [
        (0, next(sequence), '', start),
    ]
    end = Pos(3, 3)
    return find_longest(end, passcode, queue)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
