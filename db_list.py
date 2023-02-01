def create_patient_entry(patient_name,patient_mrn,patient_age):
    new_patient = [patient_name, patient_mrn, patient_age,[]]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1,34))
    db.append(create_patient_entry("Bob Boyles", 2,45))
    db.append(create_patient_entry("Charlie Chou", 1,52))
    print(db)
    add_test_to_patient(db,1,"HDL",120)
    add_test_to_patient(db,2,"LDL",100)
    
    mrn_to_find = 1
    test_to_find = "HDL"
    found_patient, test_result = get_test_result(db,mrn_to_find,test_to_find)
    print("Patient {} result for {} test is {}".format(found_patient[0],test_to_find,test_result))
          
def get_test_result(db,mrn_to_find,test_name):
    patient = get_patient_entry(mrn_to_find,db)
    for test in patient[3]:
        if test[0] == test_name:
            return patient, test[1]
        else:
            return False
        
def print_directory(db,room_numbers):
    for i,patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0],room_numbers[i]))
    for patient,rn in zip(db,room_numbers):
        print("Patient {} is in room {}".format(patient[0],rn))
                      
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

