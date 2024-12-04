import tkinter
import tkinter.messagebox

import click

from ._utils import _generate_new_default_session_id, _get_home_folder
from .._measurement_registration import MeasurementRegistry


class ShoppingListBox(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        session_id: str | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_measurements: int = 35,
    ) -> None:
        """A modular component for displaying, writing, and externally opening a shopping list."""
        super().__init__(master=master)

        # Setup local app folders
        self.home_folder_path = _get_home_folder()
        self.home_folder_path.mkdir(exist_ok=True)

        session_id = session_id or _generate_new_default_session_id()
        self.session_folder_path = self.home_folder_path / session_id
        self.session_folder_path.mkdir(exist_ok=False)

        # Setup attributes and subcomponents
        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_measurements = minimum_number_of_displayed_measurements

        self.setup_attributes()
        self.setup_frame()

    def setup_attributes(self) -> None:
        """Define all mutable attributes used to control underlying states of the application."""
        self.current_measurement_registry = MeasurementRegistry()

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        self.shopping_list_label = tkinter.Label(master=self, text="Shopping list")
        self.shopping_list_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_measurements,
        )

        self.open_shopping_list_button = tkinter.Button(
            master=self,
            text="Open shopping list",
            command=self.open_shopping_list,
        )

        self.shopping_list_label.pack(side="top", pady=5)
        self.shopping_list_box.pack(side="top")
        self.open_shopping_list_button.pack(side="top", pady=5)

    def update_shopping_list(self) -> None:
        """Update the shopping list from the current registry."""
        # TODO: enable when all units are in grams
        # shopping_list = self.current_measurement_registry.get_shopping_list().split("\n")
        shopping_list = str(self.current_measurement_registry).split("\n")
        self.shopping_list_box.delete(first=0, last="end")
        self.shopping_list_box.insert("end", *shopping_list)

    def open_shopping_list(self) -> None:
        """Write the shopping list to a file and open default text editor on that file."""
        # TODO: enable when all units are in grams
        # shopping_list = self.current_measurement_registry.get_shopping_list()
        shopping_list = str(self.current_measurement_registry)

        shopping_list_file_path = self.session_folder_path / "shopping_list.txt"
        with shopping_list_file_path.open(mode="w") as io:
            io.write(shopping_list)

        click.edit(filename=str(shopping_list_file_path))
