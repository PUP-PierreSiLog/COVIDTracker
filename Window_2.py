import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import csv
class SecondWindow(tk.Toplevel):
    def save_user_response(self):
        #Get responses from the Widgets
        name=self.name_entry.get()
        age = self.age_entry.get()
        contact_number = self.contact_number_entry.get()
        address = self.address_entry.get()
        fever_response = self.radio_fever_var.get()
        cough_response = self.radio_cough_var.get()
        pains_response = self.radio_pains_var.get()
        sore_throat_response = self.radio_sore_throat_var.get()
        fatigue_response = self.radio_fatigue_var.get()
        diarrhea_response = self.radio_diarrhea_var.get()
        taste_response = self. radio_taste_var.get()
        breathing_response = self.radio_breathing_var.get()
        ftf_response = self.radio_ftf_var.get()
        PPE_response = self.radio_PPE_var.get()
        international_travel_response = self.radio_travel_international_var.get()
        domestic_travel_response = self.radio_travel_domestic_var.get()
        domestic_travel_place_response = self.travel_dom_entry.get()
        #Creation of a CSV file
        with open("COVID Contact Trace.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Contact Number", "Address", "Fever Response", "Cough Response", "Pains Response", "Sore Throat Response", "Fatigue Response", "Diarrhea Response", "Taste Respomnse", "Breathing Response", "Close Contact?", "Contact without PPE?", "Went for Int'l Travel?", "Went for Domestic Travel?", "If yes, where?"])
            writer.writerow([name, age, contact_number, address, fever_response, cough_response, pains_response, sore_throat_response, fatigue_response, diarrhea_response, taste_response, breathing_response, ftf_response, PPE_response, international_travel_response, domestic_travel_response, domestic_travel_place_response])
        
        messagebox.showinfo("Response", "Response Recorded!")
        self.save_user_response()
        

    def radio_select(self):
        selected_option=self.radio_var.get()
        return selected_option

    def __init__(self):
        super().__init__()

        #Second Window
        self.title("Health Declaration Form")
        self.geometry("560x560")

        #Header Preferences
        header_font=font.Font(self, family="Helvetica", size="12", weight="bold")
        #Separator
        main_separator_h = tk.Canvas(self, height=2, bg="black")
        main_separator_h_2 = tk.Canvas(self, height=2, bg="black")

        #Instruction
        self.label = tk.Label(self, text="PART 1: PERSONAL INFORMATION", font=header_font)
        self.label.grid(row=0, column=0, sticky="ew", columnspan=4)

        #User enters name here
        self.name_label=tk.Label(self, text="Name:")
        self.name_entry=tk.Entry(self, width="50")
        self.name_label.grid(row=1, column=0, sticky="e")
        self.name_entry.grid(row=1, column=1, columnspan=2)

        #User enters age here
        self.age_label=tk.Label(self, text="Age:")
        self.age_entry=tk.Entry(self, width="50")
        self.age_label.grid(row=2, column=0, sticky="e")
        self.age_entry.grid(row=2, column=1, columnspan=2)

        #User enters contact number here
        self.contact_number_label=tk.Label(self, text="Contact Number:")
        self.contact_number_entry=tk.Entry(self, width="50")
        self.contact_number_label.grid(row=3, column=0, sticky="e")
        self.contact_number_entry.grid(row=3, column=1, columnspan=2)

        #User enters address here
        self.address_label=tk.Label(self, text="Address:")
        self.address_entry=tk.Entry(self, width="50")
        self.address_label.grid(row=4, column=0, sticky="e")
        self.address_entry.grid(row=4, column=1, columnspan=2)

    #Separates part 1 from part 2
        main_separator_h.grid(row=5, column=0, columnspan=4, sticky="ew")

    #Radio Button Style
        style = ttk.Style()
        style.configure("Tradiobutton", relief="flat", borderwidth=0)
    
    #Radio Variable Handling
        self.radio_fever_var = tk.StringVar()
        self.radio_cough_var = tk.StringVar()
        self.radio_pains_var = tk.StringVar()
        self.radio_sore_throat_var = tk.StringVar()
        self.radio_fatigue_var = tk.StringVar()
        self.radio_headache_var = tk.StringVar()
        self.radio_diarrhea_var = tk.StringVar()
        self.radio_taste_var = tk.StringVar()
        self.radio_breathing_var = tk.StringVar()
        self.radio_ftf_var = tk.StringVar()
        self.radio_PPE_var = tk.StringVar()
        self.radio_travel_international_var = tk.StringVar()
        self.radio_travel_domestic_var = tk.StringVar()


    #User checks their symptoms present
        #Instruction
        self.radiobutton_instruction=tk.Label(self, text="PART 2: SYMPTOMS, POSSIBLE EXPOSURES, AND TRAVEL HISTORY", font=header_font)
        self.radiobutton_instruction.grid(row=6, column=0, columnspan=4)

        #General Symptoms
        self.symptoms_label=tk.Label(self, text="Are you currently or have experienced the following symptoms in the past 14 days?", wraplength=90)
        self.symptoms_label.grid(row=7, column=0, sticky="w", rowspan=8)

        #Fever
        self.fever_label=tk.Label(self, text="Fever")
        self.fever_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_fever_var, value="Y_Fever")
        self.fever_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_fever_var, value="N_Fever")
        #Fever->Alignment
        self.fever_label.grid(row=7, column=1)
        self.fever_radio_yes.grid(row=7, column=2)
        self.fever_radio_no.grid(row=7, column=3)

        #Colds
        self.colds_label=tk.Label(self, text="Cough and/or Colds")
        self.colds_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_cough_var, value="Y_colds")
        self.colds_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_cough_var, value="N_colds")
        #Colds->Alignment
        self.colds_label.grid(row=8, column=1)
        self.colds_radio_yes.grid(row=8, column=2)
        self.colds_radio_no.grid(row=8, column=3)

        #Body Pains
        self.body_pains_label=tk.Label(self, text="Body Pains")
        self.body_pains_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_pains_var, value="Y_pains")
        self.body_pains_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_pains_var, value="N_pains")
        #Body Pains->Alignment
        self.body_pains_label.grid(row=9, column=1)
        self.body_pains_radio_yes.grid(row=9, column=2)
        self.body_pains_radio_no.grid(row=9, column=3)

        #Sore Throat
        self.sore_throat_label=tk.Label(self, text="Sore Throat")
        self.sore_throat_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_sore_throat_var, value="Y_sore_throat")
        self.sore_throat_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_sore_throat_var, value="N_sore_throat")
        #Sore Throat->Alignment
        self.sore_throat_label.grid(row=10, column=1)
        self.sore_throat_radio_yes.grid(row=10, column=2)
        self.sore_throat_radio_no.grid(row=10, column=3)

        #Fatigue
        self.fatigue_label=tk.Label(self, text="Fatigue")
        self.fatigue_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_fatigue_var, value="Y_fatigue")
        self.fatigue_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_fatigue_var, value="N_fatigue")
        #Fatigue->Alignment
        self.fatigue_label.grid(row=11, column=1)
        self.fatigue_radio_yes.grid(row=11, column=2)
        self.fatigue_radio_no.grid(row=11, column=3)

        #Diarrhea
        self.diarrhea_label=tk.Label(self, text="Diarrhea")
        self.diarrhea_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_diarrhea_var, value="Y_diarrhea")
        self.diarrhea_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_diarrhea_var, value="N_diarrhea")
        #Diarrhea->Alignment
        self.diarrhea_label.grid(row=12, column=1)
        self.diarrhea_radio_yes.grid(row=12, column=2)
        self.diarrhea_radio_no.grid(row=12, column=3)

        #Loss of Taste
        self.taste_label=tk.Label(self, text="Loss of taste or smell")
        self.taste_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_taste_var, value="Y_taste")
        self.taste_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_taste_var, value="N_taste")
        #Loss of Taste->Alignment
        self.taste_label.grid(row=13, column=1)
        self.taste_radio_yes.grid(row=13, column=2)
        self.taste_radio_no.grid(row=13, column=3)

        #Breathing
        self.breathing_label=tk.Label(self, text="Difficulty Breathing")
        self.breathing_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_breathing_var, value="Y_breathing")
        self.breathing_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_breathing_var, value="N_breathing")
        #Breathing->Alignment
        self.breathing_label.grid(row=14, column=1)
        self.breathing_radio_yes.grid(row=14, column=2)
        self.breathing_radio_no.grid(row=14, column=3)

        #Face to Face
        self.interactions_label=tk.Label(self, text="Have you had face-to-face contact with a probable or confirmed COVID-19 case within one (1) meter and for more than 15 minutes in the past 14 days?", wraplength=400)
        self.interactions_label.grid(row=15, column=0, sticky="w", columnspan=2)
        self.interactions_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_ftf_var, value="Y_ftf")
        self.interactions_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_ftf_var, value="N_ftf")
        #Face-to-Face->Alignment
        self.interactions_label.grid(row=15, column=0)
        self.interactions_radio_yes.grid(row=15, column=2)
        self.interactions_radio_no.grid(row=15, column=3)

        #PPE
        self.ppe_label=tk.Label(self, text="Have you provided direct care for a patient with a probable or confirmed COVID-19 case without using PPE for the past 14 days?", wraplength=400)
        self.ppe_label.grid(row=15, column=0, sticky="w", columnspan=2)
        self.ppe_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_PPE_var, value="Y_PPE")
        self.ppe_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_PPE_var, value="N_PPE")
        #PPE->Alignment
        self.ppe_label.grid(row=16, column=0)
        self.ppe_radio_yes.grid(row=16, column=2)
        self.ppe_radio_no.grid(row=16, column=3)

        #Travel International
        self.travel_label=tk.Label(self, text="Have you traveled outside the Philippines for the last 14 days?", wraplength=400)
        self.travel_label.grid(row=15, column=0, sticky="w", columnspan=2)
        self.travel_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_travel_international_var, value="Y_international")
        self.travel_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_travel_international_var, value="N_international")
        #Travel International->Alignment
        self.travel_label.grid(row=17, column=0)
        self.travel_radio_yes.grid(row=17, column=2)
        self.travel_radio_no.grid(row=17, column=3)

        #Travel Domestic
        self.travel_dom_label=tk.Label(self, text="Have you traveled outside the municipality you currently reside in?", wraplength=400)
        self.travel_dom_label_entry=tk.Label(self, text="If your answer is yes, specify where in the field on your right.", wraplength=400)
        self.travel_dom_entry=tk.Entry(self, width=25)
        self.travel_dom_label.grid(row=15, column=0, sticky="w", columnspan=2)
        self.travel_dom_radio_yes=ttk.Radiobutton(self, text="Yes", variable=self.radio_travel_domestic_var, value="Y_domestic")
        self.travel_dom_radio_no=ttk.Radiobutton(self, text="No", variable=self.radio_travel_domestic_var, value="N_domestic")
        #Travel International->Alignment
        self.travel_dom_label.grid(row=18, column=0)
        self.travel_dom_label_entry.grid(row=19, column=0, columnspan=2)
        self.travel_dom_entry.grid(row=19, column=2, sticky="e", columnspan=2)
        self.travel_dom_radio_yes.grid(row=18, column=2)
        self.travel_dom_radio_no.grid(row=18, column=3)

    #Submission Button
        #Texts
        main_separator_h_2.grid(row=20, column=0, columnspan=4, sticky="ew")
        self.submit_instruction=tk.Label(self, text="PART 3: SUBMISSION OF DATA", font=header_font)
        self.final_label=tk.Label(self, text="Please click the Submit button on your right if you are done.", wraplength=400)
        self.submit_instruction.grid(row=21, column=0, sticky="ew", columnspan=4)
        self.final_label.grid(row=22, column=0, columnspan=3)

        #Buttton
        self.submit_button=tk.Button(self, text="Submit", command=self.ok_button_clicked)
        self.submit_button.grid(row=22, column=3)


        