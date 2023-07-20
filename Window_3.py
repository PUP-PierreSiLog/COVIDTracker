import tkinter as tk
from tkinter import font
import csv
class Admin(tk.Toplevel):
    #Searching Mechanism
    def search_for_name_in_CSV(query):
        results = []
        with open ("COVID CT.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if query.lower in row[0].lower():
                    results.append(row)
        return results

    def perform_search(self):
        query = self.search_entry.get()
        results = self.search_for_name(query)
        self.display_results(results)

    def display_results(self, results):
        self.results_listbox.delete(0, tk.END)

        for result in results:
            result_string = ",".join(result)
            self.results_listbox.insert(tk.END, result_string)

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
        self.search_entry=tk.Entry(self, width=50, command=self.perform_search)
        self.search_entry.grid(row=1, column=1)
        self.search_button=tk.Button(self, text="Search")
        self.search_button.grid(row=1, column=2)

        #Create results box below the field
        results_listbox=tk.Listbox()
        results_listbox.grid(row=2, column=0, columnspan=2)