import contextlib
from pathlib import Path
from typing import Literal, cast

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Register = Literal['a', 'b', 'c', 'd']


class Computer:
    def __init__(self, commands: list[str]) -> None:
        self._registers: dict[Register, int] = dict.fromkeys(('a', 'b', 'c', 'd'), 0)
        self.commands = commands

    def __getitem__(self, x: Register) -> int:
        return self._registers[x]

    def __setitem__(self, x: Register, value: int) -> None:
        self._registers[x] = value

    def _cpy(self, x: int | Register, y: int | Register) -> None:
        if isinstance(y, int):
            return

        if isinstance(x, int):
            self._registers[y] = x
        else:
            self._registers[y] = self._registers[x]

    def _inc(self, x: Register | int) -> None:
        if isinstance(x, int):
            return

        self._registers[x] += 1

    def _dec(self, x: Register | int) -> None:
        if isinstance(x, int):
            return

        self._registers[x] -= 1

    def _tgl(self, cur_idx: int, shift: Register | int) -> None:
        idx = cur_idx + self.get_register_val_or_int(shift)
        if not (0 <= idx < len(self.commands)):
            return

        command, *args = self.commands[idx].split()
        match len(args):
            case 1:
                new_command = 'dec' if command == 'inc' else 'inc'
            case 2:
                new_command = 'cpy' if command == 'jnz' else 'jnz'
            case _:
                raise RuntimeError

        self.commands[idx] = ' '.join([new_command, *args])

    def get_register_val_or_int(self, x: Register | int) -> int:
        try:
            return int(x)
        except ValueError:
            return self[x]  # ty: ignore[invalid-argument-type]

    def run_commands(self) -> None:
        idx = 0
        num_commands = len(self.commands)
        while idx < num_commands:
            if self.commands[idx : idx + 6] == ['cpy b c', 'inc a', 'dec c', 'jnz c -2', 'dec d', 'jnz d -5']:
                self['a'] = self['b'] * self['d']
                self['c'] = 0
                self['d'] = 0
                idx += 6
                continue
            line = self.commands[idx]
            command, *args = line.split()

            x = cast(Register, args[0])
            match command:
                case 'jnz':
                    x = self.get_register_val_or_int(x)
                    if x != 0:
                        idx += self.get_register_val_or_int(args[1])  # ty: ignore[invalid-argument-type]
                        continue
                case 'cpy':
                    with contextlib.suppress(ValueError):
                        x = int(x)
                    self._cpy(x, cast(Register, args[1]))
                case 'inc':
                    self._inc(x)
                case 'dec':
                    self._dec(x)
                case 'tgl':
                    self._tgl(idx, x)

            idx += 1


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    commands = parse_data(input_path)
    computer = Computer(commands)
    computer['a'] = 7
    computer.run_commands()
    return computer['a']


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    commands = parse_data(input_path)
    computer = Computer(commands)
    computer['a'] = 12
    computer.run_commands()
    return computer['a']


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
