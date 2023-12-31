import pandas as pd
from dateutil.parser import parse
from datetime import timedelta

# Load your CSV file into a DataFrame from Merchant
df = pd.read_csv('/Users/shariquerahi/Downloads/DC_rec_Amazon_August_merch.csv')

# Function to add leading zeros to the last four digits
def add_leading_zeros(num):
    if not pd.isna(num):
        if isinstance(num, int):
            return str(num).zfill(4)
        elif isinstance(num, float):
            return f'{num:.2f}'  # Changed to format with two decimal places
    return num

# Apply the function to the "Card_last_4_digit" column to add leading zeros if required
df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(add_leading_zeros)

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/shariquerahi/Downloads/DC_rec_Amazon_August_merch.csv', index=False)

# Read the big and small files into dataframes big_file is our db data, small file is merchant data
big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Amazon_63606.csv')
small_file = pd.read_csv('/Users/shariquerahi/Downloads/DC_rec_Amazon_August_merch.csv')

print("Columns in big_file:", big_file.columns)
print("Columns in small_file:", small_file.columns)

# Function to convert date column to a common format in both the file
def convert_date_column(df, column_name):
    for i, date_str in enumerate(df[column_name]):
        try:
            parsed_date = parse(date_str)
            df.at[i, column_name] = parsed_date.strftime('%m/%d/%Y')
        except ValueError:
            # Handling any date format that can't be parsed
            print(f"Unrecognized date format in row {i}, value: {date_str}")

# Convert the 'transaction_date' column in both dataframes to a common format
convert_date_column(big_file, 'transaction_date')
convert_date_column(small_file, 'transaction_date')

# Merge the dataframes based on 'Card_last_4_digit'
result = pd.merge(big_file, small_file, on=['Card_last_4_digit'], how='inner')

# Convert the 'Card_last_4_digit' column to integers
result['Card_last_4_digit'] = result['Card_last_4_digit'].astype(int)

# Define a tolerance for 'Authorization_amount' comparison
amount_tolerance = 2  # Tolerance of 0.5 for Authorization_amount

# Define a date tolerance
date_tolerance = timedelta(days=2)  # Adjust as needed for a one-day tolerance

# Filter matching rows within the tolerances for 'Authorization_amount' and 'transaction_date'
result = result[
    (abs(result['Authorization_amount_x'] - result['Authorization_amount_y']) <= amount_tolerance) &
    (abs(pd.to_datetime(result['transaction_date_x']) - pd.to_datetime(result['transaction_date_y'])) <= date_tolerance)
]

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/out_ezy.csv', index=False)

# Find unmatched rows by using the 'indicator' parameter
unmatched_result = big_file.merge(
    small_file, on=['Card_last_4_digit'], how='left', indicator=True
).loc[lambda x: x['_merge'] == 'left_only']



# If you want to save the unmatched rows to a new CSV file
unmatched_result.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/unmt2.csv', index=False)

# Print the number of matching rows
print("Number of matching rows:", len(result))

# Print the number of unmatched rows
print("Number of unmatched rows:", len(unmatched_result))

# Provide a summary of the merged data
print("Number of matching rows:", len(result))