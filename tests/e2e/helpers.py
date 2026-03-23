from __future__ import annotations

from pathlib import Path

from recipe_normalizer.normalizer import normalize_recipe
from recipe_normalizer.parsers import get_parser


def parse_and_normalize(path: Path) -> dict:
    parser = get_parser(path.suffix)
    recipe = parser.parse(path)
    return normalize_recipe(recipe).to_dict()
