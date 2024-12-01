import tkinter

import como_recipes


class SimpleCoMoApp(tkinter.Tk):
    def __init__(self) -> None:
        """A very simple GUI implementation for the CoMo Meal Selection based on Tkinter."""
        super().__init__()

        top_banner = tkinter.Label(self, text="Welcome to the CoMo Meal Selection App!")
        top_banner.pack()

        self.available_meals = como_recipes.default_recipe_registry.get_all_recipe_names()

        available_meals_search = tkinter.Entry(self)
        available_meals_search.pack()
        available_meals_search.bind("<KeyRelease>", self.check_key_search)

        self.available_meals_box = tkinter.Listbox(self)
        self.available_meals_box.pack()
        self.update_selector(data=self.available_meals)

    def check_key_search(self, event: tkinter.Event) -> None:
        value = event.widget.get()

        if value == "":
            data = self.available_meals
        else:
            data = [item for item in self.available_meals if value.lower() in item.lower()]

        self.update_selector(data=data)

    def update_selector(self, *, data: list[str]) -> None:
        self.available_meals_box.delete(first=0, last="end")
        self.available_meals_box.insert("end", *data)


if __name__ == "__main__":
    app = SimpleCoMoApp()
    app.mainloop()
