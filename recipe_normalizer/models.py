from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ingredient:
    item: str
    quantity: int | float
    unit: str = ""
    comment: str = ""

    def to_dict(self) -> dict:
        result = {"item": self.item, "quantity": self.quantity}
        if self.unit:
            result["unit"] = self.unit
        if self.comment:
            result["comment"] = self.comment
        return result


@dataclass
class Recipe:
    name: str
    ingredients: list[Ingredient] = field(default_factory=list)
    preparations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        result: dict = {
            "name": self.name,
            "ingredients": [ing.to_dict() for ing in self.ingredients],
        }
        if self.preparations:
            result["preparations"] = self.preparations
        return result
