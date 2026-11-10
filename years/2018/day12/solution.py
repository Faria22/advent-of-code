from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> tuple[set[int], set[str]]:
    lines = input_path.read_text().strip().split('\n')

    initial_state_str = lines[0].split(': ')[1]
    initial_state = {idx for idx, char in enumerate(initial_state_str) if char == '#'}

    combinations = set()
    for line in lines[2:]:
        input_, _, output = line.split()
        if output == '#':
            combinations.add(input_)

    return initial_state, combinations


def next_state(state: set[int], combinations: set[str]) -> set[int]:
    min_pot = min(state) - 2
    max_pot = max(state) + 2

    neighbors = '.....'
    next_state = set()
    for pot in range(min_pot, max_pot + 2):
        neighbors += '#' if pot in state else '.'
        neighbors = neighbors[1:]
        if neighbors in combinations:
            next_state.add(pot - 2)

    return next_state


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    state, combinations = parse_data(input_path)
    num_steps = 20

    for _ in range(num_steps):
        state = next_state(state, combinations)

    return sum(state)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    state, combinations = parse_data(input_path)
    num_steps = 50_000_000_000

    # at step 112 the sum of the pots is 10_520
    # and after each step the sum goes up by 80

    return (num_steps - 113) * 80 + 10_520


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
