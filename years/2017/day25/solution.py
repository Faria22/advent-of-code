from collections import defaultdict
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


class State:
    def __init__(self, block: list[str]) -> None:
        block_line_parts = [line.split() for line in block]
        self.name = block_line_parts[0][-1]

        val_zero_write = int(block_line_parts[2][-1])
        val_zero_shift = 1 if block_line_parts[3][-1] == 'right' else -1
        val_zero_new_state = block_line_parts[4][-1]

        val_one_write = int(block_line_parts[6][-1])
        val_one_shift = 1 if block_line_parts[7][-1] == 'right' else -1
        val_one_new_state = block_line_parts[8][-1]

        self.val_zero_returns = (val_zero_write, val_zero_shift, val_zero_new_state)
        self.val_one_returns = (val_one_write, val_one_shift, val_one_new_state)

    def action(self, value: int) -> tuple[int, int, str]:
        """Returns the write value, index shift, and next state name."""
        if not value:
            return self.val_zero_returns
        return self.val_one_returns


class TuringMachine:
    def __init__(self, input_path: Path) -> None:
        blocks = (input_path
                  .read_text()
                  .replace('.', '')
                  .replace(':', '')
                  .strip()
                  .split('\n\n')
                  )
        blocks = [block.split('\n') for block in blocks]

        self.num_steps = int(blocks[0][1].split()[-2])

        self.idx = 0
        self.tape = defaultdict(int)

        states = [State(block) for block in blocks[1:]]
        self.states = {state.name: state for state in states}
        self.state = self.states[blocks[0][0].split()[-1]]

    def action(self) -> None:
        new_val, shift, new_state = self.state.action(self.tape[self.idx])
        self.tape[self.idx] = new_val
        self.idx += shift
        self.state = self.states[new_state]

    def checksum(self) -> int:
        return sum(self.tape.values())


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    machine = TuringMachine(input_path)
    for _ in range(machine.num_steps):
        machine.action()
    return machine.checksum()


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    machine = TuringMachine(input_path)
    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
