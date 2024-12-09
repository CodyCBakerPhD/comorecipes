import collections
import typing
import warnings

import natsort
import pydantic

from ._base._base_ingredient import Ingredient
from ._base._base_meal import Meal
from ._base._base_measurement import Measurement
from ._base._base_recipe import Recipe
from ._registration._ingredient_registry import default_ingredient_registry


class MealSelection(pydantic.BaseModel):
    """
    API for selecting meals.

    Initialize an interactive selection with `MealSelection()` then add:
        - meals with `add_meal`
        - individual measurements with `add_measurement`

    or remove:
        - meals with `remove_meal`
        - individual measurements with `remove_measurement`
    """

    _individual_measurements_to_add: dict[str, list[Measurement]] | None = None
    _individual_measurements_to_remove: dict[str, list[Measurement]] | None = None
    _meals: list[Meal, ...] | None = None

    def __init__(self, *args: list[typing.Any], **kwargs: dict[typing.Any, typing.Any]) -> None:
        if len(args) > 0:
            message = "No positional arguments are allowed."
            raise ValueError(message)

        super().__init__(**kwargs)

        self._individual_measurements_to_add = collections.defaultdict(list, self._individual_measurements_to_add or {})
        self._individual_measurements_to_remove = collections.defaultdict(
            list,
            self._individual_measurements_to_remove or {},
        )
        self._meals = self._meals or []

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Calculates and returns the total number of measured ingredients combined across recipes and manual additions.
        """
        message = "The MealSelection class has no intuitive notion of length."

        raise NotImplementedError(message)

    def __repr__(self) -> str:
        """
        Logic defining the `repr` operator, most commonly used by printout of variables in Python/iPython shells.

        This is intended to be as programmatic (machine-readable) as possible; a user ought to be able to copy and paste
        the representation and run it as code to generate a new instance of the object.

        As a style choice, the representation is padded before and after with empty space.
        """
        if self.is_empty():
            return "\ncomo_recipes.MealSelection()\n"

        representation = "\ncomo_recipes.MealSelection(\n"

        if any(self._meals):
            representation += "\t_meals=[\n"
            for meal in self._meals:
                recipe_names_string = ", ".join(f'"{recipe_name}"' for recipe_name in meal.recipes)
                representation += f"\t\tcomo_recipes.Meal(_recipes=[{recipe_names_string}]),\n"
            representation += "\t],\n"
        if any(self._individual_measurements_to_add):
            representation += "\t_individual_measurements_to_add={\n"
            for ingredient_name, measurement in self._individual_measurements_to_add.items():
                representation += f'\t\t"{ingredient_name}": {measurement!r}\n'
            representation += "\t},\n"
        if any(self._individual_measurements_to_remove):
            representation += "\t_individual_measurements_to_remove={\n"
            for ingredient_name, measurement in self._individual_measurements_to_remove.items():
                representation += f'\t\t"{ingredient_name}": {measurement!r}\n'
            representation += "\t},\n"

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        if self.is_empty():
            return "como_recipes.MealSelection with 0 selected meals or measurements\n"

        printout = ""

        if any(self._meals):
            header = f"{len(self._meals)} selected meals\n"
            printout += header + "-" * len(header) + "\n\n"
            for meal in self._meals:
                recipe_names_string = ", ".join(f'"{recipe_name}"' for recipe_name in meal.recipes)
                printout += f"{recipe_names_string}\n"
            printout += "\n"
        if any(self._individual_measurements_to_add):
            header = f"{len(self._individual_measurements_to_add)} added measurements\n"
            printout += header + "-" * len(header) + "\n\n"
            for measurement in self._individual_measurements_to_add:
                printout += f"{measurement!s}\n"
            printout += "\n"
        if any(self._individual_measurements_to_remove):
            header = f"{len(self._individual_measurements_to_remove)} removed measurements\n"
            printout += header + "-" * len(header) + "\n\n"
            for measurement in self._individual_measurements_to_remove:
                printout += f"{measurement!s}\n"
            printout += "\n"

        return printout

    def is_empty(self) -> bool:
        """Check if the meal selection is empty."""
        is_any_not_empty = any(
            any(attribute)
            for attribute in (
                self._individual_measurements_to_add,
                self._individual_measurements_to_remove,
                self._meals,
            )
        )

        return not is_any_not_empty

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
            seq=combined_measurements.items(),
            key=lambda item_tuple: item_tuple[0],
        ):
            printout += f"{ingredient_name}\n"
            printout += self._printout_nested_ingredients(measurements_by_ingredient=measurements_by_ingredient)

            measurements_to_remove = self._individual_measurements_to_remove.get(ingredient_name, [])
            if len(measurements_to_remove) > 0:
                for measurement in measurements_to_remove:
                    printout += f"  -{measurement.amount} {measurement.unit}\n"

        return printout

    @pydantic.validate_call
    def add_measurement(self, *, measurement: Measurement) -> None:
        """
        Add a single custom measurement to the registry.

        Parameters
        ----------
        measurement : Measurement
            Measurement to add to the registry.

        """
        self._individual_measurements_to_add[measurement.ingredient.name].append(measurement)

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

    @pydantic.validate_call
    def add_recipe(self, *, recipe: Recipe) -> None:
        """
        Add a recipe (and by way, all of its constituent measurements) to the registry.

        Parameters
        ----------
        recipe : Recipe
            Recipe to add to the registry.

        """
        self._recipe_registry.add_recipe(recipe=recipe)

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
            seq=combined_measurements.items(),
            key=lambda item_tuple: item_tuple[0],
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
            measurement_unit = next(iter(measurement_units_per_ingredient))

            total_per_ingredient_to_add = sum(measurement.amount for measurement in measurements_by_ingredient)
            total_per_ingredient_to_remove = sum(
                measurement.amount for measurement in self._individual_measurements_to_remove.get(ingredient_name, [])
            )
            total_per_ingredient = total_per_ingredient_to_add - total_per_ingredient_to_remove

            if total_per_ingredient < 0:
                warnings.warn(
                    message=f"Negative amount of '{ingredient_name}' found in shopping list; ignoring.",
                    stacklevel=2,
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

        While this method might intuitively belong to the `IngredientRegistry` class, the interaction with
        the `default_ingredient_registry` makes this impossible due to circularity.

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
