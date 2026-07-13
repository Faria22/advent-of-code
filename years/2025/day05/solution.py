import operator
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_input(data: str) -> tuple[list[tuple], set[int]]:
    fresh_id_ranges, available_ids = data.split('\n\n')

    fresh_ids = []
    for r in fresh_id_ranges.split('\n'):
        start, end = r.split('-')
        fresh_ids.append((int(start), int(end) + 1))

    available_ids = {int(a_id) for a_id in available_ids.split('\n')}

    return fresh_ids, available_ids


def part_one(fresh_ids: list[tuple], available_ids: set[int]) -> int:
    """Return the answer to part one."""
    total = 0
    for available_id in available_ids:
        if any(available_id in range(*fresh_id) for fresh_id in fresh_ids):
            total += 1

    return total


def part_two(fresh_ids: list[tuple]) -> int:
    """Return the answer to part two."""
    fresh_ids.sort(key=operator.itemgetter(0))
    consolidaded_ids = [fresh_ids[0]]

    i = 1
    while i < len(fresh_ids):
        start, end = consolidaded_ids[-1]
        next_start, next_end = fresh_ids[i]
        if end - 1 >= next_start:
            consolidaded_ids[-1] = (start, max(end, next_end))
        else:
            consolidaded_ids.append((next_start, next_end))

        i += 1

    return sum(len(range(*fresh_id)) for fresh_id in consolidaded_ids)


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    fresh_ids, available_ids = parse_input(data)
    print(f'Part 1: {part_one(fresh_ids, available_ids)}')
    print(f'Part 2: {part_two(fresh_ids)}')


if __name__ == '__main__':
    main()
