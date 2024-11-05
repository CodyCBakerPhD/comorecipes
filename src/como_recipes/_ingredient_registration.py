import pydantic
import natsort

from ._base_ingredient import Ingredient


class IngredientRegistry(pydantic.BaseModel):
    _ingredients: dict[str, Ingredient] = {}

    def __len__(self) -> int:
        return len(self._ingredients)

    def __repr__(self) -> str:
        number_of_registered_ingredients = len(self)

        printout = f"{number_of_registered_ingredients} registered ingredients\n"
        printout += f"{'-' * (len(printout)-1)}\n\n"
        for name, ingredient in natsort.natsorted(seq=self._ingredients.items(), key=lambda item_tuple: item_tuple[0]):
            printout += f"{ingredient.name}\n"

        return printout

    def __str__(self) -> str:
        return self.__repr__()

    @pydantic.validate_call
    def get(self, *, name: str) -> Ingredient:
        """
        Get an ingredient from the registry by name; returns a default base Ingredient if unregistered.

        Parameters
        ----------
        name : str
            Name of the ingredient.
        """
        return self._ingredients.get(name, Ingredient(name=name))

    @pydantic.validate_call
    def add_ingredient(self, *, ingredient: Ingredient) -> None:
        """
        Add a custom ingredient to the registry.

        Parameters
        ----------
        ingredient : Ingredient
            Custom ingredient to add to the registry
        """
        self._ingredients[ingredient.name] = ingredient
        return None


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_ingredient_registry = IngredientRegistry()
