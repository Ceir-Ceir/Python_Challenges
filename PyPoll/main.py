import csv

# Path to the election data
file_path = 'Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ''
max_votes = 0

# Read the CSV file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Analyze the data to find the winner and percentages
for candidate, votes in candidates.items():
    if votes > max_votes:
        winner = candidate
        max_votes = votes

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open('analysis/election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
