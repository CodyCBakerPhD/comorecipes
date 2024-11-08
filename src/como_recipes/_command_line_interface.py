"""Command line interface for como_recipes."""

import pathlib
import click
import importlib

from ._base_recipe import Recipe
from ._recipe_registration import default_recipe_registry
from ._measurement_registration import MeasurementRegistry


@click.command(name="write_missing_markdown_recipes")
@click.option("--limit", type=int, default=None, help="Limit the number of recipes to write.")
def _write_missing_markdown_recipes(*, limit: int | None = None) -> None:  # pragma: no cover
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
def _write_missing_pydantic_recipes(*, limit: int | None = None) -> None:  # pragma: no cover
    """
    Write missing Pydantic (.py) recipes from Markdown (.md) recipe files.

    Please note that custom ingredient model files will not be generated; consider adding this manually over time.
    """
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


@click.command(name="select_recipes")
def _select_recipes() -> None:
    """Interactively select available recipes and generate a shopping list for them."""
    recipe_selection = MeasurementRegistry()

    default_recipe_integer_map: dict[int, str] = {
        selection_value: recipe_name
        for selection_value, recipe_name in enumerate(default_recipe_registry.get_all_recipe_names())
    }
    default_recipe_full_name_map: dict[str, bool] = {
        recipe_name: True for recipe_name in default_recipe_registry.get_all_recipe_names()
    }

    start_message = (
        "\n\nWelcome to the CoMo Recipes Meal Selection Interface!\n\n"
        "To exit, enter 'q'.\n"
        "To see all available recipes and their identifiers (IDs), enter 'l'.\n"
        "To add a recipe to the selection, enter the corresponding ID or type its full name.\n"
        "To remove a recipe from the selection, enter 'r' followed by the ID or its full name.\n"
        "To see the list of currently selected recipes, enter 'c'.\n"
        "To see this command-line options menu again, enter 'm'.\n\n"
    )
    click.echo(message=start_message)

    unrecognized_input_message = (
        "Input for '{input_value}' is not recognized. Please try again.\n"
        "To see the command-line options menu, enter 'm'\n"
    )

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        input_value = click.prompt(text="", prompt_suffix="", type=str)

        match input_value:
            case "q":
                break
            case "m":
                click.echo(message=start_message)
            case "l":
                click.echo(message="\nAvailable recipes:\n")
                message = ""
                for input_value, recipe_name in default_recipe_integer_map.items():
                    message += f"{input_value}) {recipe_name}\n"
                message += "\n\n"
                click.echo(message=message)
            case "c":
                click.echo(message=f"\nCurrently selected recipes:\n{recipe_selection.get_all_recipe_names()}")
            case "a":
                input_value = click.prompt(text="Recipe to add: ", prompt_suffix="", type=str)
                if input_value.isdigit():
                    recipe_name = default_recipe_integer_map[int(input_value)]
                elif default_recipe_full_name_map.get(input_value, False) is True:
                    recipe_name = input_value
                else:
                    click.echo(message=unrecognized_input_message)
                    continue

                recipe_selection.add_recipe(recipe=default_recipe_registry.get_recipe(recipe_name=recipe_name))
                click.echo(message=f"\nRecipe '{recipe_name}' added to the list.\n")
            case "r":
                input_value = click.prompt(text="Recipe to add: ", prompt_suffix="", type=str)
                if input_value.isdigit():
                    recipe_name = default_recipe_integer_map[int(input_value)]
                elif default_recipe_full_name_map.get(input_value, False) is True:
                    recipe_name = input_value
                else:
                    click.echo(message=unrecognized_input_message)
                    continue

                pass  # TODO: Implement recipe removal
            case _:
                click.echo(message=unrecognized_input_message)

        iteration += 1

    return None
