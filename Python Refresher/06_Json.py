import json

py_obj = {"name" : "Iman",
       "age" : 21,
       "city" : "Kolkata",
       }

json_str = json.dumps(py_obj) # dumps convert a python dict to a json
print(type(json_str))
print(json_str)

python_dict = json.loads(json_str) # loads convert a json to a python dict
print(type(python_dict))
print(python_dict)

with open("data.json", "w") as f:
    json.dump(py_obj, f) # Convert the Python object (py_obj) into JSON format and write it directly into the file