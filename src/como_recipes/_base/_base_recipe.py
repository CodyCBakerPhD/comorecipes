import fractions
import pathlib
from typing import Self

import pydantic

from ._base_measurement import Measurement


class Recipe(pydantic.BaseModel):
    """
    A recipe is a named and tagged collection of measured ingredients with instructions and notes.

    Notes can be warnings or other common reminders.

    Parameters
    ----------
    name : str
        Name of the recipe.
    tags : tuple[str], optional
        List of tags associated with the recipe.
    measurements : tuple[Measurement]
        List of ingredients.
    instructions : tuple[str]
        List of instructions.
    notes : tuple[str], optional
        List of notes.

    """

    name: str
    tags: tuple[str, ...] | None = None
    measurements: tuple[Measurement, ...]
    instructions: tuple[str, ...]
    notes: tuple[str] | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Does not apply to this class as it is multivalued.
        """
        message = "The Recipe class has no intuitive notion of length."

        raise NotImplementedError(message)

    def __eq__(self, other: "Recipe") -> bool:
        """Primary used by consistency assertions in the tests."""
        if not isinstance(other, type(self).mro()[1]):
            return False

        fields_to_compare = ["name", "tags", "measurements", "instructions", "notes"]
        result = all(getattr(self, field) == getattr(other, field) for field in fields_to_compare)

        return result

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        representation = f'Recipe(\n\tname="{self.name}",\n'

        if self.tags is not None:
            representation += f"\ttags={self.tags},\n"

        representation += "\tmeasurements=(\n"
        for measurement in self.measurements:
            representation += f"\t\t{measurement},\n"
        representation += "\t),\n"

        representation += "\tinstructions=(\n"
        for instruction in self.instructions:
            representation += f'\t\t"{instruction}",\n'
        representation += "\t),\n"

        if self.notes is not None:
            representation += f'\tnotes="{self.notes}",\n'

        representation += ")"

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
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

    def __hash__(self) -> int:
        return hash(self.name)

    @pydantic.validate_call
    def to_pydantic_file(self, *, file_path: pydantic.NewPath) -> None:
        """
        Save recipe to a .py file in Pydantic format.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the Pydantic (.py) file.

        """
        indent = " " * 4

        camel_case_name = "".join(word.capitalize() for word in self.name.replace("-", " ").split(" "))
        python_text = "from ..._base_measurement import Measurement\n"
        python_text += "from ..._base_recipe import Recipe\n"
        python_text += "from ..._measurement_registration import MeasurementRegistry\n"
        python_text += "from ..._recipe_registration import default_recipe_registry\n\n\n"
        python_text += f"class {camel_case_name}(Recipe):\n"
        python_text += f'{indent}name: str = "{self.name}"\n'

        if self.tags is not None:
            python_text += f"{indent}tags: tuple[str, ...] = (" + ", ".join(f'"{tag}"' for tag in self.tags)
            python_text += ",)\n" if len(self.tags) == 1 else ")\n"

        python_text += f"{indent}measurements: tuple[Measurement, ...] = (\n"
        for measurement in self.measurements:
            measurement_text = f"{indent}{indent}MeasurementRegistry.get_measurement(amount={measurement.amount}, "
            measurement_text += f'unit="{measurement.unit}", '
            measurement_text += f'name="{measurement.ingredient.name}"),\n'
            python_text += measurement_text
        python_text += f"{indent})\n"

        python_text += f"{indent}instructions: tuple[str, ...] = (\n"
        for instruction in self.instructions:
            python_text += f'{indent}{indent}"{instruction}",\n'
        python_text += f"{indent})\n"

        python_text += f"\n\ndefault_recipe_registry.add_recipe(recipe={camel_case_name}())\n"

        with file_path.open(mode="w") as io:
            io.write(python_text)

        # Expose the new recipe class in the 'recipes' submodule __init__.py file so that it can be imported
        init_file_path = pathlib.Path(file_path).parent / "__init__.py"
        if not init_file_path.exists():  # For friendly compatibility with tests and non-default recipes
            return

        with init_file_path.open(mode="r") as io:
            current_init_file_lines = io.readlines()

        # Insert to the top (after comment) and let pre-commit deal with proper ordering
        current_init_file_lines.insert(1, f"from .{file_path.stem} import {camel_case_name}\n")

        with init_file_path.open(mode="w") as io:
            io.writelines(current_init_file_lines)

        return

    @pydantic.validate_call
    def to_markdown_file(self, *, file_path: pydantic.NewPath) -> None:
        """
        Save recipe to a .md file in Markdown format.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the Markdown (.md) file

        """
        markdown_text = f"# {self.name}\n\n"

        if self.tags is not None:
            markdown_text += f"Tags: {', '.join(self.tags)}\n\n\n\n"

        markdown_text += "## Ingredients\n\n"
        for measurement in self.measurements:
            markdown_text += f"{measurement.amount} {measurement.unit}"
            markdown_text += f" {measurement.ingredient.name}\n\n" if measurement.ingredient.name != "" else "\n\n"
        markdown_text += "\n\n"

        markdown_text += "## Instructions\n\n"
        for instruction in self.instructions:
            markdown_text += f"{instruction}\n\n"

        with file_path.open(mode="w") as io:
            io.write(markdown_text[:-1])

    @classmethod
    @pydantic.validate_call
    def from_markdown_file(cls, *, file_path: pydantic.FilePath, include_instructions: bool = True) -> Self:
        """
        Load recipe from a .md file in Markdown format.

        Parameters
        ----------
        file_path : pydantic.FilePath
            Path to the Markdown (.md) file.
        include_instructions : bool, optional
            Whether to include the instructions in the recipe.

        """
        from .._registration._ingredient_registry import IngredientRegistry

        with file_path.open(mode="r") as io:
            lines = [parsed_line for line in io.readlines() if (parsed_line := line.rstrip()) != ""]

        if lines[0][:2] != "# ":
            message = "Markdown recipe does not begin with '# '."
            raise ValueError(message)
        if "## Ingredients" not in lines:
            message = "Markdown recipe does not have a section titled '## Ingredients'."
            raise ValueError(message)

        recipe_name = lines[0][2:].rstrip(" ")
        tags = tuple(lines[1].split(": ")[1].split(", ")) if "Tags" in lines[1] else None

        ingredient_line_index = lines.index("## Ingredients")
        instruction_line_index = lines.index("## Instructions")

        measurements = []
        for line in lines[(ingredient_line_index + 1) : instruction_line_index]:
            ingredient_line = line.split(" ")
            amount = fractions.Fraction(ingredient_line[0])
            unit = ingredient_line[1]
            ingredient_name = " ".join(ingredient_line[2:])
            measurements.append(
                IngredientRegistry.get_measurement(amount=amount, unit=unit, ingredient_name=ingredient_name),
            )
        measurements = tuple(measurements)

        # Not necessary for planning tools
        instructions = tuple(lines[instruction_line_index + 1 :]) if include_instructions is True else None

        return Recipe(name=recipe_name, tags=tags, measurements=measurements, instructions=instructions)
