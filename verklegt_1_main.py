def open_file(filename) :
    file_object = open(filename, "r")
    return file_object

def make_crew_dict(file_object) :
    crew_dict= {}
    for line in file_object :
        ssn,name,role,rank,licence = line.strip().split(",")
        
        key = name
        crew_dict[key] = (int(ssn), role, rank, licence)
    return crew_dict
        
def main() :
    filename = "crew.csv"
    file_object = open_file(filename)
    crew_dict = make_crew_dict(file_object)
    print(crew_dict)

main()