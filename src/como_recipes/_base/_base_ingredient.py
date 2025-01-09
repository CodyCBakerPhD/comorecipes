import math
import typing

import pydantic
import yaml


class Ingredient(pydantic.BaseModel):
    """
    An ingredient is a single food item to be shopped for and therefore includes package information as found in stores.

    Parameters
    ----------
    name : str
        Name of the ingredient.
    default_grams_per_package : numeric, optional
        Size of the default package (in grams) as commonly found in stores.
        If this size is variable (such as garlic heads), then the lower end of the range is estimated.
    default_package_unit : string, optional
        Unit of the default package size as commonly found in stores.
    portions_text : string, optional
        Special text for the portions of the ingredient.
        For example, "cloves" for the ingredient named "garlic".

    """

    name: str
    default_grams_per_package: int | float | None = None
    default_package_unit: str | None = None
    portions_text: str | None = None
    model_config = pydantic.ConfigDict(extra="forbid")

    def __repr__(self) -> str:
        """Used in programmatic places, such as equality assertions in the tests."""
        representation = f'Ingredient(name="{self.name}"'
        if self.default_grams_per_package is not None:
            representation += f", default_grams_per_package={self.default_grams_per_package}"
        if self.default_package_unit is not None:
            representation += f', default_package_unit="{self.default_package_unit}"'
        if self.portions_text is not None:
            representation += f', portions_text="{self.portions_text}"'
        representation += ")"

        return representation

    def __eq__(self, other: "Ingredient") -> bool:
        """
        Logic defining the `==` operator.

        Primarily used by consistency assertions in the tests.

        Compares only the contained fields of the object, not including its memory address (two imported instances
        of the class with the same fields will be considered equal).
        """
        fields_to_compare = ["name", "default_grams_per_package", "default_package_unit"]
        result = all(getattr(self, field) == getattr(other, field) for field in fields_to_compare)

        return result

    @pydantic.validate_call
    def get_number_of_packages(self, *, amount_in_grams: int | float) -> int:
        """Convert the amount of this ingredient to the default package size."""
        if self.default_grams_per_package is None or self.default_package_unit is None:
            message = "The default size or unit of packages containing this ingredient is not specified."
            raise NotImplementedError(message)

        return int(math.ceil(amount_in_grams / self.default_grams_per_package))

    @pydantic.validate_call
    def to_yaml_file(self, *, file_path: pydantic.NewPath | pydantic.FilePath) -> None:
        """
        Save ingredient to a .yaml file.

        Parameters
        ----------
        file_path : pydantic.NewPath
            Path to the .yaml file

        """
        data = {
            "name": self.name,
            "default_grams_per_package": self.default_grams_per_package,
            "default_package_unit": self.default_package_unit,
            "portions_text": self.portions_text,
        }
        with file_path.open(mode="w") as io:
            yaml.dump(data=data, stream=io)

    @classmethod
    @pydantic.validate_call
    def from_yaml_file(cls, *, file_path: pydantic.FilePath) -> typing.Self:
        """
        Load ingredient from a .yaml file.

        Parameters
        ----------
        file_path : pydantic.FilePath
            Path to the .yaml file.

        """
        with file_path.open(mode="r") as io:
            ingredient_info = yaml.safe_load(stream=io)

        return cls(**ingredient_info)
