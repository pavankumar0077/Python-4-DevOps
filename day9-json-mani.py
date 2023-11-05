import json

json_date = '{"name": "Pavan", "age":23,"city":"Hyd"}'
data = json.loads(json_date)

print(data)

print(data['name'])
print(data['age'])

data['country'] = 'India'
data['age'] = 25

print(data)


updated_json_data = json.dumps(data)
print(updated_json_data)


date = '{"name": "Pavan", "age":23,"city":"Hyd"}'

# wRITE the data to a JSON file named 'output.json'
with open('output.json', 'w') as file:
    json.dump(data, file)

# READing from json file
with open('output.json', 'r') as file:
    xyz = json.load(file)

print(xyz)