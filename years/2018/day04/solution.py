from collections import Counter, defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return sorted(input_path.read_text().strip().split('\n'))


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = iter(parse_data(input_path))
    guards: dict[int, Counter] = defaultdict(Counter)
    guard_id = -1
    while line := next(lines, None):
        if 'Guard' in line:
            guard_id = int(line.split()[3][1:])
            continue
        # Guard falls asleep
        start_minute = int(line.split()[1][3:5])
        end_minute = int(next(lines).split()[1][3:5])

        guards[guard_id].update(range(start_minute, end_minute))

    sleepiest_guard_id = max(guards, key=lambda k: guards[k].total())
    most_slept_minute = guards[sleepiest_guard_id].most_common(1)[0][0]
    return sleepiest_guard_id * most_slept_minute


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = iter(parse_data(input_path))
    guards: dict[int, Counter] = defaultdict(Counter)
    guard_id = -1
    while line := next(lines, None):
        if 'Guard' in line:
            guard_id = int(line.split()[3][1:])
            continue
        # Guard falls asleep
        start_minute = int(line.split()[1][3:5])
        end_minute = int(next(lines).split()[1][3:5])

        guards[guard_id].update(range(start_minute, end_minute))

    sleepiest_guard_id = max(guards, key=lambda k: guards[k].most_common(1)[0][1])
    most_slept_minute = guards[sleepiest_guard_id].most_common(1)[0][0]
    return sleepiest_guard_id * most_slept_minute


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
