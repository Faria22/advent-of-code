from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Range:
    start: int
    end: int

    def __iter__(self) -> Iterator[int]:
        yield self.start
        yield self.end


def add_range(ranges: list[Range], r: tuple[int, int]) -> None:
    """Assuming that we add ranges where the start is sorted"""
    for idx, (start, end) in enumerate(ranges):
        # r is fully inside an existing range
        if all(start <= v <= end for v in r):
            return

        # r start inside the current range but ends after
        if start <= r[0] <= end + 1:
            ranges[idx].end = max(ranges[idx].end, r[1])
            return

    # r is outside any previous range
    ranges.append(Range(*r))


def parse_data(input_path: Path) -> list[tuple[int, int]]:
    ranges = []
    for line in input_path.read_text().strip().split('\n'):
        a, b = line.split('-')
        ranges.append((int(a), int(b)))
    return sorted(ranges)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    raw_ranges = parse_data(input_path)
    ranges = []
    for r in raw_ranges:
        add_range(ranges, r)

    lowest_range = ranges[0]
    return 1 if lowest_range.start > 1 else lowest_range.end + 1


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    raw_ranges = parse_data(input_path)
    ranges = []
    for r in raw_ranges:
        add_range(ranges, r)

    number_of_ips = 4294967296
    for r in ranges:
        number_of_ips -= r.end - r.start + 1
    return number_of_ips


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
