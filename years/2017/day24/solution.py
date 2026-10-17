from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Component = tuple[int, int]


def parse_data(input_path: Path) -> list[Component]:
    components = []
    for line in input_path.read_text().strip().split('\n'):
        component_parts = line.split('/')
        component_tuple = tuple(int(c) for c in component_parts)
        components.append(component_tuple)

    return components  # ty: ignore[invalid-return-type]


def strongest_brigde_strength(edge: int, available_components: list[Component]) -> int:
    if not available_components:
        return 0

    if not any(edge in component for component in available_components):
        return 0

    max_strength = 0
    for component in available_components:
        a, b = component
        if edge == a:
            new_edge = b
        elif edge == b:
            new_edge = a
        else:
            continue

        new_available_components = available_components.copy()
        new_available_components.remove(component)

        new_strength = sum(component) + strongest_brigde_strength(new_edge, new_available_components)
        max_strength = max(max_strength, new_strength)

    return max_strength


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    components = parse_data(input_path)
    return strongest_brigde_strength(0, components)


def longest_strongest_brigde_strength(edge: int, length: int, available_components: list[Component]) -> tuple[int, int]:
    if not available_components:
        return 0, length

    if not any(edge in component for component in available_components):
        return 0, length

    max_strength = 0
    max_length = 0
    for component in available_components:
        a, b = component
        if edge == a:
            new_edge = b
        elif edge == b:
            new_edge = a
        else:
            continue

        new_available_components = available_components.copy()
        new_available_components.remove(component)

        new_strength, new_length = longest_strongest_brigde_strength(new_edge, length + 1, new_available_components)
        new_strength += sum(component)

        if new_length == max_length:
            max_strength = max(max_strength, new_strength)
        elif new_length > max_length:
            max_strength = new_strength
            max_length = new_length

    return max_strength, max_length


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    components = parse_data(input_path)
    return longest_strongest_brigde_strength(0, 0, components)[0]


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
