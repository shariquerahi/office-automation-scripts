import os
import shutil

# Define the source directory where you want to search for files
source_directory = "/Users/shariquerahi/Desktop/Git/Python_Script"

# Define the destination directory where you want to move the CSV files
csv_destination_directory = os.path.join(source_directory, "CSV_Files")

# Ensure the destination directory exists; create it if not
os.makedirs(csv_destination_directory, exist_ok=True)

# Function to recursively search for CSV files and move them
def collect_csv_files(source_dir, dest_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".csv"):
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.move(source_file_path, dest_file_path)
                print(f"Moved: {source_file_path} -> {dest_file_path}")

# Call the function to collect CSV files
collect_csv_files(source_directory, csv_destination_directory)

print("Done!")
