import csv

# Load the total data from the CSV file
total_data_set = set()
with open('/Users/shariquerahi/Downloads/Total_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        total_data_set.add(row[0])

# Load the database data from a CSV file
database_data_set = set()
with open('/Users/shariquerahi/Downloads/database_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        database_data_set.add(row[0])
# Print the contents of both sets
print("Total data set:", total_data_set)
print("Database data set:", database_data_set)

# Find the data present in total data but not in the database
data_not_in_database = total_data_set.difference(database_data_set)

# Write the output to a CSV file
with open('/Users/shariquerahi/Downloads/output_data_111.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ACCOUNT_ID'])
    for item in data_not_in_database:
        writer.writerow([item])

print("Data found in total data but not in the database has been written to 'output_data.csv'.")

''' The provided code does the following:

1. It imports the `csv` module to work with CSV files.

2. It loads data from two CSV files: "Total_data.csv" and "database_data.csv" located in the "/Users/shariquerahi/Downloads" directory.

3. For each CSV file, it reads the data and populates sets (`total_data_set` and `database_data_set`) with the values from the first column (assuming the first column contains unique identifiers). It skips the header row using `next(reader)`.

4. It prints the contents of both sets to the console, showing the unique identifiers present in each set.

5. It calculates the set difference between `total_data_set` and `database_data_set` to find data present in the total data set but not in the database data set. This difference is stored in the `data_not_in_database` set.

6. It writes the `data_not_in_database` set to a new CSV file named "output_data_111.csv" in the same directory ("/Users/shariquerahi/Downloads"). The output CSV file contains a single column labeled "ACCOUNT_ID" with the unique identifiers found in the `data_not_in_database` set.

7. Finally, it prints a message to indicate that the data found in the total data set but not in the database data set has been written to the "output_data_111.csv" file.

The script can be saved with a `.py` file extension (e.g., `compare_data.py`) and executed using a Python interpreter. It is designed to compare data between two CSV files based on a unique identifier and generate a new CSV file with the differences.'''
