import hashlib
import re
from functools import lru_cache
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

NUM_NEEDED_KEYS = 64


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def get_hash(key: str, num: int | str = '') -> str:
    return hashlib.md5((key + str(num)).encode()).hexdigest()


@lru_cache(maxsize=1001)
def get_stretched_hash(key: str, num: int) -> str:
    stretched_hash = get_hash(key, num)
    for _ in range(2016):
        stretched_hash = get_hash(stretched_hash)
    return stretched_hash


def next_thousand_has_five_of_a_kind(char: str, key: str, num: int) -> bool:
    pattern = char * 5
    return any(pattern in get_hash(key, num + i) for i in range(1, 1001))


def next_thousand_has_five_of_a_kind_stretched(char: str, key: str, num: int) -> bool:
    pattern = char * 5
    return any(re.search(pattern, get_stretched_hash(key, num + i)) for i in range(1, 1001))


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    key = parse_data(input_path)
    num_keys = 0
    num = -1
    pattern = re.compile(r'(.)\1\1')
    while num_keys < NUM_NEEDED_KEYS:
        num += 1
        match = pattern.search(get_hash(key, num))
        if match and next_thousand_has_five_of_a_kind(match[1], key, num):
            num_keys += 1

    return num


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    key = parse_data(input_path)
    num_keys = 0
    num = -1
    pattern = re.compile(r'(.)\1\1')
    while num_keys < NUM_NEEDED_KEYS:
        num += 1
        match = pattern.search(get_stretched_hash(key, num))
        if match and next_thousand_has_five_of_a_kind_stretched(match[1], key, num):
            print(num)
            num_keys += 1

    return num


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
