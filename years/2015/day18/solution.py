from pathlib import Path

from aoc import Grid as BaseGrid
from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Grid(BaseGrid[bool]):
    def new_state(self, pos: Pos) -> bool:
        neighbors = (self[n] or False for n in pos.neighbors(diagonals=True))
        if self[pos]:
            return 1 < sum(neighbors) < 4  # ruff: ignore[magic-value-comparison]
        return sum(neighbors) == 3  # ruff: ignore[magic-value-comparison]

    def corners_on(self) -> None:
        corners = (
            Pos(0, 0),
            Pos(0, self.shape[1] - 1),
            Pos(self.shape[0] - 1, 0),
            Pos(self.shape[0] - 1, self.shape[1] - 1),
        )
        for corner in corners:
            self[corner] = True


def parse_data(input_path: Path) -> Grid:
    return Grid([[char == '#' for char in line] for line in input_path.read_text().strip().split('\n')])


def step(grid: Grid) -> Grid:
    new_grid = grid.copy()

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            p = Pos(r, c)
            new_grid[p] = grid.new_state(p)

    return new_grid


def part_one(input_path: Path, steps: int = 100) -> int:
    """Return the answer to part one."""
    grid = parse_data(input_path)
    for _ in range(steps):
        grid = step(grid)
    return sum(grid[Pos(r, c)] or False for r in range(grid.shape[0]) for c in range(grid.shape[1]))


def part_two(input_path: Path, steps: int = 100) -> int:
    """Return the answer to part two."""
    grid = parse_data(input_path)
    grid.corners_on()
    for _ in range(steps):
        grid = step(grid)
        grid.corners_on()
    return sum(grid[Pos(r, c)] or False for r in range(grid.shape[0]) for c in range(grid.shape[1]))


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
