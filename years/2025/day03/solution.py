from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def get_best_batteries(bank: list[int], n: int) -> int:
    """Get the best n batteries out of the bank"""
    battery = 0

    # The index where we start to parse the battery
    # As we parse the bank, this will move to the right
    # and we can only look at batteries after this point
    min_ind = [0]
    bank_len = len(bank)
    for i in reversed(range(n)):
        highest_battery = max(bank[min_ind[-1] : bank_len - i])
        idx_highest_battery = bank.index(highest_battery)
        min_ind.append(idx_highest_battery + 1)

        battery += highest_battery * 10**i

    return battery


def parse_bank(bank: str) -> list[int]:
    return [int(b) for b in bank]


def parse_input(data: str) -> list[list[int]]:
    return [parse_bank(line) for line in data.split('\n')]


def part_one(banks: list[list[int]]) -> int:
    """Return the answer to part one."""
    total = 0
    for bank in banks:
        total += get_best_batteries(bank, 2)
    return total


def part_two(banks: list[list[int]]):
    """Return the answer to part two."""
    return


def main() -> None:
    data = INPUT_PATH.read_text().rstrip('\n')
    banks = parse_input(data)
    print(f'Part 1: {part_one(banks)}')
    print(f'Part 2: {part_two(banks)}')


if __name__ == '__main__':
    main()
