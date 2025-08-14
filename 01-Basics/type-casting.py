# typecasting.py
# ================================================
# Topic: Typecasting in Python
# ================================================
# Typecasting (also called type conversion) means converting one data type into another.
# Python provides both:
#   1. Implicit Typecasting (Type Conversion)
#   2. Explicit Typecasting (Type Casting)
# Let's go through both in detail.

# ------------------------------------------------
# 1. Implicit Typecasting
# ------------------------------------------------
# This happens automatically when Python converts a smaller data type into a larger data type
# to avoid data loss.

print("----- Implicit Typecasting Example -----")
integer_number = 10       # int
float_number = 5.5        # float

# int is automatically converted to float in arithmetic operation
result = integer_number + float_number
print("Type of result:", type(result))  # Output: <class 'float'>
print("Value of result:", result)       # Output: 15.5


# ------------------------------------------------
# 2. Explicit Typecasting
# ------------------------------------------------
# This is when we manually convert one data type into another using Python's built-in functions.
# Common typecasting functions:
#   int(), float(), str(), bool(), list(), tuple(), set(), dict(), complex()

print("\n----- Explicit Typecasting Examples -----")

# a) int() - Convert to integer (decimal part removed, no rounding)
num_float = 9.8
num_int = int(num_float)
print("Float to int:", num_int)  # Output: 9

# b) float() - Convert to float
num_string = "15"
num_float2 = float(num_string)
print("String to float:", num_float2)  # Output: 15.0

# c) str() - Convert to string
num_int2 = 100
num_str = str(num_int2)
print("Integer to string:", num_str)   # Output: "100"
print("Type:", type(num_str))          # Output: <class 'str'>

# d) bool() - Convert to boolean
print(bool(0))       # False (0 means False)
print(bool(1))       # True
print(bool(""))      # False (empty string means False)
print(bool("Hi"))    # True (non-empty string means True)

# e) list(), tuple(), set()
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print("Tuple to List:", list_data)     # Output: [1, 2, 3]

list_data2 = [4, 5, 6]
tuple_data2 = tuple(list_data2)
print("List to Tuple:", tuple_data2)   # Output: (4, 5, 6)

list_with_duplicates = [1, 2, 2, 3]
set_data = set(list_with_duplicates)
print("List to Set:", set_data)        # Output: {1, 2, 3}

# f) complex() - Convert to complex number
complex_num = complex(5)        # Imaginary part will be 0
print("Complex Number:", complex_num)  # Output: (5+0j)

complex_num2 = complex(5, 6)    # Both real and imaginary parts
print("Complex Number (Real + Imag):", complex_num2)  # Output: (5+6j)


# ------------------------------------------------
# 3. Typecasting Errors
# ------------------------------------------------
# Not all conversions are valid.
print("\n----- Typecasting Errors -----")
try:
    invalid_conversion = int("Hello")  # Cannot convert non-numeric string to int
except ValueError as e:
    print("Error:", e)

try:
    invalid_conversion2 = float("Python")  # Cannot convert non-numeric string to float
except ValueError as e:
    print("Error:", e)


# ------------------------------------------------
# 4. Practical Example
# ------------------------------------------------
# Example: Taking numeric input from user and adding 10

print("\n----- Practical Example -----")
user_input = "25"  # Imagine this is from input()
# By default, input is string → Convert to int
user_number = int(user_input)
print("Original number:", user_number)
print("After adding 10:", user_number + 10)

# ------------------------------------------------
# Summary:
# - Implicit typecasting is automatic (Python upgrades smaller data type to larger one)
# - Explicit typecasting is manual using type functions
# - Not all conversions are possible; invalid conversions raise errors
# ------------------------------------------------
