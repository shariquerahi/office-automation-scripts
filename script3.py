import pandas as pd
from dateutil.parser import parse
from datetime import timedelta

# Load your CSV file from Merchant
df = pd.read_csv('/Users/shariquerahi/Downloads/DC recon september - Flipkart_master.csv')

# Function to add leading zeros to the last four digits
def add_leading_zeros(num):
    if not pd.isna(num):
        if isinstance(num, int):
            return str(num).zfill(4)
        elif isinstance(num, float):
            return f'{num:.1f}'
    return num

# Apply the function to the "Card_last_4_digit" column to add leading zeros if required
df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(add_leading_zeros)

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/shariquerahi/Downloads/Filpkart_updated.csv', index=False)

# Read the big and small files into dataframes. big_file is your database data, and small file is merchant data.
big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Flipkart_63601.csv')
small_file = pd.read_csv('/Users/shariquerahi/Downloads/Filpkart_updated.csv')

print("Columns in big_file:", big_file.columns)
print("Columns in small_file:", small_file.columns)

# Function to convert date column to a common format in both files
def convert_date_column(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')  # Convert to datetime with errors handled
    df[column_name] = df[column_name].dt.strftime('%m/%d/%Y')  # Format the date as required

# Convert the 'transaction_date' column in both dataframes to a common format
convert_date_column(big_file, 'transaction_date')
convert_date_column(small_file, 'transaction_date')

# Merge the dataframes with a tolerance of plus and minus one day for 'transaction_date'
one_day = timedelta(days=1)
result = pd.merge(big_file, small_file, on=['Authorization_amount', 'Card_last_4_digit'], how='inner')
#result['transaction_date_x'] = pd.to_datetime(result['transaction_date_x'])
#result['transaction_date_y'] = pd.to_datetime(result['transaction_date_y'])
#date_matches = abs(result['transaction_date_x'] - result['transaction_date_y']) <= one_day
#result = result[date_matches]

# Convert the 'Card_last_4_digit' column to integers
result['Card_last_4_digit'] = result['Card_last_4_digit'].astype(int)

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Downloads/Final_Flipkart_file.csv', index=False)

# Provide a summary of the merged data
print("Number of matching rows:", len(result))
