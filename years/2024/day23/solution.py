from collections import defaultdict
from itertools import combinations
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[tuple[str, str]]:
    connections = []
    for line in input_path.read_text().strip().split('\n'):
        a, b = line.split('-')
        connections.append((a, b))
    return connections


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    connections = parse_data(input_path)
    nodes = defaultdict(set)
    for node, b in connections:
        nodes[node].add(b)
        nodes[b].add(node)

    trimmed_nodes = {a: connections for a, connections in nodes.items() if len(connections) > 1}

    sets = set()
    for node, connections in trimmed_nodes.items():
        if node[0] != 't':
            continue

        for a, b in combinations(connections, 2):
            if b in trimmed_nodes[a]:
                sets.add(frozenset((node, a, b)))
    return len(sets)


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    connections = parse_data(input_path)
    nodes = defaultdict(set)
    for node, b in connections:
        nodes[node].add(b)
        nodes[b].add(node)

    sets = set()
    for node, connections in nodes.items():
        connected = {node}
        for a, b in combinations(connections, 2):
            if b in nodes[a]:
                connected |= {a, b}

        if not all(b in nodes[a] for a, b in combinations(connected, 2)):
            continue

        sets.add(frozenset(connected))

    return ','.join(sorted(max(sets, default={}, key=len)))


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
