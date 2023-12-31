import csv
import json

# Define a function to extract and arrange data from a JSON string
def extract_data(json_str):
    data = json.loads(json_str)
    return [
        data["amount"],
        data["cardEnding"],
        data["crdr"],
        data["description"],
        data["entityId"],
        data["extTxnId"],
        data["kitNo"],
        data["mobileNo"],
        data["transactionDateTime"],
        data["transactionType"],
        data["txnDate"],
        data["txnOrigin"],
        data["txnRefNo"],
        data["txnStatus"],
        data["walletList"]["GENERAL"]["balance"],
        data["walletList"]["GENERAL"]["currencyCode"],
        data["merchantId",'N/A'],
        data["merchantName",'N/A']
    ]

# Open the CSV file for reading
with open('/Users/shariquerahi/Downloads/ffffffffff.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Define header row for the output CSV
    header = [
        "amount", "cardEnding", "crdr", "description", "entityId", "extTxnId",
        "kitNo", "mobileNo", "transactionDateTime", "transactionType", "txnDate",
        "txnOrigin", "txnRefNo", "txnStatus", "balance", "currencyCode", "merchantId", "merchantName"
    ]

    # Create a new CSV file for writing the extracted data
    with open('/Users/shariquerahi/Downloads/payloan_aaranged_data.csv', 'w', newline='') as outputfile:
        csvwriter = csv.writer(outputfile)
        
        # Write the header row to the output CSV
        csvwriter.writerow(header)

        # Iterate through each row in the input CSV
        for row in csvreader:
            # Assuming the JSON data is in the first column of each row
            json_data = row[0]

            # Extract and arrange the data from the JSON string
            extracted_data = extract_data(json_data)

            # Write the extracted data to the output CSV
            csvwriter.writerow(extracted_data)

print("Extraction and arrangement complete. Data saved to 'output.csv'.")

