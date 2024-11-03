from typing import Literal, Self

import pydantic

from .utils import rational_string_to_float


class Ingredient(pydantic.BaseModel):
    name: str
    grams_to_default_package_conversion: int | float | None = None
    default_package_unit: str | None = None

    def convert_amount_to_package_size(self, amount: int | float, unit: str) -> int | float:
        """Convert the amount of this ingredient to the default package size."""
        if self.grams_to_default_package_conversion is None or self.default_package_size is None:
            raise NotImplementedError(
                "The default size or conversion of packages containing this ingredient is not specified."
            )
        if unit != "g":
            raise NotImplementedError(
                "The conversion rule for an ingredient amount to the default size of a package is not specified."
            )

        return amount / self.default_package_size


class MeasuredIngredient(Ingredient):
    amount: int | float
    unit: Literal[
        "cup", "cups", "tbsp", "tsp", "oz", "lb", "g", "kg", "large", "tsp.", "tbsp."
    ]  # TODO: limit to grams-base only


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
        indent = " " * 4

        camel_case_name = "".join(word.capitalize() for word in self.name.split(" "))
        python_text = "from .._base import Recipe, MeasuredIngredient\n\n"
        python_text += f"class {camel_case_name}(Recipe):\n"
        python_text += f'{indent}name = "{self.name}"\n'

        python_text += f"{indent}ingredients = [\n"
        for ingredient in self.ingredients:
            ingredient_text = f'{indent}{indent}MeasuredIngredient(name="{ingredient.name}",'
            ingredient_text += f'amount={ingredient.amount}, unit="{ingredient.unit}"),'
            ingredient_text = f'unit="{ingredient.unit}"),\n'
            python_text += ingredient_text
        python_text += f"{indent}]\n"

        python_text += f"{indent}instructions = [\n"
        for instruction in self.instructions:
            python_text += f'{indent}{indent}"{instruction}",\n'
        python_text += f"{indent}]\n"

        with open(file=file_path, mode="w") as io:
            io.write(python_text)

        return None

    def to_markdown_file(self, file_path: pydantic.FilePath) -> None:
        """Save recipe to a .md file in Markdown format."""
        markdown_text = f"# {self.name}\n\n"

        markdown_text += "## Ingredients\n\n"
        for ingredient in self.ingredients:
            markdown_text += f"{ingredient.amount} {ingredient.unit} {ingredient.name}\n"
        markdown_text += "\n\n"

        markdown_text += "## Instructions\n\n"
        for instruction in self.instructions:
            markdown_text += f"{instruction}\n"

        with open(file=file_path, mode="w") as io:
            io.write(markdown_text)

        return None

    @classmethod
    def from_markdown_file(cls, file_path: pydantic.FilePath, include_instructions: bool = True) -> Self:
        """Load recipe from a .md file in Markdown format."""
        with open(file=file_path) as io:
            lines = [parsed_line for line in io.readlines() if (parsed_line := line.rstrip()) != ""]

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
        instructions = list(lines[instruction_line + 1 :]) if include_instructions is True else None

        return Recipe(name=recipe_name, cuisine=cuisine, ingredients=ingredients, instructions=instructions)
