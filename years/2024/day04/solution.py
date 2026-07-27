from pathlib import Path
from typing import Literal, get_args

INPUT_PATH = Path(__file__).parent / 'input.txt'


WORD = 'XMAS'
CROSS = 'MAS'
Direction = Literal['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se']
DIRECTIONS = list(get_args(Direction))

type Grid = list[str]


def parse_data(data: str) -> Grid:
    return data.split('\n')


def check_letter(grid: Grid, row: int, col: int, expected_letter: str) -> bool:
    num_rows = len(grid)
    num_cols = len(grid[0])

    if not (0 <= row < num_rows) or not (0 <= col < num_cols):
        return False

    return grid[row][col] == expected_letter


def check_word(
    grid: Grid,
    start_row: int,
    start_col: int,
    direction: Direction,
) -> bool:
    match direction:
        case 'n':
            row_diff = -1
            col_diff = 0
        case 's':
            row_diff = +1
            col_diff = 0
        case 'w':
            row_diff = 0
            col_diff = -1
        case 'e':
            row_diff = 0
            col_diff = 1
        case 'nw':
            row_diff = -1
            col_diff = -1
        case 'ne':
            row_diff = -1
            col_diff = 1
        case 'sw':
            row_diff = 1
            col_diff = -1
        case 'se':
            row_diff = 1
            col_diff = 1

    return all(
        check_letter(grid, start_row + row_diff * i, start_col + col_diff * i, WORD[i]) for i in range(1, len(WORD))
    )


def check_word_in_all_directions(grid: Grid, row: int, col: int) -> int:
    return sum(check_word(grid, row, col, direction) for direction in DIRECTIONS)


def part_one(data: str) -> int:
    """Return the answer to part one."""
    grid = parse_data(data)

    word_count = 0
    for row, line in enumerate(grid):
        for col, letter in enumerate(line):
            # Only start check if letter is the first letter of the word
            if letter != WORD[0]:
                continue

            word_count += check_word_in_all_directions(grid, row, col)

    return word_count


def check_cross(grid: Grid, row: int, col: int) -> bool:
    # Check upper left to lower right
    if not any(
        check_letter(grid, row - 1, col - 1, CROSS[i]) and check_letter(grid, row + 1, col + 1, CROSS[2 - i])
        for i in [0, 2]
    ):
        return False

    # Check upper right to lower left
    return any(
        check_letter(grid, row - 1, col + 1, CROSS[i]) and check_letter(grid, row + 1, col - 1, CROSS[2 - i])
        for i in [0, 2]
    )


def part_two(data: str) -> int:
    """Return the answer to part two."""
    grid = parse_data(data)

    cross_count = 0
    for row, line in enumerate(grid):
        for col, letter in enumerate(line):
            # Only start check if letter is the middle of the X (a.k.a. 'A')
            if letter != CROSS[1]:
                continue

            if check_cross(grid, row, col):
                cross_count += 1
    return cross_count


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
