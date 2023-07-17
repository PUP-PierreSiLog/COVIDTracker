import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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

    #Response when Ok button is clicked
    def ok_button_clicked(self):
        messagebox.showinfo("Response", "Response Recorded!")

class SecondWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        #Second Window
        self.title("Health Declaration Form")
        self.geometry("600x600")

        #Instruction
        self.label = tk.Label(self, text="Please enter correct information in the required fields.", font="arial 12")
        self.label.pack()

        #User enters name here
        self.name_label=tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry=tk.Entry(self)
        self.name_entry.pack()


if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()