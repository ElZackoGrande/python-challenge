#import modules
import os
import csv

#path to file
voting_csv = os.path.join('..', 'pypoll', 'resources', 'election_data.csv')

#creating lists for variables
candidates = []
vote_count = []

#opening and reading CSV file
with open(voting_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #applying empty lists to the data columns to count votes per candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(1)
        else:
            whatindex = candidates.index(row[2])
            vote_count[whatindex] += 1
    #Find total votes
    total_votes = sum(vote_count)
    #find percentage for each candidate
    votepercentage = [round(vote_count[i]/total_votes*100,4) for i in range(0,len(vote_count))]
    #printing results using the variables and lists
    print(" Election Results ")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    for i in range(0,len(candidates)):
        print(f"{candidates[i]}: {votepercentage[i]}% ({vote_count[i]})")
    print("------------------------")
    print(f"Winner: {candidates[vote_count.index(max(vote_count))]}")

    #exporting text file with results
    with open("pollOutput.txt", "w") as text_file:
        print(" Election Results ", file=text_file)
        print("------------------------", file=text_file)
        print(f"Total Votes: {total_votes}", file=text_file)
        print("------------------------", file=text_file)
        for i in range(0,len(candidates)):
            print(f"{candidates[i]}: {votepercentage[i]}% ({vote_count[i]})", file=text_file)
        print("------------------------", file=text_file)
        print(f"Winner: {candidates[vote_count.index(max(vote_count))]}", file=text_file)
