import tkinter as tk
from tkinter import messagebox, filedialog
from sklearn import tree
import sys
sys.path.append('../')
import parsing
import decision_tree
import try_ml_model

class InlineGUI:

    """ Display main menu of Inline Test GUI. """
    def __init__(self):
        self.root = tk.Tk()

        ''' machine learning model'''
        self.clf = tree.DecisionTreeClassifier()
        try_ml_model.setup_train_set("../processed_data.csv", self.clf)

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
        self.file_menu.add_command(label="Save File as...", command=self.save_file) # save user file

        self.menu_bar.add_cascade(menu = self.file_menu, label="File")  # name of bar option
        self.root.config(menu=self.menu_bar)

        # user text input
        self.text_box = tk.Text(self.root, height=13, font=("Arial", 16))
        self.text_box.pack(padx=10, pady=10)

        # button to submit user text input
        self.submit_btn = tk.Button(self.root, text="submit", font=("Arial", 16), command=self.inline_worth)
        self.submit_btn.pack(padx=10, pady=10)

        # exit
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        ''' display '''
        self.root.mainloop()
    
    """ Create a prompt in case user accidentally closes. """
    def on_closing(self):
        if((not self.text_box.edit_modified()) and (len(self.text_box.get("1.0", tk.END)) == 1)):
            self.root.destroy()
        else:
            if(self.text_box.edit_modified() == True):
                if(messagebox.askyesno(title="Quit?", message="You haven't saved. Are you sure?")):
                    self.root.destroy()
            else:
                self.root.destroy()

    """ Print user file from 'user_files' directory into text field. """
    def open_file(self):
        if(self.text_box.edit_modified()):
            if(messagebox.askyesno(title="Text has not been saved...", message="Are you sure?")):
                self.root.filename = filedialog.askopenfile(initialdir="../../user_files", title="Select a file...", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt")))
                if(self.root.filename):
                    file_dir = open(self.root.filename.name, "r")
                    file_txt = file_dir.read()
                    file_dir.close()
                    self.text_box.delete("1.0", "end")
                    self.text_box.insert("1.0", file_txt)
                    self.text_box.edit_modified(False)

        else:
            self.root.filename = filedialog.askopenfile(initialdir="../../user_files", title="Select a file...", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt")))
            if(self.root.filename):
                file_dir = open(self.root.filename.name, "r")
                file_txt = file_dir.read()
                file_dir.close()
                if(len(self.text_box.get("1.0", tk.END)) == 1):
                    self.text_box.insert("1.0", file_txt)
                else:
                    self.text_box.delete("1.0", "end")
                    self.text_box.insert("1.0", file_txt)
                self.text_box.edit_modified(False)
    
    def save_file(self):
        prgm_stmts = self.text_box.get("1.0", tk.END)
        if(len(prgm_stmts) != 1):
            self.root.filename = filedialog.asksaveasfile(initialdir="../../user_files", title="Save file...", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt")))
            if(self.root.filename):
                file_dir = open(self.root.filename.name, "w")
                file_dir.write(prgm_stmts)
                file_dir.close()
                self.text_box.edit_modified(False)

    def inline_worth(self):
        prgm_stmts = self.text_box.get("1.0", tk.END)
        if(len(prgm_stmts) != 1):
            prgm_lines = parsing.create_single_set(prgm_stmts.strip())
            print(prgm_lines)
            prgm_stmts_pd = decision_tree.run_user_tree(prgm_lines)
            worthiness = try_ml_model.inline_worthiness(self.clf, prgm_stmts_pd)
            self.text_box.delete("1.0", "end")
            # print(prgm_lines)
            # print(worthiness)
            for n in range(0, len(prgm_lines) - 1):
                result = " # Worthy of i-test"
                if(worthiness[n] == 0):
                    result = " # NOT worthy"
                self.text_box.insert(tk.END, str(prgm_lines[n + 1][1]) + result + "\n")

InlineGUI()