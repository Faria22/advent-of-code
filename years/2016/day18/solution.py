from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

SAFE_TILE = '.'


def get_next_row(cur_row: int, num_tiles: int) -> int:
    left_neighbors = cur_row << 1
    right_neighbors = cur_row >> 1

    next_row = left_neighbors ^ right_neighbors
    mask = (1 << num_tiles) - 1
    return next_row & mask


def parse_data(input_path: Path) -> tuple[int, int]:
    row = 0
    for idx, tile in enumerate(input_path.read_text().strip()):
        if tile != SAFE_TILE:
            row += 1 << idx
    return row, idx + 1


def part_one(input_path: Path, num_rows: int = 40) -> int:
    """Return the answer to part one."""
    row, num_tiles = parse_data(input_path)
    safe_tile_count = num_tiles - row.bit_count()
    for _ in range(num_rows - 1):
        row = get_next_row(row, num_tiles)
        safe_tile_count += num_tiles - row.bit_count()

    return safe_tile_count


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    row, num_tiles = parse_data(input_path)
    safe_tile_count = num_tiles - row.bit_count()
    for _ in range(400000 - 1):
        row = get_next_row(row, num_tiles)
        safe_tile_count += num_tiles - row.bit_count()

    return safe_tile_count


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
