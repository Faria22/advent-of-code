from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent / 'input.txt'

INITIAL_DIAL_VALUE = 50
MAX_DIAL_VALUE = 100


def parse_input_line(line: str) -> int:
    """Parse a line of input into an integer."""
    if line.lower().startswith('r'):
        return int(line[1:])

    return -int(line[1:])


def move_dial_part_one(initial: int, movement: int) -> int:
    """Gets the final location of the dial.

    `initial`: is the initial position
    `movement` is the movement of the dial. Negative values correspond to left, positive corresponds to right.

    Returns the final position of the dial.
    """

    movement %= MAX_DIAL_VALUE  # Get net change of position if movement would wrap around the dial

    final = initial + movement

    final %= MAX_DIAL_VALUE  # Wrap around the dial if necessary

    return final


def part_one(data: str) -> int:
    """Return the answer to part one."""
    initial = INITIAL_DIAL_VALUE
    zero_count = 0
    for line in data.split('\n'):
        movement = parse_input_line(line)
        initial = move_dial_part_one(initial, movement)

        if initial == 0:
            zero_count += 1

    return zero_count


def move_dial_part_two(initial: int, movement: int) -> tuple[int, int]:
    """Gets the final location of the dial while counting how many times it passes through *0*.

    `initial`: is the initial position
    `movement` is the movement of the dial. Negative values correspond to left, positive corresponds to right.

    Returns the final position of the dial and how many times it goes over 0.
    """
    final = initial + movement

    # ABS because final might be negative
    zero_count = abs(final) // MAX_DIAL_VALUE

    # Add count if dial goes through zero with L movement
    if final <= 0 and initial > 0:
        zero_count += 1

    final %= MAX_DIAL_VALUE

    return final, zero_count


def part_two(data: str) -> int:
    initial = INITIAL_DIAL_VALUE
    total_zero_count = 0
    for line in data.split('\n'):
        movement = parse_input_line(line)
        initial, zero_count = move_dial_part_two(initial, movement)

        total_zero_count += zero_count

    return total_zero_count


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
