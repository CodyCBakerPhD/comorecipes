import pydantic

from como_recipes._registration._recipe_registry import default_recipe_registry

from ._base_recipe import Recipe
from ..utils import get_recipe_names_by_type


class Meal(pydantic.BaseModel):
    """
    A meal is a collection of recipes to be prepared and eaten together.

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
        recipe_names = get_recipe_names_by_type(recipes=self.recipes)

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
        recipe_names = get_recipe_names_by_type(recipes=self.recipes)

        printout = "Recipes\n"
        printout += "-------\n"
        if self.quantity_multiplier is None:
            for recipe_name in recipe_names:
                printout += f"{recipe_name}\n"
        else:
            for recipe_name in recipe_names:
                printout += f"{recipe_name} x{self.quantity_multiplier}\n"

        return printout

    def add_recipe_name(self, recipe_name: str) -> None:
        """Add a default recipe name to the meal."""
        self.recipes.add(default_recipe_registry.get_recipe(recipe_name=recipe_name))

    def remove_recipe_name(self, recipe_name: str) -> None:
        """Remove a default recipe name from the meal."""
        self.recipes.remove(default_recipe_registry.get_recipe(recipe_name=recipe_name))
