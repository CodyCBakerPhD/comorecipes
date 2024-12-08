import pathlib
from io import StringIO
from unittest.mock import patch

import pytest

from como_recipes import Recipe, RecipeRegistry


def test_recipe_registry(example_1_folder_path: pathlib.Path):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    example_recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    # Test empty registry
    new_registry = RecipeRegistry()

    expected_repr = "\ncomo_recipes.RecipeRegistry()\n"
    expected_str = "0 registered recipes\n\n"
    assert len(new_registry) == 0
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str

    # Test adding a recipe
    new_registry.add_recipe(recipe=example_recipe)

    expected_repr = (
        "\n"
        "como_recipes.RecipeRegistry(\n"
        "\t_recipes={\n"
        '\t\tcomo_recipes.Recipe(name="Example Recipe 1", ...),\n'
        "\t}\n"
        ")\n"
    )
    expected_str = "1 registered recipes\n--------------------\n\nExample Recipe 1\n\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str
    assert new_registry.get_recipe(recipe_name="Example Recipe 1") == example_recipe

    # Test removing a recipe
    recipe_2 = Recipe(
        name="Example Recipe 2",
        measurements=example_recipe.measurements,
        instructions=example_recipe.instructions,
    )
    new_registry.add_recipe(recipe=recipe_2)
    new_registry.remove_recipe(recipe_name="Example Recipe 1")

    expected_repr = (
        "\n"
        "como_recipes.RecipeRegistry(\n"
        "\t_recipes={\n"
        '\t\tcomo_recipes.Recipe(name="Example Recipe 2", ...),\n'
        "\t}\n"
        ")\n"
    )
    expected_str = "1 registered recipes\n--------------------\n\nExample Recipe 2\n\n"
    assert len(new_registry) == 1
    assert repr(new_registry) == expected_repr
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == expected_str
    assert new_registry.get_recipe(recipe_name="Example Recipe 2") == recipe_2


def test_get_recipe_error():
    new_registry = RecipeRegistry()

    with pytest.raises(ValueError, match="Recipe 'Unregistered' not found in the registry."):
        new_registry.get_recipe(recipe_name="Unregistered")
