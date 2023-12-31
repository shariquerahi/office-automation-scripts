
import pandas as pd
from datetime import datetime, timedelta
from dateutil.parser import parse
from pytz import timezone  # Import the pytz library

# Load CSV data into Pandas DataFrames
# Load CSV data into Pandas DataFrames
file1_data = pd.read_csv('/Users/shariquerahi/Downloads/DB_eASE_My_dnner.csv')
file2_data = pd.read_csv('/Users/shariquerahi/Downloads/merchant_Ezy.csv')


# Function to convert date format using dateutil
def convert_date_format(df):
    try:
        df['transaction_date'] = df['transaction_date'].apply(lambda x: parse(x))
        return df
    except ValueError:
        return None

# Function to add leading zeros to 'Card_last_4_digit'
def add_leading_zeros(df):
    df['Card_last_4_digit'] = df['Card_last_4_digit'].apply(lambda x: str(x).zfill(4))
    return df

# Function to ensure 'Card_last_4_digit' is of the same data type (string)
def ensure_card_last_4_digit_datatype(df):
    df['Card_last_4_digit'] = df['Card_last_4_digit'].astype(str)
    return df

# Function to extract only the date portion from datetime objects
def extract_date_only(df):
    df['transaction_date'] = df['transaction_date'].dt.date
    return df

# Detect and convert date format in both DataFrames
file1_data = convert_date_format(file1_data)
file2_data = convert_date_format(file2_data)

if file1_data is not None and file2_data is not None:
    # Ensure 'Card_last_4_digit' is of the same data type (string) in both DataFrames
    file1_data = ensure_card_last_4_digit_datatype(file1_data)
    file2_data = ensure_card_last_4_digit_datatype(file2_data)


    # Add leading zeros to 'Card_last_4_digit' in file2_data
    file2_data = add_leading_zeros(file2_data)

    # Extract only the date portion from datetime objects
    file1_data = extract_date_only(file1_data)
    file2_data = extract_date_only(file2_data)

    # Calculate date difference
    date_tolerance = timedelta(days=1)
    auth_tolerance = 0.5

    # Merge data
    merged_data = pd.merge(file1_data, file2_data, on='Card_last_4_digit')
    merged_data['date_diff'] = (merged_data['transaction_date_x'] - merged_data['transaction_date_y']).abs()

    # Filter matches
    matches = merged_data[
        (merged_data['date_diff'] <= date_tolerance) &
        (abs(merged_data['Authorization_amount_x'] - merged_data['Authorization_amount_y']) <= auth_tolerance)
    ]



    if not matches.empty:
        # Save the matches to a CSV file
        matches.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Output_2.csv', index=False)
        print("Matches saved to '/Users/shariquerahi/Desktop/Git/Python_Script/Output_2.csv'")
    else:
        print("No matches found.")
else:
    print("Date format mismatch. Unable to proceed.")


