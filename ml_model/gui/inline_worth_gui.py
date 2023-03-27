import tkinter as tk
from tkinter import messagebox, filedialog

class InlineGUI:

    """ Display main menu of Inline Test GUI. """
    def __init__(self):
        self.root = tk.Tk()

        ''' size and color prefs '''
        self.root.geometry("800x500")
        self.root.title("Inline Test Worthiness")

        label = tk.Label(self.root, text="Determine whether a Program Statement is worthy of an Inline Test!", font=("Arial", 16))
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
        self.text_box = tk.Text(self.root, height=13, font=("Arial", 16))
        self.text_box.pack(padx=10, pady=10)
        self.submit_btn = tk.Button(self.root, text="submit", font=("Arial", 16))
        self.submit_btn.pack(padx=10, pady=10)

        # exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        ''' display '''
        self.root.mainloop()
    
    """ Create a prompt in case user accidentally closes. """
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to close window?"):
            self.root.destroy()

    """ Print user file from 'user_files' directory into text field. """
    def open_file(self):
        self.root.filename = filedialog.askopenfile(initialdir="../../user_files", title="Select a file...", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt")))
        file_dir = open(self.root.filename.name, "r")
        file_txt = file_dir.read()
        if(len(self.text_box.get("1.0", tk.END)) == 1):
            self.text_box.insert("1.0", file_txt)
        else:
            if messagebox.askyesno(title="There is text in the text box...", message="Do you want to append it?\nYes - Append\nNo - Replace"):
                self.text_box.insert(tk.END, "\n"+file_txt)
            else:
                self.text_box.delete("1.0", "end")
                self.text_box.insert("1.0", file_txt)


InlineGUI()