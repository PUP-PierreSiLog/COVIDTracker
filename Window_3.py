import tkinter as tk
class Admin(tk.Toplevel):
    def __init__(self):
        super().__init__()

        #Second Window
        self.title("Admin Console")
        self.geometry("560x560")

        self.enter_label=tk.Label(self, text="Search here: ")
        self.enter_label.grid(row=1, column=0)