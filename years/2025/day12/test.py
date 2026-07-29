# ruff: file-ignore[magic-value-comparison]  # ruff: ignore[unused-noqa]

from pathlib import Path

import pytest
from solution import part_one

SAMPLE_PATH = Path(__file__).parent / 'sample_input.txt'


def get_sample_sections() -> tuple[str, list[str]]:
    shapes, regions = SAMPLE_PATH.read_text().rstrip('\n').rsplit('\n\n', maxsplit=1)
    return shapes, regions.splitlines()


def test_part_one_with_sample_input() -> None:
    assert part_one(SAMPLE_PATH.read_text().rstrip('\n')) == 2


@pytest.mark.parametrize(
    ('region_index', 'expected'),
    [
        (0, 1),
        (1, 1),
        (2, 0),
    ],
)
def test_part_one_for_each_sample_region(region_index: int, expected: int) -> None:
    shapes, regions = get_sample_sections()
    data = f'{shapes}\n\n{regions[region_index]}'

    assert part_one(data) == expected
