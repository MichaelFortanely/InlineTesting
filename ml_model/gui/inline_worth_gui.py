import tkinter as tk
from tkinter import messagebox, filedialog

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
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0) # create bar

        self.file_menu.add_command(label="Close", command=self.on_closing)  # close button
        self.file_menu.add_command(label="Open File", command=self.open_file) # open user file

        self.menu_bar.add_cascade(menu = self.file_menu, label="File")  # name of bar option
        self.root.config(menu=self.menu_bar)

        # user text input
        

        # exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        ''' display '''
        self.root.mainloop()
    
    """ Create a prompt in case user accidentally closes. """
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to close window?"):
            self.root.destroy()

    """ Open user file from 'user_files' directory. """
    def open_file(self):
        self.root.filename = filedialog.askopenfile(initialdir="../../user_files", title="Select a file...", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt")))

InlineGUI()