"""Command line interface for como_recipes."""

import pathlib
import click
import importlib
import datetime
import traceback
import math
import collections

from ._base_recipe import Recipe
from ._recipe_registration import default_recipe_registry
from ._measurement_registration import MeasurementRegistry
from .utils import get_terminal_size


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


def _unrecognized_input_message(input_value: str) -> str:
    """Return a standard unrecognized input message."""
    return (
        f"Input for '{input_value}' is not recognized. Please try again.\n"
        "To see the command-line options menu, enter 'sm' or 'start menu'.\n"
    )


@click.command(name="como_recipes")
def _como_recipes_command_line_interface_main_entrypoint() -> None:
    """Entry point for the interactive CoMo Recipes command-line interface."""
    click.clear()

    start_message = (
        "\n\nWelcome to CoMo Recipes!\n\n"
        "To exit, enter 'q' or 'quit'.\n"
        "To start a new meal selection session, enter 'ms' or 'meal selector'.\n"
    )
    click.echo(message=start_message)

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        input_value = click.prompt(text="What would you like to do?: ", prompt_suffix="", type=str)

        match input_value:
            case "q" | "quit":
                break
            case "ms" | "meal selector":
                _meal_selector()
                click.clear()
                click.echo(message=start_message)
            case "sm" | "start menu":
                click.echo(message=start_message)
            case _:
                click.echo(message=_unrecognized_input_message(input_value=input_value))

        iteration += 1

    if iteration >= max_iterations:
        click.echo(message="Exiting CoMo Recipes: maximum allowed operations reached.\n")

    return None


