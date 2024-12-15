import collections
import typing
import warnings

import natsort
import pydantic

from ._base._base_ingredient import Ingredient
from ._base._base_meal import Meal
from ._base._base_measurement import Measurement


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
    _recipe_names_to_meal: dict[tuple[str, ...], Meal] | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

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
        self._recipe_names_to_meal = collections.defaultdict(list, self._recipe_names_to_meal or {})

    def __len__(self) -> int:
        """
        Logic defining the `len` operator.

        Does not apply to this class as it is multivalued.
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

        if any(self._recipe_names_to_meal):
            representation += "\t_meals={\n"
            for recipe_names in self._recipe_names_to_meal:
                representation += f"\t\t{recipe_names}: como_recipes.Meal(...),\n"
            representation += "\t},\n"

        attribute_name_to_individual_measurements = {
            "_individual_measurements_to_add": self._individual_measurements_to_add,
            "_individual_measurements_to_remove": self._individual_measurements_to_remove,
        }
        for attribute_name, individual_measurements in attribute_name_to_individual_measurements.items():
            if any(individual_measurements):
                representation += f"\t{attribute_name}=" + "{\n"
                for ingredient_name, measurements in individual_measurements.items():
                    representation += f'\t\t"{ingredient_name}": [\n'
                    for measurement in measurements:
                        representation += f"\t\t\t{measurement!r},\n"
                    representation += "\t\t],\n"

                    # TODO: something like this when grams are standardized
                    # total_amount = sum(measurement.amount for measurement in measurements)
                    # measurement_string = (
                    #     f"como_recipes.Measurement(amount={total_amount}, unit={measurements.unit}, "
                    #     f"ingredient={measurement.ingredient!r})"
                    # )

                representation += "\t},\n"
        representation += ")\n"

        return representation

    def __str__(self) -> str:
        """
        Logic defining the `str` operator, which occurs either on casting to a string or when `print(...)` is called.

        This is intended to be as human-readable as possible.

        As a style choice, the printout is padded before and after with empty space.
        """
        if self.is_empty():
            return "\ncomo_recipes.MealSelection()\n"

        printout = "\n"

        if any(self._recipe_names_to_meal):
            meal_string = "meal" if len(self._recipe_names_to_meal) == 1 else "meals"

            header = f"{len(self._recipe_names_to_meal)} selected {meal_string}"
            printout += header + "\n" + "-" * len(header) + "\n\n"
            for recipe_names in self._recipe_names_to_meal:
                recipe_names_string = ", ".join(f"{recipe_name}" for recipe_name in recipe_names)
                printout += f"{recipe_names_string}\n"
            printout += "\n\n"

        operation_string_to_individual_measurements = {
            "added": self._individual_measurements_to_add,
            "removed": self._individual_measurements_to_remove,
        }
        for operation_string, individual_measurements in operation_string_to_individual_measurements.items():
            if any(individual_measurements):
                plural_string = "measurement" if len(self._individual_measurements_to_add) == 1 else "measurements"

                header = f"{len(individual_measurements)} {operation_string} {plural_string}"
                printout += header + "\n" + "-" * len(header) + "\n\n"
                for measurement in individual_measurements:
                    printout += f"{measurement!s}\n"
                printout += "\n\n"

        if printout[-3:] == "\n\n\n":
            printout = printout[:-2]

        return printout

    def __contains__(self, recipe_name: str) -> bool:
        """
        Logic defining the `in` operator.

        Intended to be used to ask if a recipe name is a part  of any meal in the selection.
        """
        # TODO: could make a lookup table for O(1) speed
        result = any(recipe_name in recipe_names for recipe_names in self._recipe_names_to_meal)

        return result

    def _calculate_combined_measurements(self) -> dict[str, list[Measurement]]:
        combined_measurements = collections.defaultdict(list)
        for measurements in self._individual_measurements_to_add.values():
            for measurement in measurements:
                combined_measurements[measurement.ingredient.name].append(measurement)
        for meal in self._recipe_names_to_meal.values():
            for recipe in meal.get_recipes_by_type():
                for measurement in recipe.measurements:
                    combined_measurements[measurement.ingredient.name].append(measurement)

        return combined_measurements

    def is_empty(self) -> bool:
        """Check if the meal selection is empty."""
        is_any_not_empty = any(
            any(attribute)
            for attribute in (
                self._individual_measurements_to_add,
                self._individual_measurements_to_remove,
                self._recipe_names_to_meal,
            )
        )

        return not is_any_not_empty

    @pydantic.validate_call
    def add_meal(self, *, meal: Meal) -> None:
        """
        Add a meal to the meal selector.

        Parameters
        ----------
        meal : Recipe
            Meal to add to the meal selector.

        """
        recipe_names = tuple(recipe.name for recipe in meal.get_recipes_by_type())
        self._recipe_names_to_meal[recipe_names] = meal

    @pydantic.validate_call
    def remove_meal(self, *, recipe_names: tuple[str, ...]) -> None:
        """
        Remove a meal (as defined by the ordered recipe names) from the meal selector.

        Parameters
        ----------
        recipe_names : tuple of strings
            Ordered names of the recipes comprising the meal to be removed from the meal selector.

        """
        self._recipe_names_to_meal.pop(recipe_names)

    def get_all_recipe_names(self) -> list[tuple[str, ...]]:
        """Get all meals in the meal selection."""
        result = list(self._recipe_names_to_meal.keys())

        return result

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
    def get_raw_measurement_list(self) -> list[str]:
        """Get a raw list of measurements by ingredient, including those to be removed."""
        if self.is_empty():
            message = "No meals or measurements have been added to the meal selection."

            raise ValueError(message)

        combined_measurements = self._calculate_combined_measurements()

        raw_measurement_list = ["Raw Ingredient List"]
        raw_measurement_list.append("-" * len(raw_measurement_list[0]))

        for ingredient_name, measurements_by_ingredient in natsort.natsorted(
            seq=combined_measurements.items(),
            key=lambda item_tuple: item_tuple[0],
        ):
            raw_measurement_list.append(f"☐  {ingredient_name}")
            raw_measurement_list.extend(
                [f"    {measurement.amount} {measurement.unit}" for measurement in measurements_by_ingredient],
            )

        return raw_measurement_list

    def _printout_nested_ingredients(self, measurements_by_ingredient: list[Measurement]) -> str:
        """TODO: plan is to deprecate this method once grams are standardized."""
        printout = ""
        for measurement in measurements_by_ingredient:
            printout += f"  {measurement.amount} {measurement.unit}\n"

        return printout

    @pydantic.validate_call
    def get_shopping_list(self) -> list[str]:
        """Get a shopping list by aggregating all contained recipes and measurements."""
        if self.is_empty():
            message = "No meals or measurements have been added to the meal selection."

            raise ValueError(message)

        combined_measurements = self._calculate_combined_measurements()

        shopping_list = ["Meals\n-----\n\n"]
        shopping_list.extend([f"☐ {recipe_names}\n" for recipe_names in self._recipe_names_to_meal.keys()])
        shopping_list.append("\n\n\nIngredients\n-----------\n\n")

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

            shopping_list.append(f"☐  {ingredient_name}\n")
            shopping_list.append(f"    {total_per_ingredient} {measurement_unit}\n")

        return shopping_list

    @pydantic.validate_call
    def to_json_dictionary(self) -> dict:
        """Convert the meal selection to an in-memory JSON-compatible dictionary."""
        individual_measurements_to_add = {
            ingredient_name: [
                {
                    "amount": measurement.amount,
                    "unit": measurement.unit,
                    "ingredient": {
                        "name": measurement.ingredient.name,
                        "default_grams_per_package": measurement.ingredient.default_grams_per_package,
                        "default_package_unit": measurement.ingredient.default_package_unit,
                    },
                }
                for measurement in measurements
            ]
            for ingredient_name, measurements in self._individual_measurements_to_add.items()
        }
        individual_measurements_to_remove = {
            ingredient_name: [
                {
                    "amount": measurement.amount,
                    "unit": measurement.unit,
                    "ingredient": {
                        "name": measurement.ingredient.name,
                        "default_grams_per_package": measurement.ingredient.default_grams_per_package,
                        "default_package_unit": measurement.ingredient.default_package_unit,
                    },
                }
                for measurement in measurements
            ]
            for ingredient_name, measurements in self._individual_measurements_to_remove.items()
        }
        recipe_names_to_meal = {
            ",".join(recipe_names): meal.to_json_dictionary()
            for recipe_names, meal in self._recipe_names_to_meal.items()
        }

        dictionary = {
            "_individual_measurements_to_add": individual_measurements_to_add,
            "_individual_measurements_to_remove": individual_measurements_to_remove,
            "_recipe_names_to_meal": recipe_names_to_meal,
        }

        return dictionary

    @classmethod
    @pydantic.validate_call
    def from_json_dictionary(cls, *, dictionary: dict) -> typing.Self:
        """Construct a new meal selection from an in-memory JSON-compatible dictionary."""
        individual_measurements_to_add = {
            ingredient_name: [
                Measurement(
                    amount=measurement["amount"],
                    unit=measurement["unit"],
                    ingredient=Ingredient(
                        name=measurement["ingredient"]["name"],
                        default_grams_per_package=measurement["ingredient"]["default_grams_per_package"],
                        default_package_unit=measurement["ingredient"]["default_package_unit"],
                    ),
                )
                for measurement in measurements
            ]
            for ingredient_name, measurements in dictionary["_individual_measurements_to_add"].items()
        }
        individual_measurements_to_remove = {
            ingredient_name: [
                Measurement(
                    amount=measurement["amount"],
                    unit=measurement["unit"],
                    ingredient=Ingredient(
                        name=measurement["ingredient"]["name"],
                        default_grams_per_package=measurement["ingredient"]["default_grams_per_package"],
                        default_package_unit=measurement["ingredient"]["default_package_unit"],
                    ),
                )
                for measurement in measurements
            ]
            for ingredient_name, measurements in dictionary["_individual_measurements_to_remove"].items()
        }
        recipe_names_to_meal = {
            tuple(recipe_names.split(",")): Meal.from_json_dictionary(dictionary=meal)
            for recipe_names, meal in dictionary["_recipe_names_to_meal"].items()
        }

        meal_selector = MealSelection()
        meal_selector._individual_measurements_to_add = individual_measurements_to_add  # noqa: SLF001
        meal_selector._individual_measurements_to_remove = individual_measurements_to_remove  # noqa: SLF001
        meal_selector._recipe_names_to_meal = recipe_names_to_meal  # noqa: SLF001

        return meal_selector
