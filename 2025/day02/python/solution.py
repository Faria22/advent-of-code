from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent / 'input.txt'


def is_invalid(number: int, count: int = -1) -> bool:
    pattern = ''
    str_number = str(number)
    for i in str_number[:-1]:  # skips the last character
        pattern += i
        if not str_number.replace(pattern, '', count):
            return True
    return False


def parse_range(id_range: str) -> range:
    start, end = id_range.split('-')
    start = int(start)
    end = int(end)
    return range(start, end + 1)


def part_one(data: str) -> int:
    total = 0
    for id_range in data.split(','):
        for number in parse_range(id_range):
            if is_invalid(number, 2):
                total += number
    return total


def part_two(data: str):
    """Return the answer to part two."""
    total = 0
    for id_range in data.split(','):
        for number in parse_range(id_range):
            if is_invalid(number):
                total += number
    return total


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
