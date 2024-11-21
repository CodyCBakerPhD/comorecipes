import math

import pydantic


class Ingredient(pydantic.BaseModel):
    """
    Automatically validated base data class for all ingredients.

    Parameters
    ----------
    name : str
        Name of the ingredient.
    default_package_size_in_grams : int | float | None, optional
        Size of the default package (in grams) as commonly found in stores.
    default_package_unit : str | None, optional
        Unit of the default package size as commonly found in stores.

    """

    name: str
    default_grams_per_package: int | float | None = None
    default_package_unit: str | None = None

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        representation = f'Ingredient(name="{self.name}"'
        if self.default_grams_per_package is not None:
            representation += f", default_grams_per_package={self.default_grams_per_package}"
        if self.default_package_unit is not None:
            representation += f', default_package_unit="{self.default_package_unit}"'
        representation += ")"

        return representation

    @pydantic.validate_call
    def get_number_of_packages(self, *, amount_in_grams: int | float) -> int:
        """Convert the amount of this ingredient to the default package size."""
        if self.default_grams_per_package is None or self.default_package_unit is None:
            message = "The default size or unit of packages containing this ingredient is not specified."
            raise NotImplementedError(message)

        return int(math.ceil(amount_in_grams / self.default_grams_per_package))
