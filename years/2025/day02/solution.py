from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def is_invalid(number: int, count: int = -1) -> bool:
    pattern = ''
    str_number = str(number)
    len_str = len(str_number)
    # only goes up to half of the digits, since the pattern couldn't be made up by more than that
    for i in str_number[: -len_str // 2]:
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
            # numbers need to have an even number of digits since the pattern appears twice
            if len(str(number)) % 2 != 0:
                continue
            if is_invalid(number, count=2):
                total += number
    return total


def part_two(data: str) -> int:
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
