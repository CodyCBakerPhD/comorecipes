import tkinter
import typing

from ._app_utils import _generate_default_app_state
from ._available_recipes_frame import AvailableRecipesFrame
from ._selected_meals_frame import SelectedMealsFrame


class MealAssembler(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        app_state: dict[str, typing.Any] | None = None,
    ) -> None:
        """A modular component for assembling meals."""
        super().__init__()
        self.app_state = app_state or _generate_default_app_state()

        self.available_recipes_by_type_subframe = tkinter.Frame(master=self)
        self.available_recipes_by_type_subframe.grid(row=0, column=0, padx=2.5, pady=2.5)

        self.entree_subframe = AvailableRecipesFrame(
            master=self.available_recipes_by_type_subframe,
            recipe_type="Entree",
        )
        self.entree_subframe.grid(row=0, column=0, padx=2.5, pady=2.5)

        self.side_subframe = AvailableRecipesFrame(master=self.available_recipes_by_type_subframe, recipe_type="Side")
        self.side_subframe.grid(row=0, column=1, padx=2.5, pady=2.5)

        self.dessert_subframe = AvailableRecipesFrame(
            master=self.available_recipes_by_type_subframe,
            recipe_type="Dessert",
        )
        self.dessert_subframe.grid(row=0, column=2, padx=2.5, pady=2.5)

        self.selected_meals_frame = SelectedMealsFrame(master=self)
        self.selected_meals_frame.grid(row=1, columnspan=3, padx=2.5, pady=2.5)
