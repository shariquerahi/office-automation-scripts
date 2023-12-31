
import pandas as pd
from datetime import datetime, timedelta

# Load CSV data into Pandas DataFrames
file1_data = pd.read_csv('/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Paytm_63603.csv')
file2_data = pd.read_csv('/Users/shariquerahi/Downloads/Paytm14Oct_Data_sat.csv')

# Function to detect and convert date format
def convert_to_common_date_format(df):
    date_formats = ['%Y-%m-%dT%H:%M:%S.%fZ', '%m/%d/%Y']  # Updated date formats
    for date_format in date_formats:
        try:
            df['transaction_date'] = pd.to_datetime(df['transaction_date'], format=date_format)
            return df
        except ValueError:
            continue
    return None

# Function to add leading zeros to 'Card_last_4_digit'
def add_leading_zeros(df):
    df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(lambda x: str(x).zfill(4))
    return df

# Detect and convert date format in both DataFrames
file1_data = convert_to_common_date_format(file1_data)
file2_data = convert_to_common_date_format(file2_data)

if file2_data is not None:
    # Add leading zeros to 'Card_last_4_digit'
    file2_data = add_leading_zeros(file2_data)

    # Calculate date difference
    date_tolerance = timedelta(days=1)
    auth_tolerance = 0.5
    merged_data = pd.merge(file1_data, file2_data, on='Card_last_4_digit')
    merged_data['date_diff'] = abs(merged_data['transaction_date_x'] - merged_data['transaction_date_y'])
    
    # Filter matches
    matches = merged_data[
        (merged_data['date_diff'] <= date_tolerance) &
        (abs(merged_data['Authorization_amount_x'] - merged_data['Authorization_amount_y']) <= auth_tolerance)
    ]

    if not matches.empty:
        # Save the matches to a CSV file
        matches.to_csv('/Users/shariquerahi/Downloads/Final_out_Paytm.csv', index=False)
        print("Matches saved to '/Users/shariquerahi/Downloads/Final_out_Paytm.csv'")
    else:
        print("No matches found.")
else:
    print("Date format mismatch. Unable to proceed.")
