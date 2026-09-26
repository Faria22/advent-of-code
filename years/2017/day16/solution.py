import string
from pathlib import Path

from bidict import bidict

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split(',')


def spin(programs: list[str], move: str) -> list[str]:
    num_programs = len(programs)
    x = int(move[1:]) % num_programs
    n = num_programs - x
    return programs[n:] + programs[:n]


def exchange(programs: list[str], move: str) -> list[str]:
    a, b = move[1:].split('/')
    idx_a = int(a)
    idx_b = int(b)

    p_a = programs[idx_a]
    p_b = programs[idx_b]

    programs[idx_a] = p_b
    programs[idx_b] = p_a

    return programs


def partner(programs: list[str], move: str) -> list[str]:
    a, b = move[1:].split('/')
    idx_a = programs.index(a)
    idx_b = programs.index(b)

    programs[idx_a] = b
    programs[idx_b] = a
    return programs


def dance(programs: str, moves: list[str]) -> str:
    programs_list = list(programs)
    for move in moves:
        match move[0]:
            case 's':
                programs_list = spin(programs_list, move)
            case 'x':
                programs_list = exchange(programs_list, move)
            case 'p':
                programs_list = partner(programs_list, move)
    return ''.join(programs_list)


def part_one(input_path: Path, num_programs: int = 16) -> str:
    """Return the answer to part one."""
    programs = string.ascii_lowercase[:num_programs]
    moves = parse_data(input_path)
    return ''.join(dance(programs, moves))


def part_two(input_path: Path, num_programs: int = 16) -> str:
    """Return the answer to part two."""
    num_repetitions = 1_000_000_000
    programs = string.ascii_lowercase[:num_programs]
    moves = parse_data(input_path)
    seen_states = bidict()
    seen_states[0] = programs

    gap = None
    for idx in range(1, num_repetitions + 1):
        programs = dance(programs, moves)
        if programs in seen_states.values():
            first_idx = seen_states.inverse[programs]
            gap = idx - first_idx
            break
        seen_states[idx] = programs

    if gap:
        remaining = num_repetitions % gap
        return seen_states[first_idx + remaining]

    return programs


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
