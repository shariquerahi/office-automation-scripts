import pandas as pd
from datetime import datetime, timedelta
import random

# Read the big and small files into dataframes
big_file = pd.read_csv('/Users/shariquerahi/Downloads/cc_eazydiner (1).csv')
small_file = pd.read_csv('/Users/shariquerahi/Downloads/CC recon.xlsx - EazyDiner Mastersheet (1).csv')

# Convert the 'debited_at' column in the big file to a common format
big_file['transaction_date'] = pd.to_datetime(big_file['transaction_date']).dt.strftime('%m/%d/%Y')

# Convert the 'transaction_date' column in the small file to a common format
small_file['transaction_date'] = pd.to_datetime(small_file['transaction_date'], format='%m/%d/%Y').dt.strftime('%m/%d/%Y')

# Define a function to compare dates with a range of +/- 1 day
def date_within_range(date1, date2):
    date1 = datetime.strptime(date1, '%m/%d/%Y')
    date2 = datetime.strptime(date2, '%m/%d/%Y')
    return abs((date1 - date2).days) <= 1

# Add random variation to the 'Authorisation_amount_x' column in the big file
big_file['Authorisation_amount'] = big_file['Authorisation_amount'] + [random.uniform(-0.5, 0.5) for _ in range(len(big_file))]

# Merge the dataframes based on 'Card_last_4_digits' and 'auth_code' with date flexibility
result = pd.merge(big_file, small_file, on=['Card_last_4_digit', 'auth_code'], how='inner')
result = result[result.apply(lambda x: date_within_range(x['transaction_date_x'], x['transaction_date_y']), axis=1)]

# Convert the 'Card_last_4_digit' column to integers
result['Card_last_4_digit'] = result['Card_last_4_digit'].astype(int)

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Output_CC_EaseD.csv', index=False)

# Print the matching rows
print("Matching Rows:")
print(result)

# Find and print rows that are in the small file but not in the output
not_in_output = small_file.merge(big_file, on=['Card_last_4_digit', 'auth_code'], how='left', indicator=True)
not_in_output = not_in_output[not_in_output['_merge'] == 'left_only']
print("Rows in Small File but not in Output:")
print(not_in_output)
