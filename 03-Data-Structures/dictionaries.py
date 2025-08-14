# dictionaries.py
# ----------------
# In this file, we will learn about **Dictionaries** in Python from scratch.
# A dictionary is a data structure in Python that stores data in key-value pairs.
# You can think of it like a real-life dictionary: a word (key) and its meaning (value).

# ----------------------------------------------------------------------
# 1. Creating Dictionaries
# ----------------------------------------------------------------------

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary with some data
student = {
    "name": "Ali",
    "age": 21,
    "course": "Computer Science"
}
print("Student dictionary:", student)

# ----------------------------------------------------------------------
# 2. Accessing Dictionary Values
# ----------------------------------------------------------------------

# Accessing value by key
print("Student's name:", student["name"])
print("Student's age:", student["age"])

# Using get() method (does not give an error if key doesn't exist)
print("Course:", student.get("course"))
print("Hobby (not present):", student.get("hobby", "Not Found"))

# ----------------------------------------------------------------------
# 3. Adding & Updating Dictionary Items
# ----------------------------------------------------------------------

# Adding a new key-value pair
student["hobby"] = "Reading"
print("After adding hobby:", student)

# Updating existing value
student["age"] = 22
print("After updating age:", student)

# ----------------------------------------------------------------------
# 4. Removing Items from Dictionary
# ----------------------------------------------------------------------

# Using pop() - removes item by key and returns its value
removed_value = student.pop("hobby")
print("Removed hobby:", removed_value)
print("After pop:", student)

# Using del keyword
del student["course"]
print("After deleting course:", student)

# Using clear() - removes all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After clear:", temp_dict)

# ----------------------------------------------------------------------
# 5. Looping Through a Dictionary
# ----------------------------------------------------------------------

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

# Loop through keys
print("\nLooping through keys:")
for key in car:
    print(key)

# Loop through values
print("\nLooping through values:")
for value in car.values():
    print(value)

# Loop through key-value pairs
print("\nLooping through key-value pairs:")
for key, value in car.items():
    print(key, ":", value)

# ----------------------------------------------------------------------
# 6. Checking if a Key Exists
# ----------------------------------------------------------------------
if "brand" in car:
    print("\n'brand' key exists in car dictionary")

if "color" not in car:
    print("'color' key does not exist in car dictionary")

# ----------------------------------------------------------------------
# 7. Dictionary Length
# ----------------------------------------------------------------------
print("\nNumber of items in car dictionary:", len(car))

# ----------------------------------------------------------------------
# 8. Nested Dictionaries
# ----------------------------------------------------------------------
students = {
    "student1": {"name": "Ali", "age": 21},
    "student2": {"name": "Sara", "age": 22}
}

print("\nNested dictionary example:")
for student_key, student_info in students.items():
    print(student_key, "->", student_info)

# ----------------------------------------------------------------------
# 9. Dictionary Methods Summary
# ----------------------------------------------------------------------
# keys()      -> Returns all keys
# values()    -> Returns all values
# items()     -> Returns all key-value pairs
# get(key)    -> Returns value for given key (or default if not found)
# pop(key)    -> Removes item with given key
# clear()     -> Removes all items
# update()    -> Updates dictionary with another dictionary

print("\nKeys:", car.keys())
print("Values:", car.values())
print("Items:", car.items())

# Example of update()
car.update({"color": "White", "year": 2021})
print("After update:", car)
