ROW = 2947
COL = 3029


def get_idx_for_row_col(row: int, col: int) -> int:
    idx_at_row_one = col * (col + 1) // 2  # Idx on the first row but correct_col

    row_shift = row * (row - 1) // 2
    if row_shift:
        row_shift += (col - 1) * (row - 1)
    return idx_at_row_one + row_shift


def part_one(row: int = ROW, col: int = COL) -> int:
    """Return the answer to part one."""
    idx = get_idx_for_row_col(row, col)
    val = 20151125
    for _ in range(idx - 1):
        val *= 252533
        val %= 33554393

    return val


def part_two() -> int:
    """Return the answer to part two."""
    return 0


def main() -> None:
    print(f'Part 1: {part_one()}')
    print(f'Part 2: {part_two()}')


if __name__ == '__main__':
    main()
