import tkinter
import tkinter.messagebox


class SelectedRecipesFrame(tkinter.Frame):

    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        selected_index_to_meals: dict[int, str] | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_selected_recipes: int = 15,
    ) -> None:
        """A modular component for displaying currently selected recipes."""
        super().__init__(master=master)

        self.selected_index_to_meals = selected_index_to_meals or {}
        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_selected_recipes = minimum_number_of_displayed_selected_recipes

        self.setup_frame()

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        self.selected_meals_label = tkinter.Label(master=self, text="Selected meals")

        self.selected_meals_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_selected_recipes,
        )

        self.selected_meals_label.pack(side="top", pady=2.5)
        self.selected_meals_box.pack(side="top", pady=2.5)
