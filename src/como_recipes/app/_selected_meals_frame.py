import tkinter
import tkinter.messagebox
import typing

from ._app_globals import recipe_types
from ._app_utils import _generate_default_app_state


class SelectedMealsFrame(tkinter.Frame):

    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        app_state: dict[str, typing.Any] | None = None,
        minimum_available_recipe_width_in_characters: int = 45,
        minimum_number_of_displayed_selected_recipes: int = 15,
    ) -> None:
        """A modular component for displaying currently selected recipes."""
        super().__init__(master=master)
        self.app_state = app_state or _generate_default_app_state()

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_selected_recipes = minimum_number_of_displayed_selected_recipes

        self.recipe_names_to_hierarchy: dict[tuple[str, ...], dict[typing.Literal[recipe_types], tuple[str, ...]]] = {}
        self.recipe_names_to_format: dict[tuple[str, ...], tuple[str]] = {}

        # Setup initial frame
        self.selected_meals_label = tkinter.Label(master=self, text="Selected meals")

        self.selected_meals_list_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_selected_recipes,
        )

        self.selected_meals_label.pack(side="top", pady=2.5)
        self.selected_meals_list_box.pack(side="top", pady=2.5)

        # Bind callbacks
        self.selected_meals_list_box.bind(
            sequence="<Double-Button-1>",
            func=self.remove_selected_meal,
        )

    def update_frame(self) -> None:
        """Update the frame with the latest selected meals."""
        self.selected_meals_list_box.delete(first=0, last="end")
        self.recipe_names_to_format = self.app_state["meal_selection"].format_selected_meals()
        self.selected_meals_list_box.insert("end", *tuple(self.recipe_names_to_format.values()))

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        formatted_name = self.selected_meals_list_box.get(first="active")

        formatted_name_to_recipe_names = {
            formatted_name: recipe_names for recipe_names, formatted_name in self.recipe_names_to_format.items()
        }
        recipe_names = formatted_name_to_recipe_names[formatted_name]

        self.selected_meals_list_box.delete(first="active")

        self.app_state["meal_selection"].remove_meal(recipe_names=recipe_names)

        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()
