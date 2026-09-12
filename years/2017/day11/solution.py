from collections import Counter
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


OPPOSITES = (
    ('n', 's'),
    ('e', 'w'),
    ('ne', 'sw'),
    ('nw', 'se'),
)


EQUIVALENTS = (
    ('n', 'se', 'ne'),
    ('n', 'sw', 'nw'),
    ('s', 'ne', 'se'),
    ('s', 'nw', 'sw'),
    ('se', 'sw', 's'),
    ('ne', 'nw', 'n'),
)


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split(',')


def get_distance_from_moves(moves: list[str]) -> int:
    move_counts = Counter(moves)

    prev_distance = sum(move_counts.values())
    while True:
        # remove irrelevant moves
        for a, b in OPPOSITES:
            num_equivalent_moves = min(move_counts[a], move_counts[b])
            move_counts[a] -= num_equivalent_moves
            move_counts[b] -= num_equivalent_moves

        # remove equivalent moves
        for a, b, c in EQUIVALENTS:
            num_equivalent_moves = min(move_counts[a], move_counts[b])
            move_counts[a] -= num_equivalent_moves
            move_counts[b] -= num_equivalent_moves
            move_counts[c] += num_equivalent_moves

        if prev_distance == (new_distance := sum(move_counts.values())):
            break

        prev_distance = new_distance

    return prev_distance


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    moves = parse_data(input_path)

    return get_distance_from_moves(moves)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    moves = parse_data(input_path)

    max_distance = 0
    for idx in range(len(moves)):
        max_distance = max(max_distance, get_distance_from_moves(moves[: idx + 1]))

    return max_distance


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
