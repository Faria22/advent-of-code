from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Programs = dict[int, set[int]]


def parse_data(input_path: Path) -> Programs:
    program_connections = {}
    for line in input_path.read_text().strip().split('\n'):
        program, connections = line.split(' <-> ')
        program_connections[int(program)] = {int(p) for p in connections.split(', ')}
    return program_connections


def get_all_programs_in_the_same_group_as_program(original_program: int, program_connections: Programs) -> set[int]:
    programs_connected_to_original = set()
    frontier = program_connections[original_program]
    while frontier:
        program = frontier.pop()
        if program in programs_connected_to_original:
            continue
        programs_connected_to_original.add(program)
        frontier.update(program_connections[program])

    return programs_connected_to_original


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    program_connections = parse_data(input_path)
    return len(get_all_programs_in_the_same_group_as_program(0, program_connections))


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    program_connections = parse_data(input_path)
    num_groups = 0
    while program_connections:
        num_groups += 1
        program = next(iter(program_connections))
        connections = get_all_programs_in_the_same_group_as_program(program, program_connections)

        for program in connections:
            del program_connections[program]

    return num_groups


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
