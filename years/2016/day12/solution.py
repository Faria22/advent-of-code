import contextlib
from pathlib import Path
from typing import Literal, cast

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Register = Literal['a', 'b', 'c', 'd']


class Computer:
    def __init__(self) -> None:
        self._registers: dict[Register, int] = dict.fromkeys(('a', 'b', 'c', 'd'), 0)

    def __getitem__(self, x: Register) -> int:
        return self._registers[x]

    def __setitem__(self, x: Register, value: int) -> None:
        self._registers[x] = value

    def _cpy(self, x: int | Register, y: Register) -> None:
        if isinstance(x, int):
            self._registers[y] = x
        else:
            self._registers[y] = self._registers[x]

    def _inc(self, x: Register) -> None:
        self._registers[x] += 1

    def _dec(self, x: Register) -> None:
        self._registers[x] -= 1

    def run_commands(self, commands: list[str]) -> None:
        idx = 0
        num_commands = len(commands)
        while idx < num_commands:
            line = commands[idx]
            command, *args = line.split()

            x = cast(Register, args[0])
            match command:
                case 'jnz':
                    try:
                        x = int(x)
                    except ValueError:
                        x = self[x]

                    if x != 0:
                        idx += int(args[1])
                        continue
                case 'cpy':
                    with contextlib.suppress(ValueError):
                        x = int(x)
                    self._cpy(x, cast(Register, args[1]))
                case 'inc':
                    self._inc(x)
                case 'dec':
                    self._dec(x)

            idx += 1


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    computer = Computer()
    computer.run_commands(parse_data(input_path))
    return computer['a']


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    computer = Computer()
    computer['c'] = 1
    computer.run_commands(parse_data(input_path))
    return computer['a']


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
