"""Command line interface wrapper around the PumpProbe conversion function."""

import click
import pydantic

from ._base import Recipe


@click.command(name="write_missing_markdown_recipes")
@click.option(
    "--pydantic_recipes_folder_path",
    help="The base folder path containing the Pydantic (.py) recipe files.",
    required=True,
    type=click.Path(writable=False),
)
def _write_missing_markdown_recipes(
    *,
    pydantic_recipes_folder_path: pydantic.DirectoryPath,
) -> None:
    """Write missing Markdown recipes from Pydantic recipe files."""
    current_pydantic_recipe_file_paths = set(pydantic_recipes_folder_path.glob("*.py")) - {"__init__.py"}

    for pydantic_recipe_file_path in current_pydantic_recipe_file_paths:
        markdown_file_name = pydantic_recipe_file_path.name.removeprefix("_").replace(".py", ".md")
        markdown_recipe_file_path = pydantic_recipe_file_path.parent.parent / "recipes" / markdown_file_name

        if not markdown_recipe_file_path.exists():
            recipe = Recipe.from_pydantic_file(pydantic_recipe_file_path)
            recipe.to_markdown_file(markdown_recipe_file_path)
