import operator
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Expression(NamedTuple):
    a: str
    op: Callable
    b: str
    out: str


OPERATIONS: dict[str, Callable] = {
    'AND': operator.and_,
    'OR': operator.or_,
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift,
    'NOT': operator.invert,
}


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_val_or_wire(val: str, values: dict[str, int]) -> int | None:
    try:
        return int(val)
    except ValueError:
        if val not in values:
            return None
        return values[val]


def result(val: int) -> int:
    return val & 0xFFFF


def solve(expressions: set[str], values: dict[str, int]) -> None:
    while expressions:
        for expression in expressions:
            inputs, output = expression.split(' -> ')
            inputs = inputs.split()
            match len(inputs):
                case 1:  # Simple assignment
                    val = get_val_or_wire(inputs[0], values)
                    if val is None:
                        continue
                    values[output] = val
                case 2 if inputs[0] == 'NOT':  # NOT
                    val = get_val_or_wire(inputs[1], values)
                    if val is None:
                        continue
                    values[output] = result(~val)
                case 2:
                    raise ValueError
                case 3 if 'shift' in inputs[1].lower():
                    val = get_val_or_wire(inputs[0], values)
                    if val is None:
                        continue
                    op = OPERATIONS[inputs[1]]
                    num = int(inputs[2])
                    values[output] = result(op(val, num))
                case 3:
                    a, op, b = inputs
                    a = get_val_or_wire(a, values)
                    if a is None:
                        continue
                    b = get_val_or_wire(b, values)
                    if b is None:
                        continue

                    op = OPERATIONS[op]
                    values[output] = result(op(a, b))
                case _:
                    raise ValueError

            break
        else:
            raise RuntimeError
        expressions.remove(expression)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    expressions = set(parse_data(input_path))
    values: dict[str, int] = {}
    solve(expressions, values)

    return values['a']


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    expressions = set(parse_data(input_path))
    expressions.remove('19138 -> b')
    values: dict[str, int] = {'b': 16076}
    solve(expressions, values)

    return values['a']


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
