import json

data = {
    "name": "Beast",
    "age": 30
}

json_string = json.dumps(data)
print(type(json_string))