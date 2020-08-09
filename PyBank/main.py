import csv
import os

file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path) as csvFile:
    csvReader = csv.reader(csvFile)
    totalMonths = -1
    totalProfitLoss = 0
    currentIncrease = 0
    currentDecrease = 0

    for row in csvReader:
        totalMonths = totalMonths + 1                           #store the value for total months
    #print(totalMonths)

        for col in csvReader:
            totalProfitLoss += (int (col[1]))                   #store the value for total profit loss
        #print(totalProfitLoss)

            if (int (col[1])) > currentIncrease:
                currentIncrease = (int (col[1]))                #store the greatest increase value
        #print(currentIncrease)

            if (int (col[1])) < currentDecrease:
                currentDecrease = (int (col[1]))                #store the greatest decrease value
        #print(currentDecrease)
        