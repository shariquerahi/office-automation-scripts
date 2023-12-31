import pandas as pd

# Read the big file into a dataframe
big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Flipkart_63601.csv')

# Convert the 'transaction_date' column to the date format
#big_file['transaction_date'] = pd.to_datetime(big_file['transaction_date']).dt.strftime('%Y-%m-%d')
big_file['transaction_date'] = pd.to_datetime(big_file['transaction_date']).dt.strftime('%m/%d/%Y')

big_file['Card_last_4_digit'] = big_file['Card_last_4_digit'].astype(str)

# Save the updated file
big_file.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Flipkart_1.csv', index=False)

# Print the updated dataframe
print(big_file) 

'''import pandas as pd
from dateutil.parser import parse

# Read the big and small files into dataframes
big_file = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Paytm_63603.csv')
small_file = pd.read_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Paytm_Merchant_Updated.csv')

# Function to convert date column to a common format
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

# Merge the dataframes based on 'Authorization_amount' and 'Card_last_4_digits' and 'transaction_date'
result = pd.merge(big_file, small_file, on=['Authorization_amount', 'Card_last_4_digit', 'transaction_date'], how='inner')

# Convert the 'Card_last_4_digit' column to integers
result['Card_last_4_digit'] = result['Card_last_4_digit'].astype(int)

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/Final_Paytm_file.csv', index=False)

# Provide a summary of the merged data
print("Number of matching rows:", len(result))
'''