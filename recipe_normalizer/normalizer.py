from __future__ import annotations

import json
import logging
from pathlib import Path

from recipe_normalizer.converter import convert_ingredient
from recipe_normalizer.models import Recipe
from recipe_normalizer.parsers import get_parser

logger = logging.getLogger(__name__)


def normalize_recipe(recipe: Recipe) -> Recipe:
    """Convert all imperial units in a recipe to metric."""
    return Recipe(
        name=recipe.name,
        ingredients=[convert_ingredient(ing) for ing in recipe.ingredients],
        preparations=recipe.preparations,
    )


def process_directory(input_dir: Path) -> list[Recipe]:
    """Read all supported recipe files from a directory and return normalized recipes."""
    recipes: list[Recipe] = []

    for file_path in sorted(input_dir.iterdir()):
        if not file_path.is_file():
            continue

        parser = get_parser(file_path.suffix)
        if parser is None:
            logger.warning("Skipping unsupported file: %s", file_path.name)
            continue

        logger.info("Parsing %s", file_path.name)
        try:
            recipe = parser.parse(file_path)
        except Exception:
            logger.warning("Failed to parse %s, skipping", file_path.name, exc_info=True)
            continue
        recipes.append(normalize_recipe(recipe))

    return recipes


def write_output(recipes: list[Recipe], output_path: Path) -> None:
    """Write normalized recipes to a JSON file."""
    data = [r.to_dict() for r in recipes]
    output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Wrote %d recipe(s) to %s", len(recipes), output_path)
