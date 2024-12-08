from io import StringIO
from unittest.mock import patch

import pytest

from como_recipes import Ingredient, IngredientRegistry


def test_add_ingredient(example_ingredient: Ingredient):
    new_registry = IngredientRegistry()

    expected_repr = "\ncomo_recipes.IngredientRegistry()\n"
    expected_str = "\n0 registered ingredients\n\n"
    assert len(new_registry) == 0
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str

    new_registry.add_ingredient(ingredient=example_ingredient)

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
    assert new_registry.get_ingredient(name="Example Ingredient 1") == example_ingredient


def test_get_ingredient_error():
    new_registry = IngredientRegistry()

    with pytest.raises(ValueError, match="Ingredient 'Unregistered' not found in the registry."):
        new_registry.get_ingredient(name="Unregistered")


def test_get_measurement_default():
    measurement = IngredientRegistry.get_measurement(amount=1.0, unit="grams", name="Garlic")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._ingredients._garlic.Garlic'>"
    assert measurement.ingredient.name == "Garlic"


def test_get_measurement_non_default():
    measurement = IngredientRegistry.get_measurement(amount=1.0, unit="grams", name="Unregistered")
    assert str(type(measurement.ingredient)) == "<class 'como_recipes._base._base_ingredient.Ingredient'>"
    assert measurement.ingredient.name == "Unregistered"
