import collections
import warnings

import natsort
import pydantic

from ._base_ingredient import Ingredient
from ._base_measurement import Measurement
from ._base_recipe import Recipe
from ._ingredient_registration import default_ingredient_registry
from ._recipe_registration import RecipeRegistry


class MeasurementRegistry(pydantic.BaseModel):
    """
    Registry for storing measurements and recipes.

    Initialize an empty registry with `MeasurementRegistry()` then add:
        - measurements with `add_measurement`
        - recipes with `add_recipe`
    """

    _individual_measurements_to_add: dict[str, list[Measurement]] | None = None
    _individual_measurements_to_remove: dict[str, list[Measurement]] | None = None
    _recipe_registry: RecipeRegistry | None = None

    def __init__(self, *args, **kwargs) -> None:
        if len(args) > 0:
            raise ValueError("No positional arguments are allowed.")

        super().__init__(**kwargs)

        self._individual_measurements_to_add = collections.defaultdict(list, self._individual_measurements_to_add or {})
        self._individual_measurements_to_remove = collections.defaultdict(
            list, self._individual_measurements_to_remove or {}
        )
        self._recipe_registry = RecipeRegistry()

    def _calculate_combined_measurements(self) -> dict[str, list[Measurement]]:
        combined_measurements = collections.defaultdict(list)
        for measurements in self._individual_measurements_to_add.values():
            for measurement in measurements:
                combined_measurements[measurement.ingredient.name].append(measurement)
        for recipe_name in self._recipe_registry.get_all_recipe_names():
            recipe = self._recipe_registry.get_recipe(recipe_name=recipe_name)
            for measurement in recipe.measurements:
                combined_measurements[measurement.ingredient.name].append(measurement)

        return combined_measurements

    def _printout_nested_ingredients(self, measurements_by_ingredient: list[Measurement]) -> str:
        printout = ""
        for measurement in measurements_by_ingredient:
            printout += f"  {measurement.amount} {measurement.unit}\n"

        return printout

    def _printout_nested_measurements(self) -> str:
        combined_measurements = self._calculate_combined_measurements()

        printout = ""
        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=combined_measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            printout += f"{ingredient_name}\n"
            printout += self._printout_nested_ingredients(measurements_by_ingredient=measurements_by_ingredient)

            measurements_to_remove = self._individual_measurements_to_remove.get(ingredient_name, [])
            if len(measurements_to_remove) > 0:
                for measurement in measurements_to_remove:
                    printout += f"  -{measurement.amount} {measurement.unit}\n"

        return printout

    def __len__(self) -> int:
        combined_measurements = self._calculate_combined_measurements()
        return len(combined_measurements)

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
        self._individual_measurements_to_add[measurement.ingredient.name].append(measurement)
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
        self._individual_measurements_to_remove[measurement.ingredient.name].append(measurement)
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
        return None

    @pydantic.validate_call
    def get_all_recipe_names(self) -> list[str]:
        """Get all recipe names from the currently attached registry."""
        return self._recipe_registry.get_all_recipe_names()

    @pydantic.validate_call
    def get_shopping_list(self) -> str:
        """Get a shopping list by aggregating all contained recipes and measurements."""
        combined_measurements = self._calculate_combined_measurements()

        shopping_list = ""
        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=combined_measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            # TODO: shouldn't be needed once grams are standardized
            measurement_units_per_ingredient = {measurement.unit for measurement in measurements_by_ingredient}
            if len(measurement_units_per_ingredient) > 1:
                message = (
                    f"\nMultiple units found for ingredient '{measurements_by_ingredient[0].ingredient.name}':\n\n[\n"
                    f"{self._printout_nested_ingredients(measurements_by_ingredient=measurements_by_ingredient)}"
                    "]"
                )
                raise ValueError(message)
            measurement_unit = list(measurement_units_per_ingredient)[0]

            total_per_ingredient_to_add = sum(measurement.amount for measurement in measurements_by_ingredient)
            total_per_ingredient_to_remove = sum(
                measurement.amount for measurement in self._individual_measurements_to_remove.get(ingredient_name, [])
            )
            total_per_ingredient = total_per_ingredient_to_add - total_per_ingredient_to_remove

            if total_per_ingredient < 0:
                warnings.warn(
                    message=f"Negative amount of '{ingredient_name}' found in shopping list; ignoring.", stacklevel=2
                )

            if total_per_ingredient == 0:
                continue

            shopping_list += f"{ingredient_name}\n"
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
        if name in default_ingredient_registry:
            ingredient = default_ingredient_registry.get_ingredient(name=name)
        else:
            ingredient = Ingredient(name=name)

        return Measurement(amount=amount, unit=unit, ingredient=ingredient)
