import pathlib

import py


from como_recipes import Recipe, MeasurementRegistry


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
    with open(file=test_pydantic_model_file_path, mode="r") as io:
        test_pydantic_model_file_lines = io.readlines()

    expected_pydantic_model_file_path = example_folder_path / "_example_recipe_1.py"
    with open(file=expected_pydantic_model_file_path, mode="r") as io:
        expected_pydantic_model_file_lines = io.readlines()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_lines == expected_pydantic_model_file_lines
