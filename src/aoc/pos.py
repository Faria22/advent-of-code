from collections.abc import Iterator
from typing import NamedTuple, Self


class Pos(NamedTuple):
    row: int
    col: int

    def __add__(self, other: 'Pos') -> 'Pos':
        return type(self)(self.row + other.row, self.col + other.col)

    def __str__(self) -> str:
        return f'({self.row}, {self.col})'

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'

    def shift(self, row_shift: int, col_shift: int) -> Self:
        return type(self)(self.row + row_shift, self.col + col_shift)

    def shift_up(self, n: int = 1) -> Self:
        return self.shift(-n, 0)

    def shift_down(self, n: int = 1) -> Self:
        return self.shift(n, 0)

    def shift_left(self, n: int = 1) -> Self:
        return self.shift(0, -n)

    def shift_right(self, n: int = 1) -> Self:
        return self.shift(0, n)

    def neighbors(self) -> Iterator[Self]:
        yield self.shift_up()
        yield self.shift_down()
        yield self.shift_left()
        yield self.shift_right()
