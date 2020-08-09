import csv
import os

file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path) as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)