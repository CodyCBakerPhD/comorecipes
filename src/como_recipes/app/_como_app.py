import importlib.metadata
import pathlib
import sys
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import webbrowser

from ._app_globals import default_recipe_registry
from ._available_recipes_frame import AvailableRecipesFrame
from ._selected_recipes_frame import SelectedRecipesFrame
from ._session_manager_frame import SessionManagerFrame
from ._shopping_list_frame import ShoppingListFrame
from .._meal_selection import MealSelection


class CoMoApp(tkinter.Tk):
    def __init__(self) -> None:
        """A relatively simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        self.setup_window()
        self.setup_frames()

    def setup_window(self) -> None:
        """Initialize the main window and menu bar."""
        # Must determine if path to asset is relative (in dev mode) or frozen (in production mode)
        base_path = pathlib.Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else pathlib.Path(__file__).parent.parent

        # Setup icon
        ico_file_path = base_path / "_assets" / "como_icon.ico"
        self.iconbitmap(default=ico_file_path)

        # Setup window and menus
        self.title(string="CoMo Meal Selector")
        self.main_menu = tkinter.Menu(master=self, tearoff=False)
        self.config(menu=self.main_menu)

        self.help_menu = tkinter.Menu(master=self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Submit issue", command=self._open_github_issue_page)

        # Components do not currently support dynamic resizing, so just freeze window size
        self.resizable(width=False, height=False)

        # Ask for session save on exit
        self.protocol(name="WM_DELETE_WINDOW", func=self._on_closing)

    def setup_frames(
        self,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_selected_recipes: int = 15,
        minimum_number_of_displayed_measurements: int = 35,
        minimum_number_of_displayed_available_recipes: int = 20,
    ) -> None:
        """Initialize all frames or components that comprise the app."""
        self.session_manager_frame = SessionManagerFrame(master=self)

        self.available_meals_frame = AvailableRecipesFrame(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_available_recipes=minimum_number_of_displayed_available_recipes,
        )
        # TODO: ideally all of these outer-level variable pointers wouldn't be necessary
        self.currently_available_index_to_meals = self.available_meals_frame.currently_available_index_to_meals

        self.shopping_list_frame = ShoppingListFrame(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_measurements=minimum_number_of_displayed_measurements,
        )
        self.current_measurement_registry = self.shopping_list_frame.current_measurement_registry

        self.selected_recipes_frame = SelectedRecipesFrame(
            master=self,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_selected_recipes=minimum_number_of_displayed_selected_recipes,
        )
        self.selected_meals_box = self.selected_recipes_frame.selected_meals_box

        package_version = importlib.metadata.version(distribution_name="como_recipes")
        self.version_label = tkinter.Label(master=self, text=f"v{package_version}")

        # Organize frames on grid
        self.session_manager_frame.grid(column=0, rowspan=4, padx=5, pady=5, sticky="NW")
        self.available_meals_frame.grid(row=1, column=1, padx=5, pady=5)
        self.selected_recipes_frame.grid(row=2, column=1, padx=5, pady=5)
        self.shopping_list_frame.grid(row=1, column=2, rowspan=2, padx=5, pady=5)
        self.version_label.grid(row=3, columnspan=3, sticky="se")

        # Link cross-frame attributes
        self.session_folder_path = self.session_manager_frame.session_folder_path
        self.selected_index_to_meals = self.session_manager_frame.selected_index_to_meals
        self.tags_to_checkbox_values = self.session_manager_frame.tags_to_checkbox_values
        self.selected_recipes_frame.selected_index_to_meals = self.selected_index_to_meals
        self.available_meals_frame.tags_to_checkbox_values = self.tags_to_checkbox_values

        # Bind callbacks
        self.session_manager_frame.session_ids_listbox.unbind(sequence="<Double-Button-1>")
        self.session_manager_frame.session_ids_listbox.bind(
            sequence="<Double-Button-1>",
            func=self.select_session,
        )

        self.available_meals_frame.currently_available_meals_box.bind(
            sequence="<Double-Button-1>",
            func=self.add_selected_meal,
        )
        self.selected_recipes_frame.selected_meals_box.bind(
            sequence="<Double-Button-1>",
            func=self.remove_selected_meal,
        )

    def select_session(self, event: tkinter.Event) -> None:
        """Extend the `SessionManagerFrame.select_session` method to refresh all relevant app components."""
        self.session_manager_frame.select_session(event=event)

        self.selected_recipes_frame.selected_meals_box.delete(first=0, last="end")
        self.selected_recipes_frame.selected_meals_box.insert(
            "end",
            *self.session_manager_frame.selected_index_to_meals.values(),
        )

        self.shopping_list_frame.current_measurement_registry = MealSelection()
        for meal in self.session_manager_frame.selected_index_to_meals.values():
            self.shopping_list_frame.current_measurement_registry.add_recipe(
                recipe=default_recipe_registry.get_recipe(recipe_name=meal),
            )
        self.shopping_list_frame.update_shopping_list()

    # def load_session(self, selected_index_to_meals: dict[int, str]) -> None:
    #     """Restore the app state for the given session."""
    #     self.session_manager_frame.load_session()
    #
    #     self.selected_recipes_frame.selected_index_to_meals = selected_index_to_meals
    #     self.selected_recipes_frame.selected_meals_box.delete(first=0, last="end")
    #     self.selected_recipes_frame.selected_meals_box.insert("end", *selected_index_to_meals.values())
    #
    #     self.shopping_list_frame.current_measurement_registry = MealSelection()
    #     for meal in selected_index_to_meals.values():
    #         self.shopping_list_frame.current_measurement_registry.add_recipe(
    #             recipe=default_recipe_registry.get_recipe(recipe_name=meal),
    #         )
    #     self.shopping_list_frame.update_shopping_list()

    def add_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the available list to the selected list."""
        selected_meal = self.available_meals_frame.currently_available_meals_box.get(first="active")
        meal_index = self.available_meals_frame.default_available_meals_to_index[selected_meal]

        self.selected_recipes_frame.selected_meals_box.insert("end", selected_meal)

        self.selected_recipes_frame.selected_index_to_meals[meal_index] = selected_meal
        self.available_meals_frame.currently_available_index_to_meals.pop(meal_index)
        self.available_meals_frame.update_available_meal_display()

        self.shopping_list_frame.current_measurement_registry.add_recipe(
            recipe=default_recipe_registry.get_recipe(recipe_name=selected_meal),
        )
        self.shopping_list_frame.update_shopping_list()

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        selected_meal = self.selected_recipes_frame.selected_meals_box.get(first="active")
        meal_index = self.available_meals_frame.default_available_meals_to_index[selected_meal]

        self.selected_recipes_frame.selected_meals_box.delete(first="active")

        self.selected_recipes_frame.selected_index_to_meals.pop(meal_index)
        self.available_meals_frame.currently_available_index_to_meals[meal_index] = selected_meal
        self.available_meals_frame.update_available_meal_display()

        self.shopping_list_frame.current_measurement_registry.remove_recipe(recipe_name=selected_meal)
        self.shopping_list_frame.update_shopping_list()

    def _on_closing(self) -> None:
        """Ask the user if they want to save the current session before closing the app."""
        response = tkinter.messagebox.askyesnocancel(
            title="Quit",
            message="Would you like to save the current session?",
        )

        if response is True:
            self.session_manager_frame.save_session()

        if response is not None:
            self.destroy()

    def _open_github_issue_page(self) -> None:
        """Open the GitHub issue page for the CoMo project."""
        webbrowser.open_new("https://github.com/CodyCBakerPhD/como_recipes/issues/new/choose")
