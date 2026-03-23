from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from recipe_normalizer.models import Ingredient, Recipe
from recipe_normalizer.parsers.base import RecipeParser


class XmlParser(RecipeParser):
    def parse(self, path: Path) -> Recipe:
        tree = ET.parse(path)
        root = tree.getroot()

        name = root.findtext("name", default="")
        ingredients: list[Ingredient] = []

        for ing_el in root.findall("ingredients"):
            item = ing_el.findtext("item", default="")
            quantity = float(ing_el.findtext("quantity", default="0"))
            unit = ing_el.findtext("unit", default="") or ""
            comment = ing_el.findtext("comment", default="") or ""
            ingredients.append(Ingredient(item=item, quantity=quantity, unit=unit, comment=comment))

        preparations = [el.text or "" for el in root.findall("preparations") if el.text]

        return Recipe(name=name, ingredients=ingredients, preparations=preparations)
