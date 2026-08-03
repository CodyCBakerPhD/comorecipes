import html
import json
import typing
import urllib.parse

import pydantic
import yaml

from ._base_measurement import Measurement

# The GitHub "mark" octicon, inlined so pages have no external image dependencies
_GITHUB_ICON_PATH = "M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49"
_GITHUB_ICON_PATH += "-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58"
_GITHUB_ICON_PATH += " 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59"
_GITHUB_ICON_PATH += ".82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27"
_GITHUB_ICON_PATH += " 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65"
_GITHUB_ICON_PATH += " 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8"
_GITHUB_ICON_PATH += "c0-4.42-3.58-8-8-8z"
_GITHUB_ICON_SVG = f'<svg viewBox="0 0 16 16" aria-hidden="true"><path d="{_GITHUB_ICON_PATH}"/></svg>'
_GITHUB_REPOSITORY_URL = "https://github.com/CodyCBakerPhD/como_recipes"

_GITHUB_LINK_HTML = f'<a class="icon-link" href="{_GITHUB_REPOSITORY_URL}" aria-label="View source on GitHub">'
_GITHUB_LINK_HTML += f"{_GITHUB_ICON_SVG}</a>"

_THEME_TOGGLE_HTML = '<button class="theme-toggle" type="button" onclick="comoToggleTheme()"'
_THEME_TOGGLE_HTML += ' aria-label="Toggle color theme"></button>'


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
    tags: tuple[str, ...] | None = None
    notes: tuple[str, ...] | None = None
    file_path: pydantic.FilePath | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

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

        restructured_measurements = []
        for measurement in ordered_model_dump["measurements"]:
            restructured_measurement = {
                "amount": measurement["amount"],
                "unit": measurement["unit"],
                "ingredient": measurement["ingredient"]["name"],
            }
            restructured_measurements.append(restructured_measurement)
        ordered_model_dump["measurements"] = restructured_measurements

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
        from .._registration._ingredient_registry import IngredientRegistry

        try:
            with file_path.open(mode="r") as io:
                recipe_info = yaml.safe_load(stream=io)
            recipe_info["tags"] = tuple(recipe_info["tags"])

            recipe_info["measurements"] = tuple(
                IngredientRegistry.get_measurement(
                    amount=amount if (amount := measurement["amount"]) != "enough" else amount,
                    unit=measurement.get("unit", None),
                    ingredient_name=measurement["ingredient"],
                    prefix=measurement.get("prefix", None),
                    suffix=measurement.get("suffix", None),
                )
                for measurement in recipe_info["measurements"]
            )
            recipe_info["instructions"] = tuple(recipe_info["instructions"])

            if "notes" in recipe_info:
                recipe_info["notes"] = tuple(recipe_info["notes"])

            recipe_info["file_path"] = file_path
            return cls(**recipe_info)
        except Exception as exception:  # noqa: BLE001
            message = f"\nUnable to load recipe from {file_path} due to...\n\n{type(exception)}:\n\t{exception}\n\n"
            raise ValueError(message)

    @pydantic.validate_call
    def to_html_file(
        self,
        *,
        file_path: pydantic.NewPath | pydantic.FilePath,
        tag_to_hue: dict[str, int] | None = None,
    ) -> None:
        """
        Save recipe to a styled .html page for use in the website.

        The page links to the shared stylesheet and favicon copied into `docs/assets` by `generate_html_recipes`.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the HTML (.html) file
        tag_to_hue : dict of str to int, optional
            Mapping of tag names to the hue (in degrees) used to color their chips, usually spread over
            every tag in the recipe database by `generate_html_recipes`.
            If unspecified, hues are spread evenly over this recipe's own tags.

        """
        from ..utils import get_rendered_units

        if tag_to_hue is None and self.tags is not None:
            sorted_tags = sorted(set(self.tags))
            tag_to_hue = {tag: index * 360 // len(sorted_tags) for index, tag in enumerate(sorted_tags)}

        escaped_name = html.escape(self.name)
        html_lines = [
            "<!DOCTYPE html>",
            '<html lang="en">',
            "<head>",
            '    <meta charset="UTF-8">',
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f"    <title>{escaped_name} · CoMo Recipes</title>",
            '    <link rel="icon" href="../assets/como_icon.ico">',
            '    <link rel="stylesheet" href="../assets/style.css">',
            '    <script src="../assets/theme.js"></script>',
            "</head>",
            '<body class="recipe-page">',
            '    <nav class="top-bar">',
            '        <a class="brand" href="../index.html">',
            '            <img class="brand-logo" src="../assets/como_logo.jpg" alt="CoMo logo">',
            "            <span>CoMo Recipes</span>",
            "        </a>",
            '        <div class="top-actions">',
            '            <a class="back-link" href="../index.html">&larr; Recipe Index</a>',
            f"            {_GITHUB_LINK_HTML}",
            f"            {_THEME_TOGGLE_HTML}",
            "        </div>",
            "    </nav>",
            '    <main class="recipe">',
            '        <header class="recipe-header">',
            f"            <h1>{escaped_name}</h1>",
        ]

        if self.tags is not None:
            html_lines += ['            <ul class="tag-list">']
            for tag in self.tags:
                tag_hue = tag_to_hue.get(tag, 0)
                tag_link = f'<a href="../index.html?tag={urllib.parse.quote(tag)}">{html.escape(tag)}</a>'
                html_lines += [f'                <li class="tag" style="--tag-hue: {tag_hue}">{tag_link}</li>']
            html_lines += ["            </ul>"]

        html_lines += [
            "        </header>",
            '        <div class="recipe-body">',
            '            <section class="ingredients">',
            "                <h2>Ingredients</h2>",
            '                <ul class="ingredient-list">',
        ]

        disallowed_units = {"": True, "portions": True}
        for measurement in self.measurements:
            amount_text = f"{measurement.amount}"

            rendered_units = get_rendered_units(measurement=measurement)
            if disallowed_units.get(rendered_units, False) is False:
                amount_text += f" {rendered_units}"

            item_words = []
            if measurement.prefix is not None:
                item_words += [measurement.prefix]
            item_words += [measurement.ingredient.name]
            if measurement.suffix is not None:
                item_words += [measurement.suffix]
            item_text = " ".join(item_words)

            amount_html = f'<span class="amount">{html.escape(amount_text)}</span>'
            item_html = f'<span class="ingredient-text">{amount_html} {html.escape(item_text)}</span>'
            html_lines += [
                '                    <li class="ingredient"><label>',
                '                        <input type="checkbox">',
                f"                        {item_html}",
                "                    </label></li>",
            ]

        html_lines += [
            "                </ul>",
            "            </section>",
            '            <div class="method">',
        ]

        if self.notes is not None:
            html_lines += [
                '                <section class="notes">',
                "                    <h2>Notes</h2>",
                '                    <ul class="note-list">',
            ]
            html_lines += [f"                        <li>{html.escape(note)}</li>" for note in self.notes]
            html_lines += [
                "                    </ul>",
                "                </section>",
            ]

        html_lines += [
            '                <section class="instructions">',
            "                    <h2>Instructions</h2>",
            '                    <ol class="step-list">',
        ]
        html_lines += [
            f"                        <li>{html.escape(instruction)}</li>" for instruction in self.instructions
        ]
        html_lines += [
            "                    </ol>",
            "                </section>",
            "            </div>",
            "        </div>",
            "    </main>",
            "</body>",
            "</html>",
        ]

        with file_path.open(mode="w") as io:
            io.write("\n".join(html_lines) + "\n")
