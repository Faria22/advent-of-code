# ruff: noqa: PLR2004

from types import SimpleNamespace

import pytest
from solution import JoltageMachine, LightMachine, parse_lights, part_one, part_two

SAMPLE_MACHINES = [
    ('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', 2),
    ('[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}', 3),
    ('[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}', 2),
]

SAMPLE_JOLTAGE_RESULTS = [10, 12, 11]


@pytest.mark.parametrize(('machine', 'expected'), SAMPLE_MACHINES)
def test_part_one_for_each_sample_machine(machine: str, expected: int) -> None:
    assert part_one(machine) == expected


def test_part_one_for_complete_sample() -> None:
    data = '\n'.join(machine for machine, _ in SAMPLE_MACHINES)
    assert part_one(data) == 7


def test_toggle_button_on_machine() -> None:
    button = 0b1010
    machine = LightMachine(correct_lights=0, buttons=[button])

    machine.press_button(0)

    assert machine.current_lights == 0b1010

    machine.press_button(0)

    assert machine.current_lights == 0


def test_check_lights() -> None:
    machine = LightMachine(correct_lights=0b1010, buttons=[0b1010])

    assert not machine.check_lights()

    machine.press_button(0)

    assert machine.check_lights()


def test_parse_lights() -> None:
    assert parse_lights('[.#..]') == 0b0010
    assert parse_lights('[.##.]') == 0b0110
    assert parse_lights('[###.]') == 0b0111
    assert parse_lights('[####]') == 0b1111
    assert parse_lights('.#..') == 0b0010
    assert parse_lights('.##.') == 0b0110
    assert parse_lights('###.') == 0b0111
    assert parse_lights('####') == 0b1111


@pytest.mark.parametrize(
    ('machine', 'expected'),
    list(zip((machine for machine, _ in SAMPLE_MACHINES), SAMPLE_JOLTAGE_RESULTS, strict=True)),
)
def test_part_two_for_each_sample_machine(machine: str, expected: int) -> None:
    assert part_two(machine) == expected


def test_part_two_for_complete_sample() -> None:
    data = '\n'.join(machine for machine, _ in SAMPLE_MACHINES)
    assert part_two(data) == 33


def test_joltage_solution_does_not_truncate_solver_roundoff(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_linprog(*_args: object, **_kwargs: object) -> SimpleNamespace:
        return SimpleNamespace(fun=59.99999999999999)

    monkeypatch.setattr('solution.linprog', fake_linprog)
    machine = JoltageMachine(correct_joltage=[0], buttons=[])

    assert machine.solve() == 60
