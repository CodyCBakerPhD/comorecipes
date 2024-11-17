import pathlib
from io import StringIO
from unittest.mock import patch

import pytest

from como_recipes import Recipe, RecipeRegistry


def test_example_recipe_1_add_to_registry():
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    new_registry = RecipeRegistry()

    assert len(new_registry) == 0
    assert repr(new_registry) == "0 registered recipes\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "0 registered recipes\n\n"

    new_registry.add_recipe(recipe=recipe)

    expected_repr = "1 registered recipes\n--------------------\n\nExample Recipe 1\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_repr + "\n"
    assert new_registry.get_recipe(recipe_name="Example Recipe 1") == recipe


def test_get_recipe_error():
    new_registry = RecipeRegistry()

    with pytest.raises(ValueError) as error_info:
        new_registry.get_recipe(recipe_name="Unregistered")
    assert str(error_info.value) == "Recipe 'Unregistered' not found in the registry."
