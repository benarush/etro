from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from recipe_normalizer.models import Recipe


class RecipeParser(ABC):
    @abstractmethod
    def parse(self, path: Path) -> Recipe:
        """Parse a recipe file and return a Recipe object."""
