from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


def parse_data(input_path: Path) -> list[int]:
    return list(map(int, input_path.read_text().strip().split()))


class Node:
    def __init__(self, num_children: int, num_metadata: int) -> None:
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children: list[Node] = []
        self.metadata: list[int] = []
        self._size: int = 0
        self._value: int = 0

    def size(self) -> int:
        if not self._size:
            size = 2 + self.num_metadata
            for child in self.children:
                size += child.size()

            self._size = size

        return self._size

    def value(self) -> int:
        if not self._value:
            if not self.num_children:
                self._value = sum(self.metadata)

            else:
                value = 0
                for m in self.metadata:
                    if m < 1 or m > self.num_children:
                        continue
                    value += self.children[m - 1].value()
                self._value = value

        return self._value


def parse_node(tree: list[int]) -> Node:
    node = Node(tree[0], tree[1])
    shift = 2
    for _ in range(node.num_children):
        child = parse_node(tree[shift:])
        node.children.append(child)
        shift += child.size()

    node.metadata = tree[shift:shift + node.num_metadata]
    return node


def sum_metadata(node: Node) -> int:
    total = sum(node.metadata)
    for child in node.children:
        total += sum_metadata(child)

    return total


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    tree = parse_data(input_path)
    root = parse_node(tree)
    return sum_metadata(root)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    tree = parse_data(input_path)
    root = parse_node(tree)
    return root.value()


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
