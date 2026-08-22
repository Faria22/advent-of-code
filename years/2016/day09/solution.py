import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def decompress_line_length(line: str) -> int:
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    new_line_len = 0
    while line:
        match = pattern.search(line)
        if match is None:
            new_line_len += len(line)
            line = ''
            continue

        before, after = line[: match.start()], line[match.end() :]
        num_chars, num_times = int(match[1]), int(match[2])

        new_line_len += len(before)
        new_line_len += num_chars * num_times
        line = after[num_chars:]

    return new_line_len


def decompress_line_length_v2(line: str) -> int:
    pattern = re.compile(r'\((\d+)x(\d+)\)')
    new_line_len = 0
    while line:
        match = pattern.search(line)
        if match is None:
            new_line_len += len(line)
            line = ''
            continue

        before, after = line[: match.start()], line[match.end() :]
        num_chars, num_times = int(match[1]), int(match[2])

        new_line_len += len(before)
        new_line_len += num_times * decompress_line_length_v2(after[:num_chars])
        line = after[num_chars:]

    return new_line_len


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    line = parse_data(input_path)
    return decompress_line_length(line)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    line = parse_data(input_path)
    return decompress_line_length_v2(line)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
