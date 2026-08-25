from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[int, int]]:
    disks = []
    for line in input_path.read_text().strip().split('\n'):
        parts = line.split()
        num_pos = int(parts[3])
        cur_pos = int(parts[-1][:-1])
        disks.append((num_pos, cur_pos))
    return disks


def passes_all_disks(t: int, disks: list[tuple[int, int]]) -> bool:
    return all((cur_pos + disk_idx + t) % num_pos == 0 for disk_idx, (num_pos, cur_pos) in enumerate(disks, 1))


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    disks = parse_data(input_path)
    t = 0
    while not passes_all_disks(t, disks):
        t += 1

    return t


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    disks = [*parse_data(input_path), (11, 0)]
    t = 0
    while not passes_all_disks(t, disks):
        t += 1

    return t


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
