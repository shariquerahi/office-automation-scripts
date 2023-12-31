import pandas as pd
from dateutil.parser import parse
from datetime import timedelta
import os

# Define file paths
big_file_path = '/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Zomato_ 63604.csv'
small_file_path = '/Users/shariquerahi/Downloads/DC_Merchant_Zomato_July.csv'
output_dir = '/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Zomato.output.csv'

# Load CSV files into DataFrames
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

big_file = load_csv(big_file_path)
small_file = load_csv(small_file_path)

if big_file is None or small_file is None:
    exit(1)  # Exit the script if file loading fails

# Function to add leading zeros to the last four digits
def add_leading_zeros(num):
    if not pd.isna(num):
        if isinstance(num, int):
            return f'{num:04}'  # Format as a 4-digit zero-padded integer
        elif isinstance(num, float):
            return f'{int(num):04}'  # Format as a 4-digit zero-padded integer
    return num

# Apply the function to the "Card_last_4_digit" column in both big and small files
big_file['Card_last_4_digit'] = big_file['Card_last_4_digit'].apply(add_leading_zeros)
small_file['Card_last_4_digit'] = small_file['Card_last_4_digit'].apply(add_leading_zeros)

# Merge the dataframes based on 'Card_last_4_digit'
result = pd.merge(big_file, small_file, on=['Card_last_4_digit'], how='inner')

# Define a tolerance for 'Authorization_amount' comparison
amount_tolerance = 1  # Tolerance of 1 for Authorization_amount

# Define a date tolerance
date_tolerance = timedelta(days=1)  # 1-day tolerance

# Filter matching rows within the tolerances for 'Authorization_amount' and 'transaction_date'
result = result[
    (abs(result['Authorization_amount_x'] - result['Authorization_amount_y']) <= amount_tolerance) &
    (abs(pd.to_datetime(result['transaction_date_x']) - pd.to_datetime(result['transaction_date_y'])) <= date_tolerance)
]

# Save the matching rows to a new CSV file
result.to_csv(os.path.join(output_dir, '/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Zomato.output.csv'), index=False)

# Find unmatched rows using the 'indicator' parameter
unmatched_result = big_file.merge(
    small_file, on=['Card_last_4_digit'], how='left', indicator=True
).loc[lambda x: x['_merge'] == 'left_only']

# Save the unmatched rows to a new CSV file
unmatched_result.to_csv(os.path.join(output_dir, '/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/unmatched_zomTO_small.csv'), index=False)

# Print the number of matching rows
print("Number of matching rows:", len(result))

# Print the number of unmatched rows
print("Number of unmatched rows:", len(unmatched_result))

# Provide a summary of the merged data
print("Summary of merged data:")
print(result.head())  # Print the first few rows of merged data
