from tkinter import messagebox
import pyperclip
import re
import threading

class ClipboardListener(threading.Thread):
    def __init__(self, app):
        super().__init__()
        self.is_listening = False
        self.app = app

    def run(self):
        self.is_listening = True
        while self.is_listening:
            clipboard_text = pyperclip.paste()
            for set_name, set_values in self.app.sets.items():
                tokens, regex = set_values
                if tokens or regex:
                    if (any(token in clipboard_text and token!='' for token in tokens.split(",")) or
                            any(re.search(r, clipboard_text) for r in regex.split(","))):
                        pyperclip.copy("Prevented by Code Guard")
                        messagebox.showwarning("Warning", f"Clipboard paste prevented for Set '{set_name}'!")

    def stop(self):
        self.is_listening = False