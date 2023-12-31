import csv

src_file_path = "/Users/shariquerahi/Downloads/Untitled spreadsheet - employer name (14).csv"
dest_file_path = "/Users/shariquerahi/Desktop/Git/Python_Script/CC_PythonScript/output_forex.csv"

# Read the source CSV file
with open(src_file_path, 'r') as src_file:
    reader = csv.reader(src_file)
    records = list(reader)

# Process the data and create the result
result = []
for idx, row in enumerate(records[1:], start=1):  # Skip header row
    date_parts = row[6].split("T")[0].split("-")
    formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"

    result_row = [
        f"FREFUND{idx}",
        formatted_date,
        row[12][:4],
        row[12],
        "C",
        row[5],
        row[4],
        formatted_date,
        f"ForexMarkupRefund/{row[0]}",
        "INR",
        "OCDEM",
        "BULKOPD"
    ]
    result.append(result_row)

# Write the result to the destination CSV file
with open(dest_file_path, 'w', newline='') as dest_file:
    writer = csv.writer(dest_file)
    writer.writerows(result)
