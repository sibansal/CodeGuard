import tkinter as tk
from CodeGuardApp import CodeGuardApp

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("400x400")
    window.eval('tk::PlaceWindow . center')
    app = CodeGuardApp(window)
    window.mainloop()