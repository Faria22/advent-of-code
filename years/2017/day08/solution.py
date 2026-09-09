import operator
from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_instruction(instruction: str) -> tuple[str, int, str]:
    register, sign, shift, _, condition = instruction.split(maxsplit=4)

    shift = int(shift)
    if sign == 'dec':
        shift = -shift

    return register, shift, condition


def evaluate_condition(condition: str, registers: defaultdict[str, int]) -> bool:
    op_map = {
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
    }

    register, op, val = condition.split()
    val = int(val)

    return op_map[op](registers[register], val)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    instructions = parse_data(input_path)
    registers = defaultdict(int)
    for instruction in instructions:
        register, shift, condition = parse_instruction(instruction)
        if evaluate_condition(condition, registers):
            registers[register] += shift

    return max(registers.values())


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    instructions = parse_data(input_path)
    registers = defaultdict(int)
    max_val = 0
    for instruction in instructions:
        register, shift, condition = parse_instruction(instruction)
        if evaluate_condition(condition, registers):
            registers[register] += shift

        max_val = max(max_val, *registers.values())

    return max_val


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
