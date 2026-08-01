from dataclasses import dataclass
from pathlib import Path

from aoc import Pos

INPUT_PATH = Path(__file__).parent / 'input.txt'

WALL_CHAR = '#'
BOX_CHAR = 'O'
ROBOT_CHAR = '@'

MOVE_OFFSETS = {
    '^': Pos(-1, 0),
    'v': Pos(1, 0),
    '<': Pos(0, -1),
    '>': Pos(0, 1),
}


@dataclass
class Warehouse:
    robot: Pos
    walls: set[Pos]
    boxes: set[Pos]
    moves: str

    def move_boxes(self, move: str) -> tuple[set[Pos], set[Pos]]:
        offset = MOVE_OFFSETS[move]
        position = self.robot + offset
        moving_boxes = set()

        # Get all boxes that are "connected" to the robot
        while position in self.boxes:
            moving_boxes.add(position)
            position += offset

        new_positions = {box + offset for box in moving_boxes}

        return moving_boxes, new_positions

    def move_robot(self, move: str) -> None:
        offset = MOVE_OFFSETS[move]
        new_robot_pos = self.robot + offset
        if new_robot_pos in self.walls:
            return

        # Get all the boxes that would be shifted
        # and find their new position
        moving_boxes, moved_boxes_new_positions = self.move_boxes(move)

        # Stop if any box would go into a wall
        if any(box in self.walls for box in moved_boxes_new_positions):
            return

        self.boxes -= moving_boxes
        self.boxes |= moved_boxes_new_positions
        self.robot = new_robot_pos

    def execute_all_moves(self) -> None:
        for move in self.moves:
            self.move_robot(move)

    @staticmethod
    def gps_coordinate(box: Pos) -> int:
        return 100 * box.row + box.col

    def sum_all_gps_coordinates(self) -> int:
        return sum(self.gps_coordinate(box) for box in self.boxes)


def parse_data(input_path: Path) -> Warehouse:
    grid, moves = input_path.read_text().strip().split('\n\n')

    walls, boxes = set(), set()
    for r, row in enumerate(grid.split('\n')):
        for c, cell in enumerate(row):
            if cell == WALL_CHAR:
                walls.add(Pos(r, c))
            elif cell == BOX_CHAR:
                boxes.add(Pos(r, c))
            elif cell == ROBOT_CHAR:
                robot_pos = Pos(r, c)

    moves = moves.replace('\n', '')
    return Warehouse(robot_pos, walls, boxes, moves)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    warehouse = parse_data(input_path)
    warehouse.execute_all_moves()
    return warehouse.sum_all_gps_coordinates()


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    data = parse_data(input_path)  # ruff: ignore[unused-variable]
    return 0


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
