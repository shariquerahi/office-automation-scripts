

import pandas as pd
import numpy as np  # Import numpy to handle NaN values

# Load your CSV file into a DataFrame
df = pd.read_csv('/Users/shariquerahi/Downloads/cheq2.csv')

# Function to add leading zeros to the last four digits
def add_leading_zeros(num):
    if not pd.isna(num):
        return str(int(num)).zfill(4)
    else:
        return '0000'  # Handle missing values by returning '0000'

# Apply the function to the "Card_last_4_digit" column
df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(add_leading_zeros)

# Save the updated DataFrame to a new CSV file
df.to_csv('/Users/shariquerahi/Downloads/cheq_updated.csv', index=False)


