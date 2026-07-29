from collections import defaultdict
from itertools import batched
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

EMPTY = -1


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def strip_blocks(blocks: list[int]) -> None:
    while (last := blocks.pop()) == EMPTY:
        continue
    blocks.append(last)


def disk_map_to_blocks(disk_map: str) -> list[int]:
    blocks = []
    for idx, num in enumerate(disk_map):
        if idx % 2 == 0:
            blocks.extend([idx // 2] * int(num))
        else:
            blocks.extend([EMPTY] * int(num))
    strip_blocks(blocks)
    return blocks


def move_individual_blocks(blocks: list[int]) -> list[int]:
    while blocks.count(EMPTY) != 0:
        empty_idx = blocks.index(EMPTY)
        blocks[empty_idx] = blocks.pop()
        strip_blocks(blocks)

    return blocks


def get_block_inds(blocks: list[int]) -> dict[int, list[int]]:
    block_inds: dict[int, list[int]] = defaultdict(list)
    prev = None
    for idx, block in enumerate(blocks):
        if block != prev:
            block_inds[block].append(idx)
            if prev is not None:
                block_inds[prev].append(idx - 1)
        prev = block

    assert prev is not None
    block_inds[prev].append(len(blocks) - 1)

    return block_inds


def move_whole_blocks(blocks: list[int]) -> list[int]:
    block_inds = get_block_inds(blocks)
    ids = reversed(sorted(block_inds.keys())[1:])
    for file_id in ids:
        block_start, block_end = block_inds[file_id]
        block_size = block_end - block_start + 1

        for idx, (empty_start, empty_end) in enumerate(batched(block_inds[EMPTY], 2)):
            if empty_start > block_start:
                continue
            empty_size = empty_end - empty_start + 1
            if empty_size >= block_size:
                blocks[empty_start : empty_start + block_size] = [file_id] * block_size
                blocks[block_start : block_end + 1] = [EMPTY] * block_size

                if empty_size > block_size:
                    block_inds[EMPTY][idx * 2] = empty_start + block_size
                else:
                    block_inds[EMPTY].pop(idx * 2)
                    block_inds[EMPTY].pop(idx * 2)
                break

    return blocks


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    data = parse_data(input_path)
    blocks = disk_map_to_blocks(data)
    blocks = move_individual_blocks(blocks)
    return sum(idx * num for idx, num in enumerate(blocks))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)
    blocks = disk_map_to_blocks(data)
    blocks = move_whole_blocks(blocks)
    return sum(idx * num for idx, num in enumerate(blocks) if num > 0)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
