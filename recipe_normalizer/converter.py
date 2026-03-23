from recipe_normalizer.models import Ingredient

# Maps every recognised imperial/US unit (including common abbreviations and plural forms)
# to a (metric_unit, multiplier) pair used during conversion.
CONVERSION_TABLE: dict[str, tuple[str, float]] = {
    # Weight
    "pound": ("gr", 453.592),
    "pounds": ("gr", 453.592),
    "lb": ("gr", 453.592),
    "lbs": ("gr", 453.592),
    "ounce": ("gr", 28.3495),
    "ounces": ("gr", 28.3495),
    "oz": ("gr", 28.3495),
    # Volume – large
    "gallon": ("liter", 3.785),
    "gallons": ("liter", 3.785),
    "quart": ("liter", 0.946),
    "quarts": ("liter", 0.946),
    # Volume – medium (cups treated as ml-equivalent weight of water)
    "cup": ("gr", 240),
    "cups": ("gr", 240),
    "pint": ("ml", 473.176),
    "pints": ("ml", 473.176),
    # Volume – small
    "fl. oz.": ("ml", 29.5735),
    "fl oz": ("ml", 29.5735),
    "tablespoon": ("ml", 14.787),
    "tablespoons": ("ml", 14.787),
    "tbsp": ("ml", 14.787),
    "teaspoon": ("ml", 4.929),
    "teaspoons": ("ml", 4.929),
    "tsp": ("ml", 4.929),
}


def _clean_quantity(value: float) -> int | float:
    """Round to 2 decimal places; return int when the result is a whole number."""
    rounded = round(value, 2)
    return int(rounded) if rounded == int(rounded) else rounded


def convert_ingredient(ingredient: Ingredient) -> Ingredient:
    """Convert imperial units to metric. Returns a new Ingredient."""
    unit_lower = ingredient.unit.strip().lower()
    if not unit_lower or unit_lower not in CONVERSION_TABLE:
        return Ingredient(
            item=ingredient.item,
            quantity=_clean_quantity(ingredient.quantity),
            unit=ingredient.unit,
            comment=ingredient.comment,
        )

    metric_unit, factor = CONVERSION_TABLE[unit_lower]
    return Ingredient(
        item=ingredient.item,
        quantity=_clean_quantity(ingredient.quantity * factor),
        unit=metric_unit,
        comment=ingredient.comment,
    )
