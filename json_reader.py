import json
with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)

type(json_data)

for key, value in json_data.items():
    print(key + ':', value)
