from typing import Literal, Self

import pydantic

from .utils import rational_string_to_float


class Ingredient(pydantic.BaseModel):
    name: str

    def default_package_size(self) -> str:
        raise NotImplementedError("The default size of packages containing this ingredient is not specified.")


class MeasuredIngredient(Ingredient):
    amount: int | float
    unit: Literal["cup", "tbsp", "tsp", "oz", "lb", "g", "kg"]  # TODO: limit to grams-base only


class Recipe(pydantic.BaseModel):
    """
    Automatically validated base data class for all recipes.

    Parameters
    ----------
    name : str
        Name of the recipe.
    ingredients : list[MeasuredIngredient]
        List of ingredients.
    instructions : list[str]
        List of instructions.
    notes : list[str] or None, optional
        List of notes.
    """

    name: str
    ingredients: list[MeasuredIngredient]
    instructions: list[str]
    notes: list[str] | None = None

    def to_pydantic_file(self, file_path: pydantic.FilePath) -> None:
        """Save recipe to a .py file in Pydantic format."""
        raise NotImplementedError("Saving recipes to files is not yet implemented.")

    def to_markdown_file(self, file_path: pydantic.FilePath) -> None:
        """Save recipe to a .md file in Markdown format."""
        raise NotImplementedError("Saving recipes to files is not yet implemented.")

    @classmethod
    def from_markdown_file(cls, file_path: pydantic.FilePath, include_instructions: bool = True) -> Self:
        """Load recipe from a .md file in Markdown format."""
        lines = list()
        with open(file=file_path) as file:
            for line in file:
                parsed_line = line.rstrip()
                if parsed_line != "":
                    lines.append(parsed_line)

        assert lines[0][:2] == "# ", "Markdown recipe does not begin with '# '."
        assert lines[1] == "## Ingredients", "Markdown recipe does not have a section titled '## Ingredients'."

        recipe_name_and_cuisine_line = lines[0][2:]
        if "(" in recipe_name_and_cuisine_line:
            recipe_name, cuisine = recipe_name_and_cuisine_line.split("(")
            cuisine = cuisine.rstrip(")")
        else:
            recipe_name = recipe_name_and_cuisine_line
            cuisine = None
        recipe_name = recipe_name.rstrip(" ")

        instruction_line = lines.index("## Instructions")

        ingredients = []
        for line in lines[2:instruction_line]:
            ingredient_line = line.split(" ")
            amount = rational_string_to_float(ingredient_line[0])
            unit = ingredient_line[1]
            name = " ".join(ingredient_line[2:])
            ingredients.append(MeasuredIngredient(amount=amount, unit=unit, name=name))

        # Not necessary for planning tools
        instructions = "".join(lines[instruction_line + 1 :]) if include_instructions is True else None

        return Recipe(name=recipe_name, cuisine=cuisine, ingredients=ingredients, instructions=instructions)
