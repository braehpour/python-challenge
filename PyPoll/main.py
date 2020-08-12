import csv

filePath = "Resources/election_data.csv"

totalVotes = 0
candidateList = []
candidateListClean = []
winner = ""
voteList = []
percentList = []

KhanCount = 0
CorreyCount = 0
LiCount = 0
OTooleyCount = 0

KhanPercent = 0
CorreyPercent = 0
LiPercent = 0
OTooleyPercent = 0

#['Khan', 'Correy', 'Li', "O'Tooley"]

with open(filePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)

    for row in csvReader:
        totalVotes = totalVotes + 1

        candidateList.append(row['Candidate'])
    candidateListClean = list(dict.fromkeys(candidateList))       #https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    #print(candidateListClean)

    KhanCount = int(candidateList.count("Khan"))
    CorreyCount = int(candidateList.count("Correy"))
    LiCount = int(candidateList.count("Li"))
    OTooleyCount = int(candidateList.count("O'Tooley"))


    KhanPercent = float(KhanCount/totalVotes*100)
    CorreyPercent = float(CorreyCount/totalVotes*100)
    LiPercent = float(LiCount/totalVotes*100)
    OTooleyPercent = float(OTooleyCount/totalVotes*100)
    
    percentList = [KhanPercent, CorreyPercent, LiPercent, OTooleyPercent]
    percentListMax = max(percentList)
    #print(percentListMax)

    if percentListMax == KhanPercent:
        winner = "Khan"
    elif percentListMax == CorreyPercent:
        winner = "Correy"
    elif percentListMax == LiPercent:
        winner = "Li"
    elif percentListMax == OTooleyPercent:
        winner = "O'Tooley"

output = f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{candidateListClean[0]}: {KhanPercent:.03f}% ({KhanCount})
{candidateListClean[1]}: {CorreyPercent:.03f}% ({CorreyCount})
{candidateListClean[2]}: {LiPercent:.03f}% ({LiCount})
{candidateListClean[3]}: {OTooleyPercent:.03f}% ({OTooleyCount})

-------------------------
Winner: {winner}
-------------------------
'''
print(output)

with open("PyPollOutput.txt", 'w') as outputFile:
    outputFile.write(output)