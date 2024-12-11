"""Command line interface for como_recipes."""

import collections
import datetime
import importlib
import importlib.metadata
import math
import os
import pathlib
import platform
import traceback

import click

from ._base._base_recipe import Recipe
from ._meal_selection import MealSelection
from ._registration._recipe_registry import default_recipe_registry
from .app import CoMoApp
from .utils import get_package_version, get_terminal_size


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


@click.command(name="como_recipes")
@click.version_option(
    version=get_package_version(),
    message="%(version)s",
)
def _como_recipes_command_line_interface_main_entrypoint() -> None:
    """Entry point for the interactive CoMo Recipes command-line interface."""
    click.clear()

    menu_message = "\n\nWelcome to CoMo Recipes!\n\n"
    menu_message += click.style(text=" Quit (q) ", fg="black", bg="bright_red")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Refresh (rf) ", fg="black", bg="white")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Launch Interactive Meal Selector (ms) ", fg="black", bg="bright_yellow")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Launch Meal Selector App (app) ", fg="black", bg="green")
    menu_message += click.style(text="\n\n", fg="black", bg="black")
    menu_message += click.style(text="What would you like to do?: ", fg="bright_blue", bg="black")

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        click.clear()
        input_value = click.prompt(text=menu_message, prompt_suffix="", type=str)

        match input_value:
            case "q":
                break
            case "rf":
                click.clear()
            case "ms":
                _meal_selector()
            case "app":
                app = CoMoApp()
                app.mainloop()

        iteration += 1

    if iteration >= max_iterations:
        error_message = click.style(text="\n\nExiting CoMo Recipes: maximum allowed operations reached.\n", fg="red")
        click.echo(message=error_message, err=True)


def _format_available_recipes(id_to_default_recipe_name_map: dict[int, str]) -> str:
    message = "\nAvailable Recipes\n"
    message += f"{'-' * (len(message) - 2)}\n\n"

    max_recipe_name_length = max(len(recipe_name) for recipe_name in default_recipe_registry.get_all_recipe_names())

    console_width, _ = get_terminal_size()
    number_of_recipes = len(id_to_default_recipe_name_map)
    number_of_columns = console_width // max_recipe_name_length
    number_of_rows = math.ceil(number_of_recipes / number_of_columns)

    recipe_table = collections.defaultdict(dict)
    for recipe_id, recipe_name in id_to_default_recipe_name_map.items():
        item = f"{recipe_name} ({recipe_id})"
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

    return message


def _format_recipe_selection(
    recipe_selection: MealSelection,
    default_recipe_name_to_id_map: dict[str, int],
) -> str:
    message = "\nCurrently Selected Recipes\n"
    message += f"{'-' * (len(message) - 2)}\n\n"

    # TODO: figure out how to render tabular
    for recipe_name in recipe_selection.get_all_recipe_names():
        recipe_id = default_recipe_name_to_id_map[recipe_name]
        message += click.style(text=f" {recipe_name} ({recipe_id}) ", fg="black", bg="bright_magenta") + "x1  "

    message += "\n\n"

    return message


def _get_shopping_list_file_path() -> pathlib.Path:
    home_folder = pathlib.Path.home() / ".como_recipes"
    home_folder.mkdir(exist_ok=True)

    shopping_list_folder_path = home_folder / "shopping_lists"
    shopping_list_folder_path.mkdir(exist_ok=True)

    date = datetime.datetime.now().strftime("%Y%m%d")
    shopping_list_file_path = shopping_list_folder_path / f"shopping_list_{date}.txt"

    counter = 0
    while shopping_list_file_path.exists():
        shopping_list_file_path = home_folder / f"shopping_list_{date}_{counter}.txt"
        counter += 1

    return shopping_list_file_path


def _get_error_file_path() -> pathlib.Path:
    home_folder = pathlib.Path.home() / ".como_recipes"
    home_folder.mkdir(exist_ok=True)

    error_folder_path = home_folder / "logs"
    error_folder_path.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    error_file_path = error_folder_path / f"error_{timestamp}.txt"

    return error_file_path


def _write_error(exception: Exception) -> None:
    issue_url = (
        "https://github.com/CodyCBakerPhD/como_recipes/issues/"
        "new?assignees=&labels=category%3A+bug&projects=&template=bug_report.yml&title=%5BBug%5D%3A+"
    )

    error_file_path = _get_error_file_path()
    with error_file_path.open(mode="a") as io:
        io.write(f"{type(exception)}: {exception!s}\n\n{traceback.format_exc()}")

    message = click.style(text=f"\n\nAn error occurred: {exception}\n\n", fg="red")
    message += click.style(text="Log file has been dumped to:\n", fg="bright_red")
    message += click.style(text=f"    {error_file_path}\n\n", fg="yellow")

    message += click.style(
        text="Please copy and paste the file contents to the issue tracker on GitHub:\n",
        fg="bright_red",
    )
    message += click.style(text=f"    {issue_url}\n", fg="yellow")

    # Print error message to console
    click.echo(message=message, err=True)

    # Automatically open the file, its folder, and the issue ticket webpage
    filename = str(error_file_path.absolute())
    click.edit(filename=filename, require_save=False)
    click.launch(url=filename, locate=True)
    click.launch(url=issue_url)


