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
        return f"Name: {self.name} - SSN: {self.ssn} - role: {self.role} - licence: {self.licence} - address: {self.address} - phonenumber: {self.phonenumber}"

    def write_self_to_csv(path_to_csv):
        with(open(path_to_csv, "a")) as csv_file:
            csv_file.write()
#           return ?????

class CrewIO():
    def __init__(self, file_stream = None) :
        self.crew = []
        if file_stream :
            self.__read_data(file_stream)
        
    def __str__(self) :
        result_str = ''
        for emp in self.crew.items():
            result_str += "{}: {}\n".format(self.crew[0], self.crew[1:])
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
        return self.crew[emp]

filename = "Crew.csv"    
file_stream = open_file(filename)
crew = CrewIO(file_stream)
print(crew)


