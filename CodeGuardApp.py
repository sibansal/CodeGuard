import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import json
from SetDialog import SetDialog
from ClipBoardListener import ClipboardListener
from AboutDialog import AboutDialog
import webbrowser

class CodeGuardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Guard")
        self.sets = {}

        self.create_ui()

        self.listener = None

        self.load_temp_store()

    def create_ui(self):
        # Create menu
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Import Token Set", command=self.import_token_set)
        file_menu.add_command(label="Export Token Set", command=self.export_token_set)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        license_menu = tk.Menu(menubar, tearoff=0)
        license_menu.add_command(label="View License", command=self.view_license)
        menubar.add_cascade(label="License", menu=license_menu)
        
        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about_dialog)
        menubar.add_cascade(label="Help", menu=about_menu)

        self.root.config(menu=menubar)

        # Create UI elements
        add_set_button = tk.Button(self.root, text="Add Set", command=self.add_set)
        edit_button = tk.Button(self.root, text="Edit", command=self.edit_set)
        delete_button = tk.Button(self.root, text="Delete", command=self.delete_set)
        save_button = tk.Button(self.root, text="Save", command=self.save_data)
        self.set_listbox = tk.Listbox(self.root)
        start_button = tk.Button(self.root, text="Start Listening", command=self.start_listening)
        stop_button = tk.Button(self.root, text="Stop Listening", command=self.stop_listening)
        self.status_label = tk.Label(self.root, text="Listening: Not started")

        #Creating layout
        add_set_button.grid(row=0, column=0, sticky="w")
        edit_button.grid(row=0, column=1, sticky="w")
        delete_button.grid(row=0, column=2, sticky="w")
        save_button.grid(row=0, column=3, sticky="w")
        self.set_listbox.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=0, pady=0)
        start_button.grid(row=2, column=0, sticky="w")
        stop_button.grid(row=2, column=1, sticky="w")
        self.status_label.grid(row=3, column=3, sticky="e")

        # Configure grid weights to allow resizing
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

    def add_set(self):
        set_name = simpledialog.askstring("Add Set", "Enter set name:")
        if set_name:
            dialog = SetDialog(self.root)
            result = dialog.show_dialog()
            self.sets[set_name] = result
            self.update_set_listbox()

    def edit_set(self):
        selected_set = self.set_listbox.curselection()
        if selected_set:
            set_name = self.set_listbox.get(selected_set)
            dialog = SetDialog(self.root, self.sets[set_name])
            result = dialog.show_dialog()
            self.sets[set_name] = result
            self.update_set_listbox()

    def delete_set(self):
        selected_set = self.set_listbox.curselection()
        if selected_set:
            set_name = self.set_listbox.get(selected_set)
            del self.sets[set_name]
            self.update_set_listbox()

    def update_set_listbox(self):
        self.set_listbox.delete(0, tk.END)
        for set_name in self.sets.keys():
            self.set_listbox.insert(tk.END, set_name)

    def start_listening(self):
        if not self.listener or not self.listener.is_listening:
            self.listener = ClipboardListener(self)
            self.listener.start()
            self.status_label.config(text="Listening: Started")

    def stop_listening(self):
        if self.listener and self.listener.is_listening:
            self.listener.stop()
            self.listener = None
            self.status_label.config(text="Listening: Stopped")

    def import_token_set(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                self.sets = data
                self.update_set_listbox()
                messagebox.showinfo("Success", "Token set imported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import token set: {str(e)}")

    def export_token_set(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if file_path:
            try:
                with open(file_path, "w") as file:
                    json.dump(self.sets, file, indent=4)
                messagebox.showinfo("Success", "Token set exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export token set: {str(e)}")

    def exit_app(self):
        self.save_temp_store()
        self.root.quit()

    def load_temp_store(self):
        try:
            with open("temp_store.json", "r") as file:
                self.sets = json.load(file)
                self.update_set_listbox()
        except FileNotFoundError:
            pass

    def save_temp_store(self):
        with open("temp_store.json", "w") as file:
            json.dump(self.sets, file, indent=4)

    def save_data(self):
        self.save_temp_store()
        messagebox.showinfo("Success", "Current state saved successfully!")

    def show_about_dialog(self):
        dialog = AboutDialog(self.root)
        dialog.show_dialog()

    def open_app_website(self):
        webbrowser.open("https://www.example.com/app")

    def open_author_website(self):
        webbrowser.open("https://www.example.com/author")

    def open_author_github(self):
        webbrowser.open("https://github.com/author")

    def open_app_github(self):
        webbrowser.open("https://github.com/app")

    def open_author_twitter(self):
        webbrowser.open("https://twitter.com/author")

    def view_license(self):
        try:
            with open("LICENSE.TXT", "r") as file:
                license_text = file.read()
            messagebox.showinfo("License", license_text)
        except FileNotFoundError:
            messagebox.showerror("Error", "License file not found.")