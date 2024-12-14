import tkinter
import tkinter.messagebox
import typing

import natsort

from ._app_globals import (
    default_index_to_recipe_name,
    default_recipe_name_to_index,
)
from ._app_utils import _generate_default_app_state
from .._base._base_meal import Meal
from .._registration._recipe_registry import default_recipe_registry


class AvailableRecipesFrame(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        app_state: dict[str, typing.Any] | None = None,
        recipe_type: typing.Literal["Entree", "Side"] | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_available_recipes: int = 20,
    ) -> None:
        """A modular component for searching and filtering the default recipes."""
        super().__init__(master=master)
        self.app_state = app_state or _generate_default_app_state()

        self.recipe_type = recipe_type
        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_available_recipes = minimum_number_of_displayed_available_recipes

        self._update_available_index_to_recipe_name()
        self.setup_frame()

    def _update_available_index_to_recipe_name(self) -> None:
        if self.recipe_type is None:
            self.available_index_to_recipe_name = {
                index: recipe_name
                for index, recipe_name in default_index_to_recipe_name.items()
                if recipe_name not in self.app_state["meal_selection"]
            }
        else:
            self.available_index_to_recipe_name = {
                index: recipe_name
                for index, recipe_name in default_index_to_recipe_name.items()
                if recipe_name not in self.app_state["meal_selection"]
                and self.recipe_type in default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
            }

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        # Left subframe - fancy selector
        self.available_recipe_names_subframe = tkinter.Frame(master=self)
        self.available_recipe_names_subframe.pack(side="left")

        self.available_meals_label = tkinter.Label(
            master=self.available_recipe_names_subframe,
            text="Available meals",
        )

        self.available_meals_search = tkinter.Entry(
            master=self.available_recipe_names_subframe,
            width=self.minimum_available_recipe_width_in_characters,
        )
        self.available_meals_search.bind(sequence="<KeyRelease>", func=self.update_frame)

        self.available_meals_list_box = tkinter.Listbox(
            master=self.available_recipe_names_subframe,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_available_recipes,
        )
        self.available_meals_list_box.insert(0, *self.available_index_to_recipe_name.values())

        self.available_meals_label.grid(row=0, column=0, pady=2.5)
        self.available_meals_search.grid(row=1, column=0, sticky="n")
        self.available_meals_list_box.grid(row=2, column=0, sticky="n")

        # Right subframe - tag filters
        self.available_meals_frame_tags_subframe = tkinter.Frame(master=self)
        self.available_meals_frame_tags_subframe.pack(side="right")

        self.tags_label = tkinter.Label(
            master=self.available_meals_frame_tags_subframe,
            text="Filter by",
        )
        self.tags_label.grid(row=0, pady=2.5)

        self.tags_to_checkboxes = {
            tag: tkinter.Checkbutton(
                master=self.available_meals_frame_tags_subframe,
                text=tag,
                variable=variable,
                justify="left",
                command=self.update_frame,
            )
            for tag, variable in self.app_state["tags_to_checkbox_values"].items()
        }
        for row, tag_checkbox in enumerate(self.tags_to_checkboxes.values()):
            tag_checkbox.grid(row=1 + row, sticky="W")

        # Bind callbacks
        self.available_meals_list_box.bind(
            sequence="<Double-Button-1>",
            func=self.add_selected_meal,
        )

    def update_frame(self, event: tkinter.Event | None = None) -> None:
        """
        Update the list of displayed meals based on the search query.

        Intended to be as 'smart' as possible.
        """
        self._update_available_index_to_recipe_name()

        for tag, checkbox in self.tags_to_checkboxes.items():
            variable = self.app_state["tags_to_checkbox_values"][tag]
            checkbox.config(variable=variable)

        if self.available_meals_search.get() == "":
            data = self.available_index_to_recipe_name.values()
        else:
            value = self.available_meals_search.get()
            data = [item for item in self.available_index_to_recipe_name.values() if value.lower() in item.lower()]

        # TODO: improve performance by offloading minimal change differences to internal variables and only
        # updating data/GUI when necessary
        filtered_data = data
        if any(self.app_state["tags_to_checkbox_values"].values()):
            selected_tags = {
                tag for tag, variable in self.app_state["tags_to_checkbox_values"].items() if variable.get() == 1
            }
            filtered_data = [
                item
                for item in data
                if selected_tags.issubset(default_recipe_registry.get_recipe(recipe_name=item).tags)
            ]

        sorted_data = natsort.natsorted(seq=filtered_data)

        # TODO: could improve the laziness/performance of add/remove operations w.r.t. current search query instead of
        # regenerating entire search every time
        self.available_meals_list_box.delete(first=0, last="end")
        self.available_meals_list_box.insert("end", *sorted_data)

    def add_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the available list to the selected list."""
        selected_meal = self.available_meals_list_box.get(first="active")
        meal_index = default_recipe_name_to_index[selected_meal]

        meal = Meal()
        meal.add_recipe(recipe=default_recipe_registry.get_recipe(recipe_name=selected_meal))
        # TODO
        # meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
        self.app_state["meal_selection"].add_meal(meal=meal)

        self._update_available_index_to_recipe_name()

        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()
