"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""

def print_dosing_interface():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
def dosing_input():
    diagnosis = int(input("Enter a number: "))
    return diagnosis

def print_weight_interface():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")

def get_weight_input():
    weight_input = input("Enter weight: ")
    return weight_input

def parse_weight(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return weight

def dose_amount_calc(diagnosis,weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_per_kg,dosage_mg_first_day

def print_dosage(weight,dosage_mg_per_kg,dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))
    
def dose_amount():
    print_dosing_interface()
    dosing_in=dosing_input()
    print_weight_interface()
    weight_in =get_weight_input()
    weight=parse_weight(weight_in)
    dose_info=dose_amount_calc(dosing_in,weight)
    print_dosage(weight,dose_info[0],dose_info[1])
    

if __name__ == '__main__':
    dose_amount()
