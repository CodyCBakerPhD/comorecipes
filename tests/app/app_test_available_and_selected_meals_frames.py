import tkinter

import como_recipes


class TestAvailableAndSelectedMealsApp(tkinter.Tk):
    """Test class for a combination of the AvailableRecipesFrame and SelectedMealsFrame."""

    def __init__(self) -> None:
        super().__init__()

        self.available_recipes_frame = como_recipes.app.AvailableRecipesFrame(master=self)
        self.available_recipes_frame.pack(side="top", padx=2.5, pady=2.5)

        self.selected_meals_frame = como_recipes.app.SelectedMealsFrame(master=self)
        self.selected_meals_frame.pack(side="bottom", padx=2.5, pady=2.5)

        self.app_state = self.available_recipes_frame.app_state
        self.selected_meals_frame.app_state = self.available_recipes_frame.app_state

    def update_frames(self):
        self.available_recipes_frame.update_frame()
        self.selected_meals_frame.update_frame()


if __name__ == "__main__":
    app = TestAvailableAndSelectedMealsApp()

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    app.app_state["meal_selection"].add_meal(meal=meal)

    app.update_frames()

    app.mainloop()
