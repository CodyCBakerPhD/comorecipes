import collections

import pydantic
import natsort

from ._base_recipe import Recipe
from ._ingredient_registration import default_ingredient_registry
from ._base_measurement import Measurement


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

        ingredient = default_ingredient_registry.get_ingredient(name=name)
        return Measurement(amount=amount, unit=unit, ingredient=ingredient)
