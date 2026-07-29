from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'

EMPTY = '.'


class Pos(NamedTuple):
    row: int
    col: int

    def __str__(self) -> str:
        return f'({self.row},{self.col})'


def parse_data(input_path: Path) -> tuple[dict[str, set[Pos]], Pos]:
    antenas: dict[str, set[Pos]] = defaultdict(set)
    for row, line in enumerate(input_path.read_text().strip().split('\n')):
        for col, cell in enumerate(line):
            if cell != EMPTY:
                antenas[cell].add(Pos(row, col))

    return antenas, Pos(row, col)


def get_antinodes(a: Pos, b: Pos, max_pos: Pos | None = None, /, all_nodes: bool = False) -> set[Pos]:
    row_diff = b.row - a.row
    col_diff = b.col - a.col

    if not all_nodes:
        node1 = Pos(a.row - row_diff, a.col - col_diff)
        node2 = Pos(b.row + row_diff, b.col + col_diff)

        nodes = {node1, node2}
    else:
        assert max_pos is not None
        nodes = set()

        # going up the diff
        edge_row = max_pos.row if row_diff > 0 else 0
        edge_col = max_pos.col if col_diff > 0 else 0
        n = (edge_row - a.row) // row_diff
        m = (edge_col - a.col) // col_diff
        nodes.update(Pos(a.row + i * row_diff, a.col + i * col_diff) for i in range(min(n, m) + 1))

        # going down the diff
        row_diff *= -1
        col_diff *= -1
        edge_row = max_pos.row if row_diff > 0 else 0
        edge_col = max_pos.col if col_diff > 0 else 0
        n = (edge_row - a.row) // row_diff
        m = (edge_col - a.col) // col_diff
        nodes.update(Pos(a.row + i * row_diff, a.col + i * col_diff) for i in range(min(n, m) + 1))

    return nodes


def in_bounds(node: Pos, max_pos: Pos) -> bool:
    return all(0 <= node[i] <= max_pos[i] for i in range(2))


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    antenas, max_pos = parse_data(input_path)

    antinodes: set[Pos] = set()
    for positions in antenas.values():
        for a, b in combinations(positions, 2):
            antinode_candidates = get_antinodes(a, b)
            for antinode in antinode_candidates:
                if in_bounds(antinode, max_pos):
                    antinodes.add(antinode)

    return len(antinodes)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    antenas, max_pos = parse_data(input_path)

    antinodes: set[Pos] = set()
    for positions in antenas.values():
        for a, b in combinations(positions, 2):
            antinodes.update(get_antinodes(a, b, max_pos, all_nodes=True))

    return len(antinodes)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
