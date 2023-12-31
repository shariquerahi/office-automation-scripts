import csv

input_file = "/Users/shariquerahi/Downloads/Easemytrip_Recon_FIDCEMT.xlsx - EMT Mastersheet.csv"
output_file = "/Users/shariquerahi/Desktop/Git/Python_Script/EMT_input_correct.csv"

with open(input_file, "r", newline="") as input_csv, open(output_file, "w", newline="") as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    
    # Write the header row as is
    header = next(reader)
    writer.writerow(header)

    # Process and write the data rows
    for row in reader:
        # Remove commas from the numeric fields
        modified_row = [row[0]] + [int(field.replace(",", "")) for field in row[1:]]
        writer.writerow(modified_row)

print("Data has been processed and saved to", output_file)
