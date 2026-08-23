from collections.abc import Iterator
from copy import deepcopy
from typing import Self, overload

from aoc.pos import Pos


class Grid[T]:
    def __init__(self, grid: list[list[T]]) -> None:
        self._grid = grid
        self.shape = (len(self._grid), len(self._grid[0]))

    def in_bounds(self, pos: Pos) -> bool:
        return 0 <= pos.row < self.shape[0] and 0 <= pos.col < self.shape[1]

    def copy(self) -> Self:
        return type(self)(deepcopy(self._grid))

    @overload
    def __getitem__(self, key: Pos) -> T | None: ...

    @overload
    def __getitem__(self, key: int) -> list[T]: ...

    def __getitem__(self, key: Pos | int) -> T | list[T] | None:
        if isinstance(key, int):
            if not (0 <= key < self.shape[0]):
                return None
            return self._grid[key]

        if not self.in_bounds(key):
            return None

        return self._grid[key.row][key.col]

    @overload
    def __setitem__(self, key: Pos, value: T) -> None: ...

    @overload
    def __setitem__(self, key: int, value: list[T]) -> None: ...

    def __setitem__(self, key: Pos | int, value: T | list[T]) -> None:
        if isinstance(key, int):
            if not (0 <= key < self.shape[0]):
                raise IndexError('grid row index out of range')
            if not isinstance(value, list) or len(value) != self.shape[1]:
                raise ValueError('replacement row must match the grid width')
            self._grid[key] = value
            return

        if not self.in_bounds(key):
            raise IndexError('grid position out of range')

        self._grid[key.row][key.col] = value  # ty: ignore[invalid-assignment]

    def __iter__(self) -> Iterator[list[T]]:
        yield from self._grid

    def __repr__(self) -> str:
        return f'Grid{self.shape}'
