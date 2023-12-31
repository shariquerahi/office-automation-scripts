'''import pandas as pd

# Load the orignal file fetched from presto
df1 = pd.read_csv('/Users/shariquerahi/Downloads/orignal_file.csv') 

# Load the second CSV file which we received from merchant
df2 = pd.read_csv('/Users/shariquerahi/Downloads/cheq_updated.csv')

# Merge the two DataFrames on both LastFourDigits and AuthorizationAmount columns
result = pd.merge(df1, df2, on=['Card_last_4_digit', 'Authorization_amount'], how='inner')

# Save the result to a new CSV file or perform further operations as needed
result.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/common_data.csv', index=False) '''
''''
import pandas as pd

# Read the big and small files into dataframes
big_file = pd.read_csv('/Users/shariquerahi/Downloads/CC_OFFER - total_data.csv')
small_file = pd.read_csv('/Users/shariquerahi/Downloads/CC_OFFER - removed_data.csv')

# Convert the 'debited_at' column in the big file to a common format
#big_file['transaction_date'] = pd.to_datetime(big_file['transaction_date']).dt.strftime('%m/%d/%Y')

# Convert the 'transaction_date' column in the small file to a common format
#small_file['transaction_date'] = pd.to_datetime(small_file['transaction_date'], format='%m/%d/%Y').dt.strftime('%m/%d/%Y')

# Merge the dataframes based on 'Authorisation_amount' and 'Card_last_4_digits'
result = pd.merge(big_file, small_file, on=['CUST_ID'], how='inner')

# Convert the 'Card_last_4_digit' column to integers
#result['CUST_ID'] = result['CUST_ID'].astype(int) 

# If you want to save the matching rows to a new CSV file
result.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/output_data.csv', index=False)



# Print the matching rows
print(result)
'''




'''import pandas as pd
import numpy as np

# Read the first file
file1 = pd.read_csv("/Users/shariquerahi/Downloads/orignal_file.csv")
# Read the second file
file2 = pd.read_csv("/Users/shariquerahi/Downloads/cheq_updated.csv")

# Merge the two DataFrames based on matching columns, and select specific columns
# Cast "Card_last_4_digit" to integer in both DataFrames
file1["Card_last_4_digit"] = file1["Card_last_4_digit"].astype(int)
file2["Card_last_4_digit"] = file2["Card_last_4_digit"].astype(int)

# Merge the two DataFrames based on matching columns
merged_data = pd.merge(file1, file2, on=["Card_last_4_digit", "Authorization_amount"])

# Save the merged data to a new file
merged_data.to_csv("/Users/shariquerahi/Desktop/Git/Python_Script/common_data.csv", index=False) '''


import pandas as pd

# Load the big file into a DataFrame
big_file_data = pd.read_csv("/Users/shariquerahi/Downloads/Loan_Data - Total.csv", sep=',')

# Load the small file into a DataFrame
small_file_data = pd.read_csv("/Users/shariquerahi/Downloads/Application_Started_But_Not_completed.csv")

# Use the merge function to match the CUST_ID values and fetch the matching data
matched_data = big_file_data.merge(small_file_data, on="CUST_ID")

# Print the matched data
print(matched_data)
