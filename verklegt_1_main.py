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
    print("\t(5) - Register destinations") #5
    print("\t(6) - Register airplanes") #6
    print("\t(7) - Create voyage") #7
    choice = input("Select an operation with a corresponding number: ")
    return choice

def main() :
    choice = print_main_menu()

main()