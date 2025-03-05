import tkinter
import typing

from ._app_globals import exclusive_availability_recipe_types, recipe_types
from ._app_utils import _generate_default_app_state
from ._available_recipes_frame import AvailableRecipesFrame
from ._selected_meals_frame import SelectedMealsFrame
from .._base._base_meal import Meal
from .._registration._default_recipe_registry import default_recipe_registry


class MealAssemblerFrame(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        app_state: dict[str, typing.Any] | None = None,
    ) -> None:
        """A modular component for assembling meals."""
        super().__init__()
        self.app_state = app_state or _generate_default_app_state()

        self.available_recipes_by_type_subframe = tkinter.Frame(master=self)

        self.available_recipes_subframe_by_type = {}
        for recipe_type in recipe_types:
            self.available_recipes_subframe_by_type[recipe_type] = AvailableRecipesFrame(
                master=self.available_recipes_by_type_subframe,
                recipe_type=recipe_type,
                app_state=self.app_state,
            )
            self.available_recipes_subframe_by_type[recipe_type].disable_list_box_callback()

        self.select_meal_button = tkinter.Button(master=self, text="Select meal", command=self.select_meal)

        self.selected_meals_frame = SelectedMealsFrame(
            master=self,
            app_state=self.app_state,
            minimum_available_recipe_width_in_characters=80,
        )

        # Organize grid
        self.available_recipes_by_type_subframe.grid(row=0, column=0, padx=2.5, pady=2.5)

        for column_index, recipe_type in enumerate(recipe_types):
            self.available_recipes_subframe_by_type[recipe_type].grid(
                row=0,
                column=column_index,
                padx=2.5,
                pady=2.5,
                sticky="s",
            )

        self.select_meal_button.grid(row=1, columnspan=3, padx=2.5, pady=2.5)
        self.selected_meals_frame.grid(row=2, columnspan=3, padx=2.5, pady=2.5)

    def select_meal(self) -> None:
        """Select the meal."""
        selected_indices_by_recipe_type: dict[str, tuple[int, ...]] = {}
        for recipe_type in recipe_types:
            indices = self.available_recipes_subframe_by_type[recipe_type].available_meals_list_box.curselection()
            selected_indices_by_recipe_type[recipe_type] = indices

        selected_recipe_names_by_type: dict[str, tuple[str, ...]] = {}
        for recipe_type in recipe_types:
            selected_recipe_names_by_type[recipe_type] = tuple(
                self.available_recipes_subframe_by_type[recipe_type].available_meals_list_box.get(first=index)
                for index in selected_indices_by_recipe_type[recipe_type]
            )

        meal = Meal()
        for recipe_names_per_type in selected_recipe_names_by_type.values():
            for recipe_name in recipe_names_per_type:
                meal.add_recipe(recipe=default_recipe_registry.get_recipe(recipe_name=recipe_name))

        self.app_state["meal_selection"].add_meal(meal=meal)
        for recipe_type in recipe_types:
            self.available_recipes_subframe_by_type[recipe_type].update_available_index_to_recipe_name()

        for recipe_type in recipe_types:
            self.available_recipes_subframe_by_type[recipe_type].available_meals_list_box.selection_clear(0, "end")

        for recipe_type in exclusive_availability_recipe_types:
            self.available_recipes_subframe_by_type[recipe_type].update_available_index_to_recipe_name()

        self.update_frames()

    def update_frame(self) -> None:
        for recipe_type in recipe_types:
            self.available_recipes_subframe_by_type[recipe_type].update_frame()
        self.selected_meals_frame.update_frame()

    def update_frames(self) -> None:
        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()
