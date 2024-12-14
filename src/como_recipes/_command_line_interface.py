"""Command line interface for como_recipes."""

import importlib
import importlib.metadata
import pathlib

import click

from .utils import get_executable_stem, get_package_version


@click.command(name="write_missing_markdown_recipes")
@click.option("--limit", type=int, default=None, help="Limit the number of recipes to write.")
def _write_missing_markdown_recipes(*, limit: int | None = None) -> None:  # pragma: no cover
    """Write missing Markdown (.md) recipes from Pydantic (.py) recipe files."""
    if importlib.util.find_spec(name="como_recipes") is None:
        message = "The 'como_recipes' module is not installed."
        raise ImportError(message)
    como_recipes_module = importlib.import_module(name="como_recipes")
    default_recipes = como_recipes_module.default_recipe_registry

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

        camel_case_name = " ".join(word.capitalize() for word in markdown_recipe_file_path.stem.split("_"))
        recipe = default_recipes.get_recipe(recipe_name=camel_case_name)

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


@click.command(name="como_recipes_version")
def _version() -> None:
    message = get_package_version()

    click.echo(message=message)


@click.command(name="como_recipes_executable_stem")
def _executable_stem() -> None:
    message = get_executable_stem()

    click.echo(message=message)
