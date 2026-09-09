import re
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def score_groups(input_str: str) -> int:
    score = 0
    group_idx = 0
    for char in input_str:
        match char:
            case '{':
                group_idx += 1
                score += group_idx
            case '}':
                group_idx -= 1
            case _:
                raise RuntimeError
    return score


def part_one(input_str: str = parse_data(INPUT_PATH)) -> int:
    """Return the answer to part one."""
    # remove exclamation points
    input_str = re.sub(r'!.', '', input_str)

    # remove garbage
    input_str = re.sub(r'<.*?>', '', input_str)

    # remove commas
    input_str = input_str.replace(',', '')

    return score_groups(input_str)


def part_two(input_str: str = parse_data(INPUT_PATH)) -> int:
    """Return the answer to part two."""
    input_str = re.sub(r'!.', '', input_str)
    non_canceled_chars_in_garbage = ''.join(re.findall(r'<(.*?)>', input_str))
    return len(non_canceled_chars_in_garbage)


def main() -> None:
    print(f'Part 1: {part_one()}')
    print(f'Part 2: {part_two()}')


if __name__ == '__main__':
    main()