def _meal_selector() -> None:
    """Interactively select available recipes and generate a shopping list for them."""
    os.system("cls" if platform.system() == "Windows" else "clear")
    click.clear()

    recipe_selection = MealSelection()

    id_to_default_recipe_name_map: dict[int, str] = dict(enumerate(default_recipe_registry.get_all_recipe_names()))
    default_recipe_name_to_id_map: dict[str, int] = {value: key for key, value in id_to_default_recipe_name_map.items()}

    menu_message = click.style(text=" Quit (q) ", fg="black", bg="bright_red")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Refresh (rf) ", fg="black", bg="white")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Remove recipe from selection (rm) ", fg="black", bg="bright_yellow")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Clear all recipes (cl) ", fg="black", bg="yellow")
    menu_message += click.style(text=" ", fg="black", bg="black")
    menu_message += click.style(text=" Get shopping list (gsl) ", fg="black", bg="bright_green")
    menu_message += click.style(text="\n\n", fg="black", bg="black")
    menu_message += click.style(text="What would you like to do?: ", fg="bright_blue", bg="black")

    max_iterations = 1_000_000
    iteration = 0
    while iteration < max_iterations:
        try:
            os.system("cls" if platform.system() == "Windows" else "clear")
            click.clear()

            formatted_available_recipes = _format_available_recipes(
                id_to_default_recipe_name_map=id_to_default_recipe_name_map,
            )
            prompt_message = click.style(text=formatted_available_recipes, fg="black", bg="bright_cyan")
            formatted_current_recipes = _format_recipe_selection(
                recipe_selection=recipe_selection,
                default_recipe_name_to_id_map=default_recipe_name_to_id_map,
            )
            prompt_message += "\n\n" + click.style(text=formatted_current_recipes, fg="black", bg="bright_magenta")
            prompt_message += "\n\n" + menu_message
            input_value = click.prompt(text=prompt_message, prompt_suffix="", type=str)

            match input_value:
                case "q":
                    break
                case "rf":
                    click.clear()
                case "rm":
                    input_value = click.prompt(text="ID of recipe to remove: ", prompt_suffix="", type=str)
                    if not input_value.isdigit():
                        continue

                    recipe_name = id_to_default_recipe_name_map[int(input_value)]
                    recipe_selection.remove_recipe(recipe_name=recipe_name)
                case "cl":
                    recipe_selection = MealSelection()
                case "gsl" | "get shopping list":
                    shopping_list_file_path = _get_shopping_list_file_path()

                    # TODO: remove when grams are standardized
                    try:
                        message = "\nShopping List\n"
                        message += f"{'-' * (len(message) - 2)}\n\n"

                        message += recipe_selection.get_shopping_list()
                        click.echo(message=message)

                        if (
                            click.prompt(text="Would you like to save this shopping list to a file? (y/n): ", type=str)
                            != "y"
                        ):
                            continue

                        with shopping_list_file_path.open(mode="w") as io:
                            io.write(message)
                        click.edit(filename=str(shopping_list_file_path.absolute()), require_save=False)
                    except Exception as exception:
                        message = click.style(
                            text=(
                                "\n\nMy apologies, shopping list generation is error-prone until all units are "
                                "standardized to grams.\n\n"
                                f"Error: {exception}\n\n"
                            ),
                            fg="bright_red",
                        )
                        click.echo(message=message)

                        message = click.style(
                            text="Defaulting to printing all ingredients instead.\n\n",
                            fg="yellow",
                        )
                        click.echo(message=message)

                        message = str(recipe_selection) + "\n\n"
                        click.echo(message=message)

                        if (
                            click.prompt(text="Would you like to save this shopping list to a file? (y/n): ", type=str)
                            != "y"
                        ):
                            continue

                        with shopping_list_file_path.open(mode="w") as io:
                            io.write(message)
                        click.edit(filename=str(shopping_list_file_path.absolute()), require_save=False)
                case input_value if input_value.isdigit():
                    if id_to_default_recipe_name_map.get(int(input_value), False) is False:
                        click.echo(
                            message=click.style(
                                text=f"ID '{input_value}' not found in the available recipes. Please enter a valid ID.",
                                fg="red",
                            ),
                        )
                        continue

                    recipe_name = id_to_default_recipe_name_map[int(input_value)]

                    recipe_selection.add_recipe(recipe=default_recipe_registry.get_recipe(recipe_name=recipe_name))
        except Exception as exception:
            _write_error(exception=exception)
            break

        iteration += 1

    if iteration >= max_iterations:
        error_message = click.style(
            text="\n\nExiting Interactive Meal Selector: maximum allowed operations reached.\n",
            fg="red",
        )
        click.echo(message=error_message, err=True)
