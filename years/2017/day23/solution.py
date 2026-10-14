from collections import defaultdict
from math import isqrt
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_val(x: str, registers: dict[str, int]) -> int:
    """Get a value from x regardless if it is a literal or register."""
    try:
        return int(x)
    except ValueError:
        return registers[x]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    instructions = parse_data(input_path)
    num_instructions = len(instructions)
    registers: dict[str, int] = defaultdict(int)

    mul_count = 0
    idx = 0
    while 0 <= idx < num_instructions:
        instruction_parts = instructions[idx].split()
        x_name = instruction_parts[1]
        x = get_val(x_name, registers)
        match instruction_parts[0]:
            case 'set':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] = y
            case 'sub':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] -= y
            case 'mul':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] *= y
                mul_count += 1
            case 'jnz':
                y = get_val(instruction_parts[2], registers)
                if x != 0:
                    idx += y - 1
            case _:
                raise RuntimeError(f'Unknown instruction: {instructions[idx]}')
        idx += 1

    return mul_count


def is_composite(num: int) -> bool:
    return any(num % i == 0 for i in range(2, isqrt(num) + 1))


def part_two() -> int:
    """Return the answer to part two."""
    num_composites = 0
    b = 84 * 100 + 100_000
    c = b + 17_000
    for i in range(b, c + 1, 17):
        if is_composite(i):
            num_composites += 1
    return num_composites


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two()}')


if __name__ == '__main__':
    main()
