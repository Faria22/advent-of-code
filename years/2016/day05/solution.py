import hashlib
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


PASSWORD_LEN = 8


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    key = parse_data(input_path)
    password = ''

    num = 1
    for _ in range(PASSWORD_LEN):
        while not (hash_str := hashlib.md5((key + str(num)).encode()).hexdigest()).startswith('00000'):
            num += 1

        password += hash_str[5]
        num += 1

    return password


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    key = parse_data(input_path)
    password = [''] * PASSWORD_LEN

    num = 1
    seen = set()
    while len(seen) != PASSWORD_LEN:
        while not (hash_str := hashlib.md5((key + str(num)).encode()).hexdigest()).startswith('00000'):
            num += 1

        idx, val = hash_str[5:7]
        try:
            if 0 <= (idx := int(idx)) < PASSWORD_LEN and idx not in seen:
                seen.add(idx)
                password[idx] = val
        except ValueError:
            pass

        num += 1

    return ''.join(password)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
