import tkinter as tk
class SecondWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #Second Window
        self.title("Health Declaration Form")
        self.geometry("600x600")


if __name__=="__main__":
    SWindow = SecondWindow()
    SWindow.mainloop()