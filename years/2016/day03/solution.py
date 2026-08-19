from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[int, ...]]:
    triangle_sides = []
    for line in input_path.read_text().strip().split('\n'):
        sides = line.split()
        sides = tuple(int(s) for s in sides)
        triangle_sides.append(sides)

    return triangle_sides


def possible_triangle(sides: tuple[int, ...]) -> bool:
    for i, c in enumerate(sides):
        a, b = sides[:i] + sides[i + 1 :]
        if a + b <= c:
            return False
    return True


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    triangle_sides = parse_data(input_path)
    return sum(possible_triangle(sides) for sides in triangle_sides)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    original_data = parse_data(input_path)
    num_rows = len(original_data)

    possible_triangles = 0
    for col in range(3):
        idx = 0
        while idx < num_rows:
            sides = tuple(original_data[idx + i][col] for i in range(3))
            possible_triangles += 1 if possible_triangle(sides) else 0
            idx += 3

    return possible_triangles


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
