def open_file(filename) :
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError :
        return None

class Employee:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
    
    def __str__(self):
        return f"Name: {self.name} - SSN: {self.ssn}"

    def write_self_to_csv(path_to_csv):
        with(open(path_to_csv, "a")) as csv_file:
            csv_file.write()

class CrewIO():
    def __init__(self, file_stream = None) :
        self.crew = {}
        if file_stream :
            self.__read_data(file_stream)
        
    def __str__(self) :
        result_str = ''
        for key, value in self.crew.items():
            result_str += "{}: {}\n".format(key, value)
        return result_str

    def __read_data(self, file_object) :
        header = True
        for line in file_object :
            if header :
                header = False
                continue
            else: 
                ssn,name,role,rank,licence,address,phonenumber = line.strip().split(",")
                emp = Employee(name, ssn)
                key = name
                self.crew[key] = (int(ssn), role, rank, licence, address, int(phonenumber))
                self.crew[emp]
        return self.crew


filename = "Crew.csv"    
file_stream = open_file(filename)
crew_dict = CrewIO(file_stream)
print(crew_dict)



