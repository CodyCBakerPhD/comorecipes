import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    shopping_list_frame = como_recipes.app.ShoppingListFrame(master=app)
    shopping_list_frame.session_folder_path = shopping_list_frame.session_folder_path.parent / "test"
    shopping_list_frame.pack(padx=2.5, pady=2.5)

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))

    shopping_list_frame.meal_selection.add_meal(meal=meal)
    shopping_list_frame.update_frame()

    app.mainloop()
