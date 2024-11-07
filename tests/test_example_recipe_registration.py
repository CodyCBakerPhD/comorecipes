import pathlib

from io import StringIO
from unittest.mock import patch
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

    assert len(new_registry) == 1
    assert repr(new_registry) == "1 registered recipes\n--------------------\n\nExample Recipe 1\n"
    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(new_registry)
    assert captured_output.getvalue() == "1 registered recipes\n--------------------\n\nExample Recipe 1\n\n"
    assert new_registry.get_recipe(recipe_name="Example Recipe 1") == recipe
