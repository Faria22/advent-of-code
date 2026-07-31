from collections.abc import Iterator
from typing import overload

from advent_of_code.pos import Pos


class Grid[T]:
    def __init__(self, grid: list[list[T]]) -> None:
        self._grid = grid
        self.shape = (len(self._grid), len(self._grid[0]))

    @overload
    def __getitem__(self, key: Pos) -> T: ...

    @overload
    def __getitem__(self, key: int) -> list[T]: ...

    def __getitem__(self, key: Pos | int) -> T | list[T]:
        if isinstance(key, int):
            return self._grid[key]

        return self._grid[key.row][key.col]

    def __iter__(self) -> Iterator[list[T]]:
        yield from self._grid

    def in_bounds(self, pos: Pos) -> bool:
        return 0 <= pos.row < self.shape[0] and 0 <= pos.col < self.shape[1]

    def __repr__(self) -> str:
        return f'Grid{self.shape}'
