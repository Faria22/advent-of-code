from functools import cache
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> tuple[int, ...]:
    line = input_path.read_text().strip()
    return tuple(int(stone) for stone in line.split())


@cache
def blink(stone: int, num_blinks_left: int) -> int:
    """Returns the number of stones left for stone with num_blinks_left"""
    if num_blinks_left == 0:
        return 1

    num_blinks_left -= 1

    if stone == 0:
        return blink(1, num_blinks_left)

    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        middle = len(str_stone) // 2
        left = int(str_stone[:middle])
        right = int(str_stone[middle:])
        return blink(left, num_blinks_left) + blink(right, num_blinks_left)

    return blink(stone * 2024, num_blinks_left)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    stones = parse_data(input_path)
    return sum(blink(stone, 25) for stone in stones)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    stones = parse_data(input_path)
    return sum(blink(stone, 75) for stone in stones)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
