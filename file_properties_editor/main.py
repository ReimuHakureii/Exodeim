# Main application file for File Properties Editor

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from file_properties_editor.constants import APP_TITLE, APP_W, APP_H, DARK
from file_properties_editor.utils import ts_to_str, str_to_ts
from file_properties_editor.widgets import StyledButton, Separator
from file_properties_editor.tabs.general_tab import GeneralTab
from file_properties_editor.tabs.timestamps_tab import TimestampsTab
from file_properties_editor.tabs.attributes_tab import AttributesTab
from file_properties_editor.tabs.permissions_tab import PermissionsTab
from file_properties_editor.tabs.hashes_tab import HashesTab
from file_properties_editor.tabs.preview_tab import PreviewTab

class FilePropertiesEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{APP_W}x{APP_H}")
        self.configure(bg=DARK)
        self.minsize(900, 600)
        self._current_path: str = ""
        self._build_ui()

    def _build_ui(self):
        # Header
        hdr = tk.Frame(self, bg=DARK, pady=0)
        hdr.pack(fill="x")
        tk.Label(hdr, text="⬡  File Properties Editor", bg=DARK, fg="white",
                 font=("Segoe UI Semibold", 13), padx=20, pady=12).pack(side="left")
        Separator(self).pack(fill="x")

        # Toolbar
        tb = tk.Frame(self, bg=DARK, pady=8, padx=14)
        tb.pack(fill="x")
        StyledButton(tb, "📂  Open File", self._open_file, accent=True).pack(side="left", padx=4)
        StyledButton(tb, "📁  Open Folder", self._open_folder).pack(side="left", padx=4)
        tk.Frame(tb, bg=DARK).pack(side="left", expand=True)

        # Tabs
        self._notebook = ttk.Notebook(self)
        self._notebook.pack(fill="both", expand=True, padx=0, pady=0)

        self._tab_general = GeneralTab(self._notebook)
        self._tab_timestamps = TimestampsTab(self._notebook)
        self._tab_attributes = AttributesTab(self._notebook)
        self._tab_permissions = PermissionsTab(self._notebook)
        self._tab_hashes = HashesTab(self._notebook)
        self._tab_preview = PreviewTab(self._notebook)

        self._notebook.add(self._tab_general, text="  General  ")
        self._notebook.add(self._tab_timestamps, text="  Timestamps  ")
        self._notebook.add(self._tab_attributes, text="  Attributes  ")
        self._notebook.add(self._tab_permissions, text="  Permissions  ")
        self._notebook.add(self._tab_hashes, text="  Hashes  ")
        self._notebook.add(self._tab_preview, text="  Preview  ")

    def _open_file(self):
        p = filedialog.askopenfilename(title="Select a file")
        if p:
            self._current_path = p

    def _open_folder(self):
        p = filedialog.askdirectory(title="Select a folder")
        if p:
            self._current_path = p

if __name__ == "__main__":
    app = FilePropertiesEditor()
    app.mainloop()