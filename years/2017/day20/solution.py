import re
from itertools import combinations
from math import sqrt
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Coordinate = tuple[int, int, int]


def get_values_inside_brakets(raw_string: str) -> Coordinate:
    raw_values = re.findall(r'<(-?\d+),(-?\d+),(-?\d+)>', raw_string)[0]
    return int(raw_values[0]), int(raw_values[1]), int(raw_values[2])


def parse_data(input_path: Path) -> tuple[list[Coordinate], list[Coordinate], list[Coordinate]]:
    positions = []
    velocities = []
    accelerations = []
    for line in input_path.read_text().strip().split('\n'):
        p, v, a = line.split()
        positions.append(get_values_inside_brakets(p))
        velocities.append(get_values_inside_brakets(v))
        accelerations.append(get_values_inside_brakets(a))

    return positions, velocities, accelerations


def manhattan_distance(coordinate: Coordinate) -> int:
    return sum(abs(c) for c in coordinate)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    _, _, accelerations = parse_data(input_path)
    max_idx = 0
    min_acceleration_magnitude = manhattan_distance(accelerations[0])
    for idx, acceleration in enumerate(accelerations):
        if (acceleration_magnitude := manhattan_distance(acceleration)) < min_acceleration_magnitude:
            max_idx = idx
            min_acceleration_magnitude = acceleration_magnitude

    return max_idx


def collision_time_1d(a_p: int, a_v: int, a_a: int, b_p: int, b_v: int, b_a: int) -> list[int]:
    if a_p == b_p and a_v == b_v and a_a == b_a:
        return [0]

    delta_a = a_a - b_a
    delta_v = a_v - b_v
    delta_p = a_p - b_p

    if delta_a == delta_v == delta_p == 0:
        return [0]

    # These are a, b, c from the quadratic formula
    a = delta_a
    b = delta_a + 2 * delta_v
    c = 2 * delta_p

    delta = b**2 - 4 * a * c
    if delta < 0:
        return []

    if a == 0:
        if b == 0:
            return []
        time = -c / b
        if time < 0 or time != int(time):
            return []
        return [int(time)]

    low_time = (-b - sqrt(delta)) / (2 * a)
    high_time = (-b + sqrt(delta)) / (2 * a)

    collision_times = []
    if low_time > 0 and low_time == int(low_time):
        collision_times.append(int(low_time))
    if high_time > 0 and high_time == int(high_time):
        collision_times.append(int(high_time))

    return collision_times


def collision_time_3d(
    a_p: Coordinate,
    a_v: Coordinate,
    a_a: Coordinate,
    b_p: Coordinate,
    b_v: Coordinate,
    b_a: Coordinate,
) -> int | None:
    prev_collision_time: list[int] | int | None = None
    for d in range(3):
        collision_time_d = collision_time_1d(a_p[d], a_v[d], a_a[d], b_p[d], b_v[d], b_a[d])
        if collision_time_d == 0:  # if the time is 0 that means they are always together in that dimension
            continue

        if prev_collision_time is None and collision_time_d:
            prev_collision_time = collision_time_d
            continue

        if not collision_time_d:
            return None

        if isinstance(prev_collision_time, list):
            if not any(time in prev_collision_time for time in collision_time_d):
                return None
            if prev_collision_time[0] in collision_time_d:
                prev_collision_time = prev_collision_time[0]
            else:
                prev_collision_time = prev_collision_time[1]
        elif prev_collision_time not in collision_time_d:
            return None

    assert isinstance(prev_collision_time, int) or prev_collision_time is None
    return prev_collision_time


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    positions, velocities, accelerations = parse_data(input_path)
    num_particles = len(positions)
    collisions = {}
    for idx_a, idx_b in combinations(range(num_particles), 2):
        if (
            collision_time := collision_time_3d(
                positions[idx_a],
                velocities[idx_a],
                accelerations[idx_a],
                positions[idx_b],
                velocities[idx_b],
                accelerations[idx_b],
            )
        ) is not None:
            collisions[idx_a, idx_b] = collision_time

    sorted_collisions = sorted(collisions, key=collisions.get)  # ty: ignore[no-matching-overload]
    destroyed = set()
    prev_destroyed_time = 0
    for idx_a, idx_b in sorted_collisions:
        if (destroyed_time := collisions[idx_a, idx_b]) == prev_destroyed_time:
            destroyed.update((idx_a, idx_b))
            continue

        if any(idx in destroyed for idx in (idx_a, idx_b)):
            continue

        prev_destroyed_time = destroyed_time
        destroyed.update((idx_a, idx_b))

    return num_particles - len(destroyed)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
