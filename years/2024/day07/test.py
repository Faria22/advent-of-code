# ruff: file-ignore[magic-value-comparison]  # ruff: ignore[unused-noqa]
from pathlib import Path

from solution import part_one, part_two, solve_expression

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH) == 3749


def test_part_two_with_sample_input() -> None:
    assert part_two(SAMPLE_PATH) == 11387


def test_solve_expression() -> None:
    assert solve_expression([10, 20], ['+']) == 30
    assert solve_expression([10, 20], ['*']) == 200
    assert solve_expression([10, 20], ['||']) == 1020
    assert solve_expression([10, 20, 30], ['+', '+']) == 60
    assert solve_expression([10, 20, 30], ['+', '*']) == 900
    assert solve_expression([10, 20, 30], ['+', '||']) == 3030
    assert solve_expression([10, 20, 30], ['*', '+']) == 230
    assert solve_expression([10, 20, 30], ['*', '*']) == 6000
    assert solve_expression([10, 20, 30], ['*', '||']) == 20030
    assert solve_expression([10, 20, 30], ['||', '+']) == 1050
    assert solve_expression([10, 20, 30], ['||', '*']) == 30600
    assert solve_expression([10, 20, 30], ['||', '||']) == 102030
