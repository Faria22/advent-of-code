from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

END_DEVICE = 'out'


def parse_data(data: str) -> dict[str, set[str]]:
    devices = {}
    for line in data.split('\n'):
        start, outputs = line.split(':')
        outputs = set(outputs.strip().split())
        devices[start] = outputs

    return devices


def solve_part_one(devices: dict[str, set[str]], cache: dict[str, int], start_point: str) -> None:
    if start_point in cache:
        return

    for device in devices[start_point]:
        if device == END_DEVICE:
            cache[start_point] += 1
        elif device not in cache:
            solve_part_one(devices, cache, device)
        cache[start_point] += cache[device]


def solve_part_two(
    devices: dict[str, set[str]],
    cache: dict[tuple[str, bool, bool], int],
    start_point: str,
    has_seen_dac: bool,
    has_seen_fft: bool,
) -> None:
    if (start_point, has_seen_dac, has_seen_fft) in cache:
        return

    for device in devices[start_point]:
        child_has_seen_dac = device == 'dac' or has_seen_dac
        child_has_seen_fft = device == 'fft' or has_seen_fft

        if device == END_DEVICE:
            cache[start_point, has_seen_dac, has_seen_fft] += 1 if has_seen_dac and has_seen_fft else 0
        elif device not in cache:
            solve_part_two(devices, cache, device, child_has_seen_dac, child_has_seen_fft)

        cache[start_point, has_seen_dac, has_seen_fft] += cache[device, child_has_seen_dac, child_has_seen_fft]


def part_one(data: str) -> int:
    """Return the answer to part one."""
    devices = parse_data(data)
    cache: dict[str, int] = defaultdict(int)
    start_point = 'you'

    solve_part_one(devices, cache, start_point)
    return cache[start_point]


def part_two(data: str) -> int:
    """Return the answer to part two."""
    devices = parse_data(data)
    cache: dict[tuple[str, bool, bool], int] = defaultdict(int)
    start_point = 'svr'

    solve_part_two(devices, cache, start_point, False, False)
    return cache[start_point, False, False]


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
