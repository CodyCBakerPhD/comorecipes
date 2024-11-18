from io import StringIO
from unittest.mock import patch

import pytest

from como_recipes import Ingredient, IngredientRegistry


def test_add_ingredient(example_ingredient: Ingredient):
    new_registry = IngredientRegistry()

    assert len(new_registry) == 0
    assert repr(new_registry) == "0 registered ingredients\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "0 registered ingredients\n\n"

    new_registry.add_ingredient(ingredient=example_ingredient)

    expected_repr = "1 registered ingredients\n------------------------\n\nExample Ingredient 1\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"
    assert new_registry.get_ingredient(name="Example Ingredient 1") == example_ingredient


def test_get_ingredient_error():
    new_registry = IngredientRegistry()

    with pytest.raises(ValueError, match="Ingredient 'Unregistered' not found in the registry."):
        new_registry.get_ingredient(name="Unregistered")
