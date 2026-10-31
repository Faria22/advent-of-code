from pathlib import Path

import numpy as np
from numpy.typing import NDArray

INPUT_PATH = Path(__file__).parent / 'input.txt'

SIZE = 300


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def power_level[T: (int, NDArray[np.int_])](x: T, y: T, serial_no: int) -> T:
    rack_id = x + 10
    power_level = rack_id * y + serial_no
    power_level *= rack_id
    hundreds_digit = (power_level // 100) % 10
    return hundreds_digit - 5  # ty: ignore[invalid-return-type]


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    serial_no = parse_data(input_path)

    x, y = np.indices((SIZE, SIZE))
    fuel_cells = power_level(x, y, serial_no)

    windows = np.lib.stride_tricks.sliding_window_view(fuel_cells, (3, 3))
    square_total_power = windows.sum(axis=(-2, -1))

    pos = np.unravel_index(np.argmax(square_total_power), square_total_power.shape)
    return f'{pos[0]},{pos[1]}'


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    serial_no = parse_data(input_path)

    x, y = np.indices((SIZE, SIZE))
    fuel_cells = power_level(x, y, serial_no)

    max_power = 0
    identifier = ''
    for window_size in range(1, SIZE + 1):
        windows = np.lib.stride_tricks.sliding_window_view(fuel_cells, (window_size, window_size))
        square_total_power = windows.sum(axis=(-2, -1))

        pos = np.unravel_index(np.argmax(square_total_power), square_total_power.shape)
        cur_max_power = square_total_power[pos]

        if cur_max_power > max_power:
            max_power = cur_max_power
            identifier = f'{pos[0]},{pos[1]},{window_size}'

    return identifier


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
