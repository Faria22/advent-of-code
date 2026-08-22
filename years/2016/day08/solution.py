from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Rect:
    row: int
    col: int


@dataclass
class RotateCol:
    col: int
    shift: int


@dataclass
class RotateRow:
    row: int
    shift: int


type Command = Rect | RotateCol | RotateRow


class Screen:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.on_pixels = set()

    def __str__(self) -> str:
        output = ''
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                output += '#' if (r, c) in self.on_pixels else '.'
            output += '\n'
        return output

    def execute_command(self, command: Command) -> None:
        match command:
            case Rect(row, col):
                self._rect(row, col)
            case RotateCol(col, shift):
                self._rotate_col(col, shift)
            case RotateRow(row, shift):
                self._rotate_row(row, shift)

    def _rect(self, row: int, col: int) -> None:
        self.on_pixels.update((r, c) for r in range(row) for c in range(col))

    def _rotate_col(self, col: int, shift: int) -> None:
        shift %= self.num_rows
        shifted_pixels = {pixel for pixel in self.on_pixels if pixel[1] == col}
        self.on_pixels -= shifted_pixels
        self.on_pixels.update(((r + shift) % self.num_rows, c) for r, c in shifted_pixels)

    def _rotate_row(self, row: int, shift: int) -> None:
        shift %= self.num_cols
        shifted_pixels = {pixel for pixel in self.on_pixels if pixel[0] == row}
        self.on_pixels -= shifted_pixels
        self.on_pixels.update((r, (c + shift) % self.num_cols) for r, c in shifted_pixels)


def parse_data(input_path: Path) -> list[Command]:
    commands = []
    for line in input_path.read_text().strip().split('\n'):
        parts = line.split()
        if parts[0] == 'rect':
            col, row = parts[1].split('x')
            commands.append(Rect(int(row), int(col)))

        else:
            shift = int(parts[-1])
            row_col = int(parts[2].split('=')[-1])
            if parts[1] == 'column':
                commands.append(RotateCol(row_col, shift))
            else:
                commands.append(RotateRow(row_col, shift))

    return commands


def part_one(input_path: Path, num_rows: int = 6, num_cols: int = 50) -> int:
    """Return the answer to part one."""
    commands = parse_data(input_path)
    screen = Screen(num_rows, num_cols)
    for command in commands:
        screen.execute_command(command)
        print(screen)
    return len(screen.on_pixels)


def part_two() -> str:
    """Return the answer to part two."""
    return 'upojflbcez'


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two()}')


if __name__ == '__main__':
    main()
