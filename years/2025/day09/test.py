# ruff: noqa: PLR2004
from pathlib import Path

from solution import (
    Edge,
    edge_crosses_rectangle,
    get_edges,
    get_red_tiles,
    is_center_allowed,
    part_one,
    part_two,
)


def test_part_one() -> None:
    input_path = Path(__file__).parent / 'sample_input.txt'
    data = input_path.read_text().rstrip('\n')
    assert part_one(data) == 50


def test_part_two() -> None:
    input_path = Path(__file__).parent / 'sample_input.txt'
    data = input_path.read_text().rstrip('\n')
    assert part_two(data) == 24


def test_part_two_rejects_rectangle_containing_an_off_center_notch() -> None:
    data = """0,0
10,0
10,10
9,10
9,6
7,6
7,10
0,10"""

    # The 11x11 bounding rectangle is invalid because it contains the notch.
    # The largest valid rectangle runs from (0, 0) to (7, 10).
    assert part_two(data) == 88


def test_center_ray_through_vertex_uses_half_open_edge_ranges() -> None:
    data = """0,0
4,0
4,2
2,2
2,4
0,4"""
    edges = get_edges(get_red_tiles(data))

    # (1, 2) is inside the L-shaped polygon. The ray passes through the y=2
    # endpoints of two vertical edges, so only one endpoint should be counted.
    assert is_center_allowed(1, 2, edges)


def test_edge_crosses_rectangle() -> None:
    crossing_edge = Edge('h', const=6, min=7, max=9)
    outside_edge = Edge('h', const=11, min=0, max=10)

    # The first edge lies wholly inside the rectangle; the second is above it.
    assert edge_crosses_rectangle(crossing_edge, 0, 0, 10, 10)
    assert not edge_crosses_rectangle(outside_edge, 0, 0, 10, 10)
