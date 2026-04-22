import tkinter as tk

class AttributesTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Attribues").pack()