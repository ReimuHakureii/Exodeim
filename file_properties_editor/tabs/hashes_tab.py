import tkinter as tk
import hashlib

class HashesTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self)
        self.label.pack()

    def load(self, path):
        try:
            h = hashlib.md5(open(path, 'rb').read()).hexdigest()
            self.label.config(text=h)
        except:
            self.label.config(text="Error")