import csv
from datetime import datetime

# Input and output file paths
input_file = "input.csv"
output_file = "output.csv"

# Open the input and output CSV files
with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
    reader = csv.DictReader(in_file)
    fieldnames = reader.fieldnames

    # Write the header row to the output file
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Format the date from "YYYY-MM-DDTHH:MM:SS.000Z" to "MM/DD/YYYY"
        transaction_date = datetime.strptime(row['transaction_date'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%m/%d/%Y")

        # Convert Authorization_amount and Card_last_4_digit to float
        authorization_amount = float(row['Authorization_amount'])
        card_last_4_digit = int(row['Card_last_4_digit'])

        # Write the formatted data to the output file
        writer.writerow({
            'transaction_date': transaction_date,
            'Authorization_amount': authorization_amount,
            'Card_last_4_digit': card_last_4_digit,
            'display_name': row['display_name']
        })

print("Output CSV file has been created: " + output_file)
