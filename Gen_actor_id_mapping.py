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
    "b6d89da3-4c80-4f86-9757-015fe20471b3"
]

rows = [
    ["2e4bc86b-8656-46d9-80a4-5e828fa3c199", "9632007381", "arunkumarsnc99@gmail.com"],
    ["4cadb1a1-e37e-4aaf-92e9-4563918bd641", "8148920620", "viven0606@gmail.com"],
    ["ff739938-621d-43e4-aff4-822984013f77", "9953760619", "mk7193933@gmail.com"],
    ["4250d669-6854-4262-9707-b4f6ae587b6a", "9949624284", "vramaraju14@gmail.com"],
    ["8d0d280a-f0e2-4a30-aa96-7f8ab0832b1f", "9029944326", "saurabhrajguru17@gmail.com"],
    ["538b748a-c7c8-4ecc-85f2-228a8b81b63e", "9895858558", "varischemnad@gmail.com"],
    ["f2961b61-bda0-466a-9d91-35c8132093d6", "8295963178", "arch1995@gmail.com"],
    ["1196dee6-d0cd-4954-9d78-9b203a6d5115", "9871212122", "ramanchandhok11@yahoo.com"],
    ["0974f777-f616-4a75-912d-6dea06a5ad58", "9871309694", "sufisakib8@gmail.com"],
    ["d074efdb-9639-4c9e-95ad-a50a8efe6641", "9566811811", "rkrvivek@gmail.com"],
    ["9853fb0b-9a0b-420c-af08-0896bfc8cb09", "9832094929", "samirmondal94695@gmail.com"],
    ["2ab6a7aa-74cf-424a-a28d-447c43a35cb4", "7204422451", "sharathj32@gmail.com"],
    ["08edc01c-cb4c-4eb8-91c7-2ecba8ee1527", "9765935256", "mickyagrawal5256@gmail.com"],
    ["345bec83-b6d0-490e-a7d8-c389959500f1", "9121075964", "priyasoudami@gmail.com"],
    ["2a8bbfcf-f686-460a-aa94-86e4d610e870", "9886777038", "harsha3445@gmail.com"],
    ["3181f420-b048-44ab-b209-f134135eadad", "9848075143", "thalapula@gmail.com"],
    ["326416d2-4b8b-4b85-a901-13b9f0ce93fc", "9379950839", "pbmarilin@gmail.com"],
    ["d8a88597-fa61-4457-9b6c-5d84d60b9b96", "8128642001", "vj33586@gmail.com"],
    ["47652ea7-9044-4ab0-8cdc-5dbd76c6f0e7", "7773927609", "minasonawane09@gmail.com"],
    ["0d89f731-e5a5-4462-9fa9-d6e16be94fdc", "8425897474", "gpardeshi029@gmail.com"],
    ["be7419d7-efd2-40aa-b3d2-cfb73a28844e", "8892849548", "rr7281712@gmail.com"],
    ["3165b8ab-88d0-4be0-ab33-f9866a814b1f", "8248752307", "nelsonkumar84@gmail.com"]
]

mp = {}
for row in rows:
    mp[row[0]] = [row[1], row[2]]

for actor_id in actor_ids:
    print(actor_id, " ", mp[actor_id][0], "  ", mp[actor_id][1])

    '''The provided code defines a Python script that appears to be associating actor IDs with email and phone information. Here's what the code does:

1. It defines a class called `Info` with a constructor `__init__` that takes two parameters, `email` and `phone`, and initializes instance variables `email` and `phone` with the provided values.

2. It defines a list called `actor_ids` that contains a series of actor IDs as strings.

3. It defines a list called `rows` where each element is a list containing three items: an actor ID (as a string), a phone number, and an email address.

4. It creates a dictionary `mp` to map actor IDs to their corresponding phone numbers and email addresses. It iterates through the `rows` list and populates the dictionary with actor IDs as keys and lists containing phone numbers and email addresses as values.

5. It then iterates through the `actor_ids` list and prints the actor ID, phone number, and email address associated with each actor ID using the information stored in the `mp` dictionary.

6. The script prints this information to the console.

Regarding the script name, you can choose a name that reflects its purpose. Since it appears to be associating actor IDs with contact information, you could name it something like "actor_info.py" or "actor_id_mapping.py." Choose a name that makes it clear what the script does.'''
