import tkinter as tk
import tkinter as ttk

class COVIDTracker(tk.Tk):
    def __init__(self):
        super().__init__()
    
        #Main Window
        self.title("COVID-19 Tracker")
        self.geometry("500x500")

        #Label
        self.HDF_title = ttk.Label(self, text = "Health Declaration Form", font="arial 12")
        self.HDF_title.pack()

        #Label2
        self.HDF_Content = ttk.Label(self, text = "I declare under oath that I personally accomplished this Health Declaration form. Further, I declare that the information given are true, correct, and complete statements pursuant to the provisions of pertinent laws, rules, and regulations of the Republic of the Philippines.", wraplength=300, justify="center")
        self.HDF_Content.pack()

if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()