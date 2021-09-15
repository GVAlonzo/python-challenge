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

# Create lists to store unique candidate names, their vote counts, and total votes
candidate = []
vote_count=[]
vote_pct=[]

tot_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header, per the Rubric, but not used
    csv_header = next(csvreader)

    #-----------------------------------------------------------------------------
    #-- Main logic to loop through each row in csv
    #--        - Search candidate list, append if not previously stored
    #--        - Count votes using list (index corresponds with candidate index)
    #--        - Initialize percent list (index corresponds with candidate index)
    #-----------------------------------------------------------------------------

    for row in csvreader:
        tot_votes += 1
        # If candidate list is empty, initialize w/ first row
        if len(candidate) == 0:
            candidate.append(row[2])
            vote_count.append(1)
            vote_pct.append(0.00)
        else: 
            i=0
            isfound = False
            # Search/loop through candidate list, if not previously stored, append.
            while i < len(candidate) and isfound == False:
                #isfound = True
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

#------------------------------------------------------
#-- Print logic for display on terminal and text file
#------------------------------------------------------
# Loop through the percentages list and calculate & format % for each candidate
j=0
while j < len(candidate):
    pct = (vote_count[j] / tot_votes)
    formatted_pct = "{:.3%}".format(pct)
    vote_pct[j] = formatted_pct
    j += 1

# Find the index of the lists for the winner
max_votes = max(vote_count)
winner_index = vote_count.index(max_votes)

# Print results to terminal
print("        ELECTION RESULTS        ")
print("--------------------------------")
print(f'Total Votes: {tot_votes}')
print("--------------------------------")

# Print each item in list, on same line
k=0
while k < len(candidate):
    print(f'{candidate[k]}: {vote_pct[k]} ({vote_count[k]})')
    k += 1

print("--------------------------------")
print(f'Winner: {candidate[winner_index]}')
print("--------------------------------")

# Print analysis output to a text file in the analysis folder
# Specify the file to write to
output_path = os.path.join("analysis", "PyPollAnalysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w') as txtfile:

    txtfile.write("        ELECTION RESULTS        ")
    txtfile.write('\n'"--------------------------------")
    txtfile.write('\n'f'Total Votes: {tot_votes}')
    txtfile.write('\n'"--------------------------------")

    l=0
    while l < len(candidate):
        txtfile.write('\n'f'{candidate[l]}: {vote_pct[l]} ({vote_count[l]})')
        l += 1

    txtfile.write('\n'"--------------------------------")
    txtfile.write('\n'f'Winner: {candidate[winner_index]}')
    txtfile.write('\n'"--------------------------------")
