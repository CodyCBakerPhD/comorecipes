"""Command line interface for como_recipes."""

import pathlib
import click
import pydantic
import importlib

from ._base import Recipe


@click.command(name="write_missing_markdown_recipes")
@click.option("--limit", type=int, default=None, help="Limit the number of recipes to write.")
@pydantic.validate_call
def _write_missing_markdown_recipes(*, limit: int | None = None) -> None:
    """Write missing Markdown (.md) recipes from Pydantic (.py) recipe files."""
    if importlib.util.find_spec(name="como_recipes") is None:
        raise ImportError("The 'como_recipes' module is not installed.")
    como_recipes_module = importlib.import_module(name="como_recipes")

    pydantic_recipes_folder_path = pathlib.Path(__file__).parent / "_recipes" / "_pydantic"
    current_pydantic_recipe_file_paths = tuple(
        file_path for file_path in pydantic_recipes_folder_path.glob("*.py") if file_path.stem != "__init__"
    )

    count = 0
    for pydantic_recipe_file_path in current_pydantic_recipe_file_paths:
        if limit is not None and count >= limit:
            break

        markdown_file_name = pydantic_recipe_file_path.name.removeprefix("_").replace(".py", ".md")
        markdown_recipe_file_path = pydantic_recipe_file_path.parent.parent / "_markdown" / markdown_file_name

        camel_case_name = "".join(word.capitalize() for word in markdown_recipe_file_path.stem.split("_"))
        recipe = getattr(como_recipes_module.recipes, camel_case_name, None)

        if recipe is None:
            message = (
                f"Pydantic recipe file path exists at '{pydantic_recipe_file_path}' "
                f"but the import of the class '{camel_case_name}' was not successful."
            )
            raise ValueError(message)

        if not markdown_recipe_file_path.exists():
            count += 1
            recipe.to_markdown_file(file_path=markdown_recipe_file_path)

    if count == 0:
        print("\nNo missing Markdown recipe files were found.\n")

    return None


@click.command(name="write_missing_pydantic_recipes")
@click.option("--limit", type=int, default=None, help="Limit the number of recipes to write.")
@pydantic.validate_call
def _write_missing_pydantic_recipes(*, limit: int | None = None) -> None:
    """Write missing Pydantic (.py) recipes from Markdown (.md) recipe files."""
    markdown_recipes_folder_path = pathlib.Path(__file__).parent / "_recipes" / "_markdown"
    current_markdown_recipe_file_paths = tuple(markdown_recipes_folder_path.glob("*.md"))

    count = 0
    for markdown_recipe_file_path in current_markdown_recipe_file_paths:
        if limit is not None and count >= limit:
            break

        pydantic_file_name = "_" + markdown_recipe_file_path.name.replace(".md", ".py")
        pydantic_recipe_file_path = markdown_recipe_file_path.parent.parent / "_pydantic" / pydantic_file_name

        if not pydantic_recipe_file_path.exists():
            count += 1
            recipe = Recipe.from_markdown_file(file_path=markdown_recipe_file_path)
            recipe.to_pydantic_file(file_path=pydantic_recipe_file_path)

    if count == 0:
        print("\nNo missing Pydantic recipe files were found.\n")

    return None
