import collections

import pydantic
import natsort

from ._base_recipe import Recipe
from ._base_ingredient import Ingredient
from ._ingredient_registration import default_ingredient_registry
from ._base_measurement import Measurement


class MeasurementRegistry(pydantic.BaseModel):
    _measurements: dict[str, list[Measurement]] = collections.defaultdict(list)

    def __len__(self) -> int:
        return len(self._measurements)

    def __repr__(self) -> str:
        number_of_registered_measurements = len(self)

        printout = f"{number_of_registered_measurements} registered measurements\n"

        if number_of_registered_measurements == 0:
            return printout

        printout += f"{'-' * (len(printout)-1)}\n\n"
        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=self._measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            printout += f"{ingredient_name}\n"
            for measurement in measurements_by_ingredient:
                printout += f"  {measurement.amount} {measurement.unit}\n"

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

    @pydantic.validate_call
    def get_shopping_list(self) -> str:
        """Get a shopping list by aggregating all contained recipes and measurements."""
        shopping_list = ""

        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=self._measurements.items(), key=lambda item_tuple: item_tuple[0]
        ):
            shopping_list += f"{ingredient_name}\n"

            # TODO: shouldn't be needed once grams are standardized
            measurement_units_per_ingredient = {measurement.unit for measurement in measurements_by_ingredient}
            if len(measurement_units_per_ingredient) > 1:
                message = (
                    f"\nMultiple units found for ingredient {measurements_by_ingredient[0].ingredient.name}:\n\n"
                    f"{measurements_by_ingredient}"
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
        # global default_ingredient_registry

        if name in default_ingredient_registry:
            ingredient = default_ingredient_registry.get_ingredient(name=name)
        else:
            ingredient = Ingredient(name=name)

        return Measurement(amount=amount, unit=unit, ingredient=ingredient)
