from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[int, int, int]]:
    lines = input_path.read_text().strip().split('\n')

    dimensions = []
    for line in lines:
        x, y, z = line.split('x')
        dimensions.append((int(x), int(y), int(z)))

    return dimensions


def required_paper(dimentions: tuple[int, int, int]) -> int:
    x, y, z = dimentions
    area = 2 * x * y + 2 * x * z + 2 * y * z
    extra = min(x * y, x * z, y * z)
    return area + extra


def required_ribbon(dimentions: tuple[int, int, int]) -> int:
    x, y, z = dimentions
    volume = x * y * z
    extra = 2 * min(x + y, x + z, y + z)
    return volume + extra


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    dimentions = parse_data(input_path)
    return sum(required_paper(dim) for dim in dimentions)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    dimentions = parse_data(input_path)
    return sum(required_ribbon(dim) for dim in dimentions)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
