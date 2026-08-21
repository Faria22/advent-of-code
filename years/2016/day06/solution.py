from collections import Counter
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    num_cols = len(lines[0])

    message = ''
    for col in range(num_cols):
        letter_counts = Counter(line[col] for line in lines)
        message += letter_counts.most_common(1)[0][0]

    return message


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    num_cols = len(lines[0])

    message = ''
    for col in range(num_cols):
        letter_counts = Counter(line[col] for line in lines)
        message += letter_counts.most_common()[-1][0]

    return message


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
