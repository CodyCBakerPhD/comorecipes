import fractions
import json
import typing

import pydantic
import yaml

from ._base_measurement import Measurement
from .._registration._ingredient_registry import IngredientRegistry
from ..utils import string_to_numeric


class Recipe(pydantic.BaseModel):
    """
    A recipe is a named and tagged collection of measured ingredients with instructions and notes.

    Notes can be warnings or other common reminders.

    Parameters
    ----------
    name : str
        Name of the recipe.
    snake_case_name : str, optional
        Name of the recipe in 'snake_case'.
        If unspecified, this is automatically created from the `name` using a heuristic.
    camel_case_name : str, optional
        Name of the recipe in 'CamelCase'.
        If unspecified, this is automatically created from the `name` using a heuristic.
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
    measurements: tuple[Measurement, ...]
    instructions: tuple[str, ...]
    # snake_case_name: str | None = None
    # camel_case_name: str | None = None
    tags: tuple[str, ...] | None = None
    notes: tuple[str, ...] | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    # def __init__(
    #     self,
    #     name: str,
    #     measurements: tuple[Measurement, ...],
    #     instructions: tuple[str, ...],
    #     snake_case_name: str | None = None,
    #     camel_case_name: str | None = None,
    #     tags: tuple[str, ...] | None = None,
    #     notes: tuple[str, ...] | None = None,
    # ) -> None:
    #     super().__init__(
    #         name=name,
    #         snake_case_name=snake_case_name,
    #         camel_case_name=camel_case_name,
    #         tags=tags,
    #         measurements=measurements,
    #         instructions=instructions,
    #         notes=notes,
    #     )
    #
    #     self.snake_case_name = self.snake_case_name or self.name.lower().replace(" ", "_")
    #     self.camel_case_name = self.camel_case_name or "".join(
    #     word.capitalize() for word in self.snake_case_name.split("_")
    #     )

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Does not apply to this class as it is multivalued.
        """
        message = "The Recipe class has no intuitive notion of length."

        raise NotImplementedError(message)

    def __eq__(self, other: "Recipe") -> bool:
        """
        Logic defining the `==` operator.

        Primarily used by consistency assertions in the tests.

        Compares only the contained fields of the object, not including its memory address (two imported instances
        of the class with the same fields will be considered equal).
        """
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
            representation += "\tnotes=(\n"
            for note in self.notes:
                representation += f'\t\t"{note}",\n'
            representation += "\t),\n"

        representation += ")"

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        printout = f"\n{self.name}\n"
        printout += f"{'=' * len(self.name)}\n\n"
        printout += "Tags: " + ", ".join(self.tags) + "\n\n"

        printout += "Ingredients\n"
        printout += "-----------\n"
        for measurement in self.measurements:
            printout += f"{measurement.amount} {measurement.unit} {measurement.ingredient.name}\n"
        printout += "\n\n"

        if self.notes is not None:
            printout += "Notes\n"
            printout += "-----\n"
            for note in self.notes:
                printout += f"{note}\n"
            printout += "\n\n"

        printout += "Instructions\n"
        printout += "------------\n"
        for instruction in self.instructions:
            printout += f"{instruction}\n"

        return printout

    def __hash__(self) -> int:
        return hash(self.name)

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

        if self.notes is not None:
            markdown_text += "## Notes\n\n"
            for note in self.notes:
                markdown_text += f"{note}\n\n"
            markdown_text += "\n\n"

        markdown_text += "## Instructions\n\n"
        for instruction in self.instructions:
            markdown_text += f"{instruction}\n\n"

        with file_path.open(mode="w") as io:
            io.write(markdown_text[:-1])

    @pydantic.validate_call
    def to_yaml_file(self, *, file_path: pydantic.NewPath | pydantic.FilePath) -> None:
        """
        Save recipe to a .yaml file.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the .yaml file

        """
        # Standardize the order of the fields in the YAML file
        key_order = ["name", "tags", "measurements", "instructions", "notes"]
        model_dump = json.loads(s=self.model_dump_json())
        ordered_model_dump = {key: value for key in key_order if (value := model_dump.get(key)) is not None}

        cleaned_measurements = []
        for measurement in ordered_model_dump["measurements"]:
            cleaned_ingredient = {"name": measurement["ingredient"]["name"]}  # Remove extraneous (usually null) info
            cleaned_measurement = {
                "amount": measurement["amount"],
                "unit": measurement["unit"],
                "ingredient": cleaned_ingredient,
            }
            cleaned_measurements.append(cleaned_measurement)
        ordered_model_dump["measurements"] = cleaned_measurements

        # Additional newline padding is applied across each field so YAML file is more readable
        # Does require some adjustments to dumping however
        if file_path.exists():
            file_path.unlink()

        for key, value in ordered_model_dump.items():
            with file_path.open(mode="a") as io:
                io.write(yaml.dump(data={key: value}, sort_keys=False))
                io.write("\n")

    @classmethod
    @pydantic.validate_call
    def from_yaml_file(cls, *, file_path: pydantic.FilePath) -> typing.Self:
        """
        Load recipe from a .yaml file.

        Parameters
        ----------
        file_path : pydantic.FilePath
            Path to the .yaml file.

        """
        with file_path.open(mode="r") as io:
            recipe_info = yaml.safe_load(stream=io)
        recipe_info["tags"] = tuple(recipe_info["tags"])
        recipe_info["measurements"] = tuple(
            IngredientRegistry.get_measurement(
                amount=string_to_numeric(string=amount) if (amount := measurement["amount"]) != "enough" else amount,
                unit=measurement.get("unit", None),
                ingredient_name=measurement["ingredient"]["name"],
            )
            for measurement in recipe_info["measurements"]
        )
        recipe_info["instructions"] = tuple(recipe_info["instructions"])

        if "notes" in recipe_info:
            recipe_info["notes"] = tuple(recipe_info["notes"])

        return Recipe(**recipe_info)

    @pydantic.validate_call
    def to_html_file(self, *, file_path: pydantic.NewPath | pydantic.FilePath) -> None:
        """
        Save recipe to a .html file in a markdown-like structure for use in the website.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the HTML (.html) file

        """
        html_lines = ['<p><a href="../index.html">Back to Recipe Index</a></p>\n\n']
        html_lines += [f"<h1>{self.name}</h1>\n\n"]

        if self.tags is not None:
            html_lines += [f"<p>Tags: {', '.join(self.tags)}</p>\n\n\n\n"]

        html_lines += ["<br>"]
        html_lines += ["<h2>Ingredients</h2>\n\n"]
        for measurement in self.measurements:
            html_lines += ["<p>"]
            html_lines += [f"{measurement.amount} {measurement.unit}"]
            html_lines += [f" {measurement.ingredient.name}</p>\n" if measurement.ingredient.name != "" else "</p>\n"]

        if self.notes is not None:
            html_lines += ["<br>"]
            html_lines += ["<h2>Notes</h2>\n\n"]
            for note in self.notes:
                html_lines += [f"<p>{note}</p>\n"]

        html_lines += ["<h2>Instructions</h2>\n\n"]
        for instruction in self.instructions:
            html_lines += [f"<p>{instruction}</p>\n"]

        with file_path.open(mode="w") as io:
            io.writelines(html_lines)

    @classmethod
    @pydantic.validate_call
    def from_markdown_file(cls, *, file_path: pydantic.FilePath, include_instructions: bool = True) -> typing.Self:
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

        ingredient_start_index = lines.index("## Ingredients")
        instruction_start_index = lines.index("## Instructions")

        # TODO: wished there was a lazier way to do this
        if include_instructions is True and "## Notes" in lines:
            notes_start_index = lines.index("## Notes")
            notes = tuple(lines[(notes_start_index + 1) : instruction_start_index])
        else:
            notes = None

        measurement_end_index = instruction_start_index if notes is None else notes_start_index
        measurements = []
        for line in lines[(ingredient_start_index + 1) : measurement_end_index]:
            ingredient_line = line.split(" ")
            amount = fractions.Fraction(ingredient_line[0])
            unit = ingredient_line[1]
            ingredient_name = " ".join(ingredient_line[2:])
            measurements.append(
                IngredientRegistry.get_measurement(amount=amount, unit=unit, ingredient_name=ingredient_name),
            )
        measurements = tuple(measurements)

        # Not necessary for planning tools
        instructions = tuple(lines[instruction_start_index + 1 :]) if include_instructions is True else None

        return Recipe(name=recipe_name, tags=tags, measurements=measurements, instructions=instructions, notes=notes)
