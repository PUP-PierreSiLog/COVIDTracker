import tkinter as tk
class SecondWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        #Second Window
        self.title("Health Declaration Form")
        self.geometry("600x600")

        #Instruction
        self.label = tk.Label(self, text="Please enter correct information in the required fields.")
        self.label.pack        