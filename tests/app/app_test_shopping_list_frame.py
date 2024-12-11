import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    shopping_list_frame = como_recipes.app.ShoppingListFrame(master=app)
    shopping_list_frame.pack(padx=2.5, pady=2.5)

    default_home_folder = shopping_list_frame.app_state["home_folder_path"]
    test_home_folder = default_home_folder.parent / ".como_recipes_tests"
    test_home_folder.mkdir(exist_ok=True)
    test_session_folder_path = test_home_folder / "test_shopping_list_frame"
    test_home_folder.mkdir(exist_ok=True)

    shopping_list_frame.app_state["session_folder_path"] = test_session_folder_path

    meal = como_recipes.Meal()
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"))
    meal.add_recipe(recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Sauteed Green Beans"))

    shopping_list_frame.app_state["meal_selection"].add_meal(meal=meal)
    shopping_list_frame.update_frame()

    app.mainloop()
