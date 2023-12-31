import csv

def search_csv_for_word(csv_file, search_word):
    found_lines = []

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                if search_word in cell:
                    found_lines.append(row)
                    break

    return found_lines

if __name__ == "__main__":
    csv_file_path = "/Users/shariquerahi/Downloads/Detailed_Transaction_Report (8).csv"  # Replace with the name or path of your CSV file
    search_word = "5430012992"

    found_lines = search_csv_for_word(csv_file_path, search_word)

    if found_lines:
        for line in found_lines:
            print(",".join(line))
    else:
        print(f"No lines containing '{search_word}' were found in the CSV file.")

'''The provided code defines a Python script that searches a CSV file for a specific word (or substring) and prints the lines in which that word is found. Here's what the code does:

1. It imports the `csv` module to work with CSV files.

2. It defines a function called `search_csv_for_word` that takes two arguments:
   - `csv_file`: The path to the CSV file you want to search.
   - `search_word`: The word (or substring) you want to search for within the CSV file.

3. Within the `search_csv_for_word` function:
   - It initializes an empty list called `found_lines` to store the lines where the search word is found.

   - It opens the specified CSV file using `open` with the `newline=''` argument to handle line endings properly.

   - It uses a `csv.reader` to iterate through each row in the CSV file.

   - For each row, it iterates through the cells in that row and checks if the `search_word` is present in any of the cells. If the word is found, it appends the entire row to the `found_lines` list and breaks out of the inner loop.

   - The function returns the `found_lines` list, which contains the lines where the search word was found.

4. In the `if __name__ == "__main__"` block, the script is executed when the Python script is run directly (not imported as a module).

5. It defines the `csv_file_path` variable with the path to the CSV file you want to search. You can replace this with the name or path of your specific CSV file.

6. It specifies the `search_word` variable, which is the word you want to search for within the CSV file.

7. It calls the `search_csv_for_word` function with the specified CSV file and search word, storing the result in the `found_lines` list.

8. It checks if any lines were found containing the search word:
   - If lines are found, it iterates through the `found_lines` list and prints each line as a comma-separated string.

   - If no lines are found, it prints a message indicating that no lines containing the search word were found in the CSV file.

As for the script name, you can choose a meaningful name based on its purpose. For example, you could name it something like "search_csv.py" to indicate that it searches for a specific word in a CSV file.'''