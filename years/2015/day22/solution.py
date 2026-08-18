import re
from dataclasses import dataclass
from enum import Enum
from math import inf
from pathlib import Path

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Spell(Enum):
    MAGIC_MISSILE = 53
    DRAIN = 73
    SHIELD = 113
    POISON = 173
    RECHARGE = 229


@dataclass
class State:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    shield_timer: int
    poison_timer: int
    recharge_timer: int
    mana_spent: int
    hard: bool

    def cache_key(self) -> tuple[int, ...]:
        return (
            self.player_hp,
            self.player_mana,
            self.boss_hp,
            self.shield_timer,
            self.poison_timer,
            self.recharge_timer,
        )

    @staticmethod
    def new(boss_hp: int, boss_damage: int) -> 'State':
        return State(50, 500, boss_hp, boss_damage, 0, 0, 0, 0, False)

    def copy(self) -> 'State':
        return State(
            self.player_hp,
            self.player_mana,
            self.boss_hp,
            self.boss_damage,
            self.shield_timer,
            self.poison_timer,
            self.recharge_timer,
            self.mana_spent,
            self.hard,
        )

    def cast_spell(self, spell: Spell) -> None:
        self.player_mana -= spell.value
        self.mana_spent += spell.value

        match spell:
            case Spell.MAGIC_MISSILE:
                self.boss_hp -= 4
            case Spell.DRAIN:
                self.boss_hp -= 2
                self.player_hp += 2
            case Spell.SHIELD:
                self.shield_timer = 6
            case Spell.POISON:
                self.poison_timer = 6
            case Spell.RECHARGE:
                self.recharge_timer = 5

    def apply_effects(self) -> None:
        self.boss_hp -= 3 if self.poison_timer > 0 else 0
        self.player_mana += 101 if self.recharge_timer > 0 else 0

        # No need to worry if it is negative
        self.shield_timer = max(0, self.shield_timer - 1)
        self.poison_timer = max(0, self.poison_timer - 1)
        self.recharge_timer = max(0, self.recharge_timer - 1)

    def play_round(self, spell: Spell) -> bool | None:
        # Player turn
        if self.hard:
            self.player_hp -= 1
            if self.player_hp <= 0:
                return False
        self.apply_effects()

        if self.boss_hp <= 0:
            return True

        if not self.can_cast(spell):
            return False

        self.cast_spell(spell)

        if self.boss_hp <= 0:
            return True

        # Boss turn
        self.apply_effects()

        if self.boss_hp <= 0:
            return True

        shield = 7 if self.shield_timer > 0 else 0
        self.player_hp -= max(1, self.boss_damage - shield)

        if self.player_hp <= 0:
            return False

        return None  # Neither won nor lost

    def can_cast(self, spell: Spell) -> bool:
        if spell.value > self.player_mana:
            return False

        spell_timer_match = [
            (Spell.SHIELD, self.shield_timer),
            (Spell.POISON, self.poison_timer),
            (Spell.RECHARGE, self.recharge_timer),
        ]

        return all(not (spell == s and timer > 0) for s, timer in spell_timer_match)


def parse_data(input_path: Path) -> State:
    nums = re.findall(r'(\d+)', input_path.read_text().replace('\n', ''))
    nums = (int(n) for n in nums)
    return State.new(*nums)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    state = parse_data(input_path)
    states = [state]
    seen: dict[tuple[int, ...], int] = {}
    best_cost = inf
    while states:
        next_states = []
        for state in states:
            key = state.cache_key()
            previous_cost = seen.get(key)
            if previous_cost is not None and previous_cost <= state.mana_spent:
                continue

            seen[key] = state.mana_spent
            if state.mana_spent >= best_cost:
                continue

            for spell in Spell:
                next_state = state.copy()
                outcome = next_state.play_round(spell)

                if outcome:
                    best_cost = min(best_cost, next_state.mana_spent)
                elif outcome is None:
                    next_states.append(next_state)

        states = next_states

    return int(best_cost)


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    state = parse_data(input_path)
    state.hard = True
    states = [state]
    seen: dict[tuple[int, ...], int] = {}
    best_cost = inf
    while states:
        next_states = []
        for state in states:
            key = state.cache_key()
            previous_cost = seen.get(key)
            if previous_cost is not None and previous_cost <= state.mana_spent:
                continue

            seen[key] = state.mana_spent
            if state.mana_spent >= best_cost:
                continue

            for spell in Spell:
                next_state = state.copy()
                outcome = next_state.play_round(spell)

                if outcome:
                    best_cost = min(best_cost, next_state.mana_spent)
                elif outcome is None:
                    next_states.append(next_state)

        states = next_states

    return int(best_cost)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
