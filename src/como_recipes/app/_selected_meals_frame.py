import tkinter
import tkinter.messagebox

from ._app_utils import _generate_default_app_state


class SelectedMealsFrame(tkinter.Frame):

    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_available_recipe_width_in_characters: int = 45,
        minimum_number_of_displayed_selected_recipes: int = 15,
    ) -> None:
        """A modular component for displaying currently selected recipes."""
        super().__init__(master=master)
        self.app_state = getattr(self.master, "app_state", None) or _generate_default_app_state()

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_selected_recipes = minimum_number_of_displayed_selected_recipes

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

        formatted_recipe_names = [
            " + ".join(recipe_names) for recipe_names in self.app_state["meal_selection"].get_all_recipe_names()
        ]
        self.selected_meals_list_box.insert("end", *formatted_recipe_names)

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        selected_meal = self.selected_meals_list_box.get(first="active")
        recipe_names = tuple(recipe_name for recipe_name in selected_meal.split(" + "))
        # meal_index = default_recipe_name_to_index[recipe_names[0]]

        self.selected_meals_list_box.delete(first="active")

        # self.app_state["selected_index_to_meals"].pop(meal_index)  # Why do we need this?
        self.app_state["meal_selection"].remove_meal(
            recipe_names=tuple(recipe_name for recipe_name in recipe_names),
        )

        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()
