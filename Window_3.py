import tkinter as tk
from tkinter import font
import csv
import os
from Window_2 import SecondWindow
class Admin(tk.Toplevel):
    #Searching Mechanism
    def search_for_name_in_CSV(self, query):
        results = []
        # Set the desired directory path
        directory_path = os.path.join("D:/[CMPE103] OOP/Final_Project/", "COVID_CT.csv")
        with open (directory_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if query.lower() in row[0].lower():
                    results.append(row)
        return results

    def perform_search(self):
        query = self.search_entry.get()
        results = self.search_for_name_in_CSV(query)
        self.display_results(results)

    def display_results(self, results):
        self.results_listbox.delete(0, tk.END)
        SecondWindow()

        for result in results:
            result_string = ", ".join(result)
            self.results_listbox.insert(tk.END, result_string)

    #Tkinter window
    def __init__(self):
        super().__init__()

        #Third Window
        self.title("Admin Console")
        self.geometry("490x340")

        #Header Two Font
        header_two_font=font.Font(self, family="Helvetica", size="12")
        self.header = tk.Label(self, text="Search Entries", font=header_two_font)
        self.header.grid(row=0, column=0, columnspan=1)

        #Search Text and Entries
        self.enter_label=tk.Label(self, text="Search by name: ")
        self.enter_label.grid(row=1, column=0)
        self.search_entry=tk.Entry(self, width=50)
        self.search_entry.grid(row=1, column=1)
        self.search_button=tk.Button(self, text="Search", command=self.perform_search)
        self.search_button.grid(row=1, column=2)

        #Create results box below the field
        self.results_listbox=tk.Listbox(self)
        self.results_listbox.grid(row=4, column=0, columnspan=3, sticky="ew")
        scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.results_listbox.xview)
        self.results_listbox.config(xscrollcommand=scrollbar.set)
        scrollbar.grid(row=5, column=0, sticky="ew", columnspan=3)

        self.legend_label=tk.Label(self, text="Please use the opened window 2 as legend.")
        self.legend_label.grid(row=6, column=0, columnspan=4)