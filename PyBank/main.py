import csv
import os

file_path = os.path.join("Resources", "budget_data.csv")

totalMonths = 0
totalProfitLosses = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""
avgChange = 0
profitList = []

with open(file_path, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        totalMonths = totalMonths + 1
        totalProfitLosses = totalProfitLosses + int(row['Profit/Losses'])
        if greatestIncrease < int(row['Profit/Losses']):
            greatestIncrease = int(row['Profit/Losses'])
            greatestIncreaseDate = row['Date']
        
        if greatestDecrease > int(row['Profit/Losses']):
            greatestDecrease = int(row['Profit/Losses'])
            greatestDecreaseDate = row['Date']

        profitList.append(int(row['Profit/Losses']))
        avgChange = sum(profitList)/len(profitList)
    




output = f'''
Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalProfitLosses}
Average  Change: ${avgChange:.02f}
Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})
Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})
'''
print(output)

with open('pyBank_Output.txt', 'w') as outputFile:
    outputFile.write(output)