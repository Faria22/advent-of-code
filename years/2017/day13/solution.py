from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> dict[int, int]:
    layers = {}
    for line in input_path.read_text().strip().split('\n'):
        depth, range_ = line.split(': ')
        layers[int(depth)] = int(range_)
    return layers


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    layers = parse_data(input_path)
    severity = 0
    for depth, range_ in layers.items():
        # times two because it has to go and come back, and since we only care about it being at the beginning,
        # it's exact position is not relevant
        scanner_position = depth % ((range_ - 1) * 2)
        if scanner_position == 0:
            severity += depth * range_
    return severity


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    layers = parse_data(input_path)
    time = 1
    while True:
        if all((time + depth) % ((range_ - 1) * 2) != 0 for depth, range_ in layers.items()):
            return time
        time += 1


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
