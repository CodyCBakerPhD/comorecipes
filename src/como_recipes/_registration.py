import collections

import pydantic
import natsort

from ._base_recipe import Recipe
from ._base_ingredient import Ingredient
from ._base_measurement import Measurement


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
        return self.__repr__()

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


class MeasurementRegistry(pydantic.BaseModel):
    _measurements: dict[str, list[Measurement]] = collections.defaultdict(list)

    def __len__(self) -> int:
        return len(self._measurements)

    def __repr__(self) -> str:
        number_of_registered_measurements = len(self)

        printout = f"{number_of_registered_measurements} registered measurements\n"
        printout += f"{'-' * (len(printout)-1)}\n\n"
        for measurement in natsort.natsorted(seq=self._measurements):
            printout += f"{measurement.name}\n"

        return printout

    def __str__(self) -> str:
        return self.__repr__()

    @pydantic.validate_call
    def add_measurement(self, *, measurement: Measurement) -> None:
        """
        Add a measurement to the registry.

        Parameters
        ----------
        measurement : Measurement
            Measurement to add to the registry.
        """
        self._measurements[measurement.ingredient.name].append(measurement)
        return None

    @pydantic.validate_call
    def add_recipe(self, *, recipe: Recipe) -> None:
        """
        Add a recipe to the registry.

        Parameters
        ----------
        recipe : Recipe
            Recipe to add to the registry.
        """
        for measurement in recipe.measurements:
            self.add_measurement(measurement=measurement)
        return None

    @staticmethod
    @pydantic.validate_call
    def get_measurement(*, amount: int | float, unit: str, name: str) -> Measurement:
        """
        Generate a measurement of an ingredient from the ingredient registry; uses a base Ingredient if unregistered.

        Parameters
        ----------
        amount : int | float
            Amount of the ingredient.
        unit : str
            Unit of the ingredient amount.
        name : str
            Name of the ingredient.
        """
        global default_ingredient_registry

        ingredient = default_ingredient_registry.get(name=name)
        return Measurement(amount=amount, unit=unit, ingredient=ingredient)


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_recipe_registry = RecipeRegistry()
default_ingredient_registry = IngredientRegistry()
