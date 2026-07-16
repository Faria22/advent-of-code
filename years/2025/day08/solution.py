from math import prod
from pathlib import Path

import numpy as np

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Grid = np.ndarray


def parse_data(data: str) -> Grid:
    grid = [line.split(',') for line in data.split('\n')]
    return np.array(grid, dtype=int)


def get_box_distances(grid: Grid) -> np.ndarray:
    difference = grid[:, None, :] - grid[None, :, :]
    dist = np.linalg.norm(difference, axis=-1)

    # Filling diagonal so distance between the same box is not taken into account
    np.fill_diagonal(dist, np.inf)
    # Filling lower triangle so we only consider i, j pairs and not the j, i pairs
    dist[np.tril_indices_from(dist)] = np.inf

    return dist


def connect_closest_boxes(dist: np.ndarray, circuits: list[set[int]]) -> tuple[int, int] | None:
    idx_i, idx_j = np.unravel_index(np.argmin(dist), dist.shape)
    idx_i = int(idx_i)
    idx_j = int(idx_j)
    dist[idx_i, idx_j] = np.inf

    # Checks if box_i is in a circuit and if it is, what circuit index
    circuit_i_idx = None
    for idx, circuit in enumerate(circuits):
        if idx_i in circuit:
            circuit_i_idx = idx
            break

    # Same thing for box_j
    circuit_j_idx = None
    for idx, circuit in enumerate(circuits):
        if idx_j in circuit:
            circuit_j_idx = idx
            break

    # They are in the same circuit
    if circuit_i_idx == circuit_j_idx and circuit_i_idx is not None:
        return None

    # Neither box is in a circuit
    if circuit_i_idx is None and circuit_j_idx is None:
        # Then make a new circuit
        circuits.append({idx_i, idx_j})
    # Only box_j is not in a circuit
    elif circuit_j_idx is None:
        assert circuit_i_idx is not None
        circuits[circuit_i_idx].add(idx_j)
    # Only box_i is not in a circuit
    elif circuit_i_idx is None:
        assert circuit_j_idx is not None
        circuits[circuit_j_idx].add(idx_i)
    # Both are in a circuit, but in different ones
    elif circuit_i_idx != circuit_j_idx:
        # Check is needed to make sure pop indices stay correct
        if circuit_i_idx < circuit_j_idx:
            circuit_j = circuits.pop(circuit_j_idx)
            circuit_i = circuits.pop(circuit_i_idx)
        else:
            circuit_i = circuits.pop(circuit_i_idx)
            circuit_j = circuits.pop(circuit_j_idx)
        circuits.append(circuit_i | circuit_j)

    return idx_i, idx_j


def part_one(grid: Grid, connection_steps: int = 1000) -> int:
    """Return the answer to part one."""
    dist = get_box_distances(grid)
    circuits: list[set[int]] = []
    for _step in range(connection_steps):
        connect_closest_boxes(dist, circuits)

    top_three_circuits = sorted(circuits, key=len, reverse=True)[:3]
    return prod(len(x) for x in top_three_circuits)


def part_two(grid: Grid) -> int:
    """Return the answer to part two."""
    dist = get_box_distances(grid)
    circuits: list[set[int]] = []
    last_added_idxs = None
    while not (len(circuits) == 1 and sum(len(circuit) for circuit in circuits) == grid.shape[0]):
        last_added_idxs = connect_closest_boxes(dist, circuits)

    assert last_added_idxs is not None
    box_i, box_j = last_added_idxs
    return grid[box_i, 0] * grid[box_j, 0]


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    grid = parse_data(data)
    print(f'Part 1: {part_one(grid)}')
    print(f'Part 2: {part_two(grid)}')


if __name__ == '__main__':
    main()
