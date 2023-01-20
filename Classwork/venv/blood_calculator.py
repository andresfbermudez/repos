def interface():

    print("Blood Calculator")
    run = True
    while(run == True):
        print("Options:")
        print("1-HDL")
        print("9-Quit")
        choice = input("Select an option:")
        if choice == "9":
            run = False
        elif choice == "1":

    print("Program ending")
interface()

def HDL_input():
    HDL_value= input("Enter the HDL result")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if HDL_int >=60:
        answer= "Normal"
    elif 40<= HDL_int <60:
        answer= "Borderline Low"
    else:
        answer= "Low"
    return answer

def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    return HDL_analy