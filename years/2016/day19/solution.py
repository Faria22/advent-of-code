from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    num_elfs = parse_data(input_path)
    power = num_elfs.bit_length() - 1
    d = num_elfs - 2**power
    return 2 * d + 1


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    num_elfs = parse_data(input_path)
    max_power = 0
    while 3**max_power <= num_elfs:
        max_power += 1
    return num_elfs - 3 ** (max_power - 1)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
