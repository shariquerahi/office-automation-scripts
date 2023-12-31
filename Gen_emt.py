
import csv

input_filename = "/Users/shariquerahi/Downloads/CC recon.xlsx - EMT Mast2 (1).csv"
output_filename = "/Users/shariquerahi/Desktop/Git/Python_Script/out_proper_emt.csv"

with open(input_filename, "r") as infile, open(output_filename, "w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Remove spaces and commas from each element and write the cleaned row to the output file
        cleaned_row = [element.replace(" ", "").replace(",", "") for element in row]
        writer.writerow(cleaned_row)

print("Data has been formatted and saved to", output_filename)
