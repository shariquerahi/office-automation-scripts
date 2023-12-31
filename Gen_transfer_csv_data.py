import csv

# Define the input and output file names
input_file = '/Users/shariquerahi/Downloads/CC offer file w_ limit - Single name.csv'
output_file = '/Users/shariquerahi/Desktop/Git/Python_Script/cc_offer_single_name.csv'

# Define default values for missing fields
default_pan = ''
default_mob_number = ''
default_expires_at = '2023-11-22'

# Open the input and output CSV files
with open(input_file, mode='r') as csv_file, open(output_file, mode='w', newline='') as output_csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_csv_file)

    # Write the header for the output CSV file
    csv_writer.writerow(['PAN', 'customer_id', 'mob_number', 'Limit', 'expires_at'])

    # Skip the header row in the input CSV
    next(csv_reader)

    # Process each row in the input CSV
    for row in csv_reader:
        # Extract the customer_id and Limit values from the input CSV
        customer_id = row[0]
        limit = row[1]

        # Write the transformed row to the output CSV
        csv_writer.writerow([default_pan, customer_id, default_mob_number, limit, default_expires_at])

print(f"CSV data has been transformed and saved to {output_file}.")

''' The provided code does the following:

1. It imports the `csv` module for working with CSV files.

2. It defines the input and output file paths:
   - `input_file` points to the source CSV file, which is located at '/Users/shariquerahi/Downloads/Offer File extraction_CC (1).csv'.
   - `output_file` specifies the destination CSV file where the transformed data will be saved, located at '/Users/shariquerahi/Downloads/out_cc_offer.csv'.

3. It defines default values for missing fields:
   - `default_pan` is set to an empty string ('') for the 'PAN' column.
   - `default_mob_number` is set to an empty string ('') for the 'mob_number' column.
   - `default_expires_at` is set to '2023-10-22' for the 'expires_at' column.

4. It opens the input CSV file for reading (`csv_file`) and the output CSV file for writing (`output_csv_file`).

5. It sets up CSV readers and writers for the input and output files, respectively.

6. It writes the header row for the output CSV file, specifying the column names: 'PAN', 'customer_id', 'mob_number', 'Limit', and 'expires_at'.

7. It skips the header row in the input CSV file using `next(csv_reader)` to avoid processing the header data.

8. It processes each row in the input CSV file:
   - It extracts the 'customer_id' and 'Limit' values from the input CSV row.
   - It writes a new row to the output CSV file with the following values: 'default_pan', 'customer_id', 'default_mob_number', 'limit', and 'default_expires_at'.

9. After processing all rows, it prints a message indicating that the CSV data has been transformed and saved to the specified output file.

The script essentially takes an input CSV file, processes its data by adding default values for missing fields, and saves the transformed data to an output CSV file.

As for the script name, you can choose a name that reflects its purpose. For example, you could name it something like "transform_csv_data.py" to indicate that it transforms CSV data.'''