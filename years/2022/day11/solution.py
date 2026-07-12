from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def part_one(data: str):
    """Return the answer to part one."""
    return None


def part_two(data: str):
    """Return the answer to part two."""
    return None


def main() -> None:
    data = INPUT_PATH.read_text().rstrip("\n")
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")


if __name__ == "__main__":
    main()
