from Data.DataManager import DataManager

class LogicManager :
    def __init__(self) :
        self.__ = DataManager()
        pass 


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