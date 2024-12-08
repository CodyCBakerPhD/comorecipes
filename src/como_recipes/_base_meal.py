import natsort
import pydantic

from ._base_recipe import Recipe
from ._recipe_registration import default_recipe_registry


class Meal(pydantic.BaseModel):
    """
    Automatically validated base data class for all meals.

    Parameters
    ----------
    recipes : set[Recipe]
        List of ingredients.
    quantity_multiplier : int | float | None
        Default recipes tend to be scaled to 2 people, plus or minus leftovers.
        If more people need to be fed, adjust this scale accordingly.

    """

    recipes: set[Recipe, ...]
    quantity_multiplier: int | float | None = None

    def __eq__(self, other: "Meal") -> bool:
        """Primary used by consistency assertions in the tests."""
        if self.recipes != other.recipes:
            return False
        if self.quantity_multiplier is None and other.quantity_multiplier is None:
            return True
        if self.quantity_multiplier != other.quantity_multiplier:
            return False
        return True

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        recipe_names = self._get_recipe_names_by_type()

        representation = "como_recipes.Meal(\n\trecipes={\n"
        for recipe_name in recipe_names:
            representation += f'\t\tcomo_recipes.default_recipe_registry.get_recipe(recipe_name="{recipe_name}"),\n'
        representation += "\t}"
        if self.quantity_multiplier is not None:
            representation += ",\n"
            representation += f"\tquantity_multiplier={self.quantity_multiplier},\n"
        else:
            representation += "\n"
        representation += ")\n"

        return representation

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        recipe_names = self._get_recipe_names_by_type()

        printout = "Recipes\n"
        printout += "-------\n"
        if self.quantity_multiplier is None:
            for recipe_name in recipe_names:
                printout += f"{recipe_name}\n"
        else:
            for recipe_name in recipe_names:
                printout += f"{recipe_name} x{self.quantity_multiplier}\n"

        return printout

    def _get_recipe_names_by_type(self) -> list[str]:
        """
        Common logic used by both `__repr__` and `__str__`.

        Fetch the recipe names in a deterministic order given alphabetically by tags (Entree vs. Side).
        """
        entrees = natsort.natsorted(seq=(recipe.name for recipe in self.recipes if "Entree" in recipe.tags))
        sides = natsort.natsorted(seq=(recipe.name for recipe in self.recipes if "Side" in recipe.tags))
        others = natsort.natsorted(seq=({recipe.name for recipe in self.recipes} - set(entrees) - set(sides)))
        recipe_names_by_type = entrees + sides + others

        return recipe_names_by_type

    def add_recipe_name(self, recipe_name: str) -> None:
        """Add a default recipe name to the meal."""
        self.recipes.add(default_recipe_registry.get_recipe(recipe_name=recipe_name))

    def remove_recipe_name(self, recipe_name: str) -> None:
        """Remove a default recipe name from the meal."""
        self.recipes.remove(default_recipe_registry.get_recipe(recipe_name=recipe_name))
