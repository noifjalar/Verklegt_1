import csv



def print_main_menu():
    print("\tMain Menu")
    print("")
    print("Shift manager:")
    print("\t(1) - Register employee") #1
    print("\t(2) - Change employee info") #2
    print("\t(3) - Assign cabin/pilot to voyage") #3
    print("\t(4) - Display voyage") #4
    print("")
    print("Registration manager:")
    print("\t(5) - Register destination") #5
    print("\t(6) - Register airplanes") #6
    print("\t(7) - Create voyage") #7
    choice = input("Select an operation with a corresponding number: ")
    return choice

def choose_main_menu(choice):
    if choice == "1":
        register_employee()
    elif choice == "2":
        change_employee_info()
    elif choice == "3":
        assign_cabin_pilot_to_voyage()
    elif choice == "4":
        display_voyage()
    elif choice == "5":
        register_destination()
    elif choice == "6":
        register_airplanes()
    elif choice == "7":
        chreate_voyage()
    elif choice.lower() == "q":
        print("")
        #Vantar ehv hérna
    else:
        print("Input error! Try again")
        # Hérna líka
    return None

def register_employee():
    new_emp = []
    name = input("Name: ")
    new_emp.append(name)
    ssn = input("SSN: ")
    new_emp.append(ssn)
    address = input("Address: ")
    new_emp.append(address)
    role = input("Role: ")
    new_emp.append(role)
    rank = input("Rank: ")
    new_emp.append(rank)
    mobile = input("Mobile: ")
    new_emp.append(mobile)
    licence = input("Licence: ")
    new_emp.append(licence)
    #emp = Employee(name, ssn, address)
    #emp.write_to_csv("Crew.csv")
    
    



    new_emp4print = (",".join(new_emp))
    # print(new_emp4print)

    # crew_file = open("Crew.csv","a")

    with open("Crew.csv","a") as crew_file:
        crew_file.write("\n")
        crew_file.write(new_emp4print)

    #print(crew_file)æ

    
    



def main() :
    choice = print_main_menu()
    choose_main_menu(choice)


main()


