import tkinter as tk
import webbrowser
from tkinter import messagebox

class AboutDialog:
    def __init__(self, root):
        self.root = root

    def show_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("About")
        dialog.geometry("400x200")
        dialog.resizable(width=False, height=False)

        app_name_label = tk.Label(dialog, text="Code Guard", font=("Arial", 16, "bold"))
        app_name_label.pack(pady=10)

        author_name_label = tk.Label(dialog, text="Developed by Simran Bansal")
        author_name_label.pack()

        author_github_label = tk.Label(dialog, text="GitHub", cursor="hand2", fg="blue")
        author_github_label.pack()
        author_github_label.bind("<Button-1>", lambda e: self.open_link("https://github.com/sibansal/"))

        app_github_label = tk.Label(dialog, text="Code", cursor="hand2", fg="blue")
        app_github_label.pack()
        app_github_label.bind("<Button-1>", lambda e: self.open_link("https://github.com/sibansal/CodeGuard"))

        author_twitter_label = tk.Label(dialog, text="Twitter", cursor="hand2", fg="blue")
        author_twitter_label.pack()
        author_twitter_label.bind("<Button-1>", lambda e: self.open_link("https://twitter.com/sibansal"))

        author_website_label = tk.Label(dialog, text="Website", cursor="hand2", fg="blue")
        author_website_label.pack()
        author_website_label.bind("<Button-1>", lambda e: self.open_link("https://www.sibansal.dev"))

    @staticmethod
    def open_link(url):
        webbrowser.open(url)

    def view_license(self):
        try:
            with open("LICENSE.TXT", "r") as file:
                license_text = file.read()
            messagebox.showinfo("License", license_text)
        except FileNotFoundError:
            messagebox.showerror("Error", "License file not found.")