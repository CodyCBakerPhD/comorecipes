import pathlib

import como_recipes


def test_default_recipe_load_consistency():
    package_source_folder_path = pathlib.Path(__file__).parent.parent / "src"
    markdown_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_markdown"

    for markdown_recipe_file_path in markdown_recipe_folder_path.iterdir():
        markdown_recipe = como_recipes.Recipe.from_markdown_file(file_path=markdown_recipe_file_path)
        recipe_name = markdown_recipe.name

        pydantic_recipe = como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name)

        assert markdown_recipe == pydantic_recipe
