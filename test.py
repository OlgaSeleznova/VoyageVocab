import json
with open('metadata.json', 'r') as file:
    data = json.load(file)
print(data)