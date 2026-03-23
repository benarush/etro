from .helpers import parse_and_normalize


def test_banana_bread(banana_bread_path):
    result = parse_and_normalize(banana_bread_path)
    by_item = {ing["item"]: ing for ing in result["ingredients"]}

    assert result["name"] == "banana bread"
    assert len(result["ingredients"]) == 12
    assert isinstance(result["preparations"], list)
    assert len(result["preparations"]) == 6

    for ing in result["ingredients"]:
        assert "item" in ing
        assert "quantity" in ing

    assert by_item["granulated sugar"]["unit"] == "gr"
    assert by_item["granulated sugar"]["quantity"] == 180
    assert by_item["unsalted butter"]["unit"] == "gr"
    assert by_item["whole milk"]["unit"] == "ml"
    assert by_item["vanilla essence"]["unit"] == "ml"
    assert by_item["all-purpose flour"]["unit"] == "gr"
    assert by_item["all-purpose flour"]["quantity"] == 240
    assert by_item["chopped walnuts"]["unit"] == "gr"
    assert by_item["buttermilk"]["unit"] == "ml"

    assert by_item["dark chocolate chips"]["unit"] == "g"
    assert by_item["dark chocolate chips"]["quantity"] == 100

    assert "unit" not in by_item["ripe bananas"]
    assert by_item["ripe bananas"]["quantity"] == 3
    assert "unit" not in by_item["egg"]
    assert by_item["egg"]["quantity"] == 1
