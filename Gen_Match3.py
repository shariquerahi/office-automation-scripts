import csv
from datetime import datetime, timedelta

def load_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def detect_date_format(date_str):
    formats = ['%m/%d/%Y', '%Y-%m-%d']  # Add more date formats as needed
    for date_format in formats:
        try:
            datetime.strptime(date_str, date_format)
            return date_format
        except ValueError:
            continue
    return None

def convert_to_common_date_format(date_str, date_format):
    return datetime.strptime(date_str, date_format).strftime('%m/%d/%Y')

def match_data(file1_data, file2_data):
    matches = []

    for row1 in file1_data:
        for row2 in file2_data:
            date_format1 = detect_date_format(row1['transaction_date'])
            date_format2 = detect_date_format(row2['transaction_date'])

            if date_format1 is not None and date_format2 is not None:
                common_format = '%m/%d/%Y'
                date1 = convert_to_common_date_format(row1['transaction_date'], date_format1)
                date2 = convert_to_common_date_format(row2['transaction_date'], date_format2)

                # Convert transaction_date to datetime objects for comparison
                date1 = datetime.strptime(date1, common_format)
                date2 = datetime.strptime(date2, common_format)

                # Calculate date difference
                date_diff = abs((date1 - date2).days)

                # Calculate Authorization_amount difference
                auth_amount1 = float(row1['Authorization_amount'])
                auth_amount2 = float(row2['Authorization_amount'])
                auth_diff = abs(auth_amount1 - auth_amount2)

                if (
                    row1['Card_last_4_digit'] == row2['Card_last_4_digit'] and
                    date_diff <= 1 and
                    auth_diff <= 0.5
                ):
                    matches.append({
                        'Card_last_4_digit': row1['Card_last_4_digit'],
                        'transaction_date_file1': date1.strftime('%m/%d/%Y'),
                        'transaction_date_file2': date2.strftime('%m/%d/%Y'),
                        'Authorization_amount_file1': auth_amount1,
                        'Authorization_amount_file2': auth_amount2
                    })

    return matches

file1_data = load_csv('/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/Paytm_DB_DATA_dateFmt.csv')
file2_data = load_csv('/Users/shariquerahi/Downloads/Paytm_oct.csv')


matches = match_data(file1_data, file2_data)

if matches:
    with open('output_matches.csv', mode='w', newline='') as output_file:
        fieldnames = [
            'Card_last_4_digit',
            'transaction_date_file1',
            'transaction_date_file2',
            'Authorization_amount_file1',
            'Authorization_amount_file2'
        ]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(matches)
    print("Matches saved to '/Users/shariquerahi/Downloads/Final_out_Paytm.csv'")
else:
    print("No matches found.")












