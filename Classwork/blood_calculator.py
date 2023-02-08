def interface():
    print("Blood Calculator")
    run = True
    while (run is True):
        print("Options:")
        print("1-HDL")
        print("2-LDL")
        print("3-Total")
        print("9-Quit")
        choice = input("Select an option:")
        if choice == "9":
            run = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()
    print("Program ending")


def HDL_input():
    HDL_value = input("Enter the HDL result: ")
    HDL_value = int(HDL_value)
    return HDL_value


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)


def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is consider {}".format(HDL_value,HDL_analy))


def LDL_input():
    LDL_value= input("Enter the LDL result: ")
    LDL_value = int(LDL_value)
    return LDL_value


def LDL_analysis(LDL_int):
    if LDL_int <130:
        answer= "Normal"
    elif 130<= LDL_int <=159:
        answer= "Borderline High"
    elif 160 <= LDL_int < 189:
        answer = "High"
    else:
        answer= "Very High"
    return answer


def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in,LDL_analy)


def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is consider {}".format(LDL_value,LDL_analy))


def total_input():
    total_value= input("Enter the total cholesterol result: ")
    total_value = int(total_value)
    return total_value


def total_analysis(total_int):
    if total_int <200:
        answer= "Normal"
    elif 200<= total_int <=239:
        answer= "Borderline High"
    else:
        answer= "High"
    return answer


def total_driver():
    total_in = total_input()
    total_analy = total_analysis(total_in)
    total_output(total_in,total_analy)


def total_output(total_value, total_analy):
    print("The total result of {} is consider {}".format(total_value,total_analy))


if __name__== "__main__":
    interface()
