import pandas as pd

# Read the original CSV file
df = pd.read_csv('/Users/shariquerahi/Downloads/formatted_high_credit_risk.csv.csv')

# Split the DataFrame into chunks of 100,000 rows
chunks = [df[i:i+700000] for i in range(0, len(df), 700000)]

# Save each chunk as a separate CSV file with header
for i, chunk in enumerate(chunks):
    chunk.to_csv(f'High_Risk_User_5thDec{i+1}.csv', index=False, header=True)
