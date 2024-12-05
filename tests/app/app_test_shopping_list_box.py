import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()
    shopping_list_box = como_recipes.app.ShoppingListFrame(master=app)
    shopping_list_box.pack(padx=5)

    shopping_list_box.current_measurement_registry.add_recipe(
        recipe=como_recipes.default_recipe_registry.get_recipe(recipe_name="Aglio E Olio"),
    )
    shopping_list_box.update_shopping_list()

    app.mainloop()
