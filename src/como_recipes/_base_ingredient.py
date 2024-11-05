import pydantic


class Ingredient(pydantic.BaseModel):
    """
    Automatically validated base data class for all ingredients.

    Parameters
    ----------
    name : str
        Name of the ingredient.
    grams_to_default_package_conversion : int | float | None, optional
        Conversion factor to the default package size as commonly found in stores.
    default_package_unit : str | None, optional
        Unit of the default package size as commonly found in stores.
    """

    name: str
    grams_to_default_package_conversion: int | float | None = None
    default_package_unit: str | None = None

    @pydantic.validate_call
    def convert_amount_to_package_size(self, *, amount: int | float, unit: str) -> int | float:
        """Convert the amount of this ingredient to the default package size."""
        if self.grams_to_default_package_conversion is None or self.default_package_size is None:
            raise NotImplementedError(
                "The default size or conversion of packages containing this ingredient is not specified."
            )
        if unit != "g":
            raise NotImplementedError(
                "The conversion rule for an ingredient amount to the default size of a package is not specified."
            )

        return amount / self.default_package_size
