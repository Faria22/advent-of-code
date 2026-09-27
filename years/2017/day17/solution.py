from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    step_size = parse_data(input_path)
    cur_pos = 0
    buffer = [0]
    num_inserts = 2017
    for i in range(1, num_inserts + 1):
        cur_pos = (cur_pos + step_size) % i
        cur_pos = (cur_pos + 1) % (i + 1)
        buffer.insert(cur_pos, i)

    idx = (buffer.index(num_inserts) + 1) % (num_inserts + 1)
    return buffer[idx]


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    step_size = parse_data(input_path)
    cur_pos = 0
    idx_of_zero = 0
    val_after_zero = None
    num_inserts = 50_000_000
    for i in range(1, num_inserts + 1):
        cur_pos = (cur_pos + step_size) % i
        cur_pos = (cur_pos + 1) % (i + 1)
        if cur_pos <= idx_of_zero:
            idx_of_zero += 1
        elif cur_pos == idx_of_zero + 1:
            val_after_zero = i

    assert val_after_zero is not None
    return val_after_zero


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
