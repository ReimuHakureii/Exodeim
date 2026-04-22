import tkinter as tk

class PreviewTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text = tk.Text(self)
        self.text.pack()

    def load(self, path):
        try:
            with open(path, "r", errors="ignore") as f:
                self.text.delete("1.0","end")
                self.text.insert("end", f.read(1000))
        except:
            self.text.insert("end", "Binary file")