# Total data provided as a string
total_data_string = """VENDOR_IDENTIFIER in 
(5430013796,
5430012067,
5430012548,
5430013269,
5430013855,
5430012211,
5430012023,
5430013455,
5430013313,
5430013131,
5430013213,
5430012823,
5430012875,
5430012289,
5430012481,
5430013731,
5430011890,
5430012221,
5430012634,
5430012461,
5430013316,
5430011927,
5430013129,
5430013084,
5430012174,
5430012938,
5430013141,
5430012746,
5430012894,
5430013050,
5430012199,
5430012660,
5430012123,
5430013780,
5430013194,
5430013490,
5430012465,
5430011862,
5430013235,
5430012130,
5430013164,
5430013773,
5430012948,
5430012846,
5430013876,
5430013601,
5430012492,
5430012057,
5430011955,
5430012987,
5430012736,
5430013286,
5430011954,
5430012241,
5430012695,
5430012737,
5430012022,
5430013103,
5430013287,
5430013273,
5430013839,
5430012706,
5430011989,
5430012532,
5430011838,
5430013339,
5430012513,
5430013593,
5430013059,
5430012739,
5430013266,
5430013589,
5430012644,
5430013897,
5430013820,
5430012402,
5430013939,
5430012285,
5430012223,
5430012337,
5430012340,
5430012555,
5430013272,
5430012135,
5430012037,
5430012588,
5430013776,
5430012361,
5430012762,
5430013655,
5430013683,
5430012258,
5430012282,
5430012049,
5430012315,
5430013687,
5430011819,
5430012175,
5430013167,
5430011921,
5430012389,
5430011940,
5430013202,
5430012478,
5430013325,
5430013096,
5430012692,
5430013435,
5430012718,
5430012960,
5430011959,
5430012334)"""

# Database data provided as a string
database_data_string = """VENDOR_IDENTIFIER
5430012402
5430013316
5430012548
5430013776
5430012739
5430013287
5430013820
5430013589
5430013876
5430012644
5430013687
5430011838
5430013103
5430013897
5430012736
5430013455
5430012057
5430011955
5430013325
5430012315
5430012221
5430012478
5430012718
5430013164
5430012135
5430012241
5430012223
5430012282
5430012211
5430012513
5430012532
5430013266
5430013731
5430012023
5430013773
5430013339
5430013855
5430013167
5430013235
5430012461
5430012894
5430012389
5430012492
5430012987
5430012022
5430011954"""

# Function to convert a string of data into a set of integers
def string_to_set(data_string):
    data_list = data_string.split("\n")
    data_list = [int(item.strip()) for item in data_list if item.strip().isdigit()]
    return set(data_list)

# Convert the total data and database data strings to sets
total_data_set = string_to_set(total_data_string)
database_data_set = string_to_set(database_data_string)

# Find the data present in total data but not in the database
data_not_in_database = total_data_set.difference(database_data_set)

print("Data found in total data but not in the database:")
print(data_not_in_database)

''' The provided code does the following:

1. It defines two strings, `total_data_string` and `database_data_string`, which contain data in a specific format. These strings represent data, with each line containing a unique identifier (presumably an integer).

2. It defines a function called `string_to_set` that takes a string as input, splits it into lines, and then converts each line into an integer. It creates a set from these integers and returns the set. This function is designed to convert the data in the provided strings into sets for comparison.

3. It calls the `string_to_set` function to convert both `total_data_string` and `database_data_string` into sets: `total_data_set` and `database_data_set`.

4. It finds the difference between `total_data_set` and `database_data_set` using the `difference` method. This operation identifies the unique identifiers that are present in the `total_data_set` but not in the `database_data_set`.

5. Finally, it prints the unique identifiers that are found in the `total_data_set` but not in the `database_data_set`.

The script compares two sets of unique identifiers to find the identifiers that exist in the "total data" set but not in the "database data" set.

The script doesn't have a specific name provided, so you can choose a meaningful name based on its purpose. For example, you could name it something like "compare_data_sets.py" to indicate that it compares two sets of data.'''