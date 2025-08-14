"""
data_types.py
--------------
This file covers ALL important Python data types with explanations and examples.
It is designed for learning purposes in your "Mastering Python in 30 Days" repo.
"""

# =============================
# 1. NUMBERS
# =============================

# Integers (int) - Whole numbers without a decimal point
age = 25
temperature = -5
print("Integer examples:", age, temperature)

# Float - Numbers with decimal points
pi = 3.14159
gpa = 3.8
print("Float examples:", pi, gpa)

# Complex numbers - Numbers with real and imaginary parts
complex_num = 2 + 3j
print("Complex number:", complex_num, "Real:", complex_num.real, "Imag:", complex_num.imag)


# =============================
# 2. BOOLEAN
# =============================

# Boolean values: True or False
is_python_fun = True
is_raining = False
print("Booleans:", is_python_fun, is_raining)

# Booleans are internally integers (True=1, False=0)
print("True as int:", int(True), "False as int:", int(False))


# =============================
# 3. STRINGS (str)
# =============================

# Strings - Sequence of characters
name = "Hussain"
greeting = 'Hello'
multiline = """This is
a multiline
string."""
print("Strings:", name, greeting, multiline)

# String indexing and slicing
print("First letter of name:", name[0])
print("Last letter of name:", name[-1])
print("First three letters:", name[:3])
print("Every second letter:", name[::2])

# String methods
text = "  python programming  "
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Strip:", text.strip())
print("Replace:", text.replace("python", "Java"))
print("Find 'prog':", text.find("prog"))

# f-Strings for formatting
age = 21
print(f"My name is {name} and I am {age} years old.")


# =============================
# 4. LISTS
# =============================

# Lists - Ordered, mutable collection
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("First fruit:", fruits[0])
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
fruits[1] = "mango"
print("After change:", fruits)
print("Slice:", fruits[:2])

# List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)


# =============================
# 5. TUPLES
# =============================

# Tuples - Ordered, immutable collection
coordinates = (10.5, 20.8)
print("Tuple:", coordinates)
print("First coordinate:", coordinates[0])


# =============================
# 6. SETS
# =============================

# Sets - Unordered, no duplicates
unique_numbers = {1, 2, 3, 3, 2}
print("Set (no duplicates):", unique_numbers)
unique_numbers.add(4)
print("After add:", unique_numbers)
unique_numbers.remove(2)
print("After remove:", unique_numbers)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)


# =============================
# 7. DICTIONARIES
# =============================

# Dictionaries - Key-value pairs
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print("Dictionary:", student)
print("Name:", student["name"])
student["grade"] = "A"
print("After adding grade:", student)
del student["age"]
print("After deleting age:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print("Squares dict:", squares_dict)


# =============================
# 8. NONE TYPE
# =============================

# NoneType - Represents absence of a value
nothing = None
print("None example:", nothing)
print("Type of None:", type(nothing))
