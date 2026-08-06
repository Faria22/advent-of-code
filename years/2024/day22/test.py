# ruff: file-ignore[magic-value-comparison]
from pathlib import Path

from solution import part_one, part_two, process

DIR = Path(__file__).parent


def test_part_one_with_sample_input() -> None:
    assert part_one(DIR / 'sample_input1.txt') == 37327623


def test_part_two_with_sample_input() -> None:
    assert part_two(DIR / 'sample_input2.txt') == 23


def test_process() -> None:
    assert process(123) == 15887950
    assert process(15887950) == 16495136
    assert process(16495136) == 527345
    assert process(527345) == 704524
    assert process(704524) == 1553684
    assert process(1553684) == 12683156
    assert process(12683156) == 11100544
    assert process(11100544) == 12249484
    assert process(12249484) == 7753432
    assert process(7753432) == 5908254


def test_2000_process() -> None:
    assert process(1, 2000) == 8685429
    assert process(10, 2000) == 4700978
    assert process(100, 2000) == 15273692
    assert process(2024, 2000) == 8667524
