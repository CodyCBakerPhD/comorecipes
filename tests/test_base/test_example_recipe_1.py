import pathlib
from io import StringIO
from unittest.mock import patch

import py

from como_recipes import IngredientRegistry, Recipe


def test_example_1_markdown_recipe_load(example_1_folder_path: pathlib.Path):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"

    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    assert recipe.name == "Example Recipe 1"
    assert recipe.measurements == (
        IngredientRegistry.get_measurement(amount=31 / 10, unit="tbsp.", name="ingredient 1"),
        IngredientRegistry.get_measurement(amount=4, unit="g", name="ingredient 2"),
    )
    assert recipe.instructions == ("This is an example of a recipe.",)


def test_example_1_to_pydantic(example_1_folder_path: pathlib.Path, tmpdir: py.path.local):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_pydantic_model_file_path = pathlib.Path(tmpdir) / "_example_recipe_1.py"
    recipe.to_pydantic_file(file_path=test_pydantic_model_file_path)
    with test_pydantic_model_file_path.open(mode="r") as io:
        test_pydantic_model_file_lines = io.readlines()

    expected_pydantic_model_file_path = example_1_folder_path / "_example_recipe_1.py"
    with expected_pydantic_model_file_path.open(mode="r") as io:
        expected_pydantic_model_file_lines = io.readlines()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_lines == expected_pydantic_model_file_lines


def test_example_1_to_pydantic_with_init_file(example_1_folder_path: pathlib.Path, tmpdir: py.path.local):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_folder_path = pathlib.Path(tmpdir) / "example_1_with_init"
    test_folder_path.mkdir()
    test_pydantic_model_file_path = test_folder_path / "_example_recipe_1.py"
    test_init_file_path = test_pydantic_model_file_path.parent / "__init__.py"
    test_init_file_path.touch()
    recipe.to_pydantic_file(file_path=test_pydantic_model_file_path)
    with test_pydantic_model_file_path.open(mode="r") as io:
        test_pydantic_model_file_lines = io.readlines()

    expected_pydantic_model_file_path = example_1_folder_path / "_example_recipe_1.py"
    with expected_pydantic_model_file_path.open(mode="r") as io:
        expected_pydantic_model_file_lines = io.readlines()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_lines == expected_pydantic_model_file_lines


def test_example_1_to_markdown(example_1_folder_path: pathlib.Path, tmpdir: py.path.local):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_markdown_file_path = pathlib.Path(tmpdir) / "example_recipe_1.md"
    recipe.to_markdown_file(file_path=test_markdown_file_path)
    with test_markdown_file_path.open(mode="r") as io:
        test_markdown_file_lines = io.readlines()

    with example_1_markdown_file_path.open(mode="r") as io:
        expected_markdown_file_lines = io.readlines()

    assert test_markdown_file_lines == expected_markdown_file_lines


def test_example_1_repr(example_1_folder_path: pathlib.Path):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    expected_repr = (
        "Recipe(\n"
        '\tname="Example Recipe 1",\n'
        "\ttags=('Italian', 'Pasta', 'Entree', 'Vegetarian'),\n"
        "\tmeasurements=(\n"
        '\t\tMeasurement(amount=31/10, unit="tbsp.", ingredient=Ingredient(name="ingredient 1")),\n'
        '\t\tMeasurement(amount=4, unit="g", ingredient=Ingredient(name="ingredient 2")),\n'
        "\t),\n"
        "\tinstructions=(\n"
        '\t\t"This is an example of a recipe.",\n'
        "\t),\n"
        ")"
    )
    assert repr(recipe) == expected_repr


def test_example_1_print(example_1_folder_path: pathlib.Path):
    example_1_markdown_file_path = example_1_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(recipe)

    expected_print = (
        "\n"
        "Example Recipe 1\n"
        "================\n"
        "\n"
        "Ingredients\n"
        "-----------\n"
        "31/10 tbsp. ingredient 1\n"
        "4 g ingredient 2\n"
        "\n"
        "\n"
        "Instructions\n"
        "------------\n"
        "This is an example of a recipe.\n"
        "\n"
    )
    assert captured_output.getvalue() == expected_print
