import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    available_recipe_selector = como_recipes.app.AvailableRecipesFrame(master=app)
    available_recipe_selector.pack(padx=2.5, pady=2.5)

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    available_recipe_selector.app_state["meal_selection"].add_meal(meal=meal)
    available_recipe_selector.update_frame()

    app.mainloop()
