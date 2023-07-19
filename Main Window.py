import tkinter as tk
from tkinter import messagebox
from Window_2 import SecondWindow

class COVIDTracker(tk.Tk):
    #Initial State
    def __init__(self):
        super().__init__()
    
        #Main Window
        self.title("COVID-19 Tracker")
        self.geometry("500x300")

        #HDF Title
        self.HDF_title = tk.Label(self, text = "Health Declaration Form", font="arial 12")
        self.HDF_title.pack()

        #HDF Content
        self.HDF_Content = tk.Label(self, text = "I declare under oath that I personally accomplished this Health Declaration form. Further, I declare that the information given are true, correct, and complete statements pursuant to the provisions of pertinent laws, rules, and regulations of the Republic of the Philippines.", wraplength=300, justify="center")
        self.HDF_Content.pack()

        #Ok button
        self.button = tk.Button(self, text = "Ok", command=self.HDF_proper)
        self.button.pack()
    
    #Second Window
    def HDF_proper(self):
        self.withdraw()
        SecondWindow()



if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()