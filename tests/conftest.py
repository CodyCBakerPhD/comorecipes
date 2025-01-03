import pathlib

import pytest

import como_recipes


@pytest.fixture
def example_1_folder_path() -> pathlib.Path:
    relative_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    return relative_path


@pytest.fixture
def example_ingredient() -> como_recipes.Ingredient:
    class ExampleIngredient1(como_recipes.Ingredient):
        name: str = "Example Ingredient 1"
        default_grams_per_package: int | float | None = 12.34
        default_package_unit: str | None = "container"

    return ExampleIngredient1()


@pytest.fixture
def example_measurement(example_ingredient: como_recipes.Ingredient) -> como_recipes.Measurement:
    class ExampleMeasurement(como_recipes.Measurement):
        amount: int | float
        unit: str
        ingredient: como_recipes.Ingredient

    return ExampleMeasurement(amount=45, unit="grams", ingredient=example_ingredient)


@pytest.fixture
def example_ingredient_no_conversion() -> como_recipes.Ingredient:
    class ExampleIngredient(como_recipes.Ingredient):
        """A made-up example ingredient for testing."""

        name: str = "Example Ingredient 1"
        default_grams_per_package: int | float | None = None
        default_package_unit: str | None = None

    return ExampleIngredient()
