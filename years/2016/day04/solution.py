from collections import Counter
from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


@dataclass
class Room:
    name: str
    id: int
    checksum: str

    def is_real(self) -> bool:
        letter_counts = Counter(self.name.replace('-', ''))
        sorted_letters = sorted(letter_counts, key=lambda letter: (-letter_counts[letter], letter))

        return ''.join(sorted_letters).startswith(self.checksum)

    def decripted_name(self) -> str:
        name = ''
        shift = self.id % 26
        for char in self.name:
            if char == '-':
                name += ' '
            else:
                name += chr((ord(char) + shift - 97) % 26 + 97)
        return name


def parse_data(input_path: Path) -> list[Room]:
    rooms = []
    for line in input_path.read_text().strip().split('\n'):
        name, id_checksum = line.rsplit('-', 1)
        sector_id, checksum = id_checksum[:-1].split('[')
        rooms.append(Room(name, int(sector_id), checksum))

    return rooms


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    rooms = parse_data(input_path)
    return sum(room.id for room in rooms if room.is_real())


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    rooms = parse_data(input_path)
    rooms = [room for room in rooms if room.is_real()]

    for room in rooms:
        if room.decripted_name() == 'northpole object storage':
            return room.id

    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
