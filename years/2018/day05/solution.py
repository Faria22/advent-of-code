import re
import string
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

PATTERN = re.compile('|'.join(f'{c}{c.upper()}|{c.upper()}{c}' for c in string.ascii_lowercase))


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def full_reaction(polymer: str) -> str:
    while polymer != (next_polymer := PATTERN.sub('', polymer)):
        polymer = next_polymer
    return polymer


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    polymer = parse_data(input_path)
    return len(full_reaction(polymer))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    polymer = parse_data(input_path)
    polymer = full_reaction(polymer)
    min_polymer_size = len(polymer)
    for c in string.ascii_lowercase:
        new_polymer = re.sub(f'{c}|{c.upper()}', '', polymer)
        min_polymer_size = min(min_polymer_size, len(full_reaction(new_polymer)))
    return min_polymer_size


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
