import pathlib

import como_recipes


def test_recipe_counts_consistency():
    package_source_folder_path = pathlib.Path(__file__).parent.parent.parent / "src"
    yaml_recipe_folder_path = package_source_folder_path / "como_recipes" / "_recipes" / "_yaml"

    default_recipe_count = len(como_recipes.default_recipe_registry.get_all_recipe_names())
    markdown_recipe_count = len(list(yaml_recipe_folder_path.iterdir()))

    assert markdown_recipe_count == default_recipe_count
