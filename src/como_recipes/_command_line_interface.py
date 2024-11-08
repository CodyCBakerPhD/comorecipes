"""Command line interface for como_recipes."""

import pathlib
import click
import importlib
import datetime

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
    home_folder = pathlib.Path.home() / ".como_recipes"
    home_folder.mkdir(exist_ok=True)
    session_file_path = home_folder / f"session_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
    counter = 0
    while session_file_path.exists():
        session_file_path = home_folder / f"session_{datetime.datetime.now().strftime('%Y%m%d')}_{counter}.txt"
        counter += 1

    recipe_selection = MeasurementRegistry()

    id_to_default_recipe_name_map: dict[int, str] = {
        selection_value: recipe_name
        for selection_value, recipe_name in enumerate(default_recipe_registry.get_all_recipe_names())
    }
    default_recipe_name_to_id_map: dict[str, int] = {value: key for key, value in id_to_default_recipe_name_map.items()}

    start_message = (
        "\n\nWelcome to the CoMo Recipes Meal Selection Interface!\n\n"
        "To exit, enter 'q' or 'quit'.\n"
        "To see all available recipes and their identifiers (IDs), enter 'lav' or 'list available'.\n"
        "To see the list of current recipe selections, enter 'lcs' or 'list current selection'.\n"
        "To add a recipe to the current selection, enter 'a' or 'add'.\n"
        "To remove a recipe from the current selection, enter 'r' or 'remove'.\n"
        "To get the shopping list for the current recipe selection, enter 'gsl' or 'get shopping list'.\n"
        "To see these start menu options again, enter 'sm' or 'start menu'.\n\n"
    )
    click.echo(message=start_message)

    input_value = ""
    unrecognized_input_message = (
        f"Input for '{input_value}' is not recognized. Please try again.\n"
        "To see the command-line options menu, enter 'sm' or 'start menu'.\n"
    )

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        input_value = click.prompt(text="What would you like to do?: ", prompt_suffix="", type=str)

        match input_value:
            case "q" | "quit":
                break
            case "m" | "menu":
                click.echo(message=start_message)
            case "lav" | "list available":
                click.echo(message="\nAvailable recipes:\n")
                message = ""
                for input_value, recipe_name in id_to_default_recipe_name_map.items():
                    message += f"{input_value}) {recipe_name}\n"
                message += "\n\n"
                click.echo(message=message)
            case "lsc" | "list current selection":
                recipe_names_with_ids = ""
                for recipe_name in recipe_selection.get_all_recipe_names():
                    recipe_names_with_ids += f"{recipe_name} ({default_recipe_name_to_id_map[recipe_name]})\n"
                click.echo(message=f"\nCurrently selected recipes: \n{recipe_names_with_ids}\n\n")
            case "a" | "add":
                input_value = click.prompt(text="Recipe ID or name to add: ", prompt_suffix="", type=str)
                if input_value.isdigit():
                    recipe_name = id_to_default_recipe_name_map[int(input_value)]
                elif default_recipe_name_to_id_map.get(input_value, False) is not False:
                    recipe_name = input_value
                else:
                    click.echo(message=unrecognized_input_message)
                    continue

                recipe_selection.add_recipe(recipe=default_recipe_registry.get_recipe(recipe_name=recipe_name))
                click.echo(message=f"\nRecipe '{recipe_name}' added to the list.\n")
            case "r" | "remove":
                input_value = click.prompt(text="Recipe ID or name to remove: ", prompt_suffix="", type=str)
                if input_value.isdigit():
                    recipe_name = id_to_default_recipe_name_map[int(input_value)]
                elif default_recipe_name_to_id_map.get(input_value, False) is not False:
                    recipe_name = input_value
                else:
                    click.echo(message=unrecognized_input_message)
                    continue

                pass  # TODO: Implement recipe removal
            case "gsl" | "get shopping list":
                shopping_list = recipe_selection.get_shopping_list()
                click.echo(message=shopping_list)

                if click.prompt(text="Would you like to save this shopping list to a file? (y/n): ", type=str) != "y":
                    continue

                with open(file_path=session_file_path, mode="w") as io:
                    io.write(shopping_list)
                click.launch(url=session_file_path, locate=True)
            case _:
                click.echo(message=unrecognized_input_message)

        iteration += 1

    if iteration >= max_iterations:
        click.echo(message="Exiting the CoMo Recipes Meal Selection Interface: maximum allowed operations reached.\n")

    return None
