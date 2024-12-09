import pathlib

import py

import como_recipes


def test_default_recipe_load_consistency():
    package_source_folder_path = pathlib.Path(__file__).parent.parent.parent / "src"
    markdown_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_markdown"

    for markdown_recipe_file_path in markdown_recipe_folder_path.iterdir():
        markdown_recipe = como_recipes.Recipe.from_markdown_file(file_path=markdown_recipe_file_path)
        recipe_name = markdown_recipe.name

        pydantic_recipe = como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)

        assert markdown_recipe == pydantic_recipe


def test_default_recipe_to_markdown_consistency(tmpdir: py.path.local):
    package_source_folder_path = pathlib.Path(__file__).parent.parent.parent / "src"
    markdown_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_markdown"

    for markdown_recipe_file_path in markdown_recipe_folder_path.iterdir():
        markdown_recipe = como_recipes.Recipe.from_markdown_file(file_path=markdown_recipe_file_path)
        recipe_name = markdown_recipe.name

        pydantic_recipe = como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)

        test_markdown_file_path = pathlib.Path(tmpdir) / f"test_{recipe_name}.md"
        pydantic_recipe.to_markdown_file(file_path=test_markdown_file_path)

        with test_markdown_file_path.open(mode="r") as io:
            test_markdown_file_lines = io.readlines()

        with markdown_recipe_file_path.open(mode="r") as io:
            expected_markdown_file_lines = io.readlines()

        assert test_markdown_file_lines == expected_markdown_file_lines


# TODO: could maybe do a to_pydantic consistency without pre commit messing things up
#  if the source instruction lines are properly broken up


def test_recipe_counts_consistency():
    package_source_folder_path = pathlib.Path(__file__).parent.parent.parent / "src"
    markdown_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_markdown"
    pydantic_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_pydantic"

    default_recipe_count = len(como_recipes.default_recipe_registry.get_all_recipe_names())
    markdown_recipe_count = len(list(markdown_recipe_folder_path.iterdir()))
    pydantic_recipe_count = len(
        {file_path.stem for file_path in pydantic_recipe_folder_path.iterdir()} - {"__init__", "__pycache__"},
    )

    assert markdown_recipe_count == default_recipe_count
    assert pydantic_recipe_count == default_recipe_count
