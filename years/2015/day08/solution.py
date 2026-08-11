from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_string(string: str) -> str:
    return string.encode().decode('unicode_escape')[1:-1]


def encode_string(string: str) -> str:
    return f'"{string.replace("\\", "\\\\").replace('"', r"\"")}"'


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    return sum(len(line) - len(parse_string(line)) for line in lines)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    return sum(len(encode_string(line)) - len(line) for line in lines)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
