import pydantic
import natsort

from ._base_recipe import Recipe


class RecipeRegistry(pydantic.BaseModel):
    _recipes: list[Recipe] = []

    def __len__(self) -> int:
        return len(self._recipes)

    def __repr__(self) -> str:
        number_of_registered_recipes = len(self)

        printout = f"{number_of_registered_recipes} registered recipes\n"
        printout += f"{'-' * (len(printout)-1)}\n\n"
        for recipe in natsort.natsorted(seq=self._recipes):
            printout += f"{recipe.name}\n"

        return printout

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        return repr(self)

    @pydantic.validate_call
    def add_recipe(self, *, recipe: Recipe) -> None:
        """
        Add a recipe to the registry.

        Parameters
        ----------
        recipe : Recipe
            Recipe to add to the registry.
        """
        self._recipes.append(recipe)
        return None


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_recipe_registry = RecipeRegistry()
