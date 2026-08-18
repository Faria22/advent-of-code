import re
from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> tuple[dict[str, list[str]], str]:
    replacement_lines, molecule = input_path.read_text().strip().split('\n\n')
    replacements = defaultdict(list)
    for line in replacement_lines.split('\n'):
        key, val = line.split(' => ')
        replacements[key].append(val)

    return replacements, molecule


def get_next_molecules(
    frontier: set[str],
    rules: list[tuple[str, str]],
) -> set[str]:
    frontier = {molecule.replace(start, end, 1) for molecule in frontier for start, end in rules if start in molecule}

    return set(sorted(frontier, key=len)[:1000])


def replace_nth(text: str, old: str, new: str, n: int) -> str:
    matches = [match.start() for match in re.finditer(re.escape(old), text)]

    if len(matches) <= n:
        return text

    idx = matches[n]

    return text[:idx] + new + text[idx + len(old) :]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    molecule_replacements, start = parse_data(input_path)

    next_molecules = set()

    for molecule, replacements in molecule_replacements.items():
        count = start.count(molecule)
        for replacement in replacements:
            next_molecules.update(replace_nth(start, molecule, replacement, i) for i in range(count))

    return len(next_molecules)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    molecule_replacements, final_molecule = parse_data(input_path)

    rules = [(new, old) for old, replacements in molecule_replacements.items() for new in replacements]

    frontier = {final_molecule}
    count = 0
    while 'e' not in frontier:
        frontier = get_next_molecules(frontier, rules)
        count += 1

    return count


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
