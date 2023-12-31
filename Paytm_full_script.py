import pandas as pd
from dateutil.parser import parse
from datetime import timedelta

# Load your CSV file into a DataFrame from Merchant
df = pd.read_csv('/Users/shariquerahi/Downloads/DC_rec_Amazon_August_merch.csv')

# add leading zeros to the last four digits
def add_leading_zeros(num):
    if not pd.isna(num):
        if isinstance(num, int):
            return str(num).zfill(4)
        elif isinstance(num, float):
            return f'{num:.1f}'
    return num


df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(add_leading_zeros)

df.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Amazon_update_rrecon.csv', index=False)

big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/Amazon_db_data.csv')
small_file = pd.read_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Amazon_update_rrecon.csv')

print("Columns in big_file:", big_file.columns)
print("Columns in small_file:", small_file.columns)

# common format in both the file
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

# Merge the dataframes with a tolerance of plus and minus one day for 'transaction_date'
result = pd.merge(big_file, small_file, on=['Authorization_amount', 'Card_last_4_digit'], how='inner')
'''result['transaction_date_x'] = pd.to_datetime(result['transaction_date_x'])
result['transaction_date_y'] = pd.to_datetime(result['transaction_date_y'])

one_day = timedelta(days=1)
date_matches = (result['transaction_date_x'] - result['transaction_date_y']).abs() <= one_day
result = result[date_matches] '''

# Convert the 'Card_last_4_digit' column to integers
result['Card_last_4_digit'] = result['Card_last_4_digit'].astype(int)

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/Amazon_Output.csv', index=False)

# Provide a summary of the merged data
print("Number of matching rows:", len(result))
