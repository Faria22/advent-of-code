import string
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


type Pos = tuple[int, int]


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().rstrip().split('\n')


def next_pos(pos: Pos, direction: str, grid: dict[Pos, str]) -> tuple[Pos | None, str]:
    row, col = pos
    # Try to keep going in the same direction
    match direction:
        case 's':
            row += 1
        case 'n':
            row -= 1
        case 'w':
            col += 1
        case 'e':
            col -= 1

    if (row, col) in grid:
        return (row, col), direction

    # We can try changing directions
    row, col = pos
    if grid[pos] in {*string.ascii_uppercase, '+'}:
        match direction:
            case 's' | 'n':
                if (new_pos := (row, col - 1)) in grid:
                    return new_pos, 'e'
                if (new_pos := (row, col + 1)) in grid:
                    return new_pos, 'w'
            case 'e' | 'w':
                if (new_pos := (row - 1, col)) in grid:
                    return new_pos, 'n'
                if (new_pos := (row + 1, col)) in grid:
                    return new_pos, 's'

    # next pos not found
    return None, ''


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    data = parse_data(input_path)
    grid: dict[Pos, str] = {}
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell != ' ':
                grid[row, col] = cell

    row = 0
    col = data[row].index('|')
    pos = (row, col)
    direction = 's'

    letters = []
    while pos:
        if (cell := grid[pos]) in string.ascii_uppercase:
            letters.append(cell)

        pos, direction = next_pos(pos, direction, grid)

    return ''.join(letters)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)
    grid: dict[Pos, str] = {}
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell != ' ':
                grid[row, col] = cell

    row = 0
    col = data[row].index('|')
    pos = (row, col)
    direction = 's'

    num_steps = 0
    while pos:
        num_steps += 1
        pos, direction = next_pos(pos, direction, grid)

    return num_steps


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
