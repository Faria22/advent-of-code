from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[list[int]]:
    return [sorted([int(n) for n in line.split()]) for line in input_path.read_text().strip().split('\n')]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    spreadsheet = parse_data(input_path)
    return sum(row[-1] - row[0] for row in spreadsheet)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    spreadsheet = parse_data(input_path)
    checksum = 0
    for row in spreadsheet:
        for idx, num_i in enumerate(reversed(row), 1):
            for num_j in row[:-idx]:
                if num_i % num_j == 0:
                    checksum += num_i // num_j
    return checksum


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
