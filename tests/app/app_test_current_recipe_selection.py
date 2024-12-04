import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()
    current_recipe_selection = como_recipes.app.CurrentRecipeSelection(master=app)
    current_recipe_selection.pack(padx=5, pady=2.5)

    current_recipe_selection.selected_meals_box.insert("end", "Aglio E Olio")

    app.mainloop()
