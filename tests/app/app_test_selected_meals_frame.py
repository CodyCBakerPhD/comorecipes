import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()
    selected_meals_frame = como_recipes.app.SelectedMealsFrame(master=app)
    selected_meals_frame.pack(padx=2.5, pady=2.5)

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))
    selected_meals_frame.app_state["meal_selection"].add_meal(meal=meal)
    selected_meals_frame.update_frame()

    selected_meals_frame.debug = True
    app.mainloop()
