from itertools import batched
from math import isqrt
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

START = '.#./..#/###'


def parse_data(input_path: Path) -> dict[str, str]:
    patterns = {}
    for line in input_path.read_text().strip().split('\n'):
        input_pattern, output = line.split(' => ')
        patterns[input_pattern] = output

    return patterns


def horizontal_flip(pattern: str) -> str:
    return '/'.join(row[::-1] for row in pattern.split('/'))


def vertical_flip(pattern: str) -> str:
    return '/'.join(row for row in reversed(pattern.split('/')))


def diagonal_flip(pattern: str) -> str:
    return '/'.join(''.join(row) for row in zip(*pattern.split('/')))


def permutations_of_pattern(pattern: str) -> set[str]:
    return {pattern,
        vertical_flip(pattern),
        horizontal_flip(pattern),
        diagonal_flip(pattern),
        vertical_flip(horizontal_flip(diagonal_flip(pattern))),
        diagonal_flip(horizontal_flip(pattern)),  # rotate 90
        vertical_flip(horizontal_flip(pattern)),  # rotate 180
        diagonal_flip(vertical_flip(pattern)),  # rotate 270
    }


def split_pixels_into_squares(pixels: str, square_size: int) -> list[str]:
    pixel_rows = pixels.split('/')
    num_squares = (len(pixel_rows) // square_size)**2
    squares = []

    start_row = 0
    start_col = 0
    for _ in range(num_squares):
        square = ''
        for row in range(square_size):
            for col in range(square_size):
                square += pixel_rows[start_row + row][start_col + col]
            square += '/'

        squares.append(square[:-1])

        start_col += square_size
        if start_col >= len(pixel_rows):
            start_col = 0
            start_row += square_size

    return squares


def merge_squares(squares: list[str]) -> str:
    num_squares_per_side = isqrt(len(squares))
    square_size = squares[0].count('/') + 1
    pixels = ''
    for batch in batched(squares, num_squares_per_side):
        for row in range(square_size):
            for square in batch:
                pixels += square.split('/')[row]
            pixels += '/'

    return pixels[:-1]


def iteration(pixels: str, patterns: dict[str, str]) -> str:
    size = pixels.count('/') + 1
    squares = split_pixels_into_squares(pixels, 2) if size % 2 == 0 else split_pixels_into_squares(pixels, 3)

    new_squares = [patterns[square] for square in squares]

    return merge_squares(new_squares)


def get_all_patterns(raw_patterns: dict[str, str]) -> dict[str, str]:
    patterns = {}
    for pattern, output in raw_patterns.items():
        for p_pattern in permutations_of_pattern(pattern):
            patterns[p_pattern] = output

    return patterns


def part_one(input_path: Path, num_iterations: int = 5) -> int:
    """Return the answer to part one."""
    raw_patterns = parse_data(input_path)
    patterns = get_all_patterns(raw_patterns)

    pixels = START
    for _ in range(num_iterations):
        pixels = iteration(pixels, patterns)

    return pixels.count('#')


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    raw_patterns = parse_data(input_path)
    patterns = get_all_patterns(raw_patterns)

    pixels = START
    for _ in range(18):
        pixels = iteration(pixels, patterns)

    return pixels.count('#')


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
