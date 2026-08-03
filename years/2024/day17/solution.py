from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ins_pointer = 0

    @staticmethod
    def _literal(val: int) -> int:
        return val

    def _combo(self, val: int) -> int:
        match val:
            case x if 0 <= x <= 3:  # ruff: ignore[magic-value-comparison]
                return val
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise ValueError

    def _adv(self, inp: int) -> int:
        return self.a // 2 ** self._combo(inp)

    def _jump(self, val: int) -> None:
        self.ins_pointer = val

    def _run_instruction(self) -> str | None:
        ins = self.program[self.ins_pointer]
        inp = self.program[self.ins_pointer + 1]

        output = None
        match ins:
            case 0:
                self.a = self._adv(inp)
            case 1:
                self.b ^= self._literal(inp)
            case 2:
                self.b = self._combo(inp) % 8
            case 3:
                if self.a != 0:
                    self._jump(inp)
                    return None
            case 4:
                self.b ^= self.c
            case 5:
                output = str(self._combo(inp) % 8)
            case 6:
                self.b = self._adv(inp)
            case 7:
                self.c = self._adv(inp)

        self.ins_pointer += 2
        return output

    def run_program(self) -> str:
        len_program = len(self.program)
        final_output = []
        while self.ins_pointer < len_program:
            output = self._run_instruction()
            if output is not None:
                final_output.append(output)

        return ','.join(final_output)


def parse_data(input_path: Path) -> Computer:
    a, b, c, _, p = input_path.read_text().strip().split('\n')

    a = int(a.split()[-1])
    b = int(b.split()[-1])
    c = int(c.split()[-1])

    p = p.split()[-1].split(',')
    p = [int(x) for x in p]

    return Computer(a, b, c, p)


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    computer = parse_data(input_path)
    return computer.run_program()


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    computer = parse_data(input_path)
    expected_program = ''.join(str(x) for x in computer.program)

    # a must be zero at the end of the program for it to hault
    a_possible_values = [0]
    for i in range(1, len(computer.program) + 1):
        new_a_possible_values = [
            8 * a_possible_value + digit for a_possible_value in a_possible_values for digit in range(8)
        ]
        a_possible_values = []
        for a_val in new_a_possible_values:
            output = Computer(a_val, computer.b, computer.c, computer.program).run_program().replace(',', '')
            if output[-i:] == expected_program[-i:]:
                a_possible_values.append(a_val)

    return min(a_possible_values)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
