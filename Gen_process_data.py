import csv

class Info:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

actor_ids = [
    "36ccc639-33e8-4d60-927d-bcbeccebbb31",
    "010528ae-caa2-466d-8d81-1b0d85ef78f6",
    "6b9c5891-fef2-4348-b81e-b5c252632293",
    "ac66b94b-0b6c-4eee-bb0e-d7dfe9c2a198",
    "55ab0f19-d688-49f9-ac87-c212c6d710df",
    "874a9bd4-ec62-4287-9405-2314f15cfd0f",
    "3bde1940-e0b5-4ada-8ed1-99debb53890d",
    "4e7b64cd-b20c-4936-8a23-aaac0f79ce05",
]

rows = [
    ["2e4bc86b-8656-46d9-80a4-5e828fa3c199", "9632007381", "arunkumarsnc99@gmail.com"],
    ["4cadb1a1-e37e-4aaf-92e9-4563918bd641", "8148920620", "viven0606@gmail.com         "],
    ["ff739938-621d-43e4-aff4-822984013f77", "9953760619", "mk7193933@gmail.com         "],
    ["4250d669-6854-4262-9707-b4f6ae587b6a", "9949624284", "vramaraju14@gmail.com       "],
    ["8d0d280a-f0e2-4a30-aa96-7f8ab0832b1f", "9029944326", "saurabhrajguru17@gmail.com  "],
    ["538b748a-c7c8-4ecc-85f2-228a8b81b63e", "9895858558", "varischemnad@gmail.com      "],
    ["f2961b61-bda0-466a-9d91-35c8132093d6", "8295963178", "arch1995@gmail.com          "],
    ["1196dee6-d0cd-4954-9d78-9b203a6d5115", "9871212122", "ramanchandhok11@yahoo.com   "],
    ["0974f777-f616-4a75-912d-6dea06a5ad58", "9871309694", "sufisakib8@gmail.com        "],
    ["d074efdb-9639-4c9e-95ad-a50a8efe6641", "9566811811", "rkrvivek@gmail.com          "],
    ["9853fb0b-9a0b-420c-af08-0896bfc8cb09", "9832094929", "samirmondal94695@gmail.com  "],
    ["2ab6a7aa-74cf-424a-a28d-447c43a35cb4", "7204422451", "sharathj32@gmail.com        "],
    ["08edc01c-cb4c-4eb8-91c7-2ecba8ee1527", "9765935256", "mickyagrawal5256@gmail.com  "],
]

mp = {row[0]: row[1:] for row in rows}  # Create dictionary directly

output_rows = []
for actor_id in actor_ids:
    if actor_id in mp:
        output_row = [actor_id, mp[actor_id][0], mp[actor_id][1]]
        output_rows.append(output_row)
    else:
        print(f"Data not found for actor ID: {actor_id}")

# Write output to a CSV file
output_file = "output.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Actor ID", "Phone", "Email"])
    writer.writerows(output_rows)

print(f"Output written to {output_file}")

''' This Python script does the following:

1. Imports the `csv` module.
2. Defines a class `Info` that has an `__init__` method to initialize objects with `email` and `phone` attributes.
3. Defines a list of `actor_ids` containing unique identifiers.
4. Defines a list of `rows` containing sublists with three elements: a unique identifier, a phone number, and an email address.
5. Creates a dictionary `mp` that maps the unique identifier to the corresponding phone number and email address.
6. Initializes an empty list `output_rows` to store the rows for the final output.
7. Iterates through the `actor_ids` and checks if an `actor_id` exists in the `mp` dictionary. If it does, it creates a new row with the `actor_id`, phone number, and email address and appends it to `output_rows`. If not, it prints a message indicating that data was not found for that `actor_id`.
8. Writes the `output_rows` to a CSV file named "output.csv" along with a header row containing column names ("Actor ID", "Phone", "Email").

The script effectively extracts information for the specified `actor_ids` from the `rows` data and writes it to a CSV file.

To run this script, you can save it as a `.py` file (e.g., `process_data.py`) and execute it using a Python interpreter. It will generate an "output.csv" file containing the processed data.'''