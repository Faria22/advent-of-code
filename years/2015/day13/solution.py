from collections import defaultdict
from itertools import pairwise
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


type Neighbors = dict[str, dict[str, int]]
type NeighborOption = tuple[str, ...]


def parse_data(input_path: Path) -> Neighbors:
    neighbors = defaultdict(dict)
    for line in input_path.read_text().strip().split('\n'):
        words = line.split()
        a = words[0]
        b = words[-1][:-1]
        sign = 1 if words[2] == 'gain' else -1
        delta = sign * int(words[3])
        neighbors[a][b] = int(delta)

    return neighbors


def get_neighbor_options(neighbor_option: NeighborOption, neighbors: Neighbors) -> set[NeighborOption]:
    if len(neighbor_option) == len(neighbors):
        return {neighbor_option}

    neighbor_options = set()
    for neighbor in neighbors:
        if neighbor in neighbor_option:
            continue
        cur_neighbr_option = (*neighbor_option, neighbor)
        neighbor_options.update(get_neighbor_options(cur_neighbr_option, neighbors))
    return neighbor_options


def add_myself(neighbor_options: set[NeighborOption]) -> set[NeighborOption]:
    new_neighbor_options = set()
    for neighbor_option in neighbor_options:
        for i in range(len(neighbor_option) + 1):
            list_neighbors = list(neighbor_option)
            list_neighbors.insert(i, 'myself')
            new_neighbor_options.add(tuple(list_neighbors))
    return new_neighbor_options


def get_delta(neighbor_option: NeighborOption, neighbors: Neighbors) -> int:
    delta = 0
    for a, b in pairwise(neighbor_option):
        delta += neighbors[a][b]
        delta += neighbors[b][a]

    a = neighbor_option[0]
    b = neighbor_option[-1]
    delta += neighbors[a][b] + neighbors[b][a]
    return delta


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    neighbors = parse_data(input_path)

    neighbor_options = get_neighbor_options((), neighbors)
    return max(get_delta(n_o, neighbors) for n_o in neighbor_options)


def part_two(input_path: Path) -> int:
    """Return the answer to part one."""
    neighbors = parse_data(input_path)

    neighbor_options = get_neighbor_options((), neighbors)

    people = tuple(neighbors.keys())
    for person in people:
        neighbors['myself'][person] = 0
        neighbors[person]['myself'] = 0

    neighbor_options = add_myself(neighbor_options)
    return max(get_delta(n_o, neighbors) for n_o in neighbor_options)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
