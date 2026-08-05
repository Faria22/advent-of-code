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


def find_shortcuts(
    path: list[Pos],
    min_shortcut: int,
    max_dist: int,
) -> int:
    cheats = 0
    times = {pos: time for time, pos in enumerate(path)}
    offsets = tuple(
        (row_shift, col_shift, abs(row_shift) + abs(col_shift))
        for row_shift in range(-max_dist, max_dist + 1)
        for col_shift in range(-(max_dist - abs(row_shift)), max_dist - abs(row_shift) + 1)
        if row_shift or col_shift  # to skip 0,0
    )
    for start_cheat, start_time in times.items():
        for row_shift, col_shift, distance in offsets:
            end_cheat = start_cheat.shift(row_shift, col_shift)

            end_time = times.get(end_cheat)
            if end_time is None:
                continue

            time_save = end_time - (start_time + distance)
            if time_save >= min_shortcut:
                cheats += 1
    return cheats


def get_path(start: Pos, end: Pos, walls: set[Pos]) -> list[Pos]:
    path = [start]
    current = start

    while current != end:
        next_positions = [
            neighbor for neighbor in current.neighbors() if neighbor not in walls and neighbor not in path
        ]
        assert len(next_positions) == 1

        current = next_positions[0]
        path.append(current)

    return path


def part_one(input_path: Path, min_shortcut: int = 100) -> int:
    """Return the answer to part one."""
    start, end, walls = parse_data(input_path)

    path = get_path(start, end, walls)
    return find_shortcuts(path, min_shortcut, 2)


def part_two(input_path: Path, min_shortcut: int = 100) -> int:
    """Return the answer to part two."""
    start, end, walls = parse_data(input_path)

    path = get_path(start, end, walls)
    return find_shortcuts(path, min_shortcut, 20)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
