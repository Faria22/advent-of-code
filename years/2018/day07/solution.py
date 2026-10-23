from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[str, str]]:
    step_requirements = []
    for line in input_path.read_text().strip().split('\n'):
        parts = line.split()
        step_requirements.append((parts[1], parts[7]))

    return step_requirements


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    step_requirement_pairs = parse_data(input_path)
    step_requirements: dict[str, list[str]] = defaultdict(list)
    for a, b in step_requirement_pairs:
        step_requirements[a]  # just creates the empty list if a does not have any requirements
        step_requirements[b].append(a)

    step_order = ''
    while step_requirements:
        unblocked = min(step for step, requirements in step_requirements.items() if not requirements)
        step_order += unblocked

        del step_requirements[unblocked]
        for requirements in step_requirements.values():
            if unblocked in requirements:
                requirements.remove(unblocked)

    return step_order


def part_two(input_path: Path, max_num_workers: int = 5, step_duration: int = 60) -> int:
    """Return the answer to part two."""
    step_requirement_pairs = parse_data(input_path)
    step_requirements: dict[str, list[str]] = defaultdict(list)
    for a, b in step_requirement_pairs:
        step_requirements[a]  # just creates the empty list if a does not have any requirements
        step_requirements[b].append(a)

    total_time = -1
    workers: dict[str, int] = {}
    step_order = ''
    while step_requirements:
        total_time += 1

        finished = ''
        for step in workers:  # ruff: ignore[dict-index-missing-items]
            workers[step] -= 1
            if workers[step] == 0:
                finished += step

        for step in finished:
            step_order += step
            del workers[step]
            del step_requirements[step]
            for requirements in step_requirements.values():
                if step in requirements:
                    requirements.remove(step)

        num_available_workers = max_num_workers - len(workers)
        if not num_available_workers:
            continue

        unblocked = sorted(step
            for step, requirements in step_requirements.items()
            if not requirements)[:num_available_workers]

        for step in unblocked:
            if step not in workers:
                workers[step] = ord(step) - ord('A') + step_duration + 1

    return total_time


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
