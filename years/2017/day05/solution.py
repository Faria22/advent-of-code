from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[int]:
    return [int(num) for num in input_path.read_text().strip().split('\n')]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    instructions = parse_data(input_path)
    num_instructions = len(instructions)
    instructions = dict(enumerate(instructions))
    num_steps = 0
    idx = 0
    while idx < num_instructions:
        num_steps += 1
        jump = instructions[idx]
        instructions[idx] += 1
        idx += jump

    return num_steps


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    instructions = parse_data(input_path)
    num_instructions = len(instructions)
    instructions = dict(enumerate(instructions))
    num_steps = 0
    idx = 0
    while idx < num_instructions:
        num_steps += 1
        jump = instructions[idx]
        if jump >= 3:  # ruff: ignore[magic-value-comparison]
            instructions[idx] -= 1
        else:
            instructions[idx] += 1
        idx += jump

    return num_steps


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
