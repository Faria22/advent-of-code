import operator
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Expression(NamedTuple):
    a: str
    op: str
    b: str
    out: str


OPERATIONS: dict[str, Callable] = {
    'AND': operator.and_,
    'OR': operator.or_,
    'XOR': operator.xor,
}


def parse_data(input_path: Path) -> tuple[dict[str, int], set[Expression]]:
    inputs, expression_lines = input_path.read_text().strip().split('\n\n')

    gates = {}
    for line in inputs.split('\n'):
        gate, val = line.split(': ')
        gates[gate] = int(val)

    expressions = set()
    for line in expression_lines.split('\n'):
        a, op, b, _, out = line.split()
        expressions.add(Expression(a, op, b, out))

    return gates, expressions


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    inputs, expressions = parse_data(input_path)
    while expressions:
        for expression in expressions:
            a, op, b, out = expression
            if a in inputs and b in inputs:
                inputs[out] = OPERATIONS[op](inputs[a], inputs[b])
                break
        expressions.remove(expression)

    num_z = sum(1 for input_ in inputs if input_[0] == 'z')
    output_str = '0b'
    for i in reversed(range(num_z)):
        output_str += str(inputs[f'z{i:02}'])
    return int(output_str, 0)


def is_start_wire(wire: str) -> bool:
    return wire.startswith(('x', 'y'))


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    _, expressions = parse_data(input_path)
    bad_wires = set()
    max_z = max(output for _, _, _, output in expressions if output.startswith('z'))

    for left, op, right, output in expressions:
        # Every z output except the final carry must come from XOR.
        if output.startswith('z') and output != max_z and op != 'XOR':
            bad_wires.add(output)

        # XOR expressions that are neither direct x/y XORs nor z outputs
        # should not exist in a ripple-carry adder.
        if op == 'XOR':
            direct_input_xor = is_start_wire(left) and is_start_wire(right)

            if not direct_input_xor and not output.startswith('z'):
                bad_wires.add(output)

        # Direct x/y XORs should feed another XOR,
        # except x00 XOR y00 which directly produces z00.
        if op == 'XOR' and is_start_wire(left) and is_start_wire(right) and left != 'x00' and right != 'x00':
            used_by_xor = any(
                next_op == 'XOR' and output in {next_left, next_right}
                for next_left, next_op, next_right, _ in expressions
            )

            if not used_by_xor:
                bad_wires.add(output)

        # x/y AND results should eventually participate in the carry OR.
        # Bit 0 is special because x00 AND y00 is the initial carry.
        if op == 'AND' and is_start_wire(left) and is_start_wire(right) and left != 'x00' and right != 'x00':
            used_by_or = any(
                next_op == 'OR' and output in {next_left, next_right}
                for next_left, next_op, next_right, _ in expressions
            )

            if not used_by_or:
                bad_wires.add(output)

        # Every other AND should also feed an OR.
        if op == 'AND' and not (is_start_wire(left) and is_start_wire(right)):
            used_by_or = any(
                next_op == 'OR' and output in {next_left, next_right}
                for next_left, next_op, next_right, _ in expressions
            )

            if not used_by_or:
                bad_wires.add(output)

    return ','.join(sorted(bad_wires))


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
