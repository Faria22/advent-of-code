# ruff: file-ignore[magic-value-comparison]

from solution import part_one, part_two


def test_part_one_with_sample_input() -> None:
    assert part_one('{}') == 1
    assert part_one('{{{}}}') == 6
    assert part_one('{{},{}}') == 5
    assert part_one('{{{},{},{{}}}}') == 16
    assert part_one('{<a>,<a>,<a>,<a>}') == 1
    assert part_one('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert part_one('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert part_one('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


def test_part_two_with_sample_input() -> None:
    assert part_two('<>') == 0
    assert part_two('<random characters>') == 17
    assert part_two('<<<<>') == 3
    assert part_two('<{!>}>') == 2
    assert part_two('<!!>') == 0
    assert part_two('<!!!>>') == 0
    assert part_two('<{o"i!a,<{i<a>') == 10
