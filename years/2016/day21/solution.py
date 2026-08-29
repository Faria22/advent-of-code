from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


@dataclass
class Password:
    password: list[str]

    def swap_position(self, p1: int, p2: int) -> None:
        a = self.password[p1]
        b = self.password[p2]

        self.password[p1] = b
        self.password[p2] = a

    def swap_letter(self, a: str, b: str) -> None:
        a_idx = self.password.index(a)
        b_idx = self.password.index(b)
        self.swap_position(a_idx, b_idx)

    def reverse(self, start: int, end: int) -> None:
        self.password[start : end + 1] = reversed(self.password[start : end + 1])

    def rotate_left(self, steps: int) -> None:
        steps %= len(self.password)
        self.password = self.password[steps:] + self.password[:steps]

    def rotate_right(self, steps: int) -> None:
        steps %= len(self.password)
        self.password = self.password[-steps:] + self.password[:-steps]

    def rotate_on_letter(self, letter: str) -> None:
        letter_idx = self.password.index(letter)
        steps = 1 + letter_idx
        if letter_idx > 3:  # ruff: ignore[magic-value-comparison]
            steps += 1
        self.rotate_right(steps)

    def rotate_on_letter_reversed(self, letter: str) -> None:
        tmp_password = Password(self.password)
        tmp_password.rotate_on_letter(letter)

        count = 0
        while tmp_password.password != self.password:
            count += 1
            if count > len(self.password):
                raise RuntimeError

            tmp_password = Password(self.password)
            tmp_password.rotate_left(count)
            tmp_password.rotate_on_letter(letter)

        self.rotate_left(count)

    def move(self, p1: int, p2: int) -> None:
        a = self.password.pop(p1)
        self.password.insert(p2, a)

    def __str__(self) -> str:
        return ''.join(self.password)


def part_one(input_path: Path, password_str: str = 'abcdefgh') -> str:
    """Return the answer to part one."""
    password = Password(list(password_str))
    lines = parse_data(input_path)
    for line in lines:
        parts = line.split()
        match parts[0]:
            case 'swap':
                match parts[1]:
                    case 'position':
                        p1 = int(parts[2])
                        p2 = int(parts[5])
                        password.swap_position(p1, p2)
                    case 'letter':
                        a = parts[2]
                        b = parts[5]
                        password.swap_letter(a, b)
                    case _:
                        raise RuntimeError
            case 'rotate':
                match parts[1]:
                    case 'left':
                        steps = int(parts[2])
                        password.rotate_left(steps)
                    case 'right':
                        steps = int(parts[2])
                        password.rotate_right(steps)
                    case 'based':
                        letter = parts[-1]
                        password.rotate_on_letter(letter)
                    case _:
                        raise RuntimeError
            case 'reverse':
                p1 = int(parts[2])
                p2 = int(parts[4])
                password.reverse(p1, p2)
            case 'move':
                p1 = int(parts[2])
                p2 = int(parts[5])
                password.move(p1, p2)
            case _:
                raise RuntimeError

    return str(password)


def part_two(input_path: Path, password_str: str = 'fbgdceah') -> str:
    """Return the answer to part two."""
    password = Password(list(password_str))
    lines = parse_data(input_path)
    for line in reversed(lines):
        parts = line.split()
        match parts[0]:
            case 'swap':
                match parts[1]:
                    case 'position':
                        p1 = int(parts[2])
                        p2 = int(parts[5])
                        password.swap_position(p1, p2)
                    case 'letter':
                        a = parts[2]
                        b = parts[5]
                        password.swap_letter(a, b)
                    case _:
                        raise RuntimeError
            case 'rotate':
                match parts[1]:
                    case 'left':
                        steps = int(parts[2])
                        password.rotate_right(steps)
                    case 'right':
                        steps = int(parts[2])
                        password.rotate_left(steps)
                    case 'based':
                        letter = parts[-1]
                        password.rotate_on_letter_reversed(letter)
                    case _:
                        raise RuntimeError
            case 'reverse':
                p1 = int(parts[2])
                p2 = int(parts[4])
                password.reverse(p1, p2)
            case 'move':
                p1 = int(parts[2])
                p2 = int(parts[5])
                password.move(p2, p1)
            case _:
                raise RuntimeError

    return str(password)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
