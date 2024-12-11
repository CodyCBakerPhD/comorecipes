import pathlib
import pickle
import shutil
import tkinter

import natsort

from ._app_globals import all_default_tags
from ._app_utils import _generate_default_app_state, _generate_new_default_session_id
from .._meal_selection import MealSelection


class SessionManagerFrame(tkinter.Frame):
    def __init__(
        self,
        master: tkinter.Tk | tkinter.Frame | None = None,
        minimum_number_of_displayed_measurements: int = 35,
    ) -> None:
        super().__init__(master=master)

        self.minimum_number_of_displayed_measurements = minimum_number_of_displayed_measurements

        self.setup_attributes()
        self.setup_frame()

        # Cleanup bad sessions on natural exit
        master.protocol(name="WM_DELETE_WINDOW", func=self._on_closing)

    def _on_closing(self) -> None:
        """Ask the user if they want to save the current session before closing the app."""
        response = tkinter.messagebox.askyesnocancel(
            title="Quit",
            message="Would you like to save the current session?",
        )

        if response is True:
            self.save_app_state()

        if response is not None:
            self.validate_or_remove_sessions()
            self.master.destroy()

    def setup_attributes(self) -> None:
        """Define all mutable attributes used to control underlying states of the application."""
        self.app_state = _generate_default_app_state()

        self.validate_or_remove_sessions()
        self.update_session_ids()

        # There are state-based attributes used by the main app, but relevant to session saving/loading
        self.app_state["session_folder_path"] = self.app_state["home_folder_path"] / self.selected_session_id
        self.app_state["app_state_file_path"] = (
            self.app_state["home_folder_path"] / self.selected_session_id / "app_state.pickle"
        )
        if self.app_state["app_state_file_path"].exists():
            self.load_app_state()

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        self.label = tkinter.Label(master=self, text="Sessions")

        self.add_button = tkinter.Button(
            master=self,
            text="New session",
            command=self.create_new_session,
        )

        self.list_box = tkinter.Listbox(master=self, height=self.minimum_number_of_displayed_measurements)
        elements = [f"├─ {session_id}" for session_id in self.session_ids]
        self.list_box.insert("end", *elements)
        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

        self.delete_session_popup_menu = tkinter.Menu(master=self, tearoff=False)
        self.delete_session_popup_menu.add_command(label="Delete session", command=self.delete_session)

        self.save_button = tkinter.Button(master=self, text="Save", command=self.save_app_state)

        # Organize
        self.label.grid(row=0, padx=2.5, pady=2.5)
        self.add_button.grid(row=1, padx=2.5, pady=2.5)
        self.list_box.grid(row=2, sticky="W", padx=2.5, pady=2.5)
        self.save_button.grid(row=3, padx=2.5, pady=2.5)

        # Bind callbacks
        self.list_box.bind(sequence="<Double-Button-1>", func=self.select_session)
        self.list_box.bind(sequence="<Button-3>", func=self.delete_session_popup)

    def update_session_ids(self) -> None:
        existing_session_ids = [path.name for path in self.app_state["home_folder_path"].iterdir()] or [
            _generate_new_default_session_id(home_folder=self.app_state["home_folder_path"]),
        ]
        self.session_ids = natsort.natsorted(seq=existing_session_ids, reverse=True)

        # There are frame-specific local attributes independent of the main part of the app
        # Reset them any time the session IDs list is updated
        self.selected_session_id = self.session_ids[0]
        self.selected_session_id_index = 0

    def update_frame(self) -> None:
        """Update the session manager frame display based on the current app state."""
        self.list_box.delete(first=0, last="end")

        elements = [f"├─ {session_id}" for session_id in self.session_ids]
        self.list_box.insert("end", *elements)

        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

    @staticmethod
    def _is_valid_session(session_folder_path: pathlib.Path) -> bool:
        """Check if the current session folder contents are valid."""
        if session_folder_path.exists() and len(list(session_folder_path.iterdir())) == 0:
            return False

        return True

    def validate_or_remove_sessions(self) -> None:
        """Validate all current sessions in the home folder and remove them if not."""
        session_folder_paths = list(self.app_state["home_folder_path"].iterdir())
        for session_folder_path in session_folder_paths:
            if self._is_valid_session(session_folder_path) is False:
                shutil.rmtree(path=session_folder_path, ignore_errors=True)

    def create_new_session(self) -> None:
        """Create a new session with a unique ID and update the listbox."""
        self.selected_session_id = tkinter.simpledialog.askstring(
            title="New session",
            prompt="Enter an ID for the new session:",
            initialvalue=_generate_new_default_session_id(home_folder=self.app_state["home_folder_path"]),
        )

        self.app_state["session_folder_path"] = self.app_state["home_folder_path"] / self.selected_session_id
        self.app_state["session_folder_path"].mkdir(exist_ok=True)
        self.app_state["app_state_file_path"] = self.app_state["session_folder_path"] / "app_state.pickle"
        self.update_session_ids()  # Wasteful, but at least it ensures consistency

        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "white"})
        if self.selected_session_id in self.session_ids:
            self.selected_session_id_index = self.session_ids.index(self.selected_session_id)
        else:
            self.session_ids.insert(0, self.selected_session_id)
            self.list_box.insert(0, f"├─ {self.selected_session_id}")
            self.selected_session_id_index = 0
        self.list_box.activate(index=self.selected_session_id_index)
        self.list_box.selection_set(first=self.selected_session_id_index)
        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

        self.app_state.update(
            {
                "selected_index_to_meals": {},
                "tags_to_checkbox_values": {tag: tkinter.IntVar() for tag in all_default_tags},
                "meal_selection": MealSelection(),
            },
        )

        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()

    # TODO: can I use ' / ' to avoid need for `event`?
    def select_session(self, event: tkinter.Event | None = None) -> None:
        """The callback which triggers on double-clicking an element of the session manager listbox."""
        # Reset background color of previously selected session
        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "white"})

        # Get selected session ID
        selected_value = self.list_box.get("active")
        self.selected_session_id = selected_value.split(" ")[1]
        self.selected_session_id_index = self.list_box.curselection()[0]

        # Update
        session_folder_path = self.app_state["home_folder_path"] / self.selected_session_id
        self.app_state["session_folder_path"] = session_folder_path
        self.app_state["app_state_file_path"] = session_folder_path / "app_state.pickle"
        if self.app_state["app_state_file_path"].exists():
            self.load_app_state()

        # Restore highlight
        self.list_box.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

        if hasattr(self.master, "update_frames"):
            self.master.update_frames()
        else:
            self.update_frame()

    def save_app_state(self, event: tkinter.Event | None = None) -> None:
        """Save the current session to a new folder in the app home directory."""
        self.app_state["session_folder_path"].mkdir(exist_ok=True)
        copy_without_intvar = self.app_state.copy()
        copy_without_intvar["tags_to_checkbox_values"] = {
            tag: var.get() for tag, var in self.app_state["tags_to_checkbox_values"].items()
        }
        with self.app_state["app_state_file_path"].open(mode="wb") as io:
            pickle.dump(obj=copy_without_intvar, file=io)

    def load_app_state(self, event: tkinter.Event | None = None) -> None:
        """Save the current session to a new folder in the app home directory."""
        with self.app_state["app_state_file_path"].open(mode="rb") as io:
            self.app_state.update(pickle.load(file=io))  # noqa: S301
        self.app_state["tags_to_checkbox_values"] = {
            tag: tkinter.IntVar(value=value) for tag, value in self.app_state["tags_to_checkbox_values"].items()
        }

    def delete_session_popup(self, event: tkinter.Event | None = None) -> None:
        """Display a popup menu for deleting a session when right-clicking a session ID in the listbox."""
        nearest_index = self.list_box.nearest(y=event.y)
        self.list_box.activate(index=nearest_index)
        self.list_box.selection_set(first=nearest_index)
        self.delete_session_popup_menu.post(x=event.x_root, y=event.y_root)

    def delete_session(self, event: tkinter.Event | None = None) -> None:
        """Delete the currently active (via right-click) session ID from the listbox."""
        session_id_to_delete = self.list_box.get("active").split(" ")[1]

        session_folder_path = self.app_state["home_folder_path"] / session_id_to_delete
        shutil.rmtree(path=session_folder_path, ignore_errors=True)
        session_folder_path.unlink(missing_ok=True)

        self.list_box.delete(first=self.session_ids.index(session_id_to_delete))
        self.session_ids.remove(session_id_to_delete)

        # Edge case: If the last session is deleted, create a new default session
        if len(self.session_ids) == 0:
            self.selected_session_id = tkinter.simpledialog.askstring(
                title="New session",
                prompt="Enter an ID for the new session:",
                initialvalue=_generate_new_default_session_id(home_folder=self.app_state["home_folder_path"]),
            )

            self.session_ids.insert(0, self.selected_session_id)
            self.list_box.insert(0, f"├─ {self.selected_session_id}")
            self.selected_session_id_index = 0

        # Reset active index to top
        self.selected_session_id_index = 0
        self.list_box.activate(index=self.selected_session_id_index)
        self.list_box.selection_set(first=self.selected_session_id_index)
