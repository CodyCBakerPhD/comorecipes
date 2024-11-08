import collections

import pydantic
import natsort

from ._base_recipe import Recipe
from ._base_ingredient import Ingredient
from ._ingredient_registration import default_ingredient_registry
from ._base_measurement import Measurement
from ._recipe_registration import RecipeRegistry


class MeasurementRegistry(pydantic.BaseModel):
    """
    Registry for storing measurements and recipes.

    Initialize an empty registry with `MeasurementRegistry()` then add:
        - measurements with `add_measurement`
        - recipes with `add_recipe`
    """

    _individual_measurements: dict[str, list[Measurement]] | None = None
    _combined_measurements: dict[str, list[Measurement]] | None = None
    _recipe_registry: RecipeRegistry | None = None

    def __init__(self, *args, **kwargs) -> None:
        if len(args) > 0:
            raise ValueError("No positional arguments are allowed.")

        super().__init__(**kwargs)

        self._individual_measurements = collections.defaultdict(list, self._individual_measurements or {})
        self._combined_measurements = collections.defaultdict(list, self._individual_measurements or {})
        self._recipe_registry = RecipeRegistry()

    def _printout_nested_ingredients(self, measurements_by_ingredient: list[Measurement]) -> str:
        printout = ""
        for measurement in measurements_by_ingredient:
            printout += f"  {measurement.amount} {measurement.unit}\n"

        return printout

    def _printout_nested_measurements(self) -> str:
        printout = ""
        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=self._combined_measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            printout += f"{ingredient_name}\n"
            printout += self._printout_nested_ingredients(measurements_by_ingredient=measurements_by_ingredient)

        return printout

    def __len__(self) -> int:
        return len(self._combined_measurements)

    def __repr__(self) -> str:
        number_of_registered_measurements = len(self)

        printout = f"{number_of_registered_measurements} registered measurements\n"

        if number_of_registered_measurements == 0:
            return printout

        printout += f"{'-' * (len(printout)-1)}\n\n"
        printout += self._printout_nested_measurements()

        return printout

    def __str__(self) -> str:
        """Used by calls to `print(...)`."""
        return repr(self)

    @pydantic.validate_call
    def add_measurement(self, *, measurement: Measurement) -> None:
        """
        Add a measurement to the registry.

        Parameters
        ----------
        measurement : Measurement
            Measurement to add to the registry.
        """
        self._individual_measurements[measurement.ingredient.name].append(measurement)
        self._combined_measurements[measurement.ingredient.name].append(measurement)
        return None

    @pydantic.validate_call
    def remove_measurement(self, *, measurement: Measurement) -> None:
        """
        Remove a measurement from the registry.

        Parameters
        ----------
        measurement : Measurement
            Measurement to remove from the registry.
        """
        self._individual_measurements[measurement.ingredient.name].remove(measurement)
        self._combined_measurements[measurement.ingredient.name].remove(measurement)
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
        self._recipe_registry.add_recipe(recipe=recipe)

        for measurement in recipe.measurements:
            self._combined_measurements[measurement.ingredient.name].append(measurement)

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
        self._recipe_registry.remove_recipe(recipe_name=recipe_name)

        self._combined_measurements = collections.defaultdict(list)
        for measurement in self._individual_measurements.values():
            self._combined_measurements[measurement.ingredient.name].extend(measurement)
        for recipe_name in self._recipe_registry.get_all_recipe_names():
            recipe = self._recipe_registry.get_recipe(recipe_name=recipe_name)
            for measurement in recipe.measurements:
                self._combined_measurements[measurement.ingredient.name].append(measurement)

        return None

    @pydantic.validate_call
    def get_all_recipe_names(self) -> list[str]:
        """Get all recipe names from the currently attached registry."""
        return list(self._recipe_registry._recipes.keys())

    @pydantic.validate_call
    def get_shopping_list(self) -> str:
        """Get a shopping list by aggregating all contained recipes and measurements."""
        shopping_list = ""

        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=self._combined_measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            shopping_list += f"{ingredient_name}\n"

            # TODO: shouldn't be needed once grams are standardized
            measurement_units_per_ingredient = {measurement.unit for measurement in measurements_by_ingredient}
            if len(measurement_units_per_ingredient) > 1:
                message = (
                    f"\nMultiple units found for ingredient {measurements_by_ingredient[0].ingredient.name}:\n\n["
                    f"{self._printout_nested_ingredients(measurements_by_ingredient=measurements_by_ingredient)}"
                    "]"
                )
                raise ValueError(message)
            measurement_unit = list(measurement_units_per_ingredient)[0]

            total_per_ingredient = sum(measurement.amount for measurement in measurements_by_ingredient)
            shopping_list += f"  {total_per_ingredient} {measurement_unit}\n"

        return shopping_list

    @staticmethod
    @pydantic.validate_call
    def get_measurement(*, amount: int | float, unit: str, name: str) -> Measurement:
        """
        Generate a measurement of an ingredient from the default global ingredient registry.

        Uses a base Ingredient if it is unregistered.

        Parameters
        ----------
        amount : int | float
            Amount of the ingredient.
        unit : str
            Unit of the ingredient amount.
        name : str
            Name of the ingredient.
        """
        # global default_ingredient_registry

        if name in default_ingredient_registry:
            ingredient = default_ingredient_registry.get_ingredient(name=name)
        else:
            ingredient = Ingredient(name=name)

        return Measurement(amount=amount, unit=unit, ingredient=ingredient)
