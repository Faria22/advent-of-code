import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    num = parse_data(input_path)
    num += num[0]
    pattern = re.compile(r'(?=(\d)\1)')
    return sum(int(match) for match in pattern.findall(num))


def get_shifted_char(input_str: str, idx: int) -> str:
    input_len = len(input_str)
    shift = input_len // 2
    new_idx = (idx + shift) % input_len
    return input_str[new_idx]


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    num = parse_data(input_path)
    return sum(int(char) for idx, char in enumerate(num) if char == get_shifted_char(num, idx))


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
