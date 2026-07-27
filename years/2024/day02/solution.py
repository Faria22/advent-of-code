from itertools import pairwise
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

MIN_DIFF, MAX_DIFF = 1, 3


def check_same_sign(diff: list[int]) -> bool:
    return all(d > 0 for d in diff) | all(d < 0 for d in diff)


def check_within_bounds(diff: list[int]) -> bool:
    return all(MIN_DIFF <= abs(d) <= MAX_DIFF for d in diff)


def get_diff(report: list[int]) -> list[int]:
    return [l1 - l2 for l1, l2 in pairwise(report)]


def parse_data(input_file: Path) -> tuple[list[list[int]], list[list[int]], list[bool], list[bool]]:
    reports = [[int(level) for level in line.split()] for line in input_file.read_text().rstrip('\n').split('\n')]
    diff = [get_diff(report) for report in reports]

    same_sign = [check_same_sign(d) for d in diff]

    within_bounds = [check_within_bounds(d) for d in diff]
    return reports, diff, same_sign, within_bounds


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    _reports, _diff, same_sign, within_bounds = parse_data(input_path)
    return sum(s & w for s, w in zip(same_sign, within_bounds, strict=True))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    reports, _diff, same_sign, within_bounds = parse_data(input_path)

    safe_count = 0
    for r, s, w in zip(reports, same_sign, within_bounds, strict=True):
        if s & w:
            safe_count += 1
        else:
            for level_idx in range(len(r)):
                new_r = r[:level_idx] + r[level_idx + 1 :]
                new_d = get_diff(new_r)
                if check_same_sign(new_d) & check_within_bounds(new_d):
                    safe_count += 1
                    break

    return safe_count


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
