"""Command line interface for como_recipes."""

import collections
import hashlib
import pathlib
import shutil

import click
import natsort
import yaml

from ._registration._default_recipe_registry import default_recipe_registry
from .utils import get_base_environment_variable, get_executable_name, get_package_version


@click.command(name="como_recipes_version")
def _version() -> None:
    message = get_package_version()

    click.echo(message=message)


@click.command(name="como_recipes_executable_name")
def _get_executable_name() -> None:
    message = get_executable_name()

    click.echo(message=message)


@click.command(name="como_recipes_set_base_environment_variable")
def _print_base_environment_variable() -> str:
    base_path = get_base_environment_variable()

    click.echo(message=base_path)


@click.command(name="generate_html_recipes")
def _generate_html_recipes() -> None:
    docs_base_directory = pathlib.Path(__file__).parent.parent.parent / "docs"

    if not docs_base_directory.exists():
        message = f"\nDirectory does not exist: {docs_base_directory}\n\nAre you sure you are running this in dev mode?"

        raise ValueError(message)

    # All formatted HTML recipes for GitHub pages
    formatted_recipes_directory = docs_base_directory / "formatted_recipes"
    if formatted_recipes_directory.exists():
        shutil.rmtree(path=formatted_recipes_directory, ignore_errors=True)
    formatted_recipes_directory.mkdir(exist_ok=True)

    alphabetized_relative_path_to_recipe_name: dict[str, dict[str]] = collections.defaultdict(dict)
    recipe_names = default_recipe_registry.get_all_recipe_names()
    for recipe_name in natsort.natsorted(seq=recipe_names):
        starting_letter = recipe_name[0].upper()
        recipe = default_recipe_registry.get_recipe(recipe_name=recipe_name)

        file_stem = recipe.name.lower().replace(" ", "_")
        relative_path = f"formatted_recipes/{file_stem}.html"
        alphabetized_relative_path_to_recipe_name[starting_letter][relative_path] = recipe_name
        recipe_file_path = docs_base_directory / relative_path

        recipe.to_html_file(file_path=recipe_file_path)

    # Index file for GitHub pages
    index_lines = [
        "<!DOCTYPE html>\n",
        '<html lang="en">\n',
        "<head>\n",
        '    <meta charset="UTF-8">\n',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        "    <title>Recipe Index</title>\n",
        "    <style>\n",
        "        .grid-container {\n",
        "            display: grid;\n",
        "            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));\n",
        "            gap: 5px;\n",
        "        }\n",
        "        .section {\n",
        "            break-inside: avoid;\n",
        "        }\n",
        "    </style>\n",
        "</head>\n",
        "<body>\n",
        "    <h1>Recipe Index</h1>\n",
        '    <div class="grid-container">\n',
    ]
    for starting_letter, relative_path_to_recipe_name in alphabetized_relative_path_to_recipe_name.items():
        index_lines.append('        <div class="section">\n')
        index_lines.append(f"            <h2>{starting_letter}</h2>\n")
        index_lines.append("            <ul>\n")
        for relative_path, recipe_name in relative_path_to_recipe_name.items():
            index_lines.append(f'            <li><a href="{relative_path}">{recipe_name}</a></li>\n')
        index_lines.append("            </ul>\n")
        index_lines.append("        </div>\n\n")
    index_lines += [
        "    </div>\n",
        "</body>\n",
        "</html>\n",
    ]

    index_file_path = docs_base_directory / "index.html"
    with index_file_path.open(mode="w") as io:
        io.writelines(index_lines)

    # Hidden manifest files
    databases = ["recipe", "ingredient"]
    for database in databases:
        database_directory = docs_base_directory / f"{database}s"
        manifest = {
            file_path.stem: hashlib.md5(string=file_path.read_bytes()).hexdigest()  # noqa: S324
            for file_path in database_directory.glob(pattern="*.yaml")
        }

        manifest_file_path = docs_base_directory / f"{database}_manifest.yaml"
        with manifest_file_path.open(mode="w") as io:
            yaml.dump(data=manifest, stream=io)

        manifest_hash = hashlib.md5(string=manifest_file_path.read_bytes()).hexdigest()  # noqa: S324
        manifest_hash_file_path = docs_base_directory / f"{database}_manifest_hash.txt"
        with manifest_hash_file_path.open(mode="w") as io:
            io.write(f"{manifest_hash}\n")
