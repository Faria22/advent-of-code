from aoc import Pos


def test_pos_supports_coordinate_arithmetic() -> None:
    pos = Pos(2, 3)

    assert pos + Pos(-1, 4) == Pos(1, 7)
    assert pos - Pos(-1, 4) == Pos(3, -1)
    assert pos * 2 == Pos(4, 6)


def test_neighbors_returns_cardinal_neighbors_in_order() -> None:
    pos = Pos(2, 3)

    assert list(pos.neighbors()) == [
        Pos(1, 3),
        Pos(3, 3),
        Pos(2, 2),
        Pos(2, 4),
    ]


def test_neighbors_preserves_a_pos_subclass() -> None:
    class SpecialPos(Pos):
        pass

    neighbors = SpecialPos(2, 3).neighbors()

    assert all(isinstance(pos, SpecialPos) for pos in neighbors)
