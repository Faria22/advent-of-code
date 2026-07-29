# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

import pytest
from solution import (
    EMPTY,
    disk_map_to_blocks,
    get_block_inds,
    move_individual_blocks,
    move_whole_blocks,
    parse_data,
    part_one,
    part_two,
    strip_blocks,
)

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_parse_data_strips_surrounding_whitespace(tmp_path: Path) -> None:
    input_path = tmp_path / 'input.txt'
    input_path.write_text('\n  12345  \n')

    assert parse_data(input_path) == '12345'


@pytest.mark.parametrize(
    ('disk_map', 'expected'),
    [
        ('12345', [0, EMPTY, EMPTY, 1, 1, 1, EMPTY, EMPTY, EMPTY, EMPTY, 2, 2, 2, 2, 2]),
        ('101', [0, 1]),
        ('12', [0]),
    ],
)
def test_disk_map_to_blocks(disk_map: str, expected: list[int]) -> None:
    assert disk_map_to_blocks(disk_map) == expected


def test_disk_map_to_blocks_keeps_multi_digit_file_ids_as_single_blocks() -> None:
    assert disk_map_to_blocks('10' * 10 + '1') == list(range(11))


def test_strip_blocks_removes_trailing_empty_blocks_in_place() -> None:
    blocks = [0, 1, EMPTY, EMPTY]

    result = strip_blocks(blocks)

    assert result is None
    assert blocks == [0, 1]


@pytest.mark.parametrize(
    ('blocks', 'expected'),
    [
        (
            [0, EMPTY, EMPTY, 1, 1, 1, EMPTY, EMPTY, EMPTY, EMPTY, 2, 2, 2, 2, 2],
            [0, 2, 2, 1, 1, 1, 2, 2, 2],
        ),
        ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([0, EMPTY, EMPTY], [0]),
        ([], []),
    ],
)
def test_individual_move_blocks(blocks: list[int], expected: list[int]) -> None:
    assert move_individual_blocks(blocks) == expected


def test_get_block_inds_returns_file_and_empty_spans() -> None:
    blocks = [0, 0, EMPTY, EMPTY, 1, 1, 1, EMPTY, 2, 2]

    assert get_block_inds(blocks) == {
        EMPTY: [2, 3, 7, 7],
        0: [0, 1],
        1: [4, 6],
        2: [8, 9],
    }


def test_move_whole_blocks_moves_file_into_exact_sized_left_gap() -> None:
    blocks = [0, 0, EMPTY, EMPTY, 1, 1]

    assert move_whole_blocks(blocks) == [0, 0, 1, 1, EMPTY, EMPTY]


def test_move_whole_blocks_does_not_reuse_consumed_exact_fit_gap() -> None:
    blocks = [0, EMPTY, EMPTY, 1, 1, EMPTY, EMPTY, 2, 2]

    assert move_whole_blocks(blocks) == [
        0,
        2,
        2,
        1,
        1,
        EMPTY,
        EMPTY,
        EMPTY,
        EMPTY,
    ]


def test_move_whole_blocks_preserves_disk_length() -> None:
    blocks = [0, EMPTY, EMPTY, 1, 1]
    original_length = len(blocks)

    result = move_whole_blocks(blocks)

    assert len(result) == original_length


def test_move_whole_blocks_does_not_move_file_to_the_right() -> None:
    blocks = [0, 0, 1, 1, EMPTY, EMPTY, 2, 2, 2]
    expected = blocks.copy()

    assert move_whole_blocks(blocks) == expected


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH) == 1928


def test_part_two_with_sample_input() -> None:
    assert part_two(SAMPLE_PATH) == 2858
