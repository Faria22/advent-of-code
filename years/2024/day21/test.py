# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import DirPad, NumPad, lowest_cost_move, part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH) == 126384


def test_lowest_cost_move_without_remaining_layers() -> None:
    cost = lowest_cost_move(NumPad, 'A', 'A', 0)
    assert cost == 1


def test_lowest_cost_move_accounts_for_starting_button() -> None:
    forward_cost = lowest_cost_move(DirPad, 'A', '<', 1)
    reverse_cost = lowest_cost_move(DirPad, '<', 'A', 1)

    assert forward_cost == 10
    assert reverse_cost == 8


def test_lowest_cost_move_selects_best_three_to_seven_path() -> None:
    cost = lowest_cost_move(NumPad, '3', '7', 2)
    assert cost == 23
