import natsort
import pydantic

from ._base_recipe import Recipe


class RecipeRegistry(pydantic.BaseModel):
    _recipes: dict[str, Recipe] = {}

    def __len__(self) -> int:
        return len(self._recipes)

    def __repr__(self) -> str:
        number_of_registered_recipes = len(self)

        printout = f"{number_of_registered_recipes} registered recipes\n"

        if number_of_registered_recipes == 0:
            return printout

        printout += f"{'-' * (len(printout)-1)}\n\n"
        for recipe_name in natsort.natsorted(seq=self._recipes.keys()):
            printout += f"{recipe_name}\n"

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
        self._recipes[recipe.name] = recipe
        return None

    @pydantic.validate_call
    def remove_recipe(self, *, recipe_name: str) -> None:
        """
        Remove a recipe from the registry.

        Parameters
        ----------
        recipe_name : str
            Name of the recipe to remove from the registry.

        """
        self._recipes.pop(recipe_name)
        return None

    @pydantic.validate_call
    def get_recipe(self, *, recipe_name: str) -> Recipe:
        """
        Get a recipe from the registry.

        Parameters
        ----------
        recipe_name : str
            Name of the recipe to get from the registry.

        """
        recipe = self._recipes.get(recipe_name, None)
        if recipe is None:
            raise ValueError(f"Recipe '{recipe_name}' not found in the registry.")
        return recipe

    @pydantic.validate_call
    def get_all_recipe_names(self) -> list[str]:
        """Get all recipes from the registry."""
        return list(self._recipes.keys())


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_recipe_registry = RecipeRegistry()
