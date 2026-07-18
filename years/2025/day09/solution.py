from dataclasses import dataclass
from pathlib import Path
from typing import Literal

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Tile:
    x: int
    y: int


@dataclass
class Edge:
    direction: Literal['v', 'h']
    const: int  # if v const would be the x value
    min: int  # where the edge starts
    max: int  # where the edge ends


def get_red_tiles(data: str) -> list[Tile]:
    red_tiles = []
    for row in data.split('\n'):
        x, y = row.split(',')
        red_tiles.append(Tile(int(x), int(y)))

    return red_tiles


def calculate_area(tile_i: Tile, tile_j: Tile) -> int:
    # Adding one because we have to include the tile itself
    x_size = abs(tile_i.x - tile_j.x) + 1
    y_size = abs(tile_i.y - tile_j.y) + 1

    return x_size * y_size


def get_edges(red_tiles: list[Tile]) -> list[Edge]:
    edges = []

    red_tiles.append(red_tiles[0])  # Adding the first tile again for the looping
    for i in range(len(red_tiles) - 1):
        tile_i = red_tiles[i]
        tile_j = red_tiles[i + 1]

        if tile_i.x == tile_j.x:
            edges.append(Edge('v', tile_i.x, min(tile_i.y, tile_j.y), max(tile_i.y, tile_j.y)))
        else:
            edges.append(Edge('h', tile_i.y, min(tile_i.x, tile_j.x), max(tile_i.x, tile_j.x)))

    return edges


def is_center_allowed(x: float, y: float, edges: list[Edge]) -> bool:
    # for the center to be allowed that means that casting a horizontal
    # ray to the right of the point, it would need to cross
    # an odd number of edges for it to be inside the polygon

    count = 0
    for edge in edges:
        # check if the edge is vertical
        if edge.direction != 'v':
            continue

        # check if the edge if to the right (or on top) of the point
        if edge.const < x:
            continue

        # check if point is between the edge
        if not (edge.min <= y < edge.max):
            continue

        count += 1

    return count % 2 == 1


def edge_crosses_rectangle(edge: Edge, min_x: int, min_y: int, max_x: int, max_y: int) -> bool:
    if edge.direction == 'v':
        # first check is to make sure that the edge is between the rectangle
        # the second is to check if is crossing or within the rectangle
        if min_x < edge.const < max_x and max(min_y, edge.min) < min(max_y, edge.max):
            return True
    elif min_y < edge.const < max_y and max(min_x, edge.min) < min(max_x, edge.max):
        return True
    return False


def is_allowed_rectangle(tile_i: Tile, tile_j: Tile, edges: list[Edge]) -> bool:
    min_x = min(tile_i.x, tile_j.x)
    max_x = max(tile_i.x, tile_j.x)
    min_y = min(tile_i.y, tile_j.y)
    max_y = max(tile_i.y, tile_j.y)

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    if not is_center_allowed(center_x, center_y, edges):
        return False

    # check if any edge cross the rectangle
    return all(not edge_crosses_rectangle(edge, min_x, min_y, max_x, max_y) for edge in edges)


def part_one(data: str) -> int:
    """Return the answer to part one."""
    red_tiles = get_red_tiles(data)

    max_area = 0
    for i_idx, tile_i in enumerate(red_tiles):
        for tile_j in red_tiles[i_idx + 1 :]:
            max_area = max(max_area, calculate_area(tile_i, tile_j))

    return max_area


def part_two(data: str) -> int:
    """Return the answer to part two."""
    red_tiles = get_red_tiles(data)
    edges = get_edges(red_tiles)

    max_area = 0
    for i_idx, tile_i in enumerate(red_tiles):
        for tile_j in red_tiles[i_idx + 1 :]:
            if is_allowed_rectangle(tile_i, tile_j, edges):
                max_area = max(max_area, calculate_area(tile_i, tile_j))

    return max_area


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
