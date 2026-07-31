from advent_of_code import Grid, Pos


def test_grid_supports_generic_cell_values() -> None:
    grid = Grid([['a', 'b'], ['c', 'd']])

    assert grid[Pos(1, 0)] == 'c'


def test_grid_can_return_a_row() -> None:
    grid = Grid([['a', 'b'], ['c', 'd']])

    assert grid[1] == ['c', 'd']


def test_grid_identifies_positions_in_bounds() -> None:
    grid = Grid([['a', 'b'], ['c', 'd']])

    assert grid.in_bounds(Pos(0, 0))
    assert grid.in_bounds(Pos(1, 1))
    assert not grid.in_bounds(Pos(-1, 0))
    assert not grid.in_bounds(Pos(0, -1))
    assert not grid.in_bounds(Pos(2, 0))
    assert not grid.in_bounds(Pos(0, 2))
