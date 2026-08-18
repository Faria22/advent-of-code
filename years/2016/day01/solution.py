from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

RIGHT = {
    'n': 'e',
    'e': 's',
    's': 'w',
    'w': 'n',
}
LEFT = {
    'n': 'w',
    'w': 's',
    's': 'e',
    'e': 'n',
}


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split(', ')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    moves = parse_data(input_path)
    pos = Pos(0, 0)
    direction = 'n'
    for move in moves:
        side, num = move[0], int(move[1:])
        direction = RIGHT[direction] if side == 'R' else LEFT[direction]
        match direction:
            case 'n':
                pos = pos.shift_up(num)
            case 's':
                pos = pos.shift_down(num)
            case 'e':
                pos = pos.shift_right(num)
            case 'w':
                pos = pos.shift_left(num)

    return sum(abs(p) for p in pos)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    moves = parse_data(input_path)
    pos = Pos(0, 0)
    seen = set()
    direction = 'n'
    for move in moves:
        side, num = move[0], int(move[1:])
        direction = RIGHT[direction] if side == 'R' else LEFT[direction]
        match direction:
            case 'n':
                visited = {pos.shift_up(n) for n in range(1, num + 1)}
                pos = pos.shift_up(num)
            case 's':
                visited = {pos.shift_down(n) for n in range(1, num + 1)}
                pos = pos.shift_down(num)
            case 'e':
                visited = {pos.shift_right(n) for n in range(1, num + 1)}
                pos = pos.shift_right(num)
            case 'w':
                visited = {pos.shift_left(n) for n in range(1, num + 1)}
                pos = pos.shift_left(num)

        for v_pos in visited:
            if v_pos in seen:
                return sum(abs(p) for p in v_pos)

        seen.update(visited)
    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
