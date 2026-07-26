from itertools import islice
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


PRESENT_SIDE_LEN = 3
PRESENT_SYMBOL = '#'

type Shape = frozenset[tuple[int, int]]


class Present:
    def __init__(self, data: list[str]) -> None:
        # Frozenset because it will need to be hashed when creating permutations
        self.shape: Shape = frozenset(
            (row, col) for row, line in enumerate(data) for col, cell in enumerate(line) if cell == PRESENT_SYMBOL
        )

        self.area = len(self.shape)
        self.permutations = self.get_permutations()

    def get_permutations(self) -> set[Shape]:
        permutations = {self.shape}

        # horizontal reflection
        permutations.add(self.horizontal_reflection(self.shape))

        # vertical reflection
        permutations.add(self.vertical_reflection(self.shape))

        # clockwise rotation
        permutations.add(self.vertical_reflection(self.diagonal_reflection(self.shape)))

        # counterclockwise rotation
        permutations.add(self.horizontal_reflection(self.diagonal_reflection(self.shape)))

        # double rotation
        permutations.add(self.vertical_reflection(self.horizontal_reflection(self.shape)))

        return permutations

    @staticmethod
    def horizontal_reflection(shape: Shape) -> Shape:
        return frozenset((PRESENT_SIDE_LEN - 1 - row, col) for row, col in shape)

    @staticmethod
    def vertical_reflection(shape: Shape) -> Shape:
        return frozenset((row, PRESENT_SIDE_LEN - 1 - col) for row, col in shape)

    @staticmethod
    def diagonal_reflection(shape: Shape) -> Shape:
        return frozenset((col, row) for row, col in shape)

    @staticmethod
    def translate(shape: Shape, row_offset: int, col_offset: int) -> Shape:
        return frozenset((row + row_offset, col + col_offset) for row, col in shape)


class Region:
    def __init__(self, data: str) -> None:
        dimensions, presents = data.split(maxsplit=1)
        self.width, self.height = [int(d) for d in dimensions.strip(':').split('x')]
        self.present_counts = [int(p) for p in presents.split()]

    def can_fit(self, presents: list[Present]) -> bool:
        num_presents = sum(self.present_counts)

        # checks if all the presents can fit without any overlap
        if (self.height // 3) * (self.width // 3) >= num_presents:
            return True

        # Checks if all the presents could fit regardless of their shape
        presents_area = 0
        for present, present_count in zip(presents, self.present_counts, strict=True):
            presents_area += present_count * present.area

        if presents_area > self.width * self.height:
            return False

        # Check by aranging the presents

        # Pre-computing present placements
        possible_present_placements = []
        for present in presents:
            possible_placements = {
                Present.translate(permutation, i, j)
                for permutation in present.permutations
                for i in range(self.height - PRESENT_SIDE_LEN + 1)
                for j in range(self.width - PRESENT_SIDE_LEN + 1)
            }
            possible_present_placements.append(possible_placements)

        filled_region = set()
        failed_cache = set()
        return self.arange_presents(filled_region, possible_present_placements, self.present_counts, failed_cache)

    def arange_presents(
        self,
        filled_region: set,
        possible_present_placements: list[set[Shape]],
        present_counts: list[int],
        failed_cache: set,
    ) -> bool:
        if sum(present_counts) == 0:
            return True

        state = (frozenset(filled_region), tuple(present_counts))
        if state in failed_cache:
            return False

        # Get only available present types
        all_valid_placements: list[set[Shape]] = []
        for present_ind, present_count in enumerate(present_counts):
            if present_count == 0:
                all_valid_placements.append(set())
                continue

            valid_placements = {
                placement
                for placement in possible_present_placements[present_ind]
                if filled_region.isdisjoint(placement)
            }

            # This present cannot fit at all with the current filled region
            if not valid_placements:
                failed_cache.add(state)
                return False

            all_valid_placements.append(valid_placements)

        # Gets the present index with the lowest amount of valid placements
        present_ind = min(
            (index for index, count in enumerate(present_counts) if count > 0),
            key=lambda index: len(all_valid_placements[index]),
        )

        for placement in all_valid_placements[present_ind]:
            new_filled_region = filled_region | placement

            # remove the present from present_counts
            new_present_counts = present_counts.copy()
            new_present_counts[present_ind] -= 1

            # Keep going with one less present
            if self.arange_presents(
                new_filled_region,
                all_valid_placements.copy(),
                new_present_counts,
                failed_cache,
            ):
                return True

        failed_cache.add(state)
        return False


def parse_data(data: str) -> tuple[list[Present], list[Region]]:
    presents = []
    regions = []

    lines = iter(data.split('\n'))
    for line in lines:
        if line == f'{len(presents)}:':
            presents.append(Present(list(islice(lines, 3))))
            next(lines)
        else:
            regions.append(Region(line))
    return presents, regions


def part_one(data: str) -> int:
    """Return the answer to part one."""
    presents, regions = parse_data(data)

    return sum(region.can_fit(presents) for region in regions)


def part_two(data: str):
    """Return the answer to part two."""
    return


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
