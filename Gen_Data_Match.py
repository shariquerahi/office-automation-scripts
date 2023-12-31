import pandas as pd

# Load the first CSV file with 10k rows
df1 = pd.read_csv('file1.csv')

# Load the second CSV file with 2000 rows
df2 = pd.read_csv('file2.csv')

# Define a function to extract the last four digits of the card number
def extract_last_four(card_number):
    return str(card_number)[-4:]

# Apply the function to both DataFrames
df1['LastFourDigits'] = df1['CardNumber'].apply(extract_last_four)
df2['LastFourDigits'] = df2['CardNumber'].apply(extract_last_four)

# Merge the two DataFrames on the LastFourDigits and AuthorizationAmount columns
result = pd.merge(df1, df2, on=['LastFourDigits', 'AuthorizationAmount'], how='inner')

# Drop the LastFourDigits column if you no longer need it
result = result.drop(columns=['LastFourDigits'])

# Save the result to a new CSV file or perform further operations as needed
result.to_csv('common_data.csv', index=False)

''' import pandas as pd

# Load the first CSV file with 10k rows
df1 = pd.read_csv('file1.csv')

# Load the second CSV file with 2000 rows
df2 = pd.read_csv('file2.csv')

# Merge the two DataFrames on both LastFourDigits and AuthorizationAmount columns
result = pd.merge(df1, df2, on=['LastFourDigits', 'AuthorizationAmount'], how='inner')

# Save the result to a new CSV file or perform further operations as needed
result.to_csv('common_data.csv', index=False)
'''