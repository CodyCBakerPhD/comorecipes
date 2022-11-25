"""Collection of help functions."""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

FilePathType = Union[str, Path]


@dataclass
class Ingredient:
    """Machine-readable format for a single ingredient in a recipe."""

    name: str
    amount: float
    unit: float


@dataclass
class Recipe:
    """Machine-readable format for recipes."""

    name: str
    cuisine: Optional[str]
    ingredients: List[Ingredient]
    instructions: Optional[str] = None


def rational_string_to_float(string: str) -> float:
    """Small helper function to convert strings into floats ('1/4' becomes 0.25)."""
    if "/" in string:
        numerator, denominator = string.split("/")
        return int(numerator) / int(denominator)
    else:
        return float(string)


def load_recipe(file_path: FilePathType, include_instructions: bool = False) -> Recipe:
    """Load recipe from markdown (.md) format."""
    lines = list()
    with open(file=file_path) as file:
        for line in file:
            parsed_line = line.rstrip()
            if parsed_line != "":
                lines.append(parsed_line)

    assert lines[0][:2] == "# ", "Markdown recipe does not begin with '# '."
    assert lines[1] == "## Ingredients", "Markdown recipe does not have a section titled '## Ingredients'."

    recipe_name_and_cuisine_split = lines[0][2:].split("(")
    recipe_name = recipe_name_and_cuisine_split[0].rstrip(" ")
    recipe_cuisine = recipe_name_and_cuisine_split[1].rstrip(")") if len(recipe_name_and_cuisine_split) == 2 else None

    instruction_line = lines.index("## Instructions")

    ingredients = []
    for line in lines[2:instruction_line]:
        ingredient_line = line.split(" ")
        amount = rational_string_to_float(ingredient_line[0])
        unit = ingredient_line[1]
        name = " ".join(ingredient_line[2:])
        ingredients.append(Ingredient(amount=amount, unit=unit, name=name))

    # Not necessary for planning tools
    instructions = "".join(lines[instruction_line + 1 :]) if include_instructions else None

    return Recipe(name=recipe_name, cuisine=recipe_cuisine, ingredients=ingredients, instructions=instructions)
