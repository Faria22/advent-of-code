from collections import Counter
from itertools import combinations
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    valid_passphrases = 0
    for line in lines:
        if Counter(line.split()).most_common(1)[0][1] == 1:
            valid_passphrases += 1
    return valid_passphrases


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    valid_passphrases = 0
    for line in lines:
        letter_counts_per_word = [Counter(word) for word in line.split()]
        if all(a != b for a, b in combinations(letter_counts_per_word, 2)):
            valid_passphrases += 1
    return valid_passphrases


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
