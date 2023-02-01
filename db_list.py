def create_patient_entry(patient_name,patient_mrn,patient_age):
    new_patient = [patient_name, patient_mrn, patient_age,[]]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1,34))
    db.append(create_patient_entry("Bob Boyles", 2,45))
    db.append(create_patient_entry("Charlie Chou", 1,52))
    print(db)
    print(db)
    mrn_to_find = 2
    found_patient = get_patient_entry(mrn_to_find,db)
    if found_patient is False:
       print("Patient mrn {} not found".format(mrn_to_find))
    else:
       add_test_to_patient(db,mrn_to_find,"HDL",120)
    

def get_patient_entry(mrn_to_find,db):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    else:
        return False

def add_test_to_patient(db, mrn_to_find,test_name,test_value):
    patient=get_patient_entry(mrn_to_find,db)
    patient[3].append([test_name,test_value])
    
if __name__=="__main__":
    main_driver()

