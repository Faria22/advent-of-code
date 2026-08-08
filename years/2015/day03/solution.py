from itertools import batched
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    moves = parse_data(input_path)
    cur_pos = Pos(0, 0)
    visited = {cur_pos}
    for move in moves:
        cur_pos = cur_pos.move(move)
        visited.add(cur_pos)

    return len(visited)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    moves = parse_data(input_path)
    santa_pos = Pos(0, 0)
    robot_pos = Pos(0, 0)
    visited = {santa_pos}
    for s_m, r_m in batched(moves, 2):
        santa_pos = santa_pos.move(s_m)
        robot_pos = robot_pos.move(r_m)
        visited.add(santa_pos)
        visited.add(robot_pos)

    return len(visited)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
