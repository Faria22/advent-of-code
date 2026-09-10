import operator
from functools import reduce
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

LENGTH = 256


def parse_data(input_path: Path) -> list[int]:
    return [int(n) for n in input_path.read_text().strip().split(',')]


def translate_input(input_path: Path) -> list[int]:
    lengths = [ord(char) for char in input_path.read_text().strip()]
    return [*lengths, 17, 31, 73, 47, 23]


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


def part_one(input_path: Path, num_elements: int = LENGTH) -> int:
    """Return the answer to part one."""
    lengths = parse_data(input_path)
    elements = list(range(num_elements))
    elements, _, _ = single_round(elements, lengths, 0, 0)

    return elements[0] * elements[1]


def part_two(input_path: Path) -> str:
    """Return the answer to part two."""
    lengths = translate_input(input_path)
    elements = list(range(LENGTH))

    idx = 0
    skip_size = 0
    for _ in range(64):
        elements, idx, skip_size = single_round(elements, lengths, idx, skip_size)

    sparse_hash = get_sparse_hash(elements)
    return get_knot_hash(sparse_hash)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
