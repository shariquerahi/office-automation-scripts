import pandas as pd

# Read the big and small files into dataframes
big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/Gen_test_out.csv')
small_file = pd.read_csv('/Users/shariquerahi/Downloads/Filpkart_updated.csv')

# Convert the 'transaction_date' column in both dataframes to datetime objects
big_file['transaction_date'] = pd.to_datetime(big_file['transaction_date'])
small_file['transaction_date'] = pd.to_datetime(small_file['transaction_date'], format='%m/%d/%Y')

# Initialize an empty list to store matching rows
matching_rows = []

# Iterate through the rows in the big file
for index, row in big_file.iterrows():
    start_date = row['transaction_date'] - pd.DateOffset(days=1)
    end_date = row['transaction_date'] + pd.DateOffset(days=1)
    
    # Filter the small file for matching rows within one day
    matching_small_rows = small_file[
        (small_file['Authorization_amount'] == row['Authorization_amount']) &
        (small_file['Card_last_4_digit'] == row['Card_last_4_digit']) &
        (small_file['transaction_date'] >= start_date) &
        (small_file['transaction_date'] <= end_date)
    ]
    
    if not matching_small_rows.empty:
        matching_rows.append(matching_small_rows)

# Concatenate the matching rows into a single dataframe
if matching_rows:
    matching_rows = pd.concat(matching_rows, ignore_index=True)

# If you want to save the matching rows to a new CSV file
matching_rows.to_csv('/Users/shariquerahi/Downloads/Final_Flipkart_file.csv', index=False)
