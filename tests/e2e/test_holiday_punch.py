from .helpers import parse_and_normalize


def test_holiday_punch(holiday_punch_path):
    result = parse_and_normalize(holiday_punch_path)
    by_item = {ing["item"]: ing for ing in result["ingredients"]}

    assert result["name"] == "holiday punch"
    assert len(result["ingredients"]) == 12
    assert isinstance(result["preparations"], list)
    assert len(result["preparations"]) == 5

    for ing in result["ingredients"]:
        assert "item" in ing
        assert "quantity" in ing

    assert by_item["cranberry juice"]["unit"] == "liter"
    assert by_item["fresh orange juice"]["unit"] == "gr"
    assert by_item["fresh ginger"]["unit"] == "gr"
    assert by_item["honey"]["unit"] == "ml"
    assert by_item["apple cider"]["unit"] == "liter"
    assert by_item["fresh lemon juice"]["unit"] == "ml"
    assert by_item["pomegranate seeds"]["unit"] == "gr"
    assert by_item["rum"]["unit"] == "ml"

    assert by_item["ginger ale"]["unit"] == "liter"
    assert by_item["ginger ale"]["quantity"] == 1
    assert by_item["powdered sugar"]["unit"] == "g"
    assert by_item["powdered sugar"]["quantity"] == 200

    assert "unit" not in by_item["whole cloves"]
    assert by_item["whole cloves"]["quantity"] == 10
