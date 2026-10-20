from collections import Counter
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    two_id_count = 0
    three_id_count = 0
    for line in lines:
        vals = Counter(line).values()
        if 2 in vals:  # ruff: ignore[magic-value-comparison]
            two_id_count += 1
        if 3 in vals:  # ruff: ignore[magic-value-comparison]
            three_id_count += 1

    return two_id_count * three_id_count


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    num_chars = len(lines[0])
    for char_idx in range(num_chars):
        for a_idx, a in enumerate(lines[:-1]):
            tmp_a = a[:char_idx] + a[char_idx + 1 :]
            for b in lines[a_idx + 1 :]:
                if tmp_a == b[:char_idx] + b[char_idx + 1 :]:
                    return tmp_a
    return ''


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
