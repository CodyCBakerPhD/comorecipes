import pydantic
import natsort

from ._base_recipe import Recipe


class RecipeRegistry(pydantic.BaseModel):
    recipes: list[Recipe] = []

    def __len__(self) -> int:
        return len(self.recipes)

    def __repr__(self) -> str:
        number_of_registered_recipes = len(self)

        printout = f"{number_of_registered_recipes} registered recipes\n"
        printout += f"{'-' * (len(printout)-1)}\n\n"
        for recipe in natsort.natsorted(seq=self.recipes):
            printout += f"{recipe.name}\n"

        return printout

    def __str__(self) -> str:
        return self.__repr__()

    @pydantic.validate_call
    def update_registry(self, *, recipe: Recipe):
        self.recipes.append(recipe)


# Initialize the global default recipe registry
# Items are explicitly added in their respective recipe files
default_recipe_registry = RecipeRegistry()
