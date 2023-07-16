import tkinter as tk

class SetDialog:
    def __init__(self, root, set_values=("", "")):
        self.root = root
        self.tokens = set_values[0]
        self.regex = set_values[1]
        self.tokens_entry = None
        self.regex_entry = None

    def show_dialog(self):
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Add Tokens and Regex")
        self.dialog.resizable(width=True, height=False)
        
        tokens_label = tk.Label(self.dialog, text="Tokens (comma-separated):")

        self.tokens_entry = tk.Entry(self.dialog)
        self.tokens_entry.insert(tk.END, self.tokens)

        regex_label = tk.Label(self.dialog, text="Regex (comma-separated):")

        self.regex_entry = tk.Entry(self.dialog)
        self.regex_entry.insert(tk.END, self.regex)

        save_button = tk.Button(self.dialog, text="Save", command=self.save_dialog)

        cancel_button = tk.Button(self.dialog, text="Cancel", command=self.cancel_dialog)

        # Creating Layout
        tokens_label.grid(row=0, column=0, sticky="w")
        self.tokens_entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=(0, 10))
        regex_label.grid(row=2, column=0, sticky="w")
        self.regex_entry.grid(row=3, column=0, sticky="we", columnspan=2, pady=(0, 10))
        save_button.grid(row=4, column=0, sticky="w")
        cancel_button.grid(row=4, column=1, sticky="e")

        # Configure grid weights for resizing
        self.dialog.grid_columnconfigure(0, weight=1)
        self.dialog.grid_rowconfigure(1, weight=1)
        self.dialog.grid_rowconfigure(2, weight=1)

        self.dialog.transient(self.root)
        self.dialog.grab_set()
        self.root.wait_window(self.dialog)

        return self.tokens, self.regex

    def save_dialog(self):
        self.tokens = self.tokens_entry.get()
        self.regex = self.regex_entry.get()
        self.dialog.destroy()

    def cancel_dialog(self):
        self.dialog.destroy()