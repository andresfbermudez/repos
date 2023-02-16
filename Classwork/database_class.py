class Patient:

    def __init__(self, patient_first_name, patient_last_name,
                 patient_mrn, patient_age):
        self.first_name = patient_first_name
        self.last_name = patient_last_name
        self.mrn = patient_mrn
        self.age = patient_age
        self.tests = []

    def get_full_name(self):
        full_name = "{} {}".format(self.first_name,self.last_name)
        return full_name

def main():
    new_patient = Patient("Ann", "Ables", 1, 34)
    print(new_patient)
    print(new_patient.get_full_name())
    
if __name__ == "__main__":
    main()
