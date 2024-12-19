import pathlib

import como_recipes

if __name__ == "__main__":
    app = como_recipes.app.CoMoApp()

    testing_folder = pathlib.Path.home() / ".como_recipes" / "testing"
    testing_folder.mkdir(exist_ok=True)
    testing_sessions_folder = testing_folder / "sessions"
    testing_sessions_folder.mkdir(exist_ok=True)
    test_session_folder = testing_sessions_folder / "test1"
    test_session_folder.mkdir(exist_ok=True)

    app.session_manager_frame.app_state["home_folder_path"] = testing_folder
    app.session_manager_frame.app_state["base_sessions_folder"] = testing_sessions_folder
    app.session_manager_frame.app_state["session_folder_path"] = test_session_folder
    app.session_manager_frame.app_state["app_state_file_path"] = test_session_folder / "app_state.json"

    app.session_manager_frame.update_session_ids()
    app.update_frames()

    app.mainloop()
