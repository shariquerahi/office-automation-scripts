import os

# Define the directory where you want to start the search
start_directory = "/"

# Function to recursively search for .py files
def find_py_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

# Call the function to find .py files
py_files = find_py_files(start_directory)

# Print the list of .py files
if py_files:
    print("List of .py files:")
    for py_file in py_files:
        print(py_file)
else:
    print("No .py files found on your laptop.")
