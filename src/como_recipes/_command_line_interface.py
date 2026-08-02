"""Command line interface for como_recipes."""

import collections
import hashlib
import html
import pathlib
import shutil

import click
import natsort
import yaml

from ._base._base_recipe import Recipe
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

    # Shared static assets (stylesheet and favicon) for GitHub pages
    package_assets_directory = pathlib.Path(__file__).parent / "_assets"
    site_assets_directory = docs_base_directory / "assets"
    site_assets_directory.mkdir(exist_ok=True)
    shutil.copyfile(src=package_assets_directory / "recipe_page_style.css", dst=site_assets_directory / "style.css")
    shutil.copyfile(src=package_assets_directory / "como_icon.ico", dst=site_assets_directory / "como_icon.ico")

    # All formatted HTML recipes for GitHub pages
    formatted_recipes_directory = docs_base_directory / "formatted_recipes"
    if formatted_recipes_directory.exists():
        shutil.rmtree(path=formatted_recipes_directory, ignore_errors=True)
    formatted_recipes_directory.mkdir(exist_ok=True)

    alphabetized_relative_path_to_recipe_name: dict[str, dict[str]] = collections.defaultdict(dict)
    recipes_directory = docs_base_directory / "recipes"
    recipe_file_paths = list(recipes_directory.glob(pattern="*.yaml"))
    for recipe_file_path in natsort.natsorted(seq=recipe_file_paths):
        recipe = Recipe.from_yaml_file(file_path=recipe_file_path)
        recipe_name = recipe.name
        starting_letter = recipe_name[0].upper()
        file_stem = recipe_file_path.stem

        relative_html_path = f"formatted_recipes/{file_stem}.html"
        alphabetized_relative_path_to_recipe_name[starting_letter][relative_html_path] = recipe_name
        recipe_html_file_path = docs_base_directory / relative_html_path

        recipe.to_html_file(file_path=recipe_html_file_path)

    # Index file for GitHub pages
    total_recipe_count = sum(
        len(relative_path_to_recipe_name)
        for relative_path_to_recipe_name in alphabetized_relative_path_to_recipe_name.values()
    )
    search_input_html = (
        '<input id="recipe-search" type="search" placeholder="Search recipes" aria-label="Search recipes">'
    )

    index_lines = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        "    <title>CoMo Recipes</title>",
        '    <link rel="icon" href="assets/como_icon.ico">',
        '    <link rel="stylesheet" href="assets/style.css">',
        "</head>",
        '<body class="index-page">',
        '    <header class="site-header">',
        "        <h1>CoMo Recipes</h1>",
        f'        <p class="tagline">Our household cookbook &middot; {total_recipe_count} recipes</p>',
        '        <div class="search-bar">',
        f"            {search_input_html}",
        "        </div>",
        "    </header>",
        '    <nav class="letter-nav">',
    ]
    index_lines += [
        f'        <a href="#letter-{starting_letter}">{starting_letter}</a>'
        for starting_letter in alphabetized_relative_path_to_recipe_name
    ]
    index_lines += [
        "    </nav>",
        '    <main class="index-grid">',
    ]
    for starting_letter, relative_path_to_recipe_name in alphabetized_relative_path_to_recipe_name.items():
        index_lines += [
            f'        <section class="letter-section" id="letter-{starting_letter}">',
            f"            <h2>{starting_letter}</h2>",
            "            <ul>",
        ]
        index_lines += [
            f'                <li><a href="{relative_path}">{html.escape(recipe_name)}</a></li>'
            for relative_path, recipe_name in relative_path_to_recipe_name.items()
        ]
        index_lines += [
            "            </ul>",
            "        </section>",
        ]
    index_lines += [
        "    </main>",
        '    <p class="no-results" hidden>No recipes match your search.</p>',
        '    <footer class="site-footer">',
        "        <p>CoMo Recipes</p>",
        "    </footer>",
        "    <script>",
        "        const searchInput = document.getElementById('recipe-search');",
        "        const letterNav = document.querySelector('.letter-nav');",
        "        const noResults = document.querySelector('.no-results');",
        "        const sections = Array.from(document.querySelectorAll('.letter-section'));",
        "        searchInput.addEventListener('input', () => {",
        "            const query = searchInput.value.trim().toLowerCase();",
        "            let anyMatches = false;",
        "            for (const section of sections) {",
        "                let sectionMatches = false;",
        "                for (const item of section.querySelectorAll('li')) {",
        "                    const matches = item.textContent.toLowerCase().includes(query);",
        "                    item.hidden = !matches;",
        "                    sectionMatches = sectionMatches || matches;",
        "                }",
        "                section.hidden = !sectionMatches;",
        "                anyMatches = anyMatches || sectionMatches;",
        "            }",
        "            letterNav.hidden = query !== '';",
        "            noResults.hidden = anyMatches;",
        "        });",
        "    </script>",
        "</body>",
        "</html>",
    ]

    index_file_path = docs_base_directory / "index.html"
    with index_file_path.open(mode="w") as io:
        io.write("\n".join(index_lines) + "\n")

    # Hidden manifest files
    databases = ["recipes", "ingredients"]
    for database in databases:
        database_directory = docs_base_directory / f"{database}"
        manifest = {
            file_path.stem: hashlib.md5(string=file_path.read_bytes()).hexdigest()  # noqa: S324
            for file_path in database_directory.glob(pattern="*.yaml")
        }

        manifest_file_path = docs_base_directory / "manifests" / f"{database}.yaml"
        with manifest_file_path.open(mode="w") as io:
            yaml.dump(data=manifest, stream=io)

        manifest_hash = hashlib.md5(string=manifest_file_path.read_bytes()).hexdigest()  # noqa: S324
        manifest_hash_file_path = docs_base_directory / "manifests" / f"{database}_hash.txt"
        with manifest_hash_file_path.open(mode="w") as io:
            io.write(f"{manifest_hash}\n")
