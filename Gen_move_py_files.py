import os
import shutil

# Define the source directory where you want to search for .py files
source_directory = "/Users/shariquerahi/Desktop/Git/Python_Script" #"/Users/shariquerahi/Desktop/Git/Python_Script"  #"/Users/shariquerahi/Downloads"

# Define the destination directory where you want to move the .py files
destination_directory = "/Users/shariquerahi/Desktop/Git/Python_Script/SQL_File"     #"/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files"

# Ensure the destination directory exists; create it if not
os.makedirs(destination_directory, exist_ok=True)

# Function to recursively search for .py files and move them
def collect_py_files(source_dir, dest_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".sql"):
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.move(source_file_path, dest_file_path)
                print(f"Moved: {source_file_path} -> {dest_file_path}")

# Call the function to collect .py files
collect_py_files(source_directory, destination_directory)

print("Done!")

 ##/Users/shariquerahi/Desktop/Git/Python_Script/CSV_Files/OUtput_5430013524.csv

''' The code you provided performs the following tasks:

1. It imports the `os` and `shutil` modules, which are used for working with the file system and performing file operations.

2. It defines the `source_directory` variable, which specifies the directory where the script will search for `.py` files. In this case, it's set to "/Users/shariquerahi/Downloads."

3. It defines the `destination_directory` variable, which specifies the directory where the `.py` files will be moved to. In this case, it's set to "/Users/shariquerahi/Desktop/Git/Python_Script."

4. It ensures that the `destination_directory` exists; if it doesn't, it creates the directory using `os.makedirs`.

5. It defines a function `collect_py_files` that recursively searches for `.py` files in the `source_directory` and moves them to the `destination_directory`. It does this by iterating through all files in the directory hierarchy using `os.walk`, checking if a file has a ".py" extension, and then using `shutil.move` to move the file to the destination directory. It also prints a message indicating which file is moved.

6. Finally, it calls the `collect_py_files` function with the `source_directory` and `destination_directory` as arguments to start the process of collecting and moving `.py` files.

The script collects all `.py` files from the source directory and moves them to the destination directory, preserving their directory structure. It then prints a message "Done!" when the process is complete.

The script can be saved with a `.py` file extension (e.g., `move_py_files.py`) and executed using a Python interpreter. It will move all `.py` files from the specified source directory to the destination directory.'''