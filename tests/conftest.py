import pytest
from como_recipes import Ingredient, Measurement


@pytest.fixture
def example_ingredient() -> Ingredient:
    class ExampleIngredient1(Ingredient):
        name: str = "Example Ingredient 1"
        default_grams_per_package: int | float | None = 12.34
        default_package_unit: str | None = "container"

    return ExampleIngredient1()


@pytest.fixture
def example_measurement(example_ingredient: Ingredient) -> Measurement:
    class ExampleMeasurement(Measurement):
        amount: int | float = 5.6
        unit: str = "grams"
        ingredient: Ingredient = example_ingredient

    return ExampleMeasurement()


@pytest.fixture
def example_ingredient_no_conversion() -> Ingredient:
    class ExampleIngredient(Ingredient):
        """A made-up example ingredient for testing."""

        name: str = "Example Ingredient 1"
        default_grams_per_package: int | float | None = None
        default_package_unit: str | None = None

    return ExampleIngredient()
