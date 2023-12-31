import os
import shutil

# Define the source directory where you want to search for files
source_directory = "/Users/shariquerahi/Desktop/Git/Python_Script/Gen_PythonScript"  # Source directory
destination_directory = "/Users/shariquerahi/Desktop/Git/Python_Script/Loan_PythonScript"  # Destination directory for files starting with "dc_" or "DC_"

# Ensure the destination directory exists; create it if not
os.makedirs(destination_directory, exist_ok=True)

# Function to recursively search for files and move them if their names start with "dc_" or "DC_"
def move_files_starting_with_dc(source_dir, dest_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.startswith("Loan_") or file.startswith("LOAN_"):
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.move(source_file_path, dest_file_path)
                print(f"Moved: {source_file_path} -> {dest_file_path}")

# Call the function to move files starting with "dc_" or "DC_"
move_files_starting_with_dc(source_directory, destination_directory)

print("Done!")
