from itertools import batched
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def dragon_curve(a: str) -> str:
    b = a[::-1]
    trans_map = str.maketrans({'0': '1', '1': '0'})
    b = b.translate(trans_map)
    return a + '0' + b


def get_checksum(state: str) -> str:
    checksum = ''
    for a, b in batched(state, 2):
        checksum += '1' if a == b else '0'
    return checksum


def part_one(input_path: Path, disk_size: int = 272) -> str:
    """Return the answer to part one."""
    state = parse_data(input_path)
    while len(state) < disk_size:
        state = dragon_curve(state)
    state = state[:disk_size]

    checksum = get_checksum(state)
    while len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)
    return checksum


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    state = parse_data(input_path)

    disk_size = 35651584
    while len(state) < disk_size:
        state = dragon_curve(state)
    state = state[:disk_size]

    checksum = get_checksum(state)
    while len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)
    return checksum


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
