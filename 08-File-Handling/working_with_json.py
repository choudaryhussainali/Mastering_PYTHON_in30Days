"""
working_with_json.py

This file demonstrates how to work with JSON (JavaScript Object Notation) in Python.
It includes:
1. Reading JSON from a string or file
2. Writing JSON to a file
3. Converting Python objects to JSON (Serialization)
4. Converting JSON to Python objects (Deserialization)
5. Pretty printing JSON
6. Customizing serialization (e.g., handling datetime)
"""

import json
from datetime import datetime

# ---------------------------
# 1. JSON BASICS
# ---------------------------

# Python Dictionary (can be converted to JSON)
person_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# ---------------------------
# 2. Convert Python object to JSON string
# ---------------------------
person_json_str = json.dumps(person_dict)
print("JSON String:\n", person_json_str)

# ---------------------------
# 3. Pretty Print JSON
# ---------------------------
pretty_json_str = json.dumps(person_dict, indent=4)
print("\nPretty JSON:\n", pretty_json_str)

# ---------------------------
# 4. Save JSON to file
# ---------------------------
with open("person.json", "w") as file:
    json.dump(person_dict, file, indent=4)
print("\nJSON data written to 'person.json'")

# ---------------------------
# 5. Read JSON from file
# ---------------------------
with open("person.json", "r") as file:
    data_from_file = json.load(file)
print("\nData read from 'person.json':\n", data_from_file)

# ---------------------------
# 6. Convert JSON string to Python object
# ---------------------------
json_string = '{"name": "Bob", "age": 25, "skills": ["Java", "C++"]}'
python_obj = json.loads(json_string)
print("\nPython Object from JSON string:\n", python_obj)

# ---------------------------
# 7. Handling datetime in JSON
# ---------------------------
def datetime_serializer(obj):
    """Custom serializer for datetime objects."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

data_with_date = {
    "event": "Conference",
    "date": datetime.now()
}

# Serialize with custom function
json_with_date = json.dumps(data_with_date, default=datetime_serializer, indent=4)
print("\nJSON with datetime:\n", json_with_date)

# ---------------------------
# 8. Deserialize datetime from JSON
# ---------------------------
def datetime_parser(dct):
    """Custom parser for datetime strings."""
    for key, value in dct.items():
        if key == "date":
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

json_string_with_date = json_with_date
parsed_data_with_date = json.loads(json_string_with_date, object_hook=datetime_parser)
print("\nPython object with datetime restored:\n", parsed_data_with_date)
print("Type of 'date':", type(parsed_data_with_date["date"]))

# ---------------------------
# 9. Summary
# ---------------------------
"""
Key Functions:
--------------
json.dumps(obj, **kwargs)  -> Converts Python object to JSON string
json.dump(obj, file, **kwargs)  -> Writes Python object as JSON to file
json.loads(json_str)  -> Converts JSON string to Python object
json.load(file)  -> Reads JSON from file into Python object

Common kwargs:
--------------
indent     -> pretty print JSON
default    -> function for serializing non-default types (e.g., datetime)
object_hook -> function for custom decoding
"""

