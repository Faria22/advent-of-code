from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def step(string: str) -> str:
    if len(string) == 1:
        return f'1{string}'

    prev_char = string[0]
    count = 1
    new_string = ''
    for char in string[1:]:
        if char != prev_char:
            new_string += f'{count}{prev_char}'
            count = 1
        else:
            count += 1
        prev_char = char
    new_string += f'{count}{prev_char}'
    return new_string


def part_one(input_path: Path, steps: int = 40) -> int:
    """Return the answer to part one."""
    start = parse_data(input_path)
    for _ in range(steps):
        start = step(start)
    return len(start)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    start = parse_data(input_path)
    for _ in range(50):
        start = step(start)
    return len(start)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
