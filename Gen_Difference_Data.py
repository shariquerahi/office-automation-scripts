import pandas as pd

# Load the first CSV file with Actor IDs
df1 = pd.read_csv('/Users/shariquerahi/Downloads/data - Sheet2.csv')   

# Load the second CSV file with Actor IDs
df2 = pd.read_csv('/Users/shariquerahi/Downloads/data - Sheet1 (1).csv')

# Find Actor IDs in df1 that are not in df2
missing_actor_ids = df1[~df1['EntityId'].isin(df2['Entity_ID'])]

# Save the missing Actor IDs to a new CSV file
missing_actor_ids.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Gen_PythonScript/data.csv', index=False)
