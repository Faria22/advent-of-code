import re
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Reindeer(NamedTuple):
    speed: int
    travel_time: int
    rest_time: int

    def total_travel_distance(self, time: int) -> int:
        time_per_cycle = self.travel_time + self.rest_time

        num_cycles, remaining_time = divmod(time, time_per_cycle)

        extra_travel_time = min(remaining_time, self.travel_time)

        return self.speed * (num_cycles * self.travel_time + extra_travel_time)


def parse_data(input_path: Path) -> list[Reindeer]:
    reindeers = []
    for line in input_path.read_text().strip().split('\n'):
        a, b, c = re.findall(r'\d+', line)
        reindeers.append(Reindeer(int(a), int(b), int(c)))

    return reindeers


def part_one(input_path: Path, seconds: int = 2503) -> int:
    """Return the answer to part one."""
    reindeers = parse_data(input_path)
    return max(reindeer.total_travel_distance(seconds) for reindeer in reindeers)


def part_two(input_path: Path, seconds: int = 2503) -> int:
    """Return the answer to part two."""
    reindeers = parse_data(input_path)
    points = [0] * len(reindeers)
    for t in range(1, seconds + 1):
        distances = [reindeer.total_travel_distance(t) for reindeer in reindeers]
        max_d = max(distances)
        for idx, d in enumerate(distances):
            if d == max_d:
                points[idx] += 1

    return max(points)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
