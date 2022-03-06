"""Collection of help functions."""
import jsonschema
import json
from pathlib import Path
from typing import Union
from dataclasses import dataclass

FilePathType = Union[str, Path]


@dataclass
class Recipe:
    """Machine-readable format for recipes."""

    amount: float
    ingredients: list
    instructions: str


def load_recipe(recipe_path: FilePathType):
    """Load recipe from markdown (.md) format."""
    recipe = 1
    with open(file=Path(__file__).parent / "recipe_schema.json", mode="r") as fp:
        schema = json.load(fp=fp)
    jsonschema.validate(instance=recipe, schema=schema)
