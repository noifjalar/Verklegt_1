import csv

with open('Aircraft.csv', newline= '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[])
        # print(row['planeTypeId'], row['planeType'])