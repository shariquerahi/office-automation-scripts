'''import pandas as pd



# Define the columns to use for comparison
key_columns_file1 = ['transaction_date_x', 'Card_last_4_digit']
key_columns_file2 = ['transaction_date_x', 'Card_last_4_digit']

# Merge file2 with file1 based on the key columns
merged = pd.merge(file2, file1, left_on=key_columns_file2, right_on=key_columns_file1, how='left', indicator=True)

# Filter rows that are only in 'file2'
unmatched_data = merged[merged['_merge'] == 'left_only']

# Drop the '_merge' column, which is no longer needed
unmatched_data = unmatched_data.drop(columns=['_merge'])

# Save the unmatched data to a new CSV file
unmatched_data.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/unmatched_cheq.csv', index=False)

# Display the unmatched data from file2
print(unmatched_data)'''





'''import pandas as pd

# Load data from file1 and file2
file1 = pd.read_csv("/Users/shariquerahi/Downloads/DC recon Master - updated 13oct - DC_ChecQ_Recon (1).csv")
file2 = pd.read_csv("/Users/shariquerahi/Downloads/DC recon Master - updated 13oct - CheQ mastersheet (1).csv")

# Define matching criteria and tolerances
matching_columns = ['transaction_date_x', 'Card_last_4_digit']
amount_tolerance = 1
date_tolerance = pd.Timedelta('1D')

# Convert date columns to datetime format
file1['transaction_date_x'] = pd.to_datetime(file1['transaction_date_x'])
file2['transaction_date_x1'] = pd.to_datetime(file2['transaction_date_x1'])

# Merge the DataFrames based on matching columns
merged = file2.merge(file1, on=matching_columns, how='left')

# Calculate absolute differences for amount and date
amount_diff = abs(merged['Authorization_amount_x'] - merged['Authorization_amount_x1'])
date_diff = abs(merged['transaction_date_x'] - merged['transaction_date_x1'])

# Filter the rows that do not match the criteria
non_matching_rows = merged[(amount_diff > amount_tolerance) | (date_diff > date_tolerance)]

# Select only the columns from file2
non_matching_data = non_matching_rows[file2.columns]

# Print the non-matching data
print(non_matching_data)'''

import csv

# Read the data from file 1 into a set for faster lookup
file1_data = set()
with open('/Users/shariquerahi/Downloads/DC recon Master - updated 13oct - DC_ChecQ_Recon (1).csv', 'r') as file1:
    csv_reader = csv.DictReader(file1)
    for row in csv_reader:
        transaction_date_x = row['transaction_date_x']
        card_last_4_digit = row['Card_last_4_digit']
        file1_data.add((transaction_date_x, card_last_4_digit))

# Compare with data in file 2 and find the missing records
missing_records = []
with open('/Users/shariquerahi/Downloads/DC_CheQ.csv', 'r') as file2:
    csv_reader = csv.DictReader(file2)
    for row in csv_reader:
        transaction_date_x = row['transaction_date_x']
        card_last_4_digit = row['Card_last_4_digit']
        if (transaction_date_x, card_last_4_digit) not in file1_data:
            missing_records.append(row)

# Save the missing records to a new CSV file
with open('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/unmatched_cheq.csv', 'w', newline='') as output_file:
    fieldnames = missing_records[0].keys()
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    for record in missing_records:
        csv_writer.writerow(record)

# Print the missing records
for record in missing_records:
    print(record)

