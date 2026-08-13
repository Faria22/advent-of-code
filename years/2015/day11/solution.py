from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

BAD_CHARS_INDS = (ord('i'), ord('l'), ord('o'))
MIN_IND = ord('a')
MAX_IND = ord('z')


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def allowed_password(password: list[int]) -> bool:
    if any(ind in password for ind in BAD_CHARS_INDS):
        return False

    if not any(
        char + 1 == password[idx + 1] and char + 2 == password[idx + 2] for idx, char in enumerate(password[:-2])
    ):
        return False

    idx = 0
    pair_count = 0
    while idx < len(password) - 1:
        if password[idx] == password[idx + 1]:
            pair_count += 1
            idx += 1
        idx += 1

    return pair_count > 1


def increase_password(password: list[int]) -> None:
    len_password = len(password)

    for idx in reversed(range(len_password)):
        password[idx] += 1
        if password[idx] > MAX_IND:
            password[idx] = MIN_IND
        else:
            break

    # Skips bad letters fast
    for idx in range(len_password):
        if password[idx] in BAD_CHARS_INDS:
            password[idx] += 1
            for j in range(idx + 1, len_password):
                password[j] = MIN_IND
            break


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    initial_password = parse_data(input_path)
    password = [ord(char) for char in initial_password]
    increase_password(password)
    while not allowed_password(password):
        increase_password(password)
    while not allowed_password(password):
        increase_password(password)
    return ''.join(chr(p) for p in password)


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    password = [ord(char) for char in 'cqjxxyzz']
    increase_password(password)
    while not allowed_password(password):
        increase_password(password)
    return ''.join(chr(p) for p in password)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
