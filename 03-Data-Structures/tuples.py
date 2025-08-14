# tuples.py
# ------------------------
# Topic: Tuples in Python
# ------------------------
# In Python, a tuple is an ordered, immutable (unchangeable) collection of items.
# You can store different types of values inside a tuple (integers, strings, floats, etc.).
# Once a tuple is created, you cannot modify, add, or remove its elements.
# Tuples are written inside round brackets ( ).

# 1. Creating a Tuple
fruits = ("apple", "banana", "cherry")
print("Tuple of fruits:", fruits)

# A tuple can contain different data types
mixed_tuple = (10, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# You can also create a tuple without parentheses (comma-separated values)
numbers = 1, 2, 3, 4
print("Tuple without parentheses:", numbers)

# 2. Creating a Tuple with One Item
# IMPORTANT: Add a comma after the single item, otherwise it will NOT be a tuple.
one_item_tuple = ("apple",)
print("One item tuple:", one_item_tuple)

# If you do not add a comma, it will be just a string, not a tuple
not_a_tuple = ("apple")
print("Not a tuple (it's a string):", type(not_a_tuple))

# 3. Accessing Tuple Items (Indexing)
# Index starts from 0
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexing: -1 means last element, -2 means second last, etc.
print("Last fruit:", fruits[-1])

# 4. Slicing Tuples
# Slicing works just like lists
print("First two fruits:", fruits[0:2])
print("All fruits from index 1 onwards:", fruits[1:])

# 5. Tuple Immutability
# Tuples cannot be changed after creation
# Example: fruits[0] = "mango"  # ❌ This will give an error

# 6. Looping Through a Tuple
print("\nLooping through fruits tuple:")
for fruit in fruits:
    print(fruit)

# 7. Tuple Length
print("Number of fruits:", len(fruits))

# 8. Nested Tuples
nested_tuple = (("red", "green"), ("circle", "square"))
print("Nested tuple:", nested_tuple)
print("Accessing nested item:", nested_tuple[0][1])  # 'green'

# 9. Tuple Packing and Unpacking
# Packing: putting values into a tuple
person = ("Ali", 21, "Pakistan")

# Unpacking: extracting values from a tuple into variables
name, age, country = person
print("\nName:", name)
print("Age:", age)
print("Country:", country)

# 10. Tuple Methods
# Tuples have very few methods because they are immutable

# count(value) → returns number of times the value appears in tuple
numbers_tuple = (1, 2, 2, 3, 2, 4)
print("Count of 2 in numbers_tuple:", numbers_tuple.count(2))

# index(value) → returns first index of the value
print("Index of 3 in numbers_tuple:", numbers_tuple.index(3))

# 11. Why Use Tuples Instead of Lists?
# - Tuples are faster than lists
# - Tuples are immutable, so data is safe from accidental changes
# - Good for storing fixed data that should not change

# Example: Coordinates (fixed values)
coordinates = (35.6895, 139.6917)  # Latitude & Longitude
print("\nCoordinates:", coordinates)

# End of tuples.py
