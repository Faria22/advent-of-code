from collections import Counter
from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Program:
    weight: int
    weight_under: int
    children: set[str]


def parse_data(input_path: Path) -> dict[str, Program]:
    programs = {}
    for line in input_path.read_text().strip().split('\n'):
        program, *children_str = line.split(' -> ')

        program, weight = program.split()
        weight = int(weight[1:-1])

        children = set(children_str[0].split(', ')) if children_str else set()

        programs[program] = Program(weight, 0, children)

    return programs


def part_one(input_path: Path) -> str:
    """Return the answer to part one."""
    programs = parse_data(input_path)
    child_programs = {child for program in programs.values() for child in program.children}
    return (programs.keys() - child_programs).pop()


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    programs = parse_data(input_path)
    while True:
        for parent, program in programs.items():
            # Only check programs above leaf programs
            children_programs = {child: programs[child] for child in program.children}
            if not children_programs or any(child_program.children for child_program in children_programs.values()):
                continue

            # All children have the same weight
            children_weight = {
                child: c_program.weight + c_program.weight_under for child, c_program in children_programs.items()
            }
            if len(set(children_weight.values())) == 1:
                weight_under = 0
                for child in children_programs:
                    child_program = programs.pop(child)
                    weight_under += child_program.weight + child_program.weight_under

                programs[parent] = Program(program.weight, weight_under, set())
                break

            # Weights are different
            (common, _), (different, _) = Counter(children_weight.values()).most_common()
            difference = different - common
            for child, weight in children_weight.items():
                if weight == different:
                    return programs[child].weight - difference


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