def _meal_selector() -> None:
    """Interactively select available recipes and generate a shopping list for them."""
    click.clear()

    home_folder = pathlib.Path.home() / ".como_recipes"
    home_folder.mkdir(exist_ok=True)
    date = datetime.datetime.now().strftime("%Y%m%d")
    shopping_list_file_path = home_folder / f"shopping_list_{date}.txt"
    counter = 0
    while shopping_list_file_path.exists():
        shopping_list_file_path = home_folder / f"shopping_list_{date}_{counter}.txt"
        counter += 1

    recipe_selection = MeasurementRegistry()

    id_to_default_recipe_name_map: dict[int, str] = {
        selection_value: recipe_name
        for selection_value, recipe_name in enumerate(default_recipe_registry.get_all_recipe_names())
    }
    default_recipe_name_to_id_map: dict[str, int] = {value: key for key, value in id_to_default_recipe_name_map.items()}

    start_message = (
        "\n\nWelcome to the CoMo Recipes Meal Selector!\n\n"
        "To exit, enter 'q' or 'quit'.\n"
        "To see all available recipes and their identifiers (IDs), enter 'lsa' or 'list available'.\n"
        "To see the list of current recipe selections, enter 'lsc' or 'list current selection'.\n"
        "To see the raw list of combined ingredients, enter 'lsi' or 'list all ingredients'.\n"
        "To add a recipe to the current selection, enter 'a' or 'add'.\n"
        "To remove a recipe from the current selection, enter 'r' or 'remove'.\n"
        "To get the shopping list for the current recipe selection, enter 'gsl' or 'get shopping list'.\n"
        "To see these start menu options again, enter 'sm' or 'start menu'.\n\n"
    )
    click.echo(message=start_message)

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        input_value = click.prompt(text="What would you like to do?: ", prompt_suffix="", type=str)

        try:
            match input_value:
                case "q" | "quit":
                    break
                case "clc" | "clear":
                    click.clear()
                case "lsa" | "list available":
                    message = "\nAvailable Recipes\n"
                    message += f"{'-' * (len(message)-2)}\n\n"

                    max_recipe_name_length = max(
                        len(recipe_name) for recipe_name in default_recipe_registry.get_all_recipe_names()
                    )

                    console_width, _ = get_terminal_size()
                    number_of_recipes = len(id_to_default_recipe_name_map)
                    number_of_columns = console_width // max_recipe_name_length
                    number_of_rows = math.ceil(number_of_recipes / number_of_columns)

                    recipe_table = collections.defaultdict(dict)
                    for recipe_id, recipe in id_to_default_recipe_name_map.items():
                        item = f"{id_to_default_recipe_name_map[recipe_id]} ({recipe_id})"
                        recipe_table[recipe_id % number_of_columns][recipe_id // number_of_columns] = item

                    buffers = tuple(
                        max(len(recipe_name) for recipe_name in recipe_table[column_index].values())
                        for column_index in range(number_of_columns - 1)
                    )

                    message += "\n".join(
                        " | ".join(
                            recipe_table.get(column_index, {}).get(row_index, "").ljust(buffer)
                            for column_index, buffer in enumerate(buffers)
                        )
                        for row_index in range(number_of_rows)
                    )
                    message += "\n\n"

                    click.echo(message=message)
                case "lsc" | "list current selection":
                    message = "\nCurrently Selected Recipes\n"
                    message += f"{'-' * (len(message) - 2)}\n\n"
                    for recipe_name in recipe_selection.get_all_recipe_names():
                        message += f"{recipe_name} ({default_recipe_name_to_id_map[recipe_name]})\n"
                    message += "\n\n"
                    click.echo(message=message)
                case "a" | "add":
                    input_value = click.prompt(text="Recipe ID or name to add: ", prompt_suffix="", type=str)
                    if input_value.isdigit():
                        recipe_name = id_to_default_recipe_name_map[int(input_value)]
                    elif default_recipe_name_to_id_map.get(input_value, False) is not False:
                        recipe_name = input_value
                    else:
                        click.echo(message=_unrecognized_input_message(input_value=input_value))
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
                        click.echo(message=_unrecognized_input_message(input_value=input_value))
                        continue

                    recipe_selection.remove_recipe(recipe_name=recipe_name)
                case "lsi" | "list all ingredients":
                    message = str(recipe_selection)
                    click.echo(message=message)

                    if (
                        click.prompt(text="Would you like to save this shopping list to a file? (y/n): ", type=str)
                        != "y"
                    ):
                        continue

                    with open(file=shopping_list_file_path, mode="w") as io:
                        io.write(message)
                    click.edit(filename=str(shopping_list_file_path.absolute()), require_save=False)
                case "gsl" | "get shopping list":
                    # TODO
                    message = click.style(
                        text=(
                            "\n\nMy apologies, shopping list generation is error-prone until all units are "
                            "standardized to grams.\n\n"
                            "Please print all ingredients using 'lsi' or 'list all ingredients' instead\n\n."
                        ),
                        fg="red",
                    )
                    click.echo(message=message)

                    message = "\nShopping List\n"
                    message += f"{'-' * (len(message) - 2)}\n\n"
                    message += recipe_selection.get_shopping_list()
                    click.echo(message=message)

                    if (
                        click.prompt(text="Would you like to save this shopping list to a file? (y/n): ", type=str)
                        != "y"
                    ):
                        continue

                    with open(file=shopping_list_file_path, mode="w") as io:
                        io.write(message)
                    click.edit(filename=str(shopping_list_file_path.absolute()), require_save=False)
                case "sm" | "menu":
                    click.echo(message=start_message)
                case _:
                    click.echo(message=_unrecognized_input_message(input_value=input_value))
        except Exception as exception:
            error_file_path = home_folder / f"error_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(file=error_file_path, mode="w") as io:
                io.write(f"{type(exception)}: {str(exception)}\n\n{traceback.format_exc()}")

            message = click.style(text=f"\n\nAn error occurred: {exception}\n\n", fg="red")
            message += click.style(text="Log file has been dumped to:\n", fg="bright_red")
            message += click.style(text=f"    {error_file_path}\n\n", fg="yellow")

            issue_url = "https://github.com/CodyCBakerPhD/como_recipes/issues/new/choose"
            message += click.style(
                text="Please copy and paste the file contents to the issue tracker on GitHub:\n", fg="bright_red"
            )
            message += click.style(text=f"    {issue_url}\n", fg="yellow")

            click.echo(message=message, err=True)
            click.edit(filename=str(error_file_path.absolute()), require_save=False)
            click.launch(url=issue_url)

        iteration += 1

    if iteration >= max_iterations:
        click.echo(message="Exiting the CoMo Recipes Meal Selection Interface: maximum allowed operations reached.\n")

    return None
