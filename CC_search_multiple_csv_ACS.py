import csv

def search_csv_for_words(csv_file, search_word_sets):
    found_lines = []

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and store the header row

        for row in reader:
            for search_words in search_word_sets:
                found = True
                for search_word in search_words:
                    found_in_line = False
                    for cell in row:
                        if search_word in cell:
                            found_in_line = True
                            break

                    if not found_in_line:
                        found = False
                        break

                if found:
                    found_lines.append(row)
                    break

    return header, found_lines

def main():
    # List of CSV files to search
    csv_files = ["/Users/shariquerahi/Downloads/Detailed_Transaction_Report (37).csv", "/Users/shariquerahi/Downloads/Detailed_Transaction_Report (36).csv", "/Users/shariquerahi/Downloads/Detailed_Transaction_Report (35).csv"]

    # List of search word sets, you can add more sets as needed
    search_word_sets = [
        ["5430012781", "another_word"],
        ["5430013833", "some_other_word"],
        ["5430011477", "some_other_word"]
    ]

    # List to store the combined found lines from all CSV files
    combined_found_lines = []

    for csv_file_path in csv_files:
        header, found_lines = search_csv_for_words(csv_file_path, search_word_sets)
        combined_found_lines.extend(found_lines)

    if combined_found_lines:
        # Print the found lines to the console
        print(",".join(header))
        for line in combined_found_lines:
            print(",".join(line))

        # Store the found lines in a new CSV file
        output_file_path = "/Users/shariquerahi/Downloads/output_ACS.csv"
        with open(output_file_path, "w", newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerows(combined_found_lines)

        print(f"\nFound lines from all CSV files have been saved in '{output_file_path}'.")
    else:
        print(f"No lines containing any of the specified word sets were found in any of the CSV files.")

if __name__ == "__main__":
    main()

'''The provided code defines a Python script that searches multiple CSV files for lines containing specific sets of search words and combines the results. Here's what the code does:

1. It imports the `csv` module to work with CSV files.

2. It defines a function called `search_csv_for_words` that takes two arguments:
   - `csv_file`: The path to the CSV file you want to search.
   - `search_word_sets`: A list of sets, where each set contains search words (strings) to look for in the CSV file.

3. Within the `search_csv_for_words` function:
   - It initializes an empty list called `found_lines` to store the lines where any of the specified search word sets are found.

   - It opens the specified CSV file using `open` with the `newline=''` argument to handle line endings properly.

   - It uses a `csv.reader` to iterate through each row in the CSV file.

   - For each row, it iterates through the `search_word_sets` list and checks if any of the sets of search words are found in the row. It uses nested loops to compare each search word in a set with the cell values in the row.

   - If all the search words in a set are found in the row, it appends the entire row to the `found_lines` list.

   - The function returns both the header row and the `found_lines` list.

4. The `main` function is defined:
   - It specifies a list of CSV files to search (`csv_files`) and a list of search word sets (`search_word_sets`). You can add more CSV files and search word sets as needed.

   - It initializes an empty list called `combined_found_lines` to store the combined found lines from all CSV files.

   - It iterates through each CSV file specified in `csv_files`, calls the `search_csv_for_words` function to find lines containing any of the search word sets, and appends the results to `combined_found_lines`.

   - If `combined_found_lines` is not empty, it prints the header row and the found lines to the console. It also stores the found lines in a new CSV file named "output_ACS.csv."

   - If no lines containing any of the specified word sets are found in any of the CSV files, it prints a message indicating that.

5. The script is executed when the Python script is run directly (not imported as a module) by calling the `main` function.

As for the script name, you can choose a meaningful name based on its purpose. For example, you could name it something like "search_multiple_csv.py" to indicate that it searches multiple CSV files for specific sets of words.'''