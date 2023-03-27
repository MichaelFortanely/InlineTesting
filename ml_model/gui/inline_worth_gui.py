import tkinter as tk
from tkinter import messagebox

class InlineGUI:

    """ Display main menu of Inline Test GUI. """
    def __init__(self):
        self.root = tk.Tk()

        ''' size and color prefs '''
        self.root.geometry("500x500")
        self.root.title("Determine Inline Test Worthiness")

        label = tk.Label(self.root, text="Hello, World!")
        label.pack(padx=20, pady=20)

        ''' functionality '''

        # menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.menu_bar.add_cascade(menu = self.file_menu, label="File")
        self.root.config(menu=self.menu_bar)

        # exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        ''' display '''
        self.root.mainloop()
    
    """ Create a prompt in case user accidentally closes. """
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to close window?"):
            self.root.destroy()

InlineGUI()