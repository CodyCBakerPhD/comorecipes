import shutil
import tkinter

import natsort
import yaml

from ._app_globals import all_default_tags
from ._app_utils import _generate_new_default_session_id, _get_home_folder


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

    def setup_attributes(self) -> None:
        """Define all mutable attributes used to control underlying states of the application."""
        self.home_folder_path = _get_home_folder()

        existing_session_ids = [path.name for path in self.home_folder_path.iterdir()] or [
            _generate_new_default_session_id(),
        ]
        self.session_ids = natsort.natsorted(seq=existing_session_ids, reverse=True)

        self.selected_session_id = self.session_ids[0]
        self.selected_session_id_index = 1  # Since the true first element (index 0) is always "+ New session"

        self.session_folder_path = self.home_folder_path / self.selected_session_id

        # There are state-based attributes used by the main app, but relevant to session saving/loading
        if self.session_folder_path.exists():
            self.load_session()
        else:
            # TODO: just an idea
            # self.states = {
            #     "selected_index_to_meals": {},
            #     "tags_to_checkbox_values": {tag: tkinter.IntVar() for tag in all_default_tags},
            #     "shopping_list": [],
            # }
            self.selected_index_to_meals: dict[int, str] = {}
            self.tags_to_checkbox_values: dict[str, tkinter.IntVar] = {
                tag: tkinter.IntVar() for tag in all_default_tags
            }
            self.shopping_list: list[str] = []
            self.save_session()

    def setup_frame(self) -> None:
        """Initialize and organize all subcomponents of the frame."""
        self.label = tkinter.Label(master=self, text="Sessions")

        self.session_ids_listbox = tkinter.Listbox(master=self, height=self.minimum_number_of_displayed_measurements)
        elements = ["+ New session", *[f"├─ {session_id}" for session_id in self.session_ids]]
        self.session_ids_listbox.insert("end", *elements)
        self.session_ids_listbox.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

        self.delete_session_popup_menu = tkinter.Menu(master=self, tearoff=False)
        self.delete_session_popup_menu.add_command(label="Delete session", command=self.delete_session)

        self.save_button = tkinter.Button(master=self, text="Save", command=self.save_session)

        # Organize
        self.label.grid(row=0, padx=2.5, pady=2.5)
        self.session_ids_listbox.grid(row=1, sticky="W", padx=2.5, pady=2.5)
        self.save_button.grid(row=2, padx=2.5, pady=2.5)

        # Bind callbacks
        self.session_ids_listbox.bind(sequence="<Double-Button-1>", func=self.select_session)
        self.session_ids_listbox.bind(sequence="<Button-3>", func=self.delete_session_popup)

    def validate_session(self) -> None:
        """Check if the current session folder contents are valid and remove the directory if not."""

    # TODO: can I use ' / ' to avoid need for `event`?
    def select_session(self, event: tkinter.Event | None = None) -> None:
        """The callback which triggers on double-clicking an element of the session manager listbox."""
        # Reset background color of previously selected session
        self.session_ids_listbox.itemconfig(index=self.selected_session_id_index, cnf={"bg": "white"})

        save = False
        load = False
        selected_value = self.session_ids_listbox.get("active")
        if selected_value == "+ New session":
            save = True

            self.selected_session_id = tkinter.simpledialog.askstring(
                title="New session",
                prompt="Enter an ID for the new session:",
                initialvalue=_generate_new_default_session_id(),
            )

            self.session_ids.insert(0, self.selected_session_id)
            self.session_ids_listbox.insert(1, f"├─ {self.selected_session_id}")
            self.selected_session_id_index = 1
        else:
            load = True

            self.selected_session_id = selected_value.split(" ")[1]
            self.selected_session_id_index = self.session_ids_listbox.curselection()[0]

        # Update
        self.session_folder_path = self.home_folder_path / self.selected_session_id

        if save is True:
            self.save_session()
        if load is True:
            self.load_session()

        # Restore highlight
        self.session_ids_listbox.itemconfig(index=self.selected_session_id_index, cnf={"bg": "lightgrey"})

    def save_session(self, event: tkinter.Event | None = None) -> None:
        """Save the current session to a new folder in the app home directory."""
        # print(self.session_folder_path)

        self.session_folder_path.mkdir(exist_ok=True)
        for attribute_name in ["selected_index_to_meals", "shopping_list"]:
            attribute_file_path = self.session_folder_path / f"{attribute_name}.yaml"
            with attribute_file_path.open(mode="w") as io:
                attribute_value = getattr(self, attribute_name)
                yaml.dump(data=attribute_value, stream=io)

        # Requires special encoding
        attribute_file_path = self.session_folder_path / "tags_to_checkbox_values.yaml"
        with attribute_file_path.open(mode="w") as io:
            attribute_value = {tag: int_var.get() for tag, int_var in self.tags_to_checkbox_values.items()}
            yaml.dump(data=attribute_value, stream=io)

    def load_session(self) -> None:
        """Set the internal states from the loaded session files."""
        for attribute_name in ["selected_index_to_meals", "shopping_list"]:
            attribute_file_path = self.session_folder_path / f"{attribute_name}.yaml"
            if not attribute_file_path.exists():
                continue

            with attribute_file_path.open(mode="r") as io:
                attribute_value = yaml.safe_load(stream=io)
                setattr(self, attribute_name, attribute_value)

        # Requires special decoding
        attribute_file_path = self.session_folder_path / "tags_to_checkbox_values.yaml"
        with attribute_file_path.open(mode="r") as io:
            yaml_data = yaml.safe_load(stream=io)
            attribute_value = {tag: tkinter.IntVar(value=value) for tag, value in yaml_data.items()}
            self.tags_to_checkbox_values = attribute_value

    def delete_session_popup(self, event: tkinter.Event | None = None) -> None:
        """Display a popup menu for deleting a session when right-clicking a session ID in the listbox."""
        nearest_index = self.session_ids_listbox.nearest(y=event.y)
        self.session_ids_listbox.activate(index=nearest_index)
        self.session_ids_listbox.selection_set(first=nearest_index)
        self.delete_session_popup_menu.post(x=event.x_root, y=event.y_root)

    def delete_session(self, event: tkinter.Event | None = None) -> None:
        """Delete the currently active (via right-click) session ID from the listbox."""
        session_id_to_delete = self.session_ids_listbox.get("active").split(" ")[1]

        session_folder_path = self.home_folder_path / session_id_to_delete
        shutil.rmtree(path=session_folder_path, ignore_errors=True)
        session_folder_path.unlink(missing_ok=True)

        self.session_ids_listbox.delete(first=self.session_ids.index(session_id_to_delete) + 1)
        self.session_ids.remove(session_id_to_delete)

        # Edge case: If the last session is deleted, create a new default session
        if len(self.session_ids) == 0:
            self.selected_session_id = tkinter.simpledialog.askstring(
                title="New session",
                prompt="Enter an ID for the new session:",
                initialvalue=_generate_new_default_session_id(),
            )

            self.session_ids.insert(0, self.selected_session_id)
            self.session_ids_listbox.insert(1, f"├─ {self.selected_session_id}")
            self.selected_session_id_index = 1

        # Reset active index to top
        self.selected_session_id_index = 1
        self.session_ids_listbox.activate(index=self.selected_session_id_index)
        self.session_ids_listbox.selection_set(first=self.selected_session_id_index)
