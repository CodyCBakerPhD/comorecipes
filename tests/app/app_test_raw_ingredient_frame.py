import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    raw_ingredient_frame = como_recipes.app.RawIngredientFrame(master=app)
    raw_ingredient_frame.pack(padx=2.5, pady=2.5)

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))

    raw_ingredient_frame.meal_selection.add_meal(meal=meal)
    raw_ingredient_frame.update_frame()

    app.mainloop()
