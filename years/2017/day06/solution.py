import operator
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Banks = tuple[int, ...]


def parse_data(input_path: Path) -> Banks:
    return tuple(int(n) for n in input_path.read_text().strip().split())


def next_state(banks: Banks) -> Banks:
    num_banks = len(banks)
    max_idx, max_val = max(enumerate(banks), key=operator.itemgetter(1))

    overall_shift, partial_shift = divmod(max_val, num_banks)

    new_banks = [num + overall_shift if idx != max_idx else overall_shift for idx, num in enumerate(banks)]

    spaces_to_the_right = num_banks - max_idx - 1
    shift_to_the_right = partial_shift
    if partial_shift > spaces_to_the_right:
        wraped_shift = partial_shift - spaces_to_the_right
        shift_to_the_right -= wraped_shift
        for i in range(wraped_shift):
            new_banks[i] += 1

    # Does the spaces to the right
    for i in range(max_idx + 1, max_idx + 1 + shift_to_the_right):
        new_banks[i] += 1

    return tuple(new_banks)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    banks = parse_data(input_path)
    num_steps = 0
    seen_banks = set()
    while banks not in seen_banks:
        seen_banks.add(banks)
        num_steps += 1
        banks = next_state(banks)
    return num_steps


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    banks = parse_data(input_path)
    seen_banks = set()
    while banks not in seen_banks:
        seen_banks.add(banks)
        banks = next_state(banks)

    target_banks = banks
    num_steps = 1
    banks = next_state(banks)
    while banks != target_banks:
        num_steps += 1
        banks = next_state(banks)
    return num_steps


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
