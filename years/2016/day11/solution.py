import re
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Floor = frozenset[str]


@dataclass(frozen=True, slots=True)
class State:
    elevator_floor: int
    generators: tuple[Floor, ...]
    chips: tuple[Floor, ...]
    moves: int

    def is_final(self) -> bool:
        return all(not (self.generators[floor] or self.chips[floor]) for floor in range(3))

    def is_valid(self) -> bool:
        for floor in range(4):
            # No need to check the floor if there are no chips on the floor
            if not self.chips[floor]:
                continue

            # If there are chips but no generators then the floor is safe
            if not self.generators[floor]:
                continue

            for chip in self.chips[floor]:
                if chip not in self.generators[floor]:
                    return False

        return True

    def next_states(self) -> set['State']:
        cur_floor = self.elevator_floor
        next_floors = self.next_floors(cur_floor)

        next_states = set()

        # Move 1 chip
        for chip in self.chips[cur_floor]:
            for new_floor in next_floors:
                new_chips = self.move_items(self.chips, {chip}, cur_floor, new_floor)
                next_states.add(State(new_floor, self.generators, new_chips, self.moves + 1))

        # Move 1 generator
        for generator in self.generators[cur_floor]:
            for new_floor in next_floors:
                new_generators = self.move_items(self.generators, {generator}, cur_floor, new_floor)
                next_states.add(State(new_floor, new_generators, self.chips, self.moves + 1))

        # Move 2 chips
        for chip_a, chip_b in combinations(self.chips[cur_floor], 2):
            for new_floor in next_floors:
                new_chips = self.move_items(self.chips, {chip_a, chip_b}, cur_floor, new_floor)
                next_states.add(State(new_floor, self.generators, new_chips, self.moves + 1))

        # Move 2 generators
        for generator_a, generator_b in combinations(self.generators[cur_floor], 2):
            for new_floor in next_floors:
                new_generators = self.move_items(self.generators, {generator_a, generator_b}, cur_floor, new_floor)
                next_states.add(State(new_floor, new_generators, self.chips, self.moves + 1))

        # Move 1 generator and 1 chip
        for item in self.generators[cur_floor]:
            # Skip if there is no generator chip match
            if item not in self.chips[cur_floor]:
                continue

            for new_floor in next_floors:
                new_generators = self.move_items(self.generators, {item}, cur_floor, new_floor)
                new_chips = self.move_items(self.chips, {item}, cur_floor, new_floor)
                next_states.add(State(new_floor, new_generators, new_chips, self.moves + 1))

        return next_states

    def add_chips(self, chips: set[str], floor: int) -> 'State':
        new_chips = self.move_items(self.chips, chips, -1, floor)
        return State(self.elevator_floor, self.generators, new_chips, self.moves)

    def add_generators(self, generators: set[str], floor: int) -> 'State':
        new_generators = self.move_items(self.generators, generators, -1, floor)
        return State(self.elevator_floor, new_generators, self.chips, self.moves)

    @staticmethod
    def move_items(cur_items: tuple[Floor, ...], items: set[str], cur_floor: int, new_floor: int) -> tuple[Floor, ...]:
        if cur_floor == new_floor:
            raise RuntimeWarning

        new_items = []
        for floor, floor_items in enumerate(cur_items):
            if floor == cur_floor:
                new_items.append(floor_items - items)
            elif floor == new_floor:
                new_items.append(floor_items | items)
            else:
                new_items.append(floor_items)

        return tuple(new_items)

    def next_floors(self, floor: int) -> list[int]:
        if floor == 0:
            return [1]

        if floor == 3:  # ruff: ignore[magic-value-comparison]
            return [2]

        if not any(self.chips[f] or self.generators[f] for f in range(floor)):
            return [floor + 1]

        return [floor - 1, floor + 1]

    def canonical_key(self) -> tuple:
        pairs = []
        for g_floor in range(4):
            for generator in self.generators[g_floor]:
                for c_floor in range(4):
                    pairs.extend((g_floor, c_floor) for chip in self.chips[c_floor] if generator == chip)

        return (self.elevator_floor, tuple(sorted(pairs)))


def parse_data(input_path: Path) -> State:
    generators = []
    chips = []

    generator_pattern = re.compile(r'(\w+)\sgenerator')
    chip_pattern = re.compile(r'(\w+)-compatible\smicrochip')
    for line in input_path.read_text().strip().split('\n'):
        generators_match = generator_pattern.findall(line)
        chips_match = chip_pattern.findall(line)
        if generators_match:
            generators.append(frozenset(generators_match))
        else:
            generators.append(frozenset())

        if chips_match:
            chips.append(frozenset(chips_match))
        else:
            chips.append(frozenset())

    return State(0, tuple(generators), tuple(chips), 0)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    state = parse_data(input_path)
    frontier = {state}
    seen = set()
    final = 1000
    while frontier:
        new_frontier = set()
        for state in frontier:
            key = state.canonical_key()

            if key in seen:
                continue

            seen.add(key)
            if state.is_final():
                final = min(final, state.moves)

            if state.is_valid() and state.moves < final:
                new_frontier.update(state.next_states())
        frontier = new_frontier - seen

    return final


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    state = parse_data(input_path)
    frontier = {state.add_chips({'elerium', 'dilithium'}, 0).add_generators({'elerium', 'dilithium'}, 0)}
    seen = set()
    final = 10000
    while frontier:
        new_frontier = set()
        for state in frontier:
            key = state.canonical_key()

            if key in seen:
                continue

            seen.add(key)
            if state.is_final():
                final = min(final, state.moves)

            if state.is_valid() and state.moves < final:
                new_frontier.update(state.next_states())
        frontier = new_frontier - seen

    return final


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
