'''import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Paytm_63603.csv')

# Convert the 'transaction_date' column to the desired format
df['transaction_date'] = pd.to_datetime(df['transaction_date']).dt.strftime('%m/%d/%Y')

# Save the modified DataFrame back to a CSV file
df.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Paytm_DB_DATA_dateFmt.csv', index=False) '''

'''import pandas as pd

# Define the data types for each column
dtype_dict = {
    'transaction_date': str,  # Keep the date as a string
    'Authorization_amount': object,  # Change to object
    'Card_last_4_digit': int,
    'display_name': str
}

# Load the CSV data into a DataFrame with specified data types
df = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Paytm_63603.csv', dtype=dtype_dict)

# Convert the 'transaction_date' column to the desired format
df['transaction_date'] = pd.to_datetime(df['transaction_date']).dt.strftime('%m/%d/%Y')

# Save the modified DataFrame back to a CSV file
#df.to_csv('output_data.csv', index=False)



# Save the modified DataFrame back to a CSV file
df.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Paytm_DB_DATA_dateFmt.csv', index=False)
'''
import csv
from datetime import datetime

# Read the CSV data
with open('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Amazon_63606.csv', mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Define a function to format the date
def format_date(input_date):
    date_obj = datetime.fromisoformat(input_date)
    return date_obj.strftime('%m/%d/%Y')

# Modify the transaction_date column
for row in data:
    row['transaction_date'] = format_date(row['transaction_date'])

# Write the modified data back to a new CSV file
with open('/Users/shariquerahi/Desktop/Reconsile Merchant Data/Amazon_db_data.csv', mode='w', newline='') as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
