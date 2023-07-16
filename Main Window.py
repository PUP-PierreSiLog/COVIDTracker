import tkinter as tk
import tkinter as ttk

class COVIDTracker(tk.Tk):
    def __init__(self):
        super().__init__()
    
        #Main Window
        self.title("COVID-19 Tracker")
        self.geometry("1000x1000")

        #Label
        self.label = ttk.Label(self, text = "Health Declaration Form")
        self.label.pack()


if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()