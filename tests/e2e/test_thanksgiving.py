from .helpers import parse_and_normalize


def test_thanksgiving(thanksgiving_path):
    result = parse_and_normalize(thanksgiving_path)
    by_item = {ing["item"]: ing for ing in result["ingredients"]}

    assert result["name"] == "thanksgiving feast"
    assert len(result["ingredients"]) == 12
    assert isinstance(result["preparations"], list)
    assert len(result["preparations"]) == 4

    for ing in result["ingredients"]:
        assert "item" in ing
        assert "quantity" in ing

    assert by_item["turkey"]["unit"] == "gr"
    assert by_item["unsalted butter"]["unit"] == "gr"
    assert by_item["apple cider"]["unit"] == "liter"
    assert by_item["all-purpose flour"]["unit"] == "gr"
    assert by_item["vanilla extract"]["unit"] == "ml"
    assert by_item["olive oil"]["unit"] == "ml"
    assert by_item["chicken stock"]["unit"] == "liter"
    assert by_item["heavy cream"]["unit"] == "ml"
    assert by_item["soy sauce"]["unit"] == "ml"

    assert by_item["rosemary extract"]["unit"] == "ml"
    assert by_item["rosemary extract"]["quantity"] == 15

    assert "unit" not in by_item["eggs"]
    assert by_item["eggs"]["quantity"] == 3
    assert "unit" not in by_item["garlic cloves"]
    assert by_item["garlic cloves"]["quantity"] == 6
