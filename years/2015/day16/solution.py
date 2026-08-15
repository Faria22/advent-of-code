from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


type Aunt = dict[str, int]


CORRECT_AUNT = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_aunt(line: str) -> Aunt:
    parameters = line.split(': ', 1)[1]
    return {key.strip(): int(value) for item in parameters.split(',') for key, value in [item.split(':', 1)]}


def aunts_match(aunt: Aunt) -> bool:
    return all(aunt[key] == CORRECT_AUNT[key] for key in aunt)


def aunts_match_updated(aunt: Aunt) -> bool:
    max_value = max(CORRECT_AUNT.values()) + 1
    for key in ('cats', 'trees'):
        if aunt.get(key, max_value) <= CORRECT_AUNT[key]:
            return False

    for key in ('pomeranians', 'goldfish'):
        if aunt.get(key, 0) >= CORRECT_AUNT[key]:
            return False

    for key in ('cats', 'trees', 'pomeranians', 'goldfish'):
        aunt.pop(key, None)

    return all(aunt[key] == CORRECT_AUNT[key] for key in aunt)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    for idx, line in enumerate(lines, 1):
        aunt = parse_aunt(line)
        if aunts_match(aunt):
            return idx

    return 0


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    for idx, line in enumerate(lines, 1):
        aunt = parse_aunt(line)
        if aunts_match_updated(aunt):
            return idx

    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
