import tkinter

import como_recipes

if __name__ == "__main__":
    app = tkinter.Tk()

    session_manager_frame = como_recipes.app.SessionManagerFrame(master=app)
    session_manager_frame.pack(padx=2.5, pady=2.5)

    default_home_folder = session_manager_frame.app_state["home_folder_path"]
    test_home_folder = default_home_folder / "test_sessions"
    test_home_folder.mkdir(exist_ok=True)
    test_session_folder_path = test_home_folder / "test_session_1"
    test_app_state_file_path = test_session_folder_path / "app_state.pickle"

    session_manager_frame.app_state["home_folder_path"] = test_home_folder
    session_manager_frame.update_session_ids()
    session_manager_frame.update_frame()

    session_manager_frame.debug = True
    app.mainloop()
