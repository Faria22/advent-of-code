import hashlib
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    key = parse_data(input_path)
    num = 1
    while not hashlib.md5((key + str(num)).encode()).hexdigest().startswith('00000'):
        num += 1
    return num


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    key = parse_data(input_path)
    num = 1
    while not hashlib.md5((key + str(num)).encode()).hexdigest().startswith('000000'):
        num += 1
    return num


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
