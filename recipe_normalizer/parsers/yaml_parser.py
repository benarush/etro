from __future__ import annotations

from pathlib import Path

import yaml

from recipe_normalizer.models import Ingredient, Recipe
from recipe_normalizer.parsers.base import RecipeParser


class YamlParser(RecipeParser):
    def parse(self, path: Path) -> Recipe:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        name = data.get("name", "")
        ingredients: list[Ingredient] = []

        for ing in data.get("ingredients", []):
            ingredients.append(
                Ingredient(
                    item=ing.get("item", ""),
                    quantity=float(ing.get("quantity", 0)),
                    unit=ing.get("unit", ""),
                    comment=ing.get("comment", ""),
                )
            )

        preparations = data.get("preparations", [])

        return Recipe(name=name, ingredients=ingredients, preparations=preparations)
