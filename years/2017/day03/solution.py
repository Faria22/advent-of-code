from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> int:
    return int(input_path.read_text().strip())


def get_location_pos(location: int) -> Pos:
    if location == 1:
        return Pos(0, 0)

    ring = 3
    while ring**2 < location:
        ring += 2

    start_row = (ring - 3) // 2
    start_col = start_row + 1

    if location == ring**2:
        return Pos(start_row + 1, start_col)

    start_location = (ring - 2) ** 2 + 1
    num_locations_up = ring - 2
    num_locations_left = num_locations_down = num_locations_right = num_locations_up + 1

    # Check if location is above start of the ring
    if start_location <= location <= start_location + num_locations_up:
        shift = location - start_location
        return Pos(start_row - shift, start_col)

    start_row -= num_locations_up
    start_location += num_locations_up

    # Check if location is above and left start of the ring
    if start_location <= location <= start_location + num_locations_left:
        shift = location - start_location
        return Pos(start_row, start_col - shift)

    start_col -= num_locations_left
    start_location += num_locations_left

    # Check if location is above, left, and down start of the ring
    if start_location <= location <= start_location + num_locations_down:
        shift = location - start_location
        return Pos(start_row + shift, start_col)

    start_row += num_locations_down
    start_location += num_locations_down

    # Check if location is above, left, down, right start of the ring
    if start_location <= location <= start_location + num_locations_right:
        shift = location - start_location
        return Pos(start_row, start_col + shift)

    raise RuntimeError


def part_one(location: int = parse_data(INPUT_PATH)) -> int:
    """Return the answer to part one."""
    return sum(abs(x) for x in get_location_pos(location))


def part_two(input_val: int = parse_data(INPUT_PATH)) -> int:
    """Return the answer to part two."""
    location_values = {Pos(0, 0): 1}
    for location in range(2, input_val**2):
        pos = get_location_pos(location)
        if (val := sum(location_values.get(neighbor, 0) for neighbor in pos.neighbors(diagonals=True))) > input_val:
            return val

        location_values[pos] = val

    return 0


def main() -> None:
    print(f'Part 1: {part_one()}')
    print(f'Part 2: {part_two()}')


if __name__ == '__main__':
    main()
