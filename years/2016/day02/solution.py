from pathlib import Path

from aoc import Grid, Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


class NumPad(Grid):
    def __init__(self, grid: list[list[str]], start_pos: Pos) -> None:
        super().__init__(grid)
        self._cur_button_pos = start_pos

    def move(self, move: str) -> None:
        match move:
            case 'U':
                next_button_pos = self._cur_button_pos.shift_up()
            case 'D':
                next_button_pos = self._cur_button_pos.shift_down()
            case 'L':
                next_button_pos = self._cur_button_pos.shift_left()
            case 'R':
                next_button_pos = self._cur_button_pos.shift_right()

        if self.in_bounds(next_button_pos):
            self._cur_button_pos = next_button_pos

    def get_current_button(self) -> str:
        return self._grid[self._cur_button_pos[0]][self._cur_button_pos[1]]

    def in_bounds(self, pos: Pos) -> bool:
        return super().in_bounds(pos) and self._grid[pos[0]][pos[1]]


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    numpad = NumPad([['1', '2', '3'], ['4', '5', '5'], ['7', '8', '9']], Pos(1, 1))
    code = ''
    for line in lines:
        for move in line:
            numpad.move(move)
        code += numpad.get_current_button()

    return code


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    numpad = NumPad(
        [
            ['', '', '1', '', ''],
            ['', '2', '3', '4', ''],
            ['5', '6', '7', '8', '9'],
            ['', 'A', 'B', 'C', ''],
            ['', '', 'D', '', ''],
        ],
        Pos(2, 0),
    )
    code = ''
    for line in lines:
        for move in line:
            numpad.move(move)
        code += numpad.get_current_button()

    return code


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
