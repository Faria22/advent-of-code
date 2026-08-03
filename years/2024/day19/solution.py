from functools import cache
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> tuple[tuple[str, ...], list[str]]:
    patterns, designs = input_path.read_text().strip().split('\n\n')

    patterns = tuple(patterns.split(', '))
    designs = designs.split('\n')

    return patterns, designs


@cache
def can_be_built(design: str, patterns: tuple[str, ...]) -> int:
    if not design:
        return 1

    num_options = 0
    for pattern in patterns:
        if design.startswith(pattern):
            num_options += can_be_built(design[len(pattern) :], patterns)

    return num_options


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    patterns, designs = parse_data(input_path)

    possible_designs_count = 0
    for design in designs:
        if can_be_built(design, patterns):
            possible_designs_count += 1
    return possible_designs_count


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    patterns, designs = parse_data(input_path)

    num_options = 0
    for design in designs:
        num_options += can_be_built(design, patterns)
    return num_options


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
