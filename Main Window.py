import tkinter as tk
from tkinter import messagebox
from tkinter import font
from Window_2 import SecondWindow

class COVIDTracker(tk.Tk):
    #Initial State
    def __init__(self):
        super().__init__()
    
        #Main Window
        self.title("COVID-19 Tracker")
        self.geometry("400x300")

        #HDF Title
        header_font=font.Font(self, family="Helvetica", size="14", weight="bold")
        self.HDF_title = tk.Label(self, text = "COVID-19 HEALTH DECLARATION FORM", font=header_font)
        self.HDF_title.grid(row=0, column=0, sticky="ew")

        #HDF Content
        header_two_font=font.Font(self, family="Helvetica", size="12")
        self.HDF_user_title = tk.Label(self, text="NOTICE FOR USERS", font=header_two_font)
        self.HDF_Content = tk.Label(self, text = "I declare under oath that I personally accomplished this Health Declaration form. Further, I declare that the information given are true, correct, and complete statements pursuant to the provisions of pertinent laws, rules, and regulations of the Republic of the Philippines.", wraplength=400, justify="center")
        self.HDF_user_title.grid(row=1, column=0, sticky="ew")
        self.HDF_Content.grid(row=2, column=0)

        #Ok button
        self.button = tk.Button(self, text = "Ok", command=self.HDF_proper)
        self.button.grid(row=3, column=0)

        #Administrator
        main_separator_h = tk.Canvas(self, height=2, bg="black")
        main_separator_h.grid(row=4, column=0, columnspan=4, sticky="ew")
        self.admin_title=tk.Label(self, text="NOTICE FOR ADMINISTRATORS", font=header_two_font)
        self.admin_title.grid(row=5, column=0)
    
    #Second Window
    def HDF_proper(self):
        self.withdraw()
        SecondWindow()




if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()