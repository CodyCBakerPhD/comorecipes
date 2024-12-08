import pydantic

from ._base_recipe import Recipe


class Meal(pydantic.BaseModel):
    """
    Automatically validated base data class for all meals.

    Parameters
    ----------
    name : str
        Name of the recipe.
    tags : tuple[str], optional
        List of tags associated with the recipe.
    recipes : tuple[Recipe]
        List of ingredients.
    instructions : tuple[str]
        List of instructions.
    notes : tuple[str], optional
        List of notes.

    """

    name: str
    tags: tuple[str, ...] | None = None
    recipes: tuple[Recipe, ...]

    def __eq__(self, other: "Meal") -> bool:
        """Primary used by consistency assertions in the tests."""
        if not isinstance(other, type(self).mro()[1]):
            return False

        if self.name != other.name:
            return False

        fields_to_compare = ["tags", "recipes"]
        result = all(set(getattr(self, field)) == set(getattr(other, field)) for field in fields_to_compare)

        return result

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        representation = f'Meal(\n\tname="{self.name}",\n'

        if self.tags is not None:
            representation += f"\ttags={self.tags},\n"

        representation += "\trecipes=(\n"
        for recipe in self.recipes:
            representation += f"\t\t{recipe.name},\n"
        representation += "\t),\n"

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        printout = f"\n{self.name}\n"
        printout += f"{'=' * len(self.name)}\n\n"

        printout += "Recipes\n"
        printout += "-------\n"
        for recipe in self.recipes:
            printout += str(recipe)
        printout += "\n\n"

        return printout
