'''import csv
import ast

# Input and output file names
input_csv_file = '/Users/shariquerahi/Downloads/On_demand_report_2023-10-18T17_25_32.635Z_5761b2b0-6ddb-11ee-8e28-557e366aa670.csv'
output_csv_file = '/Users/shariquerahi/Desktop/Git/Python_Script/output2_kibana.csv' '''

import csv
import json

# Define input and output files
input_file = '/Users/shariquerahi/Downloads/On_demand_report_2023-10-18T17_25_32.635Z_5761b2b0-6ddb-11ee-8e28-557e366aa670.csv'
output_file = '/Users/shariquerahi/Desktop/Git/Python_Script/output2_kibana.csv'

# Open the input CSV file for reading and the output file for writing
with open(input_file, 'r', newline='') as csv_input_file, open(output_file, 'w', newline='') as csv_output_file:
    # Create a CSV reader for the input file
    reader = csv.DictReader(csv_input_file)

    # Retrieve the header fields from the input file
    header = reader.fieldnames

    # Create a CSV writer for the output file with the same header
    writer = csv.DictWriter(csv_output_file, fieldnames=header)

    # Write the header to the output CSV file
    writer.writeheader()

    # Iterate through the rows in the input CSV file and clean and write them to the output CSV file
    for row in reader:
        # Remove extra double quotes from the values
        clean_row = {key: value.strip('"') for key, value in row.items()}
        writer.writerow(clean_row)

print(f"Data has been saved to {output_file}")
