import tkinter as tk
from tkinter import font
import csv
class Admin(tk.Toplevel):
    #Searching Mechanism
    def search_for_name(query):
        results = []
        with open ("COVID CT.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if query.lower in row[0].lower():
                    results.append(row)
        return results

    #Tkinter window
    def __init__(self):
        super().__init__()

        #Third Window
        self.title("Admin Console")
        self.geometry("560x560")

        #Header Two Font
        header_two_font=font.Font(self, family="Helvetica", size="12")
        self.header = tk.Label(self, text="Search Entries", font=header_two_font)
        self.header.grid(row=0, column=0, columnspan=1)

        #Search Text and Entries
        self.enter_label=tk.Label(self, text="Search by name: ")
        self.enter_label.grid(row=1, column=0)
        self.search_entry=tk.Entry(self, width=50)
        self.search_entry.grid(row=1, column=1)
        self.search_button=tk.Button(self, text="Search")
        self.search_button.grid(row=1, column=2)
