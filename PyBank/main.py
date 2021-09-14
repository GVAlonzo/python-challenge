#*****************************************************************************
#**
#**  Python Homework: Py Me Up, Charlie
#**
#**   PyBank
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
csvpath = os.path.join('Resources',"budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store the header, per the Rubric, will not use in the summaries
    csv_header = next(csvreader)

    # Create and initialize variables for summary output
    row_counter = 0
    profit_losses = 0
    tot_profit_losses = 0
    max_inc = 0
    max_dec = 0

    for row in csvreader:
        row_counter += 1
        profit_losses = int(row[1])
        tot_profit_losses += profit_losses

        # Check and store newly found greatest increase in profits
        if(max_inc < profit_losses):
            max_inc = profit_losses
            max_inc_month = row[0]

        # Check and store newly found greatest decrease in profits
        if(max_dec > profit_losses):
            max_dec = profit_losses
            max_dec_month = row[0]

    # Print analysis output to the terminal
    print("               FINANCIAL ANALYSIS               ")
    print("------------------------------------------------")
    print(f'                Total Months: {row_counter}')
    print(f'                       Total: ${tot_profit_losses}')
    avg_change = tot_profit_losses / row_counter
    print(f'              Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})')
    print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')

    # Print analysis output to a text file in the analysis folder

    # Specify the file to write to
    output_path = os.path.join("analysis", "PyBankAnalysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:

        txtfile.write("               FINANCIAL ANALYSIS               ")
        txtfile.write('\n'"------------------------------------------------")
        txtfile.write('\n'f'                Total Months: {row_counter}')
        txtfile.write('\n'f'                       Total: ${tot_profit_losses}')
        txtfile.write('\n'f'              Average Change: ${avg_change}')
        txtfile.write('\n'f'Greatest Increase in Profits: {max_inc_month} (${max_inc})')
        txtfile.write('\n'f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')



