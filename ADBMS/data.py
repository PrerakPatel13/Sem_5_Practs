import json
with open("data.json",'r') as file:
    data=json.load(file)

for record in data:
    print("Name:",record["name"])
    print("Location:",record["location"])
    print("Country:",record["country"])
    print()