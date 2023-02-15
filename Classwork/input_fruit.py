# Open file
in_file = open("input_data.txt", "r")

# Puts each line in a list of strings
fruits = in_file.readlines()
in_file.close()
print(fruits)

# Other option
in_file = open("input_data.txt", "r")
first_fruit = in_file.readline()
second_fruit = in_file.readline()
in_file.close()
print(first_fruit)
print(second_fruit)

#For file
def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    patient_id = first_line.strip("\n").split("=")
    patient_id = int(patient_id[1])
    return patient_id

def test_read_file():
    filename = "input_file.txt"
    answer = read_file(filename)
    expected = 50
    assert answer == expected
    
