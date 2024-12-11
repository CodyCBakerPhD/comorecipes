import datetime
import pathlib
import tkinter.messagebox
import typing

from .._meal_selection import MealSelection


def _get_home_folder() -> pathlib.Path:
    """Get the home folder (and create if it does not exist) for all app and package operations."""
    folder_path = pathlib.Path.home() / ".como_recipes"
    folder_path.mkdir(exist_ok=True)
    return folder_path


def _generate_new_default_session_id(home_folder: pathlib.Path | None = None) -> str | None:
    """Generate a new possible session ID, but do not automatically create the session folder."""
    home_folder = home_folder or _get_home_folder()

    date = datetime.datetime.now().strftime("%Y%m%d")
    default_session_folder_path = home_folder / date

    if not default_session_folder_path.exists():
        session_id = date
        return session_id

    counter = 2
    maximum_iterations = 100
    while default_session_folder_path.exists() and counter < maximum_iterations:
        session_id = f"{date}_{counter}"
        default_session_folder_path = home_folder / session_id
        counter += 1

    if counter == maximum_iterations:
        # TODO: replace with better pop-up
        tkinter.messagebox.showerror(
            title="Error",
            message=f"Too many session IDs (> {maximum_iterations}) with the current date ({date})!",
        )
        return None

    return session_id


def _generate_default_app_state() -> dict[str, typing.Any]:
    """Generate the default app state."""
    home_folder_path = _get_home_folder()
    session_id = _generate_new_default_session_id(home_folder=home_folder_path)

    default_app_state = {
        "home_folder_path": home_folder_path,
        "session_folder_path": home_folder_path / session_id,
        "app_state_file_path": home_folder_path / session_id / "app_state.pickle",
        "tags_to_checkbox_values": {},
        "meal_selection": MealSelection(),
        "selected_index_to_meals": {},
    }

    return default_app_state
