import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().replace('\n', '')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    data = parse_data(input_path)
    matches = re.findall(pattern, data)

    return sum(int(a) * int(b) for a, b in matches)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))"
    data = parse_data(input_path)
    matches = re.findall(pattern, data)

    total = 0
    on = True
    for a, b, c in matches:
        if on and c == "don't()":
            on = False
        elif not on and c == 'do()':
            on = True

        if on and a and b:
            total += int(a) * int(b)

    return total


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
