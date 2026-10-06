from collections import defaultdict, deque
from enum import Enum, auto
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_val(x: str, registers: dict[str, int]) -> int:
    """Get a value from x regardless if it is a literal or register."""
    try:
        return int(x)
    except ValueError:
        return registers[x]


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    instructions = parse_data(input_path)
    num_instructions = len(instructions)
    registers: dict[str, int] = defaultdict(int)

    last_played_sound = None
    idx = 0
    while 0 <= idx < num_instructions:
        instruction_parts = instructions[idx].split()
        x_name = instruction_parts[1]
        x = get_val(x_name, registers)
        match instruction_parts[0]:
            case 'snd':
                last_played_sound = x
            case 'set':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] = y
            case 'add':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] += y
            case 'mul':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] *= y
            case 'mod':
                y = get_val(instruction_parts[2], registers)
                registers[x_name] %= y
            case 'rcv':
                if x != 0:
                    assert last_played_sound is not None
                    return last_played_sound
            case 'jgz':
                y = get_val(instruction_parts[2], registers)
                if x > 0:
                    idx += y
                    continue
        idx += 1

    return -1


class Status(Enum):
    Ready = auto()
    Waiting = auto()
    Done = auto()


class Program:
    def __init__(self, p_num: int, instructions: list[str]) -> None:
        self.status: Status = Status.Ready
        self.instructions = instructions
        self.num_instructions = len(instructions)
        self.idx = 0
        self.registers = defaultdict(int)
        self.registers['p'] = p_num
        self.receive_register: str | None = None

    def run(self) -> int | None:
        # Check just to be sure
        if self.status != Status.Ready:
            return None

        instruction_parts = self.instructions[self.idx].split()
        x_name = instruction_parts[1]
        x = get_val(x_name, self.registers)

        match instruction_parts[0]:
            case 'snd':
                self.idx += 1
                return x
            case 'set':
                y = get_val(instruction_parts[2], self.registers)
                self.registers[x_name] = y
            case 'add':
                y = get_val(instruction_parts[2], self.registers)
                self.registers[x_name] += y
            case 'mul':
                y = get_val(instruction_parts[2], self.registers)
                self.registers[x_name] *= y
            case 'mod':
                y = get_val(instruction_parts[2], self.registers)
                self.registers[x_name] %= y
            case 'rcv':
                self.status = Status.Waiting
                self.receive_register = x_name
                return None
            case 'jgz':
                if x > 0:
                    y = get_val(instruction_parts[2], self.registers)
                    self.idx += y - 1  # minus 1 because we add 1 at the end of the function
            case _:
                raise RuntimeError

        self.idx += 1
        if not (0 <= self.idx < self.num_instructions):
            self.status = Status.Done

        return None

    def receive(self, val: int) -> None:
        assert self.receive_register is not None
        assert self.status == Status.Waiting

        self.registers[self.receive_register] = val
        self.receive_register = None

        self.idx += 1
        if 0 <= self.idx < self.num_instructions:
            self.status = Status.Ready
        else:
            self.status = Status.Done


class Programs:
    def __init__(self, instructions: list[str]) -> None:
        self.programs = [Program(p, instructions) for p in range(2)]
        self.send_queues = [deque() for _ in range(2)]

    def run(self) -> int:
        count_one_sent_values = 0

        while (any(program.status == Status.Ready for program in self.programs) or
            any(len(q) > 0 for q in self.send_queues)):
            for i in range(2):
                if self.programs[i].status == Status.Waiting and len(self.send_queues[1 - i]) > 0:
                    self.programs[i].receive(self.send_queues[1 - i].popleft())

                if self.programs[i].status == Status.Ready:
                    val = self.programs[i].run()
                    if val is not None:
                        self.send_queues[i].append(val)
                        if i == 1:
                            count_one_sent_values += 1

        return count_one_sent_values


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    instructions = parse_data(input_path)
    programs = Programs(instructions)
    return programs.run()


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
