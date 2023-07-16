import tkinter as tk

class COVIDTracker(tk.Tk):
    def Main(self):
        self.title("COVIDTracker")
        self.geometry("1000x1000")
        self.mainloop()

Ct = COVIDTracker()
Ct.Main()