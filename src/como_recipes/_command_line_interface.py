"""Command line interface for como_recipes."""

import importlib
import importlib.metadata
import pathlib

import click
import natsort

from ._registration._recipe_registry import default_recipe_registry
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


@click.command(name="generate_html_recipes")
def _generate_html_recipes() -> None:
    docs_base_directory = pathlib.Path(__file__).parent.parent.parent / "docs"

    if not docs_base_directory.exists():
        message = f"\nDirectory does not exist: {docs_base_directory}\n\nAre you sure you are running this in dev mode?"

        raise ValueError(message)

    relative_path_to_recipe_name = {}
    for recipe_name in natsort.natsorted(seq=default_recipe_registry.get_all_recipe_names()):
        recipe = default_recipe_registry.get_recipe(recipe_name=recipe_name)

        # file_stem = recipe.snake_case_name
        file_stem = recipe.name.lower().replace(" ", "_")
        relative_path = f"formatted_recipes/{file_stem}.html"
        relative_path_to_recipe_name[relative_path] = recipe_name
        recipe_file_path = docs_base_directory / relative_path

        recipe.to_html_file(file_path=recipe_file_path)

    index_lines = [
        "<!DOCTYPE html>\n",
        '<html lang="en">\n',
        "<head>\n",
        '    <meta charset="UTF-8">\n',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        "    <title>Recipe Index</title>\n",
        "</head>\n",
        "<body>\n",
        "    <h1>Recipe Index</h1>\n",
        "    <ul>\n",
    ]
    for relative_path, recipe_name in relative_path_to_recipe_name.items():
        index_lines.append(f'        <li><a href="{relative_path}">{recipe_name}</a></li>\n')
    index_lines += [
        "    </ul>\n",
        "</body>\n",
        "</html>\n",
    ]

    index_file_path = docs_base_directory / "index.html"
    with index_file_path.open(mode="w") as io:
        io.writelines(index_lines)
