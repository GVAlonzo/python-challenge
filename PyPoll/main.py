#*****************************************************************************
#**
#**  Python Homework: Py Me Up, Charlie
#**
#**   PyPoll
#**
#**     Author: George Alonzo
#**   Due Date: Sept 18, 2021
#**
#*****************************************************************************

# Import the os module
import os
# Import the the module for reading CSV files
import csv

# Create path for the input CSV file
csvpath = os.path.join('Resources',"election_data.csv")

# Create lists to store unique candidate names, votes, and total votes
candidate = []
vote_count=[]
vote_pct=[]

row_counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header, per the Rubric, will not use in the summaries
    csv_header = next(csvreader)

    # Loop through rows, search candidate list, if not previously stored, append.
    for row in csvreader:
        row_counter += 1
        # If candidate list is empty, initialize w/ first row
        if len(candidate) == 0:
            candidate.append(row[2])
            vote_count.append(1)
            vote_pct.append(0.00)
        else: 
            i=0
            isfound = False
            # Loop through candidate list
            while i < len(candidate) and isfound == False:
                isfound = True
                # If candidate previously stored, set a True flag add a vote count
                if candidate[i] == row[2]:
                    isfound = True
                    vote_count[i] += 1
                else:
                    # If candidate not found in list, set False flag
                    isfound = False
                i += 1
            # If not previously found, add candidate to list and initialize vote count & vote percentages in lists
            if isfound == False:
                candidate.append(row[2])
                vote_count.append(1)
                vote_pct.append(0.00)

# Calculate percentages for each candidate
j=0
while j < len(candidate):
    print("I= ",j," Length of Candidate: ", len(candidate))
    pct = round((vote_count[j] / row_counter) * 100,3)
    vote_pct[j] = pct
    print("Percent for ",j," : ",pct)
    j += 1

# Print results to terminal
print("        ELECTION RESULTS        ")
print("--------------------------------")
print(f'Total Votes: {row_counter}')
print("--------------------------------")

k=0
while k < len(candidate):
    print(f'{candidate[k]}: {vote_pct[k]}% ({vote_count[k]})')
    k += 1

print("--------------------------------")
print("Winner: ")
print("--------------------------------")


# Print analysis output to a text file in the analysis folder

# Specify the file to write to
output_path = os.path.join("analysis", "PyPollAnalysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w') as txtfile:

    txtfile.write("        ELECTION RESULTS        ")
    txtfile.write('\n'"--------------------------------")
    txtfile.write('\n'f'Total Votes: {row_counter}')
    txtfile.write('\n'"--------------------------------")

    l=0
    while l < len(candidate):
        txtfile.write('\n'f'{candidate[l]}: {vote_pct[l]}% ({vote_count[l]})')
        l += 1


    txtfile.write('\n'"--------------------------------")
    txtfile.write('\n'"Winner: ")
    txtfile.write('\n'"--------------------------------")
