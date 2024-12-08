import pytest

import como_recipes


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
        amount: int | float = 56
        unit: str = "grams"
        ingredient: como_recipes.Ingredient = example_ingredient

    return ExampleMeasurement()


@pytest.fixture
def example_ingredient_no_conversion() -> como_recipes.Ingredient:
    class ExampleIngredient(como_recipes.Ingredient):
        """A made-up example ingredient for testing."""

        name: str = "Example Ingredient 1"
        default_grams_per_package: int | float | None = None
        default_package_unit: str | None = None

    return ExampleIngredient()


@pytest.fixture
def example_meal_1() -> como_recipes.Meal:
    example_recipe_names = ["Aglio E Olio", "Sauteed Green Beans"]
    recipes = [
        como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name) for recipe_name in example_recipe_names
    ]
    example_meal = como_recipes.Meal(recipes=recipes)

    return example_meal


@pytest.fixture
def example_meal_2() -> como_recipes.Meal:
    example_recipe_names = ["Aglio E Olio", "Sauteed Green Beans"]
    recipes = [
        como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name) for recipe_name in example_recipe_names
    ]
    example_meal = como_recipes.Meal(recipes=recipes, quantity_multiplier=2)

    return example_meal
