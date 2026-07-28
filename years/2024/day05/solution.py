from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

type Ordering = tuple[int, int]
type Update = tuple[int, ...]


def parse_data(data: str) -> tuple[list[Ordering], list[Update]]:
    ordering_lines, update_lines = data.split('\n\n')

    ordering = [(int(left), int(right)) for left, right in (line.split('|') for line in ordering_lines.splitlines())]
    updates: list[Update] = [tuple(int(u) for u in line.split(',')) for line in update_lines.split('\n')]

    return ordering, updates


def part_one(data: str) -> int:
    """Return the answer to part one."""
    orderings, updates = parse_data(data)

    page_total = 0
    for update in updates:
        for ordering in orderings:
            if not all(o in update for o in ordering):
                continue

            a, b = ordering
            a_idx = update.index(a)
            b_idx = update.index(b)

            if b_idx < a_idx:
                break
        else:
            middle_page = update[len(update) // 2]
            page_total += middle_page

    return page_total


def join_orderings(used_orderings: list[Ordering]) -> list[int]:
    # Holds what pages have to be to the left of the key
    pages: dict[int, set] = defaultdict(set)
    for a, b in used_orderings:
        # if `b` is to the left of `page`, then `a` has to be to the left of `page` as well
        for left_pages in pages.values():
            if b in left_pages:
                left_pages.add(a)

        pages[b].add(a)
        pages[a]  # Makes sure that pages also includes `a` with an empty set if it was not seen before

    return sorted(pages, key=lambda page: len(pages[page]))


def fix_update_order(update: Update, used_orderings: list[Ordering]) -> Update:
    single_ordering = join_orderings(used_orderings)
    return tuple(single_ordering + [u for u in update if u not in single_ordering])


def part_two(data: str) -> int:
    """Return the answer to part two."""
    orderings, updates = parse_data(data)

    page_total = 0
    for update in updates:
        used_orderings = [ordering for ordering in orderings if all(o in update for o in ordering)]
        if any(update.index(b) < update.index(a) for a, b in (ordering for ordering in used_orderings)):
            new_update = fix_update_order(update, used_orderings)
            middle_page = new_update[len(new_update) // 2]
            page_total += middle_page

    return page_total


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    print(f'Part 1: {part_one(data)}')
    print(f'Part 2: {part_two(data)}')


if __name__ == '__main__':
    main()
