import pytest

from recipe_normalizer.converter import convert_ingredient, _clean_quantity
from recipe_normalizer.models import Ingredient


class TestCleanQuantity:
    def test_whole_number_becomes_int(self):
        assert _clean_quantity(200.0) == 200
        assert isinstance(_clean_quantity(200.0), int)

    def test_float_stays_float(self):
        assert _clean_quantity(3.786) == 3.79
        assert isinstance(_clean_quantity(3.786), float)

    def test_rounding(self):
        assert _clean_quantity(59.7385) == 59.74


class TestConvertIngredient:
    def test_pound_to_grams(self):
        ing = Ingredient(item="rice", quantity=0.44, unit="pound")
        result = convert_ingredient(ing)
        assert result.unit == "gr"
        assert result.quantity == pytest.approx(199.58, abs=0.5)

    def test_fl_oz_to_ml(self):
        ing = Ingredient(item="oil", quantity=2.02, unit="fl. oz.")
        result = convert_ingredient(ing)
        assert result.unit == "ml"
        assert result.quantity == pytest.approx(59.74, abs=0.5)

    def test_gallon_to_liter(self):
        ing = Ingredient(item="milk", quantity=1, unit="gallon")
        result = convert_ingredient(ing)
        assert result.unit == "liter"
        assert result.quantity == pytest.approx(3.78, abs=0.02)

    def test_cups_to_grams(self):
        ing = Ingredient(item="sugar", quantity=2, unit="cups")
        result = convert_ingredient(ing)
        assert result.unit == "gr"
        assert result.quantity == 480

    def test_tsp_to_ml(self):
        ing = Ingredient(item="salt", quantity=2, unit="tsp")
        result = convert_ingredient(ing)
        assert result.unit == "ml"
        assert result.quantity == pytest.approx(9.86, abs=0.01)

    def test_already_metric_unchanged(self):
        ing = Ingredient(item="vanilla", quantity=10, unit="ml")
        result = convert_ingredient(ing)
        assert result.unit == "ml"
        assert result.quantity == 10

    def test_no_unit_unchanged(self):
        ing = Ingredient(item="eggs", quantity=3, unit="")
        result = convert_ingredient(ing)
        assert result.unit == ""
        assert result.quantity == 3

    def test_comment_preserved(self):
        ing = Ingredient(item="onion", quantity=1, unit="", comment="diced")
        result = convert_ingredient(ing)
        assert result.comment == "diced"

    def test_case_insensitive(self):
        ing = Ingredient(item="flour", quantity=1, unit="Pound")
        result = convert_ingredient(ing)
        assert result.unit == "gr"
