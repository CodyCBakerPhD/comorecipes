"""Collection of help functions."""
from pathlib import Path
from typing import Union, Optional, List
from dataclasses import dataclass

FilePathType = Union[str, Path]


@dataclass
class Ingredient:
    """Machine-readable format for a single ingredient in a recipe."""

    amount: float
    unit: float
    name: str


@dataclass
class Recipe:
    """Machine-readable format for recipes."""

    name: float
    ingredients: List[Ingredient]
    instructions: Optional[str] = None


def rational_string_to_float(string: str):
    """Small helper function to convert strings into floats ('1/4' becomes 0.25)."""
    if "/" in string:
        numerator, denominator = string.split("/")
        return int(numerator) / int(denominator)
    else:
        return float(string)


def load_recipe(file_path: FilePathType, include_instructions: bool = False):
    """Load recipe from markdown (.md) format."""
    with open(file=file_path, mode="r") as file:
        lines = file.readlines()
    recipe_name = lines[0][2:-1]
    instruction_line = lines.index("## Instructions\n")
    ingredients = []
    for line in lines[5 : instruction_line - 2]:
        if line != "\n":
            ingredient_line = line.split(" ")
            amount = rational_string_to_float(ingredient_line[0])
            unit = ingredient_line[1]
            name = ingredient_line[2:][-1][:-1]
            ingredients.append(Ingredient(amount=amount, unit=unit, name=name))

    # Not necessary for planning tools
    instructions = "".join(lines[instruction_line + 2 :]) if include_instructions else None

    return Recipe(name=recipe_name, ingredients=ingredients, instructions=instructions)
