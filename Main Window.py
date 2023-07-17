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
        self.label.grid(row=0, column=0, columnspan=2)

        #User enters name here
        self.name_label=tk.Label(self, text="Name:")
        self.name_entry=tk.Entry(self, width="50")
        self.name_label.grid(row=1, column=0, sticky="e")
        self.name_entry.grid(row=1, column=1)

        #User enters age here
        self.age_label=tk.Label(self, text="Age:")
        self.age_entry=tk.Entry(self, width="50")
        self.age_label.grid(row=2, column=0, sticky="e")
        self.age_entry.grid(row=2, column=1)

        #User enters contact number here
        self.contact_number_label=tk.Label(self, text="Contact Number:")
        self.contact_number_entry=tk.Entry(self, width="50")
        self.contact_number_label.grid(row=3, column=0, sticky="e")
        self.contact_number_entry.grid(row=3, column=1)

        #User enters address here
        self.address_label=tk.Label(self, text="Address:")
        self.address_entry=tk.Entry(self, width="50")
        self.address_label.grid(row=4, column=0, sticky="e")
        self.address_entry.grid(row=4, column=1)

    #User checks their symptoms present
        #Instruction
        self.radiobutton_instruction=tk.Label(self, text="Please put a mark on the buttons next to each question.", font="arial 12")
        self.radiobutton_instruction.grid(row=6, column=0, columnspan=2)
        #Fever
        self.fever_label=tk.Label(self, text="Are you currently or have experienced the following symptoms in the past 14 days?", wraplength=80)
        self.fever_radio_yes=tk.Radiobutton(self, text="Yes")
        self.fever_radio_no=tk.Radiobutton(self, text="No")
        self.fever_label.grid(row=7, column=0, sticky="e")
        self.fever_radio_yes.grid(row=7, column=1)
        self.fever_radio_no.grid(row=7, column=2)

if __name__ == "__main__":
    CTracker = COVIDTracker()
    CTracker.mainloop()