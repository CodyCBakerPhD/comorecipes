import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    session_manager_frame = como_recipes.app.SessionManagerFrame(master=app)
    session_manager_frame.pack(padx=2.5, pady=2.5)

    app.mainloop()
