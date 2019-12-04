import csv

with open('PastFlights.csv', newline= '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        # print(row['planeTypeId'], row['planeType'])






class Crew():
    def __init__(self):
        self.flightNumber = ""
        self.departingFrom = ""
        self.arrivingAt = ""
        self.departure = ""
        self.arrival = ""
        self.aircraftID = ""
        self.captain = ""
        self.copilot = ""
        self.fsm = ""
        self.fa1 = ""
        self.fa2 = ""