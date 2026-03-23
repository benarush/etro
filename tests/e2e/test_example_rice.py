from .helpers import parse_and_normalize


def test_example_rice(example_rice_path):
    result = parse_and_normalize(example_rice_path)
    by_item = {ing["item"]: ing for ing in result["ingredients"]}

    assert result["name"] == "rice"
    assert len(result["ingredients"]) == 3
    assert isinstance(result["preparations"], list)
    assert len(result["preparations"]) == 1

    for ing in result["ingredients"]:
        assert "item" in ing
        assert "quantity" in ing

    assert by_item["rice"]["unit"] == "gr"
    assert by_item["oil"]["unit"] == "ml"

    assert "unit" not in by_item["onion"]
    assert by_item["onion"]["quantity"] == 1
