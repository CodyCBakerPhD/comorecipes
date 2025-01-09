import pathlib
import sys
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import webbrowser

import como_recipes.utils

from ._meal_assembler_frame import MealAssemblerFrame
from ._session_manager_frame import SessionManagerFrame
from ._shopping_list_frame import ShoppingListFrame


class CoMoApp(tkinter.Tk):
    def __init__(self) -> None:
        """A relatively simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        self.setup_window()
        self.setup_frames()
        self.update_frames()

    def _open_github_issue_page(self) -> None:
        """Open the GitHub issue page for the CoMo project."""
        webbrowser.open_new("https://github.com/CodyCBakerPhD/como_recipes/issues/new/choose")

    def _open_license_popup(self) -> None:
        """Open a popup with the license information."""
        license_text = como_recipes.utils.get_license_text()
        tkinter.messagebox.showinfo(title="License", message=license_text)

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

        self.about_menu = tkinter.Menu(master=self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="License", command=self._open_license_popup)

        # Components do not currently support dynamic resizing, so just freeze window size
        self.resizable(width=False, height=False)

    def setup_frames(
        self,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_selected_recipes: int = 15,
        minimum_number_of_displayed_measurements: int = 35,
        minimum_number_of_displayed_available_recipes: int = 20,
    ) -> None:
        """Initialize all frames or components that comprise the app."""
        self.session_manager_frame = SessionManagerFrame(master=self)

        self.meal_assembler_frame = MealAssemblerFrame(
            master=self,
            app_state=self.session_manager_frame.app_state,
        )
        self.shopping_list_frame = ShoppingListFrame(
            master=self,
            app_state=self.session_manager_frame.app_state,
            minimum_available_recipe_width_in_characters=minimum_available_recipe_width_in_characters,
            minimum_number_of_displayed_measurements=minimum_number_of_displayed_measurements,
        )
        version = como_recipes.utils.get_package_version()
        version_string = version + ".dev" if como_recipes.utils.is_bundled() is False else version
        self.version_label = tkinter.Label(master=self, text=version_string)

        # Organize frames on grid
        self.session_manager_frame.grid(column=0, rowspan=4, padx=2.5, pady=2.5, sticky="NW")
        self.meal_assembler_frame.grid(row=1, column=1, padx=2.5, pady=2.5)
        self.shopping_list_frame.grid(row=1, column=3, rowspan=2, padx=2.5, pady=2.5)
        self.version_label.grid(row=2, columnspan=4, sticky="se")

    def update_frames(self) -> None:
        """Update all frames with the latest state."""
        self.session_manager_frame.update_frame()
        self.meal_assembler_frame.update_frame()
        self.shopping_list_frame.update_frame()
