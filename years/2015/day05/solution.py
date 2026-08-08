from itertools import pairwise
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def count_vowels(string: str) -> int:
    return sum(string.count(vowel) for vowel in ('a', 'e', 'i', 'o', 'u'))


def has_bad_string(string: str) -> bool:
    return any(s in string for s in ('ab', 'cd', 'pq', 'xy'))


def has_double_letter(string: str) -> bool:
    return any(a == b for a, b in pairwise(string))


def nice_string(string: str) -> bool:
    return count_vowels(string) > 2 and not has_bad_string(string) and has_double_letter(string)  # ruff: ignore[magic-value-comparison]


def contains_two_pairs(string: str) -> bool:
    for idx in range(len(string)):
        pair = string[idx : idx + 2]
        if pair in string[idx + 2 :]:
            return True
    return False


def contains_repeat_with_letter_between(string: str) -> bool:
    return any(string[idx] == string[idx + 2] for idx in range(len(string) - 2))


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    strings = parse_data(input_path)
    return sum(nice_string(string) for string in strings)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    strings = parse_data(input_path)
    return sum(contains_two_pairs(string) and contains_repeat_with_letter_between(string) for string in strings)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
