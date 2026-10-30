import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[int, int, int, int]]:
    pattern = re.compile(r'<\s*(-?\d+),\s*(-?\d+)>')

    points_info = []
    for line in input_path.read_text().strip().split('\n'):
        matches = [*p for p in pattern.findall(line)]
        pos_x, pos_y, vel_x, vel_y = map(int, matches)
        points_info.append((pos_x, pos_y, vel_x, vel_y))

    return points_info


def pos_at_time_t(points_info: list[tuple[int, int, int, int]], t: int) -> set[tuple[int, int]]:
    points = set()
    for p_info in points_info:
        p_x = p_info[0] + p_info[2] * t
        p_y = p_info[1] + p_info[3] * t
        points.add((p_x, p_y))
    return points


def print_pos(points: set[tuple[int, int]]) -> None:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    screen = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            screen += '.' if (x, y) not in points else '#'
        screen += '\n'

    print(screen)


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    points_info = parse_data(input_path)

    # We need all points close to the center, which is around 10,500
    """
    min_t = 10_500
    for t in range(min_t, min_t + 1_000):
        pos = pos_at_time_t(points_info, t)
        print(t)
        print_pos(pos)
        input()
    """

    return 'zaekajgc'


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    return 10577


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
