import tkinter
import tkinter.messagebox

import click

from ._app_utils import _generate_new_default_session_id, _get_home_folder
from .._meal_selection import MealSelection


class ShoppingListFrame(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_measurements: int = 35,
    ) -> None:
        """A modular component for displaying, writing, and externally opening a shopping list."""
        super().__init__(master=master)

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_measurements = minimum_number_of_displayed_measurements

        # Setup initial attributes
        self.session_folder_path = _get_home_folder() / _generate_new_default_session_id()
        self.meal_selection = MealSelection()

        # Setup initial components
        self.label = tkinter.Label(master=self, text="Shopping list")
        self.list_box = tkinter.Listbox(
            self,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_measurements,
        )

        self.button = tkinter.Button(
            master=self,
            text="Open shopping list",
            command=self.open_shopping_list,
        )

        self.label.pack(side="top", pady=2.5)
        self.list_box.pack(side="top", padx=2.5, pady=2.5)
        self.button.pack(side="top", pady=2.5)

    def update_frame(self) -> None:
        """Update the shopping list from the current registry."""
        try:
            shopping_list = self.meal_selection.get_shopping_list().split("\n")
        except Exception:  # noqa: BLE001
            shopping_list = []
        self.list_box.delete(first=0, last="end")
        self.list_box.insert("end", *shopping_list)

    def open_shopping_list(self) -> None:
        """Write the shopping list to a file and open default text editor on that file."""
        try:
            shopping_list_string = "\n".join(self.meal_selection.get_shopping_list().split("\n"))
        except Exception:  # noqa: BLE001
            tkinter.messagebox.showerror(
                title="Error",
                message="Error generating shopping list.\nPlease use the raw ingredient list instead.",
            )
            return None

        self.session_folder_path.mkdir(exist_ok=True)
        shopping_list_file_path = self.session_folder_path / "shopping_list.txt"
        with shopping_list_file_path.open(mode="w", encoding="utf-8") as io:
            io.write(shopping_list_string)

        click.edit(filename=str(shopping_list_file_path))

        return None
