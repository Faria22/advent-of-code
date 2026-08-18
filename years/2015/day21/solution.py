import re
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'

WEAPONS: list[tuple[int, int]] = [
    (8, 4),
    (10, 5),
    (25, 6),
    (40, 7),
    (74, 8),
]

ARMORS: list[tuple[int, int]] = [
    (0, 0),  # No armor
    (13, 1),
    (31, 2),
    (53, 3),
    (75, 4),
    (102, 5),
]

RINGS: list[tuple[int, int, int]] = [
    (0, 0, 0),  # No ring (right hand)
    (0, 0, 0),  # No ring (left hand)
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
]


@dataclass
class Character:
    health: int
    attack: int
    armor: int

    def copy(self) -> 'Character':
        return Character(self.health, self.attack, self.armor)


def parse_data(input_path: Path) -> Character:
    nums = re.findall(r'(\d+)', input_path.read_text().replace('\n', ''))
    nums = (int(n) for n in nums)
    return Character(*nums)


def player_survives(player: Character, boss: Character) -> bool:
    player = player.copy()
    boss = boss.copy()

    while True:
        boss.health -= max(1, player.attack - boss.armor)
        if boss.health <= 0:
            return True
        player.health -= max(1, boss.attack - player.armor)
        if player.health <= 0:
            return False


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    boss = parse_data(input_path)
    player_health = 100
    best_cost = 354  # This is the max cost if we buy the most expensive items
    for w_cost, w_damage in WEAPONS:
        for a_cost, a_armor in ARMORS:
            for ring_a, ring_b in combinations(RINGS, 2):
                cost = w_cost + a_cost + ring_a[0] + ring_b[0]
                if cost >= best_cost:
                    continue
                player = Character(player_health, w_damage + ring_a[1] + ring_b[1], a_armor + ring_a[2] + ring_b[2])
                if player_survives(player, boss):
                    best_cost = min(best_cost, cost)

    return best_cost


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    boss = parse_data(input_path)
    player_health = 100
    worst_cost = 0
    for w_cost, w_damage in WEAPONS:
        for a_cost, a_armor in ARMORS:
            for ring_a, ring_b in combinations(RINGS, 2):
                cost = w_cost + a_cost + ring_a[0] + ring_b[0]
                if cost <= worst_cost:
                    continue
                player = Character(player_health, w_damage + ring_a[1] + ring_b[1], a_armor + ring_a[2] + ring_b[2])
                if not player_survives(player, boss):
                    worst_cost = max(worst_cost, cost)

    return worst_cost


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
