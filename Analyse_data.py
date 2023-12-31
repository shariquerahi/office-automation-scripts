import pandas as pd

# Load the CSV data into a Pandas DataFrame
data = pd.read_csv("/Users/shariquerahi/Downloads/Account_details - Sheet2.csv", sep=',')



# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())

# Get the basic statistics of the data
print("\nBasic statistics of the data:")
print(data.describe())

# Get information about the data types and missing values
print("\nInformation about data types and missing values:")
print(data.info())

# Count the number of unique account numbers
#unique_account_numbers = data['ACCT_NUMBER'].nunique()
#print("\nNumber of unique account numbers:", unique_account_numbers)

# Count the number of accounts by account type
account_type_counts = data['TYPE'].value_counts()
print("\nAccount type counts:")
print(account_type_counts)

# Filter the data based on specific conditions (e.g., ACCT_STATUS is 'A')
active_accounts = data[data['ACCT_STATUS'] == 'A']
print("\nActive accounts:")
print(active_accounts)

# Group and count the accounts by "REASON"
reason_counts = data.groupby('REASON').size()
print("\nAccount count by reason:")
print(reason_counts)

# Analyze KYC status
kyc_status = data['CUSTOMER KYC_UPDATED'].value_counts()
percentage_updated_kyc = (kyc_status['Y'] / len(data)) * 100
print("\nKYC Status:")
print(kyc_status)
print("Percentage of updated KYC:", percentage_updated_kyc, "%")
