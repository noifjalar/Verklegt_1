def open_file(filename) :
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError :
        return None

class EmployeeIO:
    def __init__(self, ssn, name, role, rank, licence, address, phonenumber):
        self.ssn = ssn
        self.name = name
        self.role = role 
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phonenumber = phonenumber

    def __str__(self):
        return "Name: {self.name} - SSN: {self.ssn} - role: {self.role} - licence: {self.licence} - address: {self.address} - phonenumber: {self.phonenumber} "

    def make_self_writeable(self):
        str = self.ssn + ','
        str += self.name + ','
        str += self.role + ','
        str += self.rank + ','
        str += self.licence + ','
        str += self.address + ','
        str += self.phonenumber
        return str

    def write_self_to_csv(self, path_to_csv):
        str = self.make_self_writeable()
        with(open(path_to_csv, "a")) as csv_file:
            csv_file.write(str)  


class CrewIO():
    def __init__(self, file_stream = None) :
        self.crew = []
        if file_stream :
            self.__read_data(file_stream)
        
    def __str__(self) :
        result_str = ''
        for cha in self.crew :
            result_str += str(cha)
        return result_str

    def __read_data(self, file_object) :
        header = True
        for line in file_object :
            if header :
                header = False
                continue
            else: 
                ssn, name, role, rank, licence, address, phonenumber = line.strip().split(",")
                emp = EmployeeIO(ssn, name, role, rank, licence, address, phonenumber)
                self.crew.append(emp)
        return self.crew

filename = "Crew.csv"    
file_stream = open_file(filename)
crew = CrewIO(file_stream)
ssn = input("SSN: ")
name = input("Name: ")
role = input("Role: ")
rank = input("Rank: ")
licence = input("Licence: ")
address = input("Address: ")
phonenumber = input("Phonenumber: ")
emp = EmployeeIO(ssn, name, role, rank, licence, address, phonenumber)
emp.write_self_to_csv(filename)


