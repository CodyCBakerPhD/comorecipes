from typing import Self
import pathlib

import pydantic

from .utils import rational_string_to_float
from ._base_measurement import Measurement


class Recipe(pydantic.BaseModel):
    """
    Automatically validated base data class for all recipes.

    Parameters
    ----------
    name : str
        Name of the recipe.
    measurements : list[Measurement]
        List of ingredients.
    instructions : list[str]
        List of instructions.
    notes : list[str] or None, optional
        List of notes.
    """

    name: str
    measurements: list[Measurement]
    instructions: list[str]
    notes: list[str] | None = None

    def __repr__(self) -> str:
        printout = f"\n{self.name}\n"
        printout += f"{'=' * len(self.name)}\n\n"

        printout += "Ingredients\n"
        printout += "-----------\n"
        for measurement in self.measurements:
            printout += f"{measurement.amount} {measurement.unit} {measurement.ingredient.name}\n"
        printout += "\n\n"

        printout += "Instructions\n"
        printout += "------------\n"
        for instruction in self.instructions:
            printout += f"{instruction}\n"

        return printout

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        return repr(self)

    @pydantic.validate_call
    def to_pydantic_file(self, file_path: pydantic.NewPath) -> None:
        """
        Save recipe to a .py file in Pydantic format.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the Pydantic (.py) file.
        """
        indent = " " * 4

        camel_case_name = "".join(word.capitalize() for word in self.name.split(" "))
        python_text = "from ..._base_recipe import Recipe\n"
        python_text += "from ..._base_measurement import Measurement\n"
        python_text += "from ..._recipe_registration import default_recipe_registry\n"
        python_text += "from ..._measurement_registration import MeasurementRegistry\n\n\n"
        python_text += f"class {camel_case_name}(Recipe):\n"
        python_text += f'{indent}name: str = "{self.name}"\n'

        python_text += f"{indent}measurements: list[Measurement] = [\n"
        for measurement in self.measurements:
            measurement_text = f"{indent}{indent}MeasurementRegistry.get_measurement(amount={measurement.amount}, "
            measurement_text += f'unit="{measurement.unit}", '
            measurement_text += f'name="{measurement.ingredient.name}"),\n'
            python_text += measurement_text
        python_text += f"{indent}]\n"

        python_text += f"{indent}instructions: list[str] = [\n"
        for instruction in self.instructions:
            python_text += f'{indent}{indent}"{instruction}",\n'
        python_text += f"{indent}]\n"

        python_text += f"\n\ndefault_recipe_registry.add_recipe(recipe={camel_case_name}())\n"

        with open(file=file_path, mode="w") as io:
            io.write(python_text)

        # Expose the new recipe class in the 'recipes' submodule __init__.py file so that it can be imported
        init_file_path = pathlib.Path(file_path).parent / "__init__.py"
        if not init_file_path.exists():  # For friendly compatibility with tests and non-default recipes
            return None

        with open(file=init_file_path, mode="r") as io:
            current_init_file_lines = io.readlines()

        # Insert to the top (after comment) and let pre-commit deal with proper ordering
        current_init_file_lines.insert(1, f"from .{file_path.stem} import {camel_case_name}\n")

        with open(file=init_file_path, mode="w") as io:
            io.writelines(current_init_file_lines)

        return None

    @pydantic.validate_call
    def to_markdown_file(self, file_path: pydantic.NewPath) -> None:
        """
        Save recipe to a .md file in Markdown format.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the Markdown (.md) file
        """
        markdown_text = f"# {self.name}\n\n"

        markdown_text += "## Ingredients\n\n"
        for measurement in self.measurements:
            markdown_text += f"{measurement.amount} {measurement.unit} {measurement.ingredient.name}\n\n"
        markdown_text += "\n\n"

        markdown_text += "## Instructions\n\n"
        for instruction in self.instructions:
            markdown_text += f"{instruction}\n"

        with open(file=file_path, mode="w") as io:
            io.write(markdown_text)

        return None

    @classmethod
    @pydantic.validate_call
    def from_markdown_file(cls, file_path: pydantic.FilePath, include_instructions: bool = True) -> Self:
        """
        Load recipe from a .md file in Markdown format.

        Parameters
        ----------
        file_path : pydantic.FilePath
            Path to the Markdown (.md) file.
        include_instructions : bool, optional
            Whether to include the instructions in the recipe.
        """
        from ._measurement_registration import MeasurementRegistry

        with open(file=file_path) as io:
            lines = [parsed_line for line in io.readlines() if (parsed_line := line.rstrip()) != ""]

        assert lines[0][:2] == "# ", "Markdown recipe does not begin with '# '."
        assert lines[1] == "## Ingredients", "Markdown recipe does not have a section titled '## Ingredients'."

        recipe_name_and_cuisine_line = lines[0][2:]
        if "(" in recipe_name_and_cuisine_line:
            recipe_name, _ = recipe_name_and_cuisine_line.split("(")
        else:
            recipe_name = recipe_name_and_cuisine_line
        recipe_name = recipe_name.rstrip(" ")

        instruction_line = lines.index("## Instructions")

        measurements = []
        for line in lines[2:instruction_line]:
            ingredient_line = line.split(" ")
            amount = rational_string_to_float(ingredient_line[0])
            unit = ingredient_line[1]
            ingredient_name = " ".join(ingredient_line[2:])
            measurements.append(MeasurementRegistry.get_measurement(amount=amount, unit=unit, name=ingredient_name))

        # Not necessary for planning tools
        instructions = list(lines[instruction_line + 1 :]) if include_instructions is True else None

        return Recipe(name=recipe_name, measurements=measurements, instructions=instructions)
