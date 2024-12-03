import datetime
import pathlib
import tkinter
import tkinter.messagebox

import click
import natsort

import como_recipes


class SimpleCoMoApp(tkinter.Tk):
    def __init__(self) -> None:
        """A very simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        # Setup initial window details
        self.title(string="CoMo Meal Selector")

        ico_file_path = pathlib.Path(__file__).parent / "_assets" / "como_icon.ico"
        self.iconbitmap(default=ico_file_path)

        self.main_menu = tkinter.Menu(master=self)
        self.config(menu=self.main_menu)
        self.session_menu = tkinter.Menu(master=self.main_menu)
        self.main_menu.add_cascade(label="Session", menu=self.session_menu)
        self.session_menu.add_command(label="Create")
        self.session_menu.add_command(label="Restore")

        minimum_app_window_width_in_pixels = 535
        minimum_app_window_height_in_pixels = 635
        self.minsize(width=minimum_app_window_width_in_pixels, height=minimum_app_window_height_in_pixels)

        # Dynamic sizing is not supported; clamp maximum size to minimum size
        self.maxsize(width=minimum_app_window_width_in_pixels, height=minimum_app_window_height_in_pixels)
        self.resizable(width=False, height=False)

        # Declare some instance attributes
        self.default_available_index_to_meals: dict[int, str] = {
            index: recipe_name
            for index, recipe_name in enumerate(
                natsort.natsorted(seq=como_recipes.default_recipe_registry.get_all_recipe_names()),
            )
        }
        self.default_available_meals_to_index: dict[str, int] = {
            recipe_name: index for index, recipe_name in self.default_available_index_to_meals.items()
        }

        self.currently_available_index_to_meals: dict[int, str] = self.default_available_index_to_meals.copy()
        self.currently_selected_index_to_meals: dict[int, str] = {}
        self.current_measurement_registry = como_recipes.MeasurementRegistry()

        # Initialize components
        self.available_meals_label = tkinter.Label(master=self, text="Available meals")
        self.selected_meals_label = tkinter.Label(master=self, text="Selected meals")
        self.shopping_list_label = tkinter.Label(master=self, text="Shopping list")

        minimum_available_recipe_width_in_characters = 30
        self.currently_available_meals_search = tkinter.Entry(
            master=self,
            width=minimum_available_recipe_width_in_characters,
        )
        self.currently_available_meals_search.bind(sequence="<KeyRelease>", func=self.update_available_meal_display)

        minimum_number_of_displayed_available_recipes = 20
        self.currently_available_meals_box = tkinter.Listbox(
            self,
            width=minimum_available_recipe_width_in_characters,
            height=minimum_number_of_displayed_available_recipes,
        )
        self.currently_available_meals_box.insert(0, *self.currently_available_index_to_meals.values())
        self.currently_available_meals_box.bind(sequence="<Double-Button-1>", func=self.add_selected_meal)

        minimum_number_of_displayed_selected_recipes = 15
        self.selected_meals_box = tkinter.Listbox(
            self,
            width=minimum_available_recipe_width_in_characters,
            height=minimum_number_of_displayed_selected_recipes,
        )
        self.selected_meals_box.bind(sequence="<Double-Button-1>", func=self.remove_selected_meal)

        self.warnings_labels = tkinter.Label(master=self, text="")

        minimum_number_of_displayed_measurements = 35
        self.shopping_list_box = tkinter.Listbox(
            self,
            width=minimum_available_recipe_width_in_characters,
            height=minimum_number_of_displayed_measurements,
        )

        self.open_shopping_list_button = tkinter.Button(
            master=self,
            text="Open shopping list",
            command=self.open_shopping_list,
        )

        # Organize components on grid
        self.available_meals_label.grid(row=0, column=0)
        self.currently_available_meals_search.grid(row=1, column=0, sticky="n")
        self.currently_available_meals_box.grid(row=2, column=0, sticky="n")

        self.warnings_labels.grid(row=0, column=4, rowspan=4, sticky="n")

        self.selected_meals_label.grid(row=3, column=0)
        self.selected_meals_box.grid(row=4, column=0, rowspan=4, sticky="n")

        self.shopping_list_label.grid(row=0, column=1)
        self.shopping_list_box.grid(row=1, column=1, rowspan=4, sticky="n")

        self.open_shopping_list_button.grid(row=5, column=1)

    def update_available_meal_display(self, event: tkinter.Event | None = None) -> None:
        """
        Update the list of displayed meals based on the search query.

        Intended to be as 'smart' as possible.
        """
        if self.currently_available_meals_search.get() == "":
            data = self.currently_available_index_to_meals.values()
        else:
            value = self.currently_available_meals_search.get()
            data = [item for item in self.currently_available_index_to_meals.values() if value.lower() in item.lower()]
        sorted_data = natsort.natsorted(seq=data)

        # TODO: could improve the laziness/performance of add/remove operations w.r.t. current search query instead of
        # regenerating entire search every time
        self.currently_available_meals_box.delete(first=0, last="end")
        self.currently_available_meals_box.insert("end", *sorted_data)

    def update_shopping_list(self) -> None:
        """Update the shopping list based on the selected meals."""
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

    def add_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the available list to the selected list."""
        selected_meal = self.currently_available_meals_box.get(tkinter.ACTIVE)
        meal_index = self.default_available_meals_to_index[selected_meal]

        self.selected_meals_box.insert("end", selected_meal)

        self.currently_selected_index_to_meals[meal_index] = selected_meal
        self.currently_available_index_to_meals.pop(meal_index)
        self.update_available_meal_display()

        self.current_measurement_registry.add_recipe(
            recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name=selected_meal),
        )
        self.update_shopping_list()

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        selected_meal = self.selected_meals_box.get(tkinter.ACTIVE)
        meal_index = self.default_available_meals_to_index[selected_meal]

        self.selected_meals_box.delete(tkinter.ACTIVE)

        self.currently_selected_index_to_meals.pop(meal_index)
        self.currently_available_index_to_meals[meal_index] = selected_meal
        self.update_available_meal_display()

        self.current_measurement_registry.remove_recipe(recipe_name=selected_meal)
        self.update_shopping_list()


if __name__ == "__main__":
    app = SimpleCoMoApp()
    app.mainloop()
