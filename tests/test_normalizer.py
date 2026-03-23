import json
from pathlib import Path

from recipe_normalizer.normalizer import process_directory, write_output, normalize_recipe
from recipe_normalizer.models import Ingredient, Recipe


class TestNormalizeRecipe:
    def test_converts_all_ingredients(self):
        recipe = Recipe(
            name="test",
            ingredients=[
                Ingredient(item="butter", quantity=1, unit="pound"),
                Ingredient(item="water", quantity=2, unit="cups"),
            ],
            preparations=["Mix"],
        )
        result = normalize_recipe(recipe)
        assert result.ingredients[0].unit == "gr"
        assert result.ingredients[1].unit == "gr"
        assert result.name == "test"
        assert result.preparations == ["Mix"]


class TestProcessDirectory:
    def test_reads_all_formats(self, sample_dir: Path):
        recipes = process_directory(sample_dir)
        names = {r.name for r in recipes}
        assert names == {"pancakes", "salad", "soup"}

    def test_skips_unsupported_files(self, sample_dir: Path):
        (sample_dir / "notes.txt").write_text("not a recipe")
        recipes = process_directory(sample_dir)
        assert len(recipes) == 3

    def test_conversions_applied(self, sample_dir: Path):
        recipes = process_directory(sample_dir)
        salad = next(r for r in recipes if r.name == "salad")
        lettuce = salad.ingredients[0]
        assert lettuce.unit == "gr"

    def test_empty_directory(self, tmp_path: Path):
        recipes = process_directory(tmp_path)
        assert recipes == []


class TestWriteOutput:
    def test_writes_valid_json(self, tmp_path: Path):
        recipes = [
            Recipe(
                name="test",
                ingredients=[Ingredient(item="egg", quantity=2)],
                preparations=["Boil"],
            )
        ]
        out = tmp_path / "out.json"
        write_output(recipes, out)

        data = json.loads(out.read_text())
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["name"] == "test"

    def test_omits_empty_unit(self, tmp_path: Path):
        recipes = [
            Recipe(
                name="t",
                ingredients=[Ingredient(item="egg", quantity=1)],
            )
        ]
        out = tmp_path / "out.json"
        write_output(recipes, out)
        data = json.loads(out.read_text())
        assert "unit" not in data[0]["ingredients"][0]
