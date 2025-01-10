from io import StringIO
from unittest.mock import patch

import pytest

import como_recipes


def test_get_ingredient_error():
    new_registry = como_recipes.IngredientRegistry()

    with pytest.raises(ValueError, match="Ingredient 'Unregistered' not found in the registry."):
        new_registry.get_ingredient(ingredient_name="Unregistered")


def test_ingredient_registry(example_ingredient: como_recipes.Ingredient):
    """A sequence of integration tests for the `IngredientRegistry` class."""
    # Test empty registry
    new_registry = como_recipes.IngredientRegistry()

    expected_repr = "\ncomo_recipes.IngredientRegistry()\n"
    expected_str = "\n0 registered ingredients\n\n"
    assert len(new_registry) == 0
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str

    # Test adding an ingredient
    new_registry.add_ingredient(ingredient=example_ingredient)

    test_ingredient = new_registry.get_ingredient(ingredient_name="Example Ingredient 1")

    expected_repr = (
        "\n"
        "como_recipes.IngredientRegistry(\n"
        "\t_ingredients={\n"
        '\t\tIngredient(name="Example Ingredient 1", default_grams_per_package=12.34, '
        'default_package_unit="container"),\n'
        "\t}\n"
        ")\n"
    )
    expected_str = "\n1 registered ingredients\n-------------------------\n\nExample Ingredient 1\n\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str
    assert test_ingredient == example_ingredient

    # Test removing an ingredient
    ingredient_2 = como_recipes.Ingredient(name="Example Ingredient 2")
    new_registry.add_ingredient(ingredient=ingredient_2)
    new_registry.remove_ingredient(ingredient_name="Example Ingredient 1")

    expected_repr = (
        "\n"
        "como_recipes.IngredientRegistry(\n"
        "\t_ingredients={\n"
        '\t\tIngredient(name="Example Ingredient 2"),\n'
        "\t}\n"
        ")\n"
    )
    expected_str = "\n1 registered ingredients\n-------------------------\n\nExample Ingredient 2\n\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str
    assert new_registry.get_ingredient(ingredient_name="Example Ingredient 2") == ingredient_2


def test_get_measurement_non_default():
    measurement = como_recipes.IngredientRegistry.get_measurement(
        amount=1.0,
        unit="grams",
        ingredient_name="Unregistered",
    )
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._base._base_ingredient.Ingredient'>"
    assert measurement.ingredient.name == "Unregistered"


def test_ingredient_equality_with_different_memory_address():
    test_ingredient = como_recipes.Ingredient(
        name="garlic",
        default_grams_per_package=40.0,
        default_package_unit="heads",
    )
    registered_ingredient = como_recipes.default_ingredient_registry.get_ingredient(ingredient_name="garlic")

    assert test_ingredient == registered_ingredient


def test_measurement_equality_with_different_memory_address():
    test_ingredient = como_recipes.Ingredient(
        name="garlic",
        default_grams_per_package=40.0,
        default_package_unit="heads",
    )
    test_measurement = como_recipes.Measurement(amount=1.0, unit="grams", ingredient=test_ingredient)

    registered_measurement = como_recipes.IngredientRegistry.get_measurement(
        amount=1.0,
        unit="grams",
        ingredient_name="garlic",
    )

    assert test_measurement == registered_measurement
