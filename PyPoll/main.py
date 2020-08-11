import csv

filePath = "Resources/election_data.csv"

totalVotes = 0
unique_list = []

with open(filePath) as csvFile:
    csvReader = csv.DictReader(csvFile)

    for x in csvReader:
        if x not in unique_list:
            unique_list.append(x)

    candidate_list = ['Candidate']

    print(unique_list)