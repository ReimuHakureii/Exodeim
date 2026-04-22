import tkinter as tk
from file_properties_editor.widgets import LabeledEntry, Seperator
from file_properties_editor.constants import PANEL, ACCENT
import os

class GeneralTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PANEL)

        tk.Label(self, text="General Information", bg=PANEL, fg=ACCENT).pack()

        Seperator(self).pack(fill="x")

        self.name = LabeledEntry(self, "File Name")
        self.name.pack()

        def load(self, path):
            self.name.set(os.path.basename(path))