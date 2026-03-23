from .helpers import parse_and_normalize


def test_example_pudding(example_pudding_path):
    result = parse_and_normalize(example_pudding_path)
    by_item = {ing["item"]: ing for ing in result["ingredients"]}

    assert result["name"] == "pudding"
    assert len(result["ingredients"]) == 4
    assert isinstance(result["preparations"], list)
    assert len(result["preparations"]) == 1

    for ing in result["ingredients"]:
        assert "item" in ing
        assert "quantity" in ing

    assert by_item["milk"]["unit"] == "liter"
    assert by_item["sugar"]["unit"] == "gr"
    assert by_item["sugar"]["quantity"] == 480

    assert by_item["vanilla"]["unit"] == "ml"
    assert by_item["vanilla"]["quantity"] == 10

    assert "unit" not in by_item["egg yolks"]
    assert by_item["egg yolks"]["quantity"] == 12
