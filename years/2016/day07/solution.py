import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    pattern = re.compile(r'(\[?)\w*(\w)(?!\2)(\w)\3\2')

    ip_counts = 0
    for line in lines:
        matches = pattern.findall(line)
        if not any(match[0] == '[' for match in matches) and any(match[0] != '[' for match in matches):
            ip_counts += 1
    return ip_counts


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    pattern = re.compile(r'(?=([a-z])(?!\1)([a-z])\1)')

    ip_counts = 0
    for line in lines:
        sections = re.split(r'[\[\]]', line)
        outside_sections = sections[::2]
        inside_sections = sections[1::2]

        outside_matches = []
        for section in outside_sections:
            outside_matches.extend(match for match in pattern.findall(section) if match)

        inside_matches = []
        for section in inside_sections:
            inside_matches.extend(match for match in pattern.findall(section) if match)

        if any(a == d and b == c for a, b in outside_matches for c, d in inside_matches):
            ip_counts += 1

    return ip_counts


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
