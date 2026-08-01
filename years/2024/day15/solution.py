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

    def moved_boxes_would_hit_wall(self, new_positions: set[Pos]) -> bool:
        return any(box in self.walls for box in new_positions)

    def move_robot(self, move: str) -> None:
        offset = MOVE_OFFSETS[move]
        new_robot_pos = self.robot + offset
        if new_robot_pos in self.walls:
            return

        # Get all the boxes that would be shifted
        # and find their new position
        moving_boxes, moved_boxes_new_positions = self.move_boxes(move)

        # Stop if any box would go into a wall
        if self.moved_boxes_would_hit_wall(moved_boxes_new_positions):
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


class Warehouse2(Warehouse):
    def _get_moving_boxes(self, move: str, start_point: Pos, visited_positions: set[Pos]) -> set[Pos]:
        offset = MOVE_OFFSETS[move]
        position = start_point + offset
        if position in visited_positions:
            return set()

        visited_positions.add(position)

        moving_boxes = set()
        if move in {'^', 'v'}:
            if box := self._box_at(position):
                moving_boxes.add(box)
                moving_boxes |= self._get_moving_boxes(move, box, visited_positions)
                moving_boxes |= self._get_moving_boxes(move, box.shift_right(), visited_positions)

        else:
            while box := self._box_at(position):
                moving_boxes.add(box)
                position += offset * 2

        return moving_boxes

    def _box_at(self, position: Pos) -> Pos | None:
        if position in self.boxes:
            return position

        left_half = position.shift_left()
        return left_half if left_half in self.boxes else None

    def move_boxes(self, move: str) -> tuple[set[Pos], set[Pos]]:
        moving_boxes = self._get_moving_boxes(move, self.robot, set())

        offset = MOVE_OFFSETS[move]
        new_positions = {box + offset for box in moving_boxes}

        return moving_boxes, new_positions

    def moved_boxes_would_hit_wall(self, new_positions: set[Pos]) -> bool:
        return any(box in self.walls or box.shift_right() in self.walls for box in new_positions)


def parse_data_part_two(input_path: Path) -> Warehouse2:
    expansion = str.maketrans({
        '#': '##',
        'O': 'O.',
        '.': '..',
        '@': '@.',
    })
    grid, moves = input_path.read_text().translate(expansion).strip().split('\n\n')

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
    return Warehouse2(robot_pos, walls, boxes, moves)


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
    warehouse = parse_data_part_two(input_path)
    warehouse.execute_all_moves()
    return warehouse.sum_all_gps_coordinates()


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
