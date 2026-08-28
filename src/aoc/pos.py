from collections.abc import Iterator
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, slots=True)
class Pos:
    row: int
    col: int

    def __add__(self, other: 'Pos') -> Self:
        """Return the component-wise sum of two positions."""
        return type(self)(self.row + other.row, self.col + other.col)

    def __sub__(self, other: 'Pos') -> Self:
        """Return the component-wise difference between two positions."""
        return type(self)(self.row - other.row, self.col - other.col)

    def __mul__(self, n: int) -> Self:
        """Return the position with both components multiplied by a scalar."""
        return type(self)(self.row * n, self.col * n)

    def __str__(self) -> str:
        """Return the position as a coordinate pair."""
        return f'({self.row}, {self.col})'

    def __repr__(self) -> str:
        """Return the position as a coordinate pair."""
        return f'({self.row}, {self.col})'

    def __iter__(self) -> Iterator[int]:
        """Yield the row followed by the column."""
        yield self.row
        yield self.col

    def shift(self, row_shift: int, col_shift: int) -> Self:
        """Return a position shifted by the given row and column offsets."""
        return type(self)(self.row + row_shift, self.col + col_shift)

    def shift_up(self, n: int = 1) -> Self:
        """Return a position shifted up by n rows."""
        return self.shift(-n, 0)

    def shift_down(self, n: int = 1) -> Self:
        """Return a position shifted down by n rows."""
        return self.shift(n, 0)

    def shift_left(self, n: int = 1) -> Self:
        """Return a position shifted left by n columns."""
        return self.shift(0, -n)

    def shift_right(self, n: int = 1) -> Self:
        """Return a position shifted right by n columns."""
        return self.shift(0, n)

    def neighbors(self, *, diagonals: bool = False) -> Iterator[Self]:
        """Yield up, down, left, and right, then optionally NW, NE, SW, and SE."""
        yield self.shift_up()
        yield self.shift_down()
        yield self.shift_left()
        yield self.shift_right()

        if diagonals:
            yield self.shift(-1, -1)
            yield self.shift(-1, 1)
            yield self.shift(1, -1)
            yield self.shift(1, 1)

    def move(self, move: str) -> Self:
        """Return the position reached by applying a ^, v, <, or > move."""
        match move:
            case '^':
                return self.shift_up()
            case 'v':
                return self.shift_down()
            case '>':
                return self.shift_right()
            case '<':
                return self.shift_left()
            case _:
                raise ValueError
