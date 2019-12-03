import csv

with open('Crew.csv', newline= '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        # print(row['planeTypeId'], row['planeType'])




class Crew():
    def __init__(self):
        self.ssn = ""
        self.name = ""
        self.role = ""
        self.rank = ""
        self.licence = ""
        self.address = ""
        self.phonenumber = ""
    