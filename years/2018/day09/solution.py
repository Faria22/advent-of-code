from collections import defaultdict, deque
from itertools import cycle
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

SCORING_MARBLE_NUM = 23


def parse_data(input_path: Path) -> tuple[int, int]:
    line_parts = input_path.read_text().strip().split()

    num_players = int(line_parts[0])
    last_marble = int(line_parts[-2])

    return num_players, last_marble


def highest_score(num_players: int, last_marble: int) -> int:
    if last_marble < SCORING_MARBLE_NUM:
        return 0

    players = cycle(range(1, num_players + 1))
    marbles = range(1, last_marble + 1)

    circle = deque([0])
    scores: dict[int, int] = defaultdict(int)

    for player, marble in zip(players, marbles):
        if marble % SCORING_MARBLE_NUM == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values())


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    num_players, last_marble = parse_data(input_path)
    return highest_score(num_players, last_marble)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    num_players, last_marble = parse_data(input_path)
    return highest_score(num_players, last_marble * 100)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
