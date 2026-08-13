from collections import defaultdict
from itertools import pairwise
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


type Locations = dict[str, dict[str, int]]
type Paths = set[tuple[str, ...]]


def parse_data(input_path: Path) -> Locations:
    locations = defaultdict(dict)
    for line in input_path.read_text().strip().split('\n'):
        a, _, b, _, distance = line.split()
        locations[a] |= {b: int(distance)}
        locations[b] |= {a: int(distance)}

    return locations


def get_paths(path: tuple[str, ...], locations: Locations) -> Paths:
    if len(path) == len(locations):
        return {path}

    paths = set()
    for location in locations:
        if location in path:
            continue
        cur_path = (*path, location)
        paths.update(get_paths(cur_path, locations))
    return paths


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    locations = parse_data(input_path)

    paths = get_paths((), locations)
    distances = {path: sum(locations[a][b] for a, b in pairwise(path)) for path in paths}
    return min(distances.values())


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    locations = parse_data(input_path)

    paths = get_paths((), locations)
    distances = {path: sum(locations[a][b] for a, b in pairwise(path)) for path in paths}
    return max(distances.values())


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
