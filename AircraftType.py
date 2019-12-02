import csv

list = []
with open('AircraftType.csv', newline= '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        atm = AircraftTypeModel()
        atm.planeTypeId = row["planeTypeId"]
        list.append(atm)
        # print(row)
        #for key in row:
        #    print(str(key) + ": " + str(row[key]), end=" ")
        #print(row['planeTypeId'], row['manufacturer'])

class AircraftTypeModel:
    def __init__(self):
        self.planeTypeId = ""
        self.manufacturer = ""
