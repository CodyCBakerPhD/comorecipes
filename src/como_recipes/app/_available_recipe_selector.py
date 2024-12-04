import tkinter
import tkinter.messagebox

import natsort

import como_recipes


class AvailableRecipeSelector(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_available_recipe_width_in_characters: int = 30,
        minimum_number_of_displayed_available_recipes: int = 20,
    ) -> None:
        """A modular component for searching and filtering the default recipes."""
        super().__init__(master=master)

        self.minimum_available_recipe_width_in_characters = minimum_available_recipe_width_in_characters
        self.minimum_number_of_displayed_available_recipes = minimum_number_of_displayed_available_recipes

        self.setup_attributes()
        self.setup_frame()

    def setup_attributes(self) -> None:
        """Define all mutable attributes used to control underlying states of the application."""
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

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        # Left subframe - fancy selector
        self.current_available_meals_frame_box_subframe = tkinter.Frame(master=self)
        self.current_available_meals_frame_box_subframe.pack(side="left")

        self.available_meals_label = tkinter.Label(
            master=self.current_available_meals_frame_box_subframe,
            text="Available meals",
        )

        self.currently_available_meals_search = tkinter.Entry(
            master=self.current_available_meals_frame_box_subframe,
            width=self.minimum_available_recipe_width_in_characters,
        )
        self.currently_available_meals_search.bind(sequence="<KeyRelease>", func=self.update_available_meal_display)

        self.currently_available_meals_box = tkinter.Listbox(
            master=self.current_available_meals_frame_box_subframe,
            width=self.minimum_available_recipe_width_in_characters,
            height=self.minimum_number_of_displayed_available_recipes,
        )
        self.currently_available_meals_box.insert(0, *self.currently_available_index_to_meals.values())

        self.available_meals_label.grid(row=0, column=0, pady=5)
        self.currently_available_meals_search.grid(row=1, column=0, sticky="n")
        self.currently_available_meals_box.grid(row=2, column=0, sticky="n")

        # Right subframe - tag filters
        self.current_available_meals_frame_tags_subframe = tkinter.Frame(master=self)
        self.current_available_meals_frame_tags_subframe.pack(side="right")

        self.tags_label = tkinter.Label(
            master=self.current_available_meals_frame_tags_subframe,
            text="Filter by",
        )
        self.tags_label.grid(row=0, pady=5)

        all_default_tags = natsort.natsorted(
            seq={
                tag
                for recipe_name in como_recipes.default_recipe_registry.get_all_recipe_names()
                for tag in como_recipes.default_recipe_registry.get_recipe(recipe_name=recipe_name).tags
            },
        )

        self.tags_to_checkbox_values = {tag: tkinter.IntVar() for tag in all_default_tags}
        self.tags_to_tag_checkboxes = {
            tag: tkinter.Checkbutton(
                master=self.current_available_meals_frame_tags_subframe,
                text=tag,
                variable=variable,
                justify="left",
                command=self.update_available_meal_display,
            )
            for tag, variable in self.tags_to_checkbox_values.items()
        }
        for row, tag_checkbox in enumerate(self.tags_to_tag_checkboxes.values()):
            tag_checkbox.grid(row=1 + row, sticky="W")

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

        # TODO: improve performance by offloading minimal change differences to internal variables and only
        # updating data/GUI when necessary
        filtered_data = data
        if any(self.tags_to_checkbox_values.values()):
            selected_tags = {tag for tag, variable in self.tags_to_checkbox_values.items() if variable.get() == 1}
            filtered_data = [
                item
                for item in data
                if selected_tags.issubset(como_recipes.default_recipe_registry.get_recipe(recipe_name=item).tags)
            ]

        sorted_data = natsort.natsorted(seq=filtered_data)

        # TODO: could improve the laziness/performance of add/remove operations w.r.t. current search query instead of
        # regenerating entire search every time
        self.currently_available_meals_box.delete(first=0, last="end")
        self.currently_available_meals_box.insert("end", *sorted_data)


if __name__ == "__main__":
    app = tkinter.Tk()
    available_recipe_selector = AvailableRecipeSelector(master=app)
    available_recipe_selector.pack(padx=5, pady=5)
    app.mainloop()
