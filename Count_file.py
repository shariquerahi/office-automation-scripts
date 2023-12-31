import csv
from collections import defaultdict

# Define a dictionary to store the counts for each month
month_counts = defaultdict(int)

# Open and read your CSV file
with open('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Paytm_recon_output.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        # Extract the transaction dates from both columns
        transaction_date_x = row['transaction_date_x']
        #transaction_date_y = row['transaction_date_y']

        # Split the date into components
        date_x_components = transaction_date_x.split('/')
        #date_y_components = transaction_date_y.split('/')

        # Extract the month from each date
        month_x = date_x_components[0]
        #month_y = date_y_components[0]

        # Increment the count for each month
        month_counts[month_x] += 1
        #month_counts[month_y] += 1

# Print the counts for each month
for month, count in month_counts.items():
    print(f"Month {month}: {count} transactions")
