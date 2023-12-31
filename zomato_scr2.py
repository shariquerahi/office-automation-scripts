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

# Save the updated small DataFrame to a new CSV file
small_file.to_csv(os.path.join(output_dir, 'DC_Merchant_Zomato_July.csv'), index=False)

# Modify the convert_date_column function to handle different date formats
def convert_date_column(df, column_name):
    for i, date_str in enumerate(df[column_name]):
        try:
            parsed_date = parse(date_str)
            formatted_date = parsed_date.strftime('%m/%d/%Y')  # Use the desired format
            df.at[i, column_name] = formatted_date
            print(f"Parsed date: {date_str} => {formatted_date}")
        except ValueError:
            # Handling any date format that can't be parsed
            print(f"Unrecognized date format in row {i}, value: {date_str}")

# Convert the date column in both dataframes to a common format
convert_date_column(big_file, 'transaction_date')
convert_date_column(small_file, 'transaction_date')

# Merge the dataframes based on 'Card_last_4_digit'
result = pd.merge(big_file, small_file, on=['Card_last_4_digit'], how='inner')

# Define a tolerance for 'Authorization_amount' comparison
amount_tolerance = 1  # Tolerance of 2 for Authorization_amount

# Define a date tolerance
date_tolerance = timedelta(days=1)  # 1-day tolerance

# Filter matching rows within the tolerances for 'Authorization_amount' and 'transaction_date'
result = result[
    (abs(result['Authorization_amount_x'] - result['Authorization_amount_y']) <= amount_tolerance) &
    (abs(pd.to_datetime(result['transaction_date_x']) - pd.to_datetime(result['transaction_date_y'])) <= date_tolerance)
]

# Save the matching rows to a new CSV file
result.to_csv(os.path.join(output_dir, 'Zomato.output.csv'), index=False)

# Find unmatched rows using the 'indicator' parameter
unmatched_result = big_file.merge(
    small_file, on=['Card_last_4_digit'], how='left', indicator=True
).loc[lambda x: x['_merge'] == 'left_only']

# Save the unmatched rows to a new CSV file
unmatched_result.to_csv(os.path.join(output_dir, 'unmatched_Amazon.csv'), index=False)

# Read the CSV file into a DataFrame
df_big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Zomato_63604.csv', parse_dates=['transaction_date'])
df_small_file = pd.read_csv('/Users/shariquerahi/Downloads/DC_Merchant_Zomato_July.csv', parse_dates=['transaction_date'])

# Group by the month and count the number of transactions in each month
monthly_count_big = df_big_file.groupby(df_big_file['transaction_date'].dt.strftime('%Y-%m'))['transaction_date'].count()
monthly_count_small = df_small_file.groupby(df_small_file['transaction_date'].dt.strftime('%Y-%m'))['transaction_date'].count()

# Print the result
print('monthly_count_big', monthly_count_big)
print('monthly_count_small',monthly_count_small)

# Print the number of matching rows
print("Number of matching rows:", len(result))

# Print the number of unmatched rows
print("Number of unmatched rows:", len(unmatched_result))

# Provide a summary of the merged data
print("Summary of merged data:")
print(result.head())  # Print the first few rows of merged data

# Find unmatched rows using the 'indicator' parameter
unmatched_result_small = small_file.merge(
    big_file, on=['Card_last_4_digit'], how='left', indicator=True
).loc[lambda x: x['_merge'] == 'left_only']

# Save the unmatched small file rows to a new CSV file
unmatched_result_small.to_csv(os.path.join(output_dir, 'unmatched_zomTO_small.csv'), index=False)

# Print the number of unmatched small file rows
print("Number of unmatched small file rows:", len(unmatched_result_small))

print("Rows that should match but don't:")
print(big_file[big_file['Card_last_4_digit'] == '2248']) 
print(small_file[small_file['Card_last_4_digit'] == '2248'])