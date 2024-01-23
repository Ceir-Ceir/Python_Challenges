import csv

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
monthly_change = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Path to the CSV file
csvpath = 'Resources/budget_data.csv'

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Read the first row (and set the previous month's profit/loss)
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    previous_month_profit_loss = int(first_row[1])

    # Process each row after the first
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])

        # Calculate change in profit/loss
        profit_loss_change = int(row[1]) - previous_month_profit_loss
        previous_month_profit_loss = int(row[1])
        monthly_change.append(profit_loss_change)
        month_of_change.append(row[0])

        # Calculate the greatest increase
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Calculate the greatest decrease
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average change
average_change = sum(monthly_change) / len(monthly_change)



# Calculate the average change
average_change = sum(monthly_change) / len(monthly_change)

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Save the results to a text file
with open('analysis/financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
