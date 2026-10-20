from itertools import cycle
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    data = parse_data(input_path)
    return sum(int(line) for line in data)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)
    freq_changes = cycle(int(line) for line in data)
    freq = 0
    seen_freqs = {freq}
    for change in freq_changes:
        freq += change
        if freq in seen_freqs:
            return freq
        seen_freqs.add(freq)

    return -1


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
