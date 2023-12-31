import csv

# Define the input and output file names
input_file = '/Users/shariquerahi/Downloads/Fed_CC_Approved_Dec_23.csv'
output_file = '/Users/shariquerahi/Downloads/CC_Offer_Added_20thDec2023_unsec.csv'

# Define default values for missing fields
default_pan = ''
default_mob_number = ''
default_expires_at = '2024-01-22'
default_card_program='FEDERAL:PREAPPROVED:UNSECURED::FI'
default_cc_eligibility='CC_OFFER_ELIGIBILITY_CRITERIA_STATUS_APPROVED'

# Open the input and output CSV files
with open(input_file, mode='r') as csv_file, open(output_file, mode='w', newline='') as output_csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_csv_file)

    # Write the header for the output CSV file
    csv_writer.writerow(['PAN', 'customer_id', 'mob_number', 'Limit', 'expires_at','card_program','cc_eligibility'])

    # Skip the header row in the input CSV
    next(csv_reader)

    # Process each row in the input CSV
    for row in csv_reader:
        # Extract the customer_id and Limit values from the input CSV
        customer_id = row[0]
        limit = row[1]

        # Write the transformed row to the output CSV
        csv_writer.writerow([default_pan, customer_id, default_mob_number, limit, default_expires_at,default_card_program,default_cc_eligibility])

print(f"CSV data has been transformed and saved to {output_file}.")
