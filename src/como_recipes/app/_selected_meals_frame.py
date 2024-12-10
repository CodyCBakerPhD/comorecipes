import tkinter
import tkinter.messagebox

from .._meal_selection import MealSelection


class SelectedMealsFrame(tkinter.Frame):

    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_available_recipe_width_in_characters: int = 45,
        minimum_number_of_displayed_selected_recipes: int = 15,
    ) -> None:
        """A modular component for displaying currently selected recipes."""
        super().__init__(master=master)

        self.app_state = {"meal_selection": MealSelection()}

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_selected_recipes = minimum_number_of_displayed_selected_recipes

        # Setup initial frame
        self.selected_meals_label = tkinter.Label(master=self, text="Selected meals")

        self.selected_meals_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_selected_recipes,
        )

        self.selected_meals_label.pack(side="top", pady=2.5)
        self.selected_meals_box.pack(side="top", pady=2.5)

    def update_frame(self) -> None:
        """Update the frame with the latest selected meals."""
        self.selected_meals_box.delete(first=0, last="end")

        formatted_recipe_names = [
            " + ".join(recipe_names) for recipe_names in self.app_state["meal_selection"].get_all_recipe_names()
        ]
        self.selected_meals_box.insert("end", *formatted_recipe_names)
