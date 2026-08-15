import re
from dataclasses import dataclass
from math import prod
from pathlib import Path
from typing import NamedTuple

INPUT_PATH = Path(__file__).parent / 'input.txt'


class Ingredient(NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


@dataclass
class Ingredients:
    ingredients: list[Ingredient]

    def possible_combinations(self) -> list[list[int]]:
        num_ingredients = len(self.ingredients)

        max_num_tsp = 100
        return self._possible_combination_helper(num_ingredients, max_num_tsp)

    @staticmethod
    def _possible_combination_helper(remaining_ingredients: int, remaining_tsp: int) -> list[list[int]]:
        if remaining_ingredients == 1:
            return [[remaining_tsp]]

        possible_combinations = []
        for i in range(remaining_tsp + 1):
            possible_combinations.extend(
                [i, *comb]
                for comb in Ingredients._possible_combination_helper(remaining_ingredients - 1, remaining_tsp - i)
            )

        return possible_combinations

    def get_best_score(self, scored_categories: int = 4, calories: int | None = None) -> int:
        best_score = 0
        combinations = self.possible_combinations()
        for combination in combinations:
            if calories:
                cur_calories = sum(
                    ingredient[-1] * num for ingredient, num in zip(self.ingredients, combination, strict=True)
                )
                if cur_calories != calories:
                    continue

            category_scores = [
                sum(ingredient[i] * num for ingredient, num in zip(self.ingredients, combination, strict=True))
                for i in range(scored_categories)
            ]
            category_scores = (max(0, x) for x in category_scores)
            best_score = max(best_score, prod(category_scores))

        return best_score


def parse_data(input_path: Path) -> Ingredients:
    ingredients = []
    for line in input_path.read_text().strip().split('\n'):
        nums = re.findall(r'(-?\d+)', line)
        nums = [int(n) for n in nums]
        ingredients.append(Ingredient(*nums))
    return Ingredients(ingredients)


def part_one(input_path: Path) -> int:
    """Return the answer to part one."""
    ingredients = parse_data(input_path)
    return ingredients.get_best_score()


def part_two(input_path: Path) -> int:
    """Return the answer to part two."""
    ingredients = parse_data(input_path)
    return ingredients.get_best_score(calories=500)


def main() -> None:
    print(f'Part 1: {part_one(INPUT_PATH)}')
    print(f'Part 2: {part_two(INPUT_PATH)}')


if __name__ == '__main__':
    main()
