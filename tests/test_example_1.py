import pathlib

import py


from como_recipes import Recipe, MeasuredIngredient


def test_example_1_markdown_recipe_load():
    example_1_markdown_file_path = pathlib.Path(__file__).parent / "examples" / "example_1" / "example_recipe_1.md"

    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    assert recipe.name == "Example Recipe 1"
    assert recipe.ingredients == [
        MeasuredIngredient(name="ingredient 1", amount=3, unit="tbsp."),
        MeasuredIngredient(name="ingredient 2", amount=4, unit="g"),
    ]
    assert recipe.instructions == [
        "This is an example of a recipe.",
    ]


def test_example_1_to_pydantic(tmpdir: py.path.local):
    example_folder_path = pathlib.Path(__file__).parent / "examples" / "example_1"
    example_1_markdown_file_path = example_folder_path / "example_recipe_1.md"
    recipe = Recipe.from_markdown_file(file_path=example_1_markdown_file_path)

    test_pydantic_model_file_path = tmpdir / "test_example_1_pydantic_model.py"
    recipe.to_pydantic_file(file_path=test_pydantic_model_file_path)
    with open(file=test_pydantic_model_file_path, mode="r") as io:
        test_pydantic_model_file_content = io.read()

    expected_pydantic_model_file_path = example_folder_path / "_example_recipe_1_pydantic_model.py"
    with open(file=expected_pydantic_model_file_path, mode="r") as io:
        expected_pydantic_model_file_content = io.read()

    # Skip the import styles since expected must be absolute
    assert test_pydantic_model_file_content[1:] == expected_pydantic_model_file_content[1:]
