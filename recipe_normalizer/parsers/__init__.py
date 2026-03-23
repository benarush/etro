from __future__ import annotations

from recipe_normalizer.parsers.base import RecipeParser
from recipe_normalizer.parsers.json_parser import JsonParser
from recipe_normalizer.parsers.xml_parser import XmlParser
from recipe_normalizer.parsers.yaml_parser import YamlParser

PARSER_REGISTRY: dict[str, type[RecipeParser]] = {
    ".xml": XmlParser,
    ".yaml": YamlParser,
    ".yml": YamlParser,
    ".json": JsonParser,
}


def get_parser(extension: str) -> RecipeParser | None:
    """Return a parser instance for the given file extension, or None."""
    parser_cls = PARSER_REGISTRY.get(extension.lower())
    return parser_cls() if parser_cls else None
