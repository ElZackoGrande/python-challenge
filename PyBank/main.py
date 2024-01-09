#import modules
import os
import csv

#path to file
profits_csv = os.path.join('..', 'pybank', 'resources', 'budget_data.csv')

#creating initial variables - lists and forced zeroes
date = []
profit = []
monthly_changes = []
revenue_change_list = []
months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
revenue_change = 0
previous_revenue = 0

#opening and reading CSV file
with open (profits_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #ignoring headers in the first row
    next (csvreader)
    for row in csvreader:
        #calculates total number of months
        months = months + 1
        #then appends date to column
        date.append(row[0])
        profit.append(row[1])
        #sums up total profits
        total_profit = total_profit + int(row[1])
        #calculate average change and xreate a list
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #calc average profit change
        average_change_profits = (total_change_profits/months)

        #calc greatest profit increase and lowest profit decrease
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        # locates date when highest increase and lowest decreate occurred
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]             

#printing off results
print("Financial Analysis")
print("-------------------------------------------------")
print("Total Months: " + str(months))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

#exporting .txt file with results table
with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("-----------------------------------------------------\n\n")
    text.write("    Total Months: " + str(months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")