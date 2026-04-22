import tkinter as tk
from file_properties_editor.constants import CARD, WHITE, BORDER, ACCENT, RED, PANEL, SUBTEXT, LABEL_FONT, MONO, BODY

class StyledButton(tk.Frame):
    def __init__(self, parent, text, command=None, accent=False, danger=False, small=False, **kw):
        bg = RED if danger else (ACCENT if accent else CARD)
        hover = "#e04050" if danger else ("#9d90ff" if accent else BORDER)
        super().__init__(parent, bg=bg, cursor="hand2", **kw)
        pad = (8, 4) if small else (14, 7)
        self._label = tk.Label(self, text=text, bg=bg, fg=WHITE, font=("Segoe UI Semibold", 8 if small else 9), padx=pad[0], pady=pad[1])
        self._label.pack()
        self._bg, self._hover = bg, hover
        self._cmd = command
        for w in (self, self._label):
            w.bind("<Button-1>", self.click)
            w.bind("<Enter>", lambda e: self._set(self._hover))
            w.bind("<Leave>", lambda e: self._set(self._bg))

    def _set(self, c):
        self.config(bg=c)
        self._label.config(bg=c)
    
    def _click(self, e=None):
        if self._cmd:
            self._cmd()
    
    def config_text(self, t):
        self._label.config(text=t)

class LabeledEntry(tk.Frame):
    def __init__(self, parent, label, value="", readonly=False, mono=False, width=40, **kw):
        super().__init__(parent, bg=PANEL, fg=SUBTEXT, font=LABEL_FONT, width=18, anchor="e").pack(side="left", padx=(0, 8))
        font = MONO if mono else BODY
        state = "readonly" if readonly else "normal"
        self.var = tk.StringVar(value=value)
        self.entry = tk.Entry(self, textvariable=self.var, bg=CARD, fg=WHITE, insertbackground=ACCENT, relief="flat", font=font, width=width, state=state)
        self.entry.pack(side="left")

    def get(self):
        return self.var.get()
    
    def set(self, v):
        self.var.set(v)

class Seperator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BORDER, height=1)