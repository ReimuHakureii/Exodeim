import tkinter as tk
import os
from file_properties_editor.utils import ts_to_str

class TimestampsTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self)
        self.label.pack()

    def load(self, path):
        st = os.stat(path)
        self.label.config(text=ts_to_str(st.st_mtime))