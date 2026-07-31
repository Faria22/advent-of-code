from collections.abc import Iterator
from pathlib import Path
from typing import NamedTuple

from aoc import Grid as BaseGrid
from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


class PlantGarden(BaseGrid[str]):
    def __init__(self, grid: list[list[str]]) -> None:
        super().__init__(grid)

        self.plants = {cell for row in grid for cell in row}

    def get_plant_positions(self, plant: str) -> set[Pos]:
        return {Pos(r, c) for r, row in enumerate(self) for c, cell in enumerate(row) if cell == plant}


class Edge(NamedTuple):
    """Edge is going to be mapped with the two positions surrounding the edge"""

    a: Pos
    b: Pos

    def shift_up(self) -> 'Edge':
        return Edge(self.a.shift_up(), self.b.shift_up())

    def shift_down(self) -> 'Edge':
        return Edge(self.a.shift_down(), self.b.shift_down())

    def shift_left(self) -> 'Edge':
        return Edge(self.a.shift_left(), self.b.shift_left())

    def shift_right(self) -> 'Edge':
        return Edge(self.a.shift_right(), self.b.shift_right())

    def neighbors(self) -> Iterator:
        if self.a == self.b.shift_up() or self.a == self.b.shift_down():
            yield self.shift_left()
            yield self.shift_right()
        else:
            yield self.shift_up()
            yield self.shift_down()


def get_region_and_edges(
    start_pos: Pos,
    plant_positions: set[Pos],
    found_plants: set[Pos],
) -> tuple[set[Pos], set[Edge]]:
    """other_plants and found_plants are of the same type as start_pos"""
    found_plants.add(start_pos)

    edges = set()
    for neighbor in start_pos.neighbors():
        if neighbor in found_plants:
            continue

        if neighbor not in plant_positions:
            edges.add(Edge(start_pos, neighbor))
            continue

        _, next_edges = get_region_and_edges(neighbor, plant_positions, found_plants)

        edges |= next_edges

    return found_plants, edges


def parse_data(input_path: Path) -> PlantGarden:
    grid = [list(line) for line in input_path.read_text().strip().split()]
    return PlantGarden(grid)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    grid = parse_data(input_path)
    cost = 0
    for plant in grid.plants:
        plant_positions = grid.get_plant_positions(plant)
        while plant_positions:
            found_plants, edges = get_region_and_edges(plant_positions.pop(), plant_positions, set())

            cost += len(found_plants) * len(edges)

            plant_positions -= found_plants

    return cost


def same_side_edges(start_edge: Edge, edges: set[Edge], found_edges: set[Edge]) -> set[Edge]:
    found_edges.add(start_edge)

    for neighbor in start_edge.neighbors():
        if neighbor in found_edges:
            continue

        if neighbor in edges:
            found_edges.update(same_side_edges(neighbor, edges, found_edges))

    return found_edges


def num_different_edges(edges: set[Edge]) -> int:
    edge_count = 0

    while edges:
        edge_count += 1
        edges -= same_side_edges(edges.pop(), edges, set())

    return edge_count


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    grid = parse_data(input_path)
    cost = 0
    for plant in grid.plants:
        plant_positions = grid.get_plant_positions(plant)
        while plant_positions:
            found_plants, edges = get_region_and_edges(plant_positions.pop(), plant_positions, set())

            cost += len(found_plants) * num_different_edges(edges)

            plant_positions -= found_plants

    return cost


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
