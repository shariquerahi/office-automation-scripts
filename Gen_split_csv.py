import pandas as pd

# Define the file path to the large file
large_file_path = '/Users/shariquerahi/Desktop/Reconsile Merchant Data/DC_Paytm_63603.csv'

# Define the number of lines in each smaller file
lines_per_file = 200000

# Read the large file into a Pandas DataFrame
large_dataframe = pd.read_csv(large_file_path)

# Calculate the number of smaller files needed
total_rows = len(large_dataframe)
num_files = total_rows // lines_per_file + 1

# Split the data into smaller DataFrames and save them to separate files
for i in range(num_files):
    start = i * lines_per_file
    end = (i + 1) * lines_per_file
    smaller_dataframe = large_dataframe[start:end]

    # Save the smaller DataFrame to a CSV file
    smaller_file_path = f'smaller_data_{i}.csv'
    smaller_dataframe.to_csv(smaller_file_path, index=False)

    print(f'Saved {smaller_file_path}')

print('Splitting complete.')
