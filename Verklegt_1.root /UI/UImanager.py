from Logic.LogicManager import LogicManager
from Data.DataManager import DataManager
class UImanager :
    def __init__(self) :
        self.__ = LogicManager()
        pass

    def main_menu(self) :
        choice = ""
        while choice != "q" :
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
            print("\t Press q to quit")

            choice = input("Select an operation with a corresponding number: ").lower()
            choice = str(choice)
            if choice == "1":
                the_instance = LogicManager()
                the_ret_str = the_instance.register_employee()
                print(the_ret_str)
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
            elif choice == "q":
                break
            else:
                print("Input error! Try again")
                self.main_menu()