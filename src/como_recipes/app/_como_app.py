import pathlib
import sys
import tkinter
import tkinter.messagebox
import webbrowser

import como_recipes


class CoMoApp(tkinter.Tk):
    def __init__(
        self,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_selected_recipes: int = 15,
        minimum_number_of_displayed_measurements: int = 35,
        minimum_number_of_displayed_available_recipes: int = 20,
    ) -> None:
        """A relatively simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        self.title(string="CoMo Meal Selector")

        # Must determine if path to asset is relative (in dev mode) or frozen (in production mode)
        base_path = pathlib.Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else pathlib.Path(__file__).parent.parent

        # Setup icon
        ico_file_path = base_path / "_assets" / "como_icon.ico"
        self.iconbitmap(default=ico_file_path)

        # Setup menus
        self.main_menu = tkinter.Menu(master=self, tearoff=False)
        self.config(menu=self.main_menu)

        self.session_menu = tkinter.Menu(master=self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Session", menu=self.session_menu)
        self.session_menu.add_command(label="Start new")
        self.session_menu.add_command(label="Restore previous")

        self.help_menu = tkinter.Menu(master=self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Submit issue", command=self._open_github_issue_page)

        # Components do not currently support dynamic resizing, so just freeze window size
        self.resizable(width=False, height=False)

        # Initialize all frames or components that comprise the app
        self.current_available_meals_frame = como_recipes.app.AvailableRecipeSelector(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_available_recipes=minimum_number_of_displayed_available_recipes,
        )
        # TODO: ideally all of these outer-level variable pointers wouldn't be necessary
        self.currently_available_index_to_meals = self.current_available_meals_frame.currently_available_index_to_meals
        self.current_available_meals_frame.currently_available_meals_box.bind(
            sequence="<Double-Button-1>",
            func=self.add_selected_meal,
        )

        self.shopping_list_frame = como_recipes.app.ShoppingListBox(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_measurements=minimum_number_of_displayed_measurements,
        )
        self.current_measurement_registry = self.shopping_list_frame.current_measurement_registry

        self.current_recipe_selection_frame = como_recipes.app.CurrentRecipeSelection(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_selected_recipes=minimum_number_of_displayed_selected_recipes,
        )
        self.selected_meals_box = self.current_recipe_selection_frame.selected_meals_box
        self.current_recipe_selection_frame.selected_meals_box.bind(
            sequence="<Double-Button-1>",
            func=self.remove_selected_meal,
        )

        # Organize frames on grid
        self.current_available_meals_frame.grid(row=0, column=0, padx=5, pady=5)
        self.current_recipe_selection_frame.grid(row=1, column=0, padx=5, pady=5)
        self.shopping_list_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

    def _open_github_issue_page(self) -> None:
        """Open the GitHub issue page for the CoMo project."""
        webbrowser.open_new("https://github.com/CodyCBakerPhD/como_recipes/issues/new/choose")

    def add_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the available list to the selected list."""
        selected_meal = self.current_available_meals_frame.currently_available_meals_box.get(first="active")
        meal_index = self.current_available_meals_frame.default_available_meals_to_index[selected_meal]

        self.current_recipe_selection_frame.selected_meals_box.insert("end", selected_meal)

        self.current_recipe_selection_frame.currently_selected_index_to_meals[meal_index] = selected_meal
        self.current_available_meals_frame.currently_available_index_to_meals.pop(meal_index)
        self.current_available_meals_frame.update_available_meal_display()

        self.shopping_list_frame.current_measurement_registry.add_recipe(
            recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=selected_meal),
        )
        self.shopping_list_frame.update_shopping_list()

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        selected_meal = self.current_recipe_selection_frame.selected_meals_box.get(first="active")
        meal_index = self.current_available_meals_frame.default_available_meals_to_index[selected_meal]

        self.current_recipe_selection_frame.selected_meals_box.delete(first="active")

        self.current_recipe_selection_frame.currently_selected_index_to_meals.pop(meal_index)
        self.current_available_meals_frame.currently_available_index_to_meals[meal_index] = selected_meal
        self.current_available_meals_frame.update_available_meal_display()

        self.shopping_list_frame.current_measurement_registry.remove_recipe(recipe_name=selected_meal)
        self.shopping_list_frame.update_shopping_list()


if __name__ == "__main__":
    app = CoMoApp()
    app.mainloop()
