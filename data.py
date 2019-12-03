def open_file(filename) :
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError :
        return None

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
            
                key = name
                self.crew[key] = (int(ssn), role, rank, licence, address, int(phonenumber))
        return self.crew


filename = "Crew.csv"    
file_stream = open_file(filename)
crew_dict = CrewIO(file_stream)
print(crew_dict)



