import pathlib

import pytest

import como_recipes


@pytest.fixture
def example_1_folder_path() -> pathlib.Path:
    relative_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    return relative_path


@pytest.fixture
def example_ingredient() -> como_recipes.Ingredient:
    return como_recipes.Ingredient(
        name="Example Ingredient 1",
        default_grams_per_package=12.34,
        default_package_unit="container",
    )


@pytest.fixture
def example_measurement(example_ingredient: como_recipes.Ingredient) -> como_recipes.Measurement:
    return como_recipes.Measurement(amount=45, unit="grams", ingredient=example_ingredient)


@pytest.fixture
def example_ingredient_no_conversion() -> como_recipes.Ingredient:
    return como_recipes.Ingredient(name="Example Ingredient 1")
