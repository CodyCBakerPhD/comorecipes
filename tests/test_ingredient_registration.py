from io import StringIO
from unittest.mock import patch
from como_recipes import Ingredient, IngredientRegistry


def test_add_ingredient(example_ingredient: Ingredient):
    new_registry = IngredientRegistry()

    assert len(new_registry) == 0
    assert repr(new_registry) == "0 registered ingredients\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "0 registered ingredients\n\n"

    new_registry.add_ingredient(ingredient=example_ingredient)

    assert len(new_registry) == 1
    assert repr(new_registry) == "1 registered ingredients\n------------------------\n\nExample Ingredient 1\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert (
        captured_output.getvalue() == "1 registered ingredients\n------------------------\n\nExample Ingredient 1\n\n"
    )
    assert new_registry.get_ingredient(name="Example Ingredient 1") == example_ingredient
