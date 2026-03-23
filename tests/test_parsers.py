from pathlib import Path

from recipe_normalizer.parsers import get_parser
from recipe_normalizer.parsers.xml_parser import XmlParser
from recipe_normalizer.parsers.yaml_parser import YamlParser
from recipe_normalizer.parsers.json_parser import JsonParser
from tests.conftest import SAMPLE_XML, SAMPLE_YAML, SAMPLE_JSON


class TestParserRegistry:
    def test_xml_extension(self):
        assert isinstance(get_parser(".xml"), XmlParser)

    def test_yaml_extension(self):
        assert isinstance(get_parser(".yaml"), YamlParser)

    def test_yml_extension(self):
        assert isinstance(get_parser(".yml"), YamlParser)

    def test_json_extension(self):
        assert isinstance(get_parser(".json"), JsonParser)

    def test_unsupported_returns_none(self):
        assert get_parser(".txt") is None


class TestXmlParser:
    def test_parse(self, tmp_path: Path):
        f = tmp_path / "test.xml"
        f.write_text(SAMPLE_XML)
        recipe = XmlParser().parse(f)

        assert recipe.name == "pancakes"
        assert len(recipe.ingredients) == 3
        assert recipe.ingredients[0].item == "flour"
        assert recipe.ingredients[0].quantity == 2.0
        assert recipe.ingredients[0].unit == "cups"
        assert recipe.ingredients[2].unit == ""
        assert len(recipe.preparations) == 2


class TestYamlParser:
    def test_parse(self, tmp_path: Path):
        f = tmp_path / "test.yaml"
        f.write_text(SAMPLE_YAML)
        recipe = YamlParser().parse(f)

        assert recipe.name == "salad"
        assert len(recipe.ingredients) == 3
        assert recipe.ingredients[0].item == "lettuce"
        assert recipe.ingredients[0].unit == "pound"
        assert recipe.ingredients[2].comment == "diced"
        assert len(recipe.preparations) == 2


class TestJsonParser:
    def test_parse(self, tmp_path: Path):
        f = tmp_path / "test.json"
        f.write_text(SAMPLE_JSON)
        recipe = JsonParser().parse(f)

        assert recipe.name == "soup"
        assert len(recipe.ingredients) == 2
        assert recipe.ingredients[0].unit == "gallon"
        assert len(recipe.preparations) == 2
