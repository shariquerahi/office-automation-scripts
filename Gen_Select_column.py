'''import pandas as pd

# Read the CSV file
df = pd.read_csv("/Users/shariquerahi/Downloads/amazon_aug_23_transaction.csv")

# Select and create a new DataFrame with the desired columns
selected_columns = df[['TRANSACTION_AMOUNT', 'TRANSACTION_REMARKS', 'MERCHANT_NAME', 'DEBITED_AT_IST']]

# Save the result to a new CSV file
selected_columns.to_csv("/Users/shariquerahi/Downloads/Amazon_db_data.csv", index=False)

# Display the result
print(selected_columns) '''

import pandas as pd

# Read the CSV file
df = pd.read_csv("/Users/shariquerahi/Downloads/result - 2023-10-18T100115.408.csv")

# Select and create a new DataFrame with the desired columns
selected_columns = df[['TRANSACTION_AMOUNT', 'TRANSACTION_REMARKS', 'MERCHANT_NAME', 'DEBITED_AT_IST']]

# Extract the last 4 digits from the "TRANSACTION_REMARKS" column
selected_columns['LAST_4_DIGITS'] = selected_columns['TRANSACTION_REMARKS'].str[-4:]

# Save the result to a new CSV file
selected_columns.to_csv("/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Flipkart_updated_db.csv", index=False)

# Display the result
print(selected_columns)

