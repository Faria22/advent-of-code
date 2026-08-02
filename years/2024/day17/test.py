# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import Computer, part_one, part_two

DIR = Path(__file__).parent


def test_simple_programs() -> None:
    computer = Computer(0, 0, 9, [2, 6])
    output = computer.run_program()
    assert computer.b == 1

    computer = Computer(10, 0, 0, [5, 0, 5, 1, 5, 4])
    output = computer.run_program()
    assert output == '0,1,2'

    computer = Computer(2024, 0, 0, [0, 1, 5, 4, 3, 0])
    output = computer.run_program()
    assert output == '4,2,5,6,7,7,7,7,3,1,0'
    assert computer.a == 0

    computer = Computer(0, 29, 0, [1, 7])
    output = computer.run_program()
    assert computer.b == 26

    computer = Computer(0, 2024, 43690, [4, 0])
    output = computer.run_program()
    assert computer.b == 44354


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == '4,6,3,5,6,3,5,2,1,0'


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 117440
