import json
import re
from pathlib import Path
from typing import Any

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> str:
    return input_path.read_text().strip()


def get_sum(content: str) -> int:
    numbers = re.findall(r'(-?\d+)', content)
    return sum(int(num) for num in numbers)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    line = parse_data(input_path)
    return get_sum(line)


def walk_json(value: Any) -> int:
    total = 0
    if isinstance(value, dict):
        if 'red' in value or 'red' in value.values():
            return total

        for item in value.values():
            total += walk_json(item)

    elif isinstance(value, list):
        for item in value:
            total += walk_json(item)
    elif isinstance(value, int):
        total += value
    return total


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    line = parse_data(input_path)
    data = json.loads(line)
    return walk_json(data)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
