"""Command line interface for como_recipes."""

import pathlib
import shutil

import click
import natsort

from ._registration._recipe_registry import default_recipe_registry
from .utils import get_executable_stem, get_package_version, print_base_environment_variable


@click.command(name="como_recipes_version")
def _version() -> None:
    message = get_package_version()

    click.echo(message=message)


@click.command(name="como_recipes_executable_stem")
def _executable_stem() -> None:
    message = get_executable_stem()

    click.echo(message=message)


@click.command(name="como_recipes_set_base_environment_variable")
def _print_base_environment_variable() -> str:
    print_base_environment_variable()


@click.command(name="generate_html_recipes")
def _generate_html_recipes() -> None:
    docs_base_directory = pathlib.Path(__file__).parent.parent.parent / "docs"

    if not docs_base_directory.exists():
        message = f"\nDirectory does not exist: {docs_base_directory}\n\nAre you sure you are running this in dev mode?"

        raise ValueError(message)

    formatted_recipes_directory = docs_base_directory / "formatted_recipes"
    if formatted_recipes_directory.exists():
        shutil.rmtree(path=formatted_recipes_directory, ignore_errors=True)
    formatted_recipes_directory.mkdir(exist_ok=True)

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
