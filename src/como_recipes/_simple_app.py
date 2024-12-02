import tkinter

import natsort

import como_recipes


class SimpleCoMoApp(tkinter.Tk):
    def __init__(self) -> None:
        """A very simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        self.top_banner = tkinter.Label(self, text="Welcome to the CoMo Meal Selection App!")

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

        self.currently_available_meals_search = tkinter.Entry(master=self)
        self.currently_available_meals_search.bind(sequence="<KeyRelease>", func=self.update_available_meal_display)

        self.currently_available_meals_box = tkinter.Listbox(self)
        self.currently_available_meals_box.insert(0, *self.currently_available_index_to_meals.values())
        self.currently_available_meals_box.bind(sequence="<Double-Button-1>", func=self.add_selected_meal)

        self.selected_meals_box = tkinter.Listbox(self)
        self.selected_meals_box.bind(sequence="<Double-Button-1>", func=self.remove_selected_meal)

        self.warnings_labels = tkinter.Label(master=self, text="Example warning")

        # Organize components on grid
        self.top_banner.grid(row=0, column=0, columnspan=2)
        self.currently_available_meals_search.grid(row=1, column=0)
        self.currently_available_meals_box.grid(row=2, column=0)
        self.warnings_labels.grid(row=1, column=1, rowspan=2)
        self.selected_meals_box.grid(row=3, column=0, columnspan=2)

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

    def add_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the available list to the selected list."""
        selected_meal = self.currently_available_meals_box.get(tkinter.ACTIVE)
        meal_index = self.default_available_meals_to_index[selected_meal]

        self.selected_meals_box.insert("end", selected_meal)

        self.currently_selected_index_to_meals[meal_index] = selected_meal
        self.currently_available_index_to_meals.pop(meal_index)

        self.update_available_meal_display()

    def remove_selected_meal(self, event: tkinter.Event) -> None:
        """Move a meal from the selected list back to the available list."""
        selected_meal = self.selected_meals_box.get(tkinter.ACTIVE)
        meal_index = self.default_available_meals_to_index[selected_meal]

        self.selected_meals_box.delete(tkinter.ACTIVE)

        self.currently_selected_index_to_meals.pop(meal_index)
        self.currently_available_index_to_meals[meal_index] = selected_meal

        self.update_available_meal_display()


if __name__ == "__main__":
    app = SimpleCoMoApp()
    app.mainloop()
