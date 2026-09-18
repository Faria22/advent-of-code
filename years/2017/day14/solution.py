import operator
from functools import reduce
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

LENGTH = 256
NUM_ROWS = 128


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def translate_input(input_str: str) -> list[int]:
    return [ord(char) for char in input_str] + [17, 31, 73, 47, 23]


def shift_list_left(list_: list, n: int) -> list:
    return list_[n:] + list_[:n]


def action(elements: list[int], idx: int, length: int) -> list[int]:
    elements = shift_list_left(elements, idx)
    elements[:length] = reversed(elements[:length])
    return shift_list_left(elements, -idx)


def single_round(elements: list[int], lengths: list[int], idx: int, skip_size: int) -> tuple[list[int], int, int]:
    num_elements = len(elements)
    for skip, length in enumerate(lengths, skip_size):
        elements = action(elements, idx, length)
        idx = (idx + length + skip) % num_elements

    return elements, idx, skip + 1


def get_sparse_hash(elements: list[int]) -> list[int]:
    sparse_hash = []
    for idx in range(16):
        val = reduce(operator.xor, elements[idx * 16 : idx * 16 + 16])
        sparse_hash.append(val)
    return sparse_hash


def get_knot_hash(sparse_hash: list[int]) -> str:
    return ''.join(f'{n:02x}' for n in sparse_hash)


def get_know_hash_from_string(input_str: str) -> str:
    """Return the answer to part two."""
    lengths = translate_input(input_str)
    elements = list(range(LENGTH))

    idx = 0
    skip_size = 0
    for _ in range(64):
        elements, idx, skip_size = single_round(elements, lengths, idx, skip_size)

    sparse_hash = get_sparse_hash(elements)
    return get_knot_hash(sparse_hash)


def convert_hash_to_binary(input_hash: str) -> str:
    return ''.join(f'{int(char, 16):04b}' for char in input_hash)


def part_one(input_path: Path) -> int:
    key = parse_data(input_path)
    num_used_squares = 0

    for row in range(NUM_ROWS):
        input_string = f'{key}-{row}'
        knot_hash = get_know_hash_from_string(input_string)
        num_used_squares += convert_hash_to_binary(knot_hash).count('1')

    return num_used_squares


def get_neighbors_in_used_squares(cur_square: Pos, used_squares: set[Pos], seen: set[Pos]) -> set[Pos]:
    neighbors = seen | {cur_square}
    for neighbor in cur_square.neighbors():
        if neighbor in used_squares and neighbor not in seen:
            neighbors.add(neighbor)
            neighbors |= get_neighbors_in_used_squares(neighbor, used_squares, neighbors)

    return neighbors


def part_two(input_path: Path) -> int:
    """Return the answer to part one."""
    key = parse_data(input_path)
    grid = []

    for row in range(NUM_ROWS):
        input_string = f'{key}-{row}'
        knot_hash = get_know_hash_from_string(input_string)
        grid.append([bool(int(x)) for x in convert_hash_to_binary(knot_hash)])

    used_squares = {Pos(row, col) for row in range(NUM_ROWS) for col in range(NUM_ROWS) if grid[row][col]}
    num_groups = 0
    while used_squares:
        cur_square = used_squares.pop()
        neighbors_in_group = get_neighbors_in_used_squares(cur_square, used_squares, set())
        used_squares -= neighbors_in_group
        num_groups += 1

    return num_groups


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
