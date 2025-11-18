from dataclasses import dataclass
from threading import Event
import tkinter as tk


@dataclass
class ControllerState:
    charset: str = "ascii_punctuation_only"
    color: bool = False
    stop: Event | None = None


state = ControllerState()


def _on_key(event: tk.Event) -> None:
    ch = event.char
    if ch == "p":
        state.charset = "ascii_punctuation_only"
    elif ch == "a":
        state.charset = "ascii_all"
    elif ch == "l":
        state.charset = "ascii_letters_only"
    elif ch == "d":
        state.charset = "ascii_digits_only"
    elif ch == "c":
        state.color = not state.color
    elif ch == "q":
        if state.stop is not None:
            state.stop.set()


def start_controller(state: ControllerState) -> None:
    root = tk.Tk()
    root.title("TXTure controller")
    root.geometry("100x100")
    label = tk.Label(root, text="focus here and press keys")
    label.pack(expand=True, fill="both")
    root.bind("<Key>", _on_key)
    root.mainloop()
