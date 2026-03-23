from pathlib import Path

import pytest

RECIPES_DIR = Path(__file__).parent.parent.parent / "recipes"


@pytest.fixture(scope="module")
def holiday_punch_path():
    return RECIPES_DIR / "challenge_holiday_punch.json"


@pytest.fixture(scope="module")
def banana_bread_path():
    return RECIPES_DIR / "challenge_banana_bread.yaml"


@pytest.fixture(scope="module")
def thanksgiving_path():
    return RECIPES_DIR / "challenge_thanksgiving.xml"


@pytest.fixture(scope="module")
def example_pudding_path():
    return RECIPES_DIR / "example_input_1.xml"


@pytest.fixture(scope="module")
def example_rice_path():
    return RECIPES_DIR / "example_input_2.yaml"
