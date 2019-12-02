def open_file(filename) :
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError :
        return None

def make_crew_dict(file_object) :
    crew_dict= {}
    header = True
    for line in file_object :
        if header :
            header = False
            continue
        else: 
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