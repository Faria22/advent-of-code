from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().replace(',', '').strip().split('\n')


def run_program(a: int, b: int, lines: list[str]) -> tuple[int, int]:
    idx = 0
    max_idx = len(lines)
    while idx < max_idx:
        commands = lines[idx].split()
        match commands[0]:
            case 'hlf':
                if commands[1] == 'a':
                    a //= 2
                else:
                    b //= 2
            case 'tpl':
                if commands[1] == 'a':
                    a *= 3
                else:
                    b *= 3
            case 'inc':
                if commands[1] == 'a':
                    a += 1
                else:
                    b += 1
            case 'jmp':
                idx += int(commands[1])
                continue
            case 'jie':
                val = a if commands[1] == 'a' else b
                if val % 2 == 0:
                    idx += int(commands[2])
                    continue
            case 'jio':
                val = a if commands[1] == 'a' else b
                if val == 1:
                    idx += int(commands[2])
                    continue
        idx += 1
    return a, b


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    lines = parse_data(input_path)
    return run_program(0, 0, lines)[1]


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    lines = parse_data(input_path)
    return run_program(1, 0, lines)[1]


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
