from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    data = parse_data(input_path)
    up = data.count('(')
    down = data.count(')')
    return up - down


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)
    cur_pos = 0
    for idx, char in enumerate(data, 1):
        if char == '(':
            cur_pos += 1
        else:
            cur_pos -= 1

        if cur_pos < 0:
            return idx

    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
