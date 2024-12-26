import pathlib
from io import StringIO
from unittest.mock import patch

import py

from como_recipes import IngredientRegistry, Recipe


def test_example_1_yaml_recipe_load(example_1_folder_path: pathlib.Path):
    example_1_yaml_file_path = example_1_folder_path / "example_recipe_1.yaml"

    recipe = Recipe.from_yaml_file(file_path=example_1_yaml_file_path)

    assert recipe.name == "Example Recipe 1"
    assert recipe.measurements == (
        IngredientRegistry.get_measurement(amount=31 / 10, unit="tbsp.", ingredient_name="ingredient 1"),
        IngredientRegistry.get_measurement(amount=4, unit="g", ingredient_name="ingredient 2"),
    )
    assert recipe.instructions == ("This is an example of a recipe.",)


def test_example_1_yaml_recipe_roundtrip(example_1_folder_path: pathlib.Path, tmpdir: py.path.local):
    example_1_yaml_file_path = example_1_folder_path / "example_recipe_1.yaml"

    recipe = Recipe.from_yaml_file(file_path=example_1_yaml_file_path)

    test_yaml_file_path = pathlib.Path(tmpdir) / "test_example_recipe_1.yaml"
    recipe.to_yaml_file(file_path=test_yaml_file_path)

    recipe_loaded = Recipe.from_yaml_file(file_path=test_yaml_file_path)

    assert recipe_loaded == recipe

    test_raw_lines = test_yaml_file_path.read_text().splitlines()
    expected_raw_lines = example_1_yaml_file_path.read_text().splitlines()
    assert test_raw_lines[:-1] == expected_raw_lines


def test_example_1_to_html(example_1_folder_path: pathlib.Path, tmpdir: py.path.local):
    example_1_yaml_file_path = example_1_folder_path / "example_recipe_1.yaml"
    recipe = Recipe.from_yaml_file(file_path=example_1_yaml_file_path)

    test_html_file_path = pathlib.Path(tmpdir) / "example_recipe_1.html"
    recipe.to_html_file(file_path=test_html_file_path)
    with test_html_file_path.open(mode="r") as io:
        test_html_file_lines = io.readlines()

    example_1_html_file_path = example_1_folder_path / "example_recipe_1.html"
    with example_1_html_file_path.open(mode="r") as io:
        expected_html_file_lines = io.readlines()

    assert test_html_file_lines == expected_html_file_lines


def test_example_1_repr(example_1_folder_path: pathlib.Path):
    example_1_yaml_file_path = example_1_folder_path / "example_recipe_1.yaml"
    recipe = Recipe.from_yaml_file(file_path=example_1_yaml_file_path)

    expected_repr = (
        "Recipe(\n"
        '\tname="Example Recipe 1",\n'
        "\ttags=('Italian', 'Pasta', 'Entree', 'Vegetarian'),\n"
        "\tmeasurements=(\n"
        '\t\tMeasurement(amount=31/10, unit="tbsp.", '
        'ingredient=Ingredient(name="ingredient 1")),\n'
        '\t\tMeasurement(amount=4, unit="g", ingredient=Ingredient(name="ingredient '
        '2")),\n'
        "\t),\n"
        "\tinstructions=(\n"
        '\t\t"This is an example of a recipe.",\n'
        "\t),\n"
        "\tnotes=(\n"
        '\t\t"Do not forget about the notes!",\n'
        "\t),\n"
        ")"
    )
    assert repr(recipe) == expected_repr


def test_example_1_print(example_1_folder_path: pathlib.Path):
    example_1_yaml_file_path = example_1_folder_path / "example_recipe_1.yaml"
    recipe = Recipe.from_yaml_file(file_path=example_1_yaml_file_path)

    with patch("sys.stdout", new=StringIO()) as captured_output:
        print(recipe)

    expected_print = (
        "\n"
        "Example Recipe 1\n"
        "================\n"
        "\n"
        "Tags: Italian, Pasta, Entree, Vegetarian\n"
        "\n"
        "Ingredients\n"
        "-----------\n"
        "31/10 tbsp. ingredient 1\n"
        "4 g ingredient 2\n"
        "\n"
        "\n"
        "Notes\n"
        "-----\n"
        "Do not forget about the notes!\n"
        "\n"
        "\n"
        "Instructions\n"
        "------------\n"
        "This is an example of a recipe.\n"
        "\n"
    )
    assert captured_output.getvalue() == expected_print
