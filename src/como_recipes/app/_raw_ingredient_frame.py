import tkinter
import tkinter.messagebox

import click

from ._app_utils import _generate_new_default_session_id, _get_home_folder
from .._meal_selection import MealSelection


class RawIngredientFrame(tkinter.Frame):
    """
    A modular component for displaying, writing, and externally opening a raw ingredient list.

    Will sometimes conflate the terminology of "ingredients" and "measurements" for simplicity; a user will often
    refer to them interchangeably, but measurements are the true underlying data structure being manipulated whereas
    ingredients are the more user-facing reference to avoid confusion on the frontend.
    """

    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_measurements: int = 35,
    ) -> None:
        super().__init__(master=master)

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_measurements = minimum_number_of_displayed_measurements

        # Setup initial attributes
        self.session_folder_path = _get_home_folder() / _generate_new_default_session_id()
        self.meal_selection = MealSelection()

        # Setup initial components
        self.label = tkinter.Label(master=self, text="Raw ingredients")

        self.add_and_remove_subframe = tkinter.Frame(master=self)
        self.add_button = tkinter.Button(
            master=self.add_and_remove_subframe,
            text="Add ingredient",
            command=self.add_measurement,
        )
        self.remove_button = tkinter.Button(
            master=self.add_and_remove_subframe,
            text="Remove ingredient",
            command=self.remove_measurement,
        )
        self.add_button.pack(side="left", padx=2.5)
        self.remove_button.pack(side="right", padx=2.5)

        self.list_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_measurements,
        )

        self.button = tkinter.Button(
            master=self,
            text="Open raw ingredient list",
            command=self.open_raw_ingredient_list,
        )

        self.label.pack(side="top", pady=2.5)
        self.add_and_remove_subframe.pack(side="top", pady=2.5)
        self.list_box.pack(side="top", pady=2.5)
        self.button.pack(side="top", pady=2.5)

    def add_measurement(self) -> None:
        pass

    def remove_measurement(self) -> None:
        pass

    def update_frame(self) -> None:
        """Update the raw ingredient frame display based on the current meal selection."""
        raw_ingredient_list = self.meal_selection.get_raw_measurement_list()[2:]
        self.list_box.delete(first=0, last="end")
        self.list_box.insert("end", *raw_ingredient_list)

    def open_raw_ingredient_list(self) -> None:
        """Write the raw ingredient list to a file and open default text editor on that file."""
        raw_ingredient_list_string = "\n".join(self.meal_selection.get_raw_measurement_list()[2:])

        self.session_folder_path.mkdir(exist_ok=True)
        raw_ingredient_list_file_path = self.session_folder_path / "raw_ingredient_list.txt"
        with raw_ingredient_list_file_path.open(mode="w", encoding="utf-8") as io:
            io.write(raw_ingredient_list_string)

        click.edit(filename=str(raw_ingredient_list_file_path))
