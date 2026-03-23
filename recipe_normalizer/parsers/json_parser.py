from __future__ import annotations

import json
from pathlib import Path

from recipe_normalizer.models import Ingredient, Recipe
from recipe_normalizer.parsers.base import RecipeParser


class JsonParser(RecipeParser):
    """Parses a JSON recipe file into a Recipe object."""

    def parse(self, path: Path) -> Recipe:
        data = json.loads(path.read_text(encoding="utf-8"))
        # Guard against non-object JSON (e.g. a bare array or string)
        if not isinstance(data, dict):
            raise ValueError(f"Expected a JSON object with recipe data, got {type(data).__name__}")

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
