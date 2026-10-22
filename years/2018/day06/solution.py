from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Pos = tuple[int, int]


def parse_data(input_path: Path) -> list[Pos]:
    points = []
    for line in input_path.read_text().strip().split('\n'):
        a, b = map(int, line.split(', '))
        points.append((a, b))
    return points


def is_valid_point(p: Pos, x0: int, x1: int, y0: int, y1: int) -> bool:
    return not (p[0] == x0 or p[0] == x1 or p[1] == y0 or p[1] == y1)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    points = parse_data(input_path)

    x0 = min(point[0] for point in points)
    x1 = max(point[0] for point in points)
    y0 = min(point[1] for point in points)
    y1 = max(point[1] for point in points)
    MAX_DISTANCE = x1 - x0 + y1 - y0

    areas = [0] * len(points)
    infinity_points = set()
    for x in range(x0, x1 + 1):
        x_distances = [abs(x - point[0]) for point in points]
        for y in range(y0, y1 + 1):
            min_distance = MAX_DISTANCE
            owner_idx = -1
            tied = False
            for p_idx, point in enumerate(points):
                distance = x_distances[p_idx] + abs(y - point[1])
                if distance < min_distance:
                    min_distance = distance
                    owner_idx = p_idx
                    tied = False
                elif distance == min_distance:
                    tied = True

            if tied:
                continue

            areas[owner_idx] += 1
            if not is_valid_point((x, y), x0, x1, y0, y1):
                infinity_points.add(owner_idx)

    return max(areas[idx] for idx in range(len(points)) if idx not in infinity_points)


def part_two(input_path: Path, max_distance: int = 10_000) -> int:
    """Return the answer to part two."""
    points = parse_data(input_path)

    x0 = min(point[0] for point in points)
    x1 = max(point[0] for point in points)
    y0 = min(point[1] for point in points)
    y1 = max(point[1] for point in points)

    good_pos = 0
    for x in range(x0, x1 + 1):
        total_x_distance = sum(abs(x - point[0]) for point in points)
        if total_x_distance >= max_distance:
            continue

        for y in range(y0, y1 + 1):
            total_distance = total_x_distance + sum(abs(y - point[1]) for point in points)
            if total_distance < max_distance:
                good_pos += 1

    return good_pos


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
