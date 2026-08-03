"""Command line interface for como_recipes."""

import collections
import hashlib
import html
import pathlib
import shutil

import click
import natsort
import yaml

from ._base._base_recipe import _GITHUB_LINK_HTML, _THEME_TOGGLE_HTML, Recipe
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

    # Shared static assets (stylesheet, theme script, favicon, and logo) for GitHub pages
    package_assets_directory = pathlib.Path(__file__).parent / "_assets"
    site_assets_directory = docs_base_directory / "assets"
    site_assets_directory.mkdir(exist_ok=True)
    shutil.copyfile(src=package_assets_directory / "recipe_page_style.css", dst=site_assets_directory / "style.css")
    shutil.copyfile(src=package_assets_directory / "theme.js", dst=site_assets_directory / "theme.js")
    shutil.copyfile(src=package_assets_directory / "como_icon.ico", dst=site_assets_directory / "como_icon.ico")
    shutil.copyfile(src=package_assets_directory / "full_como_icon.jpg", dst=site_assets_directory / "como_logo.jpg")

    # All formatted HTML recipes for GitHub pages
    formatted_recipes_directory = docs_base_directory / "formatted_recipes"
    if formatted_recipes_directory.exists():
        shutil.rmtree(path=formatted_recipes_directory, ignore_errors=True)
    formatted_recipes_directory.mkdir(exist_ok=True)

    recipes_directory = docs_base_directory / "recipes"
    recipe_file_paths = natsort.natsorted(seq=recipes_directory.glob(pattern="*.yaml"))
    file_stem_to_recipe = {
        recipe_file_path.stem: Recipe.from_yaml_file(file_path=recipe_file_path)
        for recipe_file_path in recipe_file_paths
    }

    # Hues are spread evenly over the alphabetized tag universe so every tag chip gets a distinct color
    all_tags = sorted({tag for recipe in file_stem_to_recipe.values() for tag in (recipe.tags or ())})
    total_tag_count = len(all_tags)
    tag_to_hue = {tag: index * 360 // total_tag_count for index, tag in enumerate(all_tags)}

    alphabetized_relative_path_to_recipe: dict[str, dict[str, Recipe]] = collections.defaultdict(dict)
    for file_stem, recipe in file_stem_to_recipe.items():
        starting_letter = recipe.name[0].upper()

        relative_html_path = f"formatted_recipes/{file_stem}.html"
        alphabetized_relative_path_to_recipe[starting_letter][relative_html_path] = recipe
        recipe_html_file_path = docs_base_directory / relative_html_path

        recipe.to_html_file(file_path=recipe_html_file_path, tag_to_hue=tag_to_hue)

    # Index file for GitHub pages
    total_recipe_count = sum(
        len(relative_path_to_recipe) for relative_path_to_recipe in alphabetized_relative_path_to_recipe.values()
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
        '    <script src="assets/theme.js"></script>',
        "</head>",
        '<body class="index-page">',
        '    <nav class="top-bar">',
        '        <div class="top-actions">',
        f"            {_THEME_TOGGLE_HTML}",
        f"            {_GITHUB_LINK_HTML}",
        "        </div>",
        "    </nav>",
        '    <header class="site-header">',
        '        <img class="site-logo" src="assets/como_logo.jpg" alt="CoMo logo">',
        "        <h1>CoMo Recipes</h1>",
        f'        <p class="tagline">Our household cookbook &middot; {total_recipe_count} recipes</p>',
        '        <div class="search-bar">',
        f"            {search_input_html}",
        "        </div>",
        '        <div class="tag-filter">',
    ]
    for tag in all_tags:
        tag_hue = tag_to_hue[tag]
        escaped_tag = html.escape(tag)
        tag_button = f'<button class="tag" type="button" style="--tag-hue: {tag_hue}" data-tag="{escaped_tag}">'
        index_lines += [f"            {tag_button}{escaped_tag}</button>"]
    index_lines += [
        "        </div>",
        "    </header>",
        '    <nav class="letter-nav">',
    ]
    index_lines += [
        f'        <a href="#letter-{starting_letter}">{starting_letter}</a>'
        for starting_letter in alphabetized_relative_path_to_recipe
    ]
    index_lines += [
        "    </nav>",
        '    <main class="index-grid">',
    ]
    for starting_letter, relative_path_to_recipe in alphabetized_relative_path_to_recipe.items():
        index_lines += [
            f'        <section class="letter-section" id="letter-{starting_letter}">',
            f"            <h2>{starting_letter}</h2>",
            "            <ul>",
        ]
        for relative_path, recipe in relative_path_to_recipe.items():
            escaped_tags = html.escape(",".join(recipe.tags or ()))
            recipe_link = f'<a href="{relative_path}">{html.escape(recipe.name)}</a>'
            index_lines += [f'                <li data-tags="{escaped_tags}">{recipe_link}</li>']
        index_lines += [
            "            </ul>",
            "        </section>",
        ]
    index_lines += [
        "    </main>",
        '    <p class="no-results" hidden>No recipes match your search.</p>',
        "    <script>",
        "        const searchInput = document.getElementById('recipe-search');",
        "        const letterNav = document.querySelector('.letter-nav');",
        "        const noResults = document.querySelector('.no-results');",
        "        const sections = Array.from(document.querySelectorAll('.letter-section'));",
        "        const tagButtons = Array.from(document.querySelectorAll('.tag-filter .tag'));",
        "        const selectedTags = new Set();",
        "        const applyFilters = () => {",
        "            const query = searchInput.value.trim().toLowerCase();",
        "            let anyMatches = false;",
        "            for (const section of sections) {",
        "                let sectionMatches = false;",
        "                for (const item of section.querySelectorAll('li')) {",
        "                    const itemTags = (item.dataset.tags || '').split(',');",
        "                    const matchesQuery = item.textContent.toLowerCase().includes(query);",
        "                    const matchesTags = [...selectedTags].every((tag) => itemTags.includes(tag));",
        "                    const matches = matchesQuery && matchesTags;",
        "                    item.hidden = !matches;",
        "                    sectionMatches = sectionMatches || matches;",
        "                }",
        "                section.hidden = !sectionMatches;",
        "                anyMatches = anyMatches || sectionMatches;",
        "            }",
        "            letterNav.hidden = query !== '' || selectedTags.size > 0;",
        "            noResults.hidden = anyMatches;",
        "        };",
        "        searchInput.addEventListener('input', applyFilters);",
        "        for (const button of tagButtons) {",
        "            button.addEventListener('click', () => {",
        "                const tag = button.dataset.tag;",
        "                if (selectedTags.has(tag)) {",
        "                    selectedTags.delete(tag);",
        "                } else {",
        "                    selectedTags.add(tag);",
        "                }",
        "                button.classList.toggle('selected');",
        "                applyFilters();",
        "            });",
        "        }",
        "        for (const tag of new URLSearchParams(location.search).getAll('tag')) {",
        "            const button = tagButtons.find((candidate) => candidate.dataset.tag === tag);",
        "            if (button != null) {",
        "                selectedTags.add(tag);",
        "                button.classList.add('selected');",
        "            }",
        "        }",
        "        if (selectedTags.size > 0) {",
        "            applyFilters();",
        "        }",
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
