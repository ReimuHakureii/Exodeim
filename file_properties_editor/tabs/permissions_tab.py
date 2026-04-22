import tkinter as tk
import os

class PermissionsTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self)
        self.label.pack()

    def load(self, path):
        self.label.config(text=oct(os.stat(path).st_mode))