from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

WALL_CHAR = '#'
START_CHAR = 'S'
END_CHAR = 'E'


def parse_data(input_path: Path) -> tuple[Pos, Pos, set[Pos]]:
    start = end = None
    walls = set()
    for row, line in enumerate(input_path.read_text().strip().split('\n')):
        for col, cell in enumerate(line):
            if cell == WALL_CHAR:
                walls.add(Pos(row, col))
            elif cell == START_CHAR:
                start = Pos(row, col)
            elif cell == END_CHAR:
                end = Pos(row, col)

    assert start is not None
    assert end is not None
    return start, end, walls


def get_neighbors_with_n_moves(pos: Pos, n: int) -> set[Pos]:
    neighbors = set()
    for i in range(-n, n + 1):
        j_size = n - abs(i)
        neighbors.update(pos.shift(i, j) for j in range(-j_size, j_size + 1))
    neighbors.remove(pos)
    return neighbors


def distance(start: Pos, end: Pos) -> int:
    return abs(start.row - end.row) + abs(start.col - end.col)


def find_shortcuts(
    path: dict[Pos, int],
    min_shortcut: int,
    max_dist: int,
) -> int:
    cheats: list[tuple[Pos, Pos]] = []
    for start_cheat, start_time in path.items():
        for end_cheat, end_time in path.items():
            if start_cheat == end_cheat:
                continue

            d = distance(start_cheat, end_cheat)
            if d > max_dist:
                continue

            time_save = end_time - (start_time + d)
            if time_save >= min_shortcut:
                cheats.append((start_cheat, end_cheat))
    return len(cheats)


def get_path(start: Pos, end: Pos, walls: set[Pos]) -> dict[Pos, int]:
    path = {start: 0}
    current = start

    while current != end:
        next_positions = [
            neighbor for neighbor in current.neighbors() if neighbor not in walls and neighbor not in path
        ]
        assert len(next_positions) == 1

        current = next_positions[0]
        path[current] = len(path)

    return path


def part_one(input_path: Path, min_shortcut: int = 100) -> int:
    """Return the answer to part one."""
    start, end, walls = parse_data(input_path)

    path: dict[Pos, int] = get_path(start, end, walls)
    return find_shortcuts(path, min_shortcut, 2)


def part_two(input_path: Path, min_shortcut: int = 100) -> int:
    """Return the answer to part two."""
    start, end, walls = parse_data(input_path)

    path: dict[Pos, int] = get_path(start, end, walls)
    return find_shortcuts(path, min_shortcut, 20)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
