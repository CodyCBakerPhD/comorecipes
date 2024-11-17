import pathlib
from io import StringIO
from unittest.mock import patch

import py

from como_recipes import MeasurementRegistry, Recipe


def test_example_1_markdown_recipe_load():
    example_1_markdown_file_path = pathlib.Path(__file__).parent / "examples" / "example_1" / "example_recipe_1.md"

    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    assert recipe.name == "Example Recipe 1"
    assert recipe.measurements == [
        MeasurementRegistry.get_measurement(amount=3, unit="tbsp.", name="ingredient 1"),
        MeasurementRegistry.get_measurement(amount=4, unit="g", name="ingredient 2"),
    ]
    assert recipe.instructions == [
        "This is an example of a recipe.",
    ]


def test_example_1_to_pydantic(tmpdir: py.path.local):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_pydantic_model_file_path = pathlib.Path(tmpdir) / "_example_recipe_1.py"
    recipe.to_pydantic_file(file_path=test_pydantic_model_file_path)
    with open(file=test_pydantic_model_file_path) as io:
        test_pydantic_model_file_lines = io.readlines()

    expected_pydantic_model_file_path = example_folder_path / "_example_recipe_1.py"
    with open(file=expected_pydantic_model_file_path) as io:
        expected_pydantic_model_file_lines = io.readlines()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_lines == expected_pydantic_model_file_lines


def test_example_1_to_pydantic_with_init_file(tmpdir: py.path.local):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_folder_path = pathlib.Path(tmpdir) / "example_1_with_init"
    test_folder_path.mkdir()
    test_pydantic_model_file_path = test_folder_path / "_example_recipe_1.py"
    test_init_file_path = test_pydantic_model_file_path.parent / "__init__.py"
    test_init_file_path.touch()
    recipe.to_pydantic_file(file_path=test_pydantic_model_file_path)
    with open(file=test_pydantic_model_file_path) as io:
        test_pydantic_model_file_lines = io.readlines()

    expected_pydantic_model_file_path = example_folder_path / "_example_recipe_1.py"
    with open(file=expected_pydantic_model_file_path) as io:
        expected_pydantic_model_file_lines = io.readlines()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_lines == expected_pydantic_model_file_lines


def test_example_1_to_markdown(tmpdir: py.path.local):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_markdown_file_path = pathlib.Path(tmpdir) / "example_recipe_1.md"
    recipe.to_markdown_file(file_path=test_markdown_file_path)
    with open(file=test_markdown_file_path) as io:
        test_markdown_file_lines = io.readlines()

    with open(file=example_1_markdown_file_path) as io:
        expected_markdown_file_lines = io.readlines()

    assert test_markdown_file_lines == expected_markdown_file_lines


def test_example_1_repr():
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    expected_repr = """
Example Recipe 1
================

Ingredients
-----------
3.0 tbsp. ingredient 1
4.0 g ingredient 2


Instructions
------------
This is an example of a recipe.
"""
    assert repr(recipe) == expected_repr


def test_example_1_print():
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"

    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(recipe)

    expected_print = """
Example Recipe 1
================

Ingredients
-----------
3.0 tbsp. ingredient 1
4.0 g ingredient 2


Instructions
------------
This is an example of a recipe.

"""
    assert captured_output.getvalue() == expected_print
