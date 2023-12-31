import csv
import json
from collections import defaultdict
import pandas as pd

# Initialize dictionaries to store data for both types of rows
type1_data = defaultdict(list)
type2_data = defaultdict(list)

# Replace "XXXX" with None for cleaner output
def clean_value(value):
    return None if value == '"XXXX"' else value

# Read the CSV file and process each row
with open('/Users/shariquerahi/Desktop/Git/Python_Script/payload_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        if row:
            # Determine the row type based on the presence of "Bin" key
            if '"Bin"' in row[0]:
                # Type 2 row
                json_data = json.loads(row[0])
                for key, value in json_data.items():
                    type2_data[key].append(clean_value(value))
            else:
                # Type 1 row
                json_data = json.loads(row[0])
                for key, value in json_data.items():
                    type1_data[key].append(clean_value(value))

# Create pandas DataFrames for each type of data
df_type1 = pd.DataFrame(type1_data)
df_type2 = pd.DataFrame(type2_data)

# Save DataFrames to output files
df_type1.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Output1_kibana.csv', index=False)
df_type2.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/output2_kibana.csv', index=False)

print("Data saved to output files: 'output_type1.csv' and 'output_type2.csv'")
