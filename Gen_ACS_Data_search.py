import csv

def search_csv_for_words(csv_file, search_words):
    found_lines = []

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and store the header row

        for row in reader:
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

    return header, found_lines

def main():
    csv_file_path = "/Users/shariquerahi/Downloads/Detailed_Transaction_Report (8).csv"   # Replace with the name or path of your CSV file

    # Enter the search words you want to use as a list
    search_words = ["5430012992",""]

    header, found_lines = search_csv_for_words(csv_file_path, search_words)

    if found_lines:
        # Print the found lines to the console
        print(",".join(header))
        for line in found_lines:
            print(",".join(line))

        # Store the found lines in a new CSV file
        output_file_path = "/Users/shariquerahi/Downloads/out_acs.csv"
        with open(output_file_path, "w", newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerows(found_lines)

        print(f"\nFound lines have been saved in '{output_file_path}'.")
    else:
        print(f"No lines containing all the specified words were found in the CSV file.")

if __name__ == "__main__":
    main()
