from collections.abc import Sequence
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

INPUT_PATH = Path(__file__).parent / 'input.txt'


class JoltageMachine:
    def __init__(self, correct_joltage: list[int], buttons: list[list[int]]) -> None:
        self.correct_joltage = correct_joltage
        self.current_joltage = [0] * len(correct_joltage)
        self.buttons = buttons

    def press_button(self, button_idx: int) -> None:
        for idx in self.buttons[button_idx]:
            self.current_joltage[idx] += 1

    def press_buttons(self, button_idxs: Sequence[int]) -> None:
        for button_idx in button_idxs:
            self.press_button(button_idx)

    def check_joltage(self) -> bool:
        return all(i == j for i, j in zip(self.correct_joltage, self.current_joltage, strict=True))

    def reset(self) -> None:
        self.current_joltage = [0] * len(self.correct_joltage)

    def solve(self) -> int:
        c = [1] * len(self.buttons)
        b = self.correct_joltage

        a_eq = np.zeros((len(self.correct_joltage), len(self.buttons)))
        for button_idx, button in enumerate(self.buttons):
            for wiring in button:
                a_eq[wiring, button_idx] = 1

        sol = linprog(c, A_eq=a_eq, b_eq=b, integrality=1).fun
        return int(round(sol))


class LightMachine:
    def __init__(self, correct_lights: int, buttons: list[int]) -> None:
        self.correct_lights = correct_lights
        self.current_lights = 0  # Lights always start off
        self.buttons = buttons

    def press_button(self, button_idx: int) -> None:
        self.current_lights ^= self.buttons[button_idx]

    def press_buttons(self, button_idxs: Sequence[int]) -> None:
        for button_idx in button_idxs:
            self.press_button(button_idx)

    def check_lights(self) -> bool:
        return self.correct_lights == self.current_lights

    def reset(self) -> None:
        self.current_lights = 0

    def solve(self) -> int:
        num_buttons = len(self.buttons)
        button_indices = range(num_buttons)
        for num_presses in range(num_buttons):  # checks up to all buttons -1
            for selected_buttons in combinations(button_indices, num_presses):
                self.press_buttons(selected_buttons)
                if self.check_lights():
                    return num_presses
                self.reset()

        # if all buttons need to be pressed we do not need to check it
        return num_buttons


def parse_lights(lights_str: str) -> int:
    lights_str = lights_str.replace('[', '').replace(']', '')
    lights = 0
    for i, light in enumerate(lights_str):
        if light == '#':
            lights += 2**i

    return lights


def parse_buttons(buttons_str: str) -> list[list[int]]:
    buttons = []
    for button_str in buttons_str.split(' '):
        wirings = button_str[1:-1].split(',')
        wirings = [int(w) for w in wirings]
        buttons.append(wirings)

    return buttons


def parse_joltage(joltage_str: str) -> list[int]:
    joltage_str = joltage_str.replace('{', '').replace('}', '')
    return [int(j) for j in joltage_str.split(',')]


def parse_data_part_one(data: str) -> list[LightMachine]:
    machines = []
    for line in data.split('\n'):
        lights, rest = line.split(' ', 1)
        buttons, _ = rest.rsplit(' ', 1)

        buttons = parse_buttons(buttons)
        buttons = [sum(2**w for w in wiring) for wiring in buttons]
        machines.append(LightMachine(parse_lights(lights), buttons))

    return machines


def parse_data_part_two(data: str) -> list[LightMachine]:
    machines = []
    for line in data.split('\n'):
        _, rest = line.split(' ', 1)
        buttons, joltage = rest.rsplit(' ', 1)

        buttons = parse_buttons(buttons)
        machines.append(JoltageMachine(parse_joltage(joltage), buttons))

    return machines


def part_one(data: str) -> int:
    """Return the answer to part one."""
    machines = parse_data_part_one(data)
    total_button_presses = 0
    for machine in machines:
        total_button_presses += machine.solve()

    return total_button_presses


def part_two(data: str) -> int:
    """Return the answer to part two."""
    machines = parse_data_part_two(data)
    total_button_presses = 0
    for machine in machines:
        total_button_presses += machine.solve()

    return total_button_presses


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
