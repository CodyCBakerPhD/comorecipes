import datetime
import pathlib
import tkinter
import tkinter.messagebox

import click

import como_recipes


class ShoppingListBox(tkinter.Frame):
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

        self.setup_attributes()
        self.setup_frame()

    def setup_attributes(self) -> None:
        """Define all mutable attributes used to control underlying states of the application."""
        self.current_measurement_registry = como_recipes.MeasurementRegistry()

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

        home_folder = pathlib.Path.home() / ".como_recipes"
        home_folder.mkdir(exist_ok=True)

        shopping_list_folder_path = home_folder / "shopping_lists"
        shopping_list_folder_path.mkdir(exist_ok=True)

        date = datetime.datetime.now().strftime("%Y%m%d")
        shopping_list_file_path = shopping_list_folder_path / f"shopping_list_{date}.txt"

        counter = 0
        maximum_iterations = 100
        while shopping_list_file_path.exists() and counter < maximum_iterations:
            shopping_list_file_path = home_folder / f"shopping_list_{date}_{counter}.txt"
            counter += 1

        if counter == maximum_iterations:
            # TODO: replace with better pop-up
            tkinter.messagebox.showerror(title="Error", message="Too many shopping lists with the current date!")
            return

        with shopping_list_file_path.open(mode="w") as io:
            io.write(shopping_list)

        click.edit(filename=str(shopping_list_file_path))


if __name__ == "__main__":
    app = tkinter.Tk()
    shopping_list_box = ShoppingListBox(master=app)
    shopping_list_box.pack(padx=5)

    shopping_list_box.current_measurement_registry.add_recipe(
        recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"),
    )
    shopping_list_box.update_shopping_list()

    app.mainloop()
