import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()
    available_recipe_selector = como_recipes.app.AvailableRecipeSelector(master=app)
    available_recipe_selector.pack(padx=5, pady=5)
    app.mainloop()
