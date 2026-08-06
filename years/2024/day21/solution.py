from functools import cache
from itertools import permutations, product
from pathlib import Path

from aoc import Pos as BasePos

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Pos(BasePos):
    def move(self, move: str) -> 'Pos':
        match move:
            case '^':
                return self.shift_up()
            case 'v':
                return self.shift_down()
            case '<':
                return self.shift_left()
            case '>':
                return self.shift_right()
            case _:
                raise ValueError(f'{move} is not a valid move')


class BasePad:
    def __init__(self, buttons: dict[str, Pos], start_button: str = 'A') -> None:
        self.buttons = buttons
        assert start_button in buttons
        self.cur_pos: Pos = buttons[start_button]

    def press_button(self, button: str) -> set[str]:
        if button not in self.buttons:
            raise ValueError('Not an available button')

        end_button_pos = self.buttons[button]

        vertical_shift, horizontal_shift = end_button_pos - self.cur_pos

        vertical_shift_str = '^' if vertical_shift < 0 else 'v'
        horizontal_shift_str = '<' if horizontal_shift < 0 else '>'

        moves = vertical_shift_str * abs(vertical_shift) + horizontal_shift_str * abs(horizontal_shift)

        possible_moves: set[str] = set()
        for move_sequence in permutations(moves, len(moves)):
            cur_pos = self.cur_pos
            for move in move_sequence:
                cur_pos = cur_pos.move(move)
                if cur_pos not in self.buttons.values():
                    break
            else:
                possible_moves.add(''.join(move_sequence) + 'A')

        self.cur_pos = end_button_pos
        return possible_moves


class DirPad(BasePad):
    def __init__(self, start_button: str) -> None:
        buttons = {
            '^': Pos(0, 1),
            'A': Pos(0, 2),
            'v': Pos(1, 1),
            '<': Pos(1, 0),
            '>': Pos(1, 2),
        }
        super().__init__(buttons, start_button)


class NumPad(BasePad):
    def __init__(self, start_button: str) -> None:
        buttons = {
            '7': Pos(0, 0),
            '8': Pos(0, 1),
            '9': Pos(0, 2),
            '4': Pos(1, 0),
            '5': Pos(1, 1),
            '6': Pos(1, 2),
            '1': Pos(2, 0),
            '2': Pos(2, 1),
            '3': Pos(2, 2),
            '0': Pos(3, 1),
            'A': Pos(3, 2),
        }
        super().__init__(buttons, start_button)


@cache
def lowest_cost_move(pad_class: type[DirPad | NumPad], start: str, end: str, remaining_layers: int) -> int:
    pad = pad_class(start)

    possible_moves = pad.press_button(end)
    if remaining_layers == 0:
        move = possible_moves.pop()
        return len(move)

    costs = []
    for possible_move in possible_moves:
        cost = 0
        prev_button = 'A'
        for button in possible_move:
            cur_cost = lowest_cost_move(DirPad, prev_button, button, remaining_layers - 1)
            cost += cur_cost
            prev_button = button
        costs.append(cost)

    return min(costs)


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def complexity(num_button_presses: int, code: str) -> int:
    num_code = int(code[:-1])
    return num_code * num_button_presses


def get_move_sequences_from_possible_moves(moves: list[set[str]]) -> list[str]:
    move_sequences = list(product(*moves))
    return [''.join(move_sequence) for move_sequence in move_sequences]


def get_final_num_moves(code: str, num_layers: int) -> int:
    prev_button = 'A'
    total_cost = 0
    for button in code:
        total_cost += lowest_cost_move(NumPad, prev_button, button, num_layers)
        prev_button = button
    return total_cost


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    codes = parse_data(input_path)

    total_complexity = 0
    for code in codes:
        num_moves = get_final_num_moves(code, 2)
        total_complexity += complexity(num_moves, code)

    return total_complexity


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    codes = parse_data(input_path)

    total_complexity = 0
    for code in codes:
        num_moves = get_final_num_moves(code, 25)
        total_complexity += complexity(num_moves, code)

    return total_complexity


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
