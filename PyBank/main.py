import csv
import os

file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    totalMonths = 0
    totalProfitLoss = 0
    currentIncrease = 0
    currentDecrease = 0
    totalChange = 0

    for row in csvReader:

        for col in csvReader:

            totalMonths = totalMonths + 1                       #store the value for total months
        #print(totalMonths)

            totalProfitLoss += (int (col[1]))                   #store the value for total profit loss
        #print(totalProfitLoss)

            if (int (col[1])) > currentIncrease:
                currentIncrease = (int (col[1]))                #store the greatest increase value
                
        #print(currentIncrease)

            if (int (col[1])) < currentDecrease:
                currentDecrease = (int (col[1]))                #store the greatest decrease value
        #print(currentDecrease)

    #print(totalMonths)
    #print(totalProfitLoss)
    #print(currentIncrease)
    #print(currentDecrease)

print("Financial Analysis")
print("----------------------------")
print("Total Months: ", totalMonths)
print("Average Change: ")
print("Greatest Increase in Profits: ", currentIncrease)
print("Greatest Decrease in Profits: ", currentDecrease)