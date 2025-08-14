# Variables.py
# ==============================================
# Python Basics - Variables
# Mastering Python in 30 Days
# ==============================================

# ---------------------------
# 1. Introduction to Variables
# ---------------------------
# A variable is a named location in memory used to store data.
# In Python, you don't need to declare the type of a variable explicitly.
# The type is inferred from the value assigned to it.

# Example:
x = 10               # Integer
name = "Hussain"     # String
price = 99.99        # Float
is_active = True     # Boolean

print("x:", x)
print("name:", name)
print("price:", price)
print("is_active:", is_active)

# ---------------------------
# 2. Variable Naming Rules
# ---------------------------
# ✅ Must start with a letter or underscore (_)
# ✅ Can contain letters, numbers, and underscores
# ❌ Cannot start with a number
# ❌ Cannot contain special characters (!, @, #, $, etc.)
# ❌ Cannot use Python keywords (like if, else, for, etc.)

# Valid examples:
_user_name = "Ali"
age2 = 20
product_price = 120.5

# Invalid examples (will cause syntax error if uncommented):
# 2age = 25
# my-name = "John"
# for = "loop"

# ---------------------------
# 3. Dynamic Typing
# ---------------------------
# Python is dynamically typed, so you can reassign variables to different types.
a = 10       # int
a = "Hello"  # now a string
a = 3.14     # now a float

# ---------------------------
# 4. Multiple Assignments
# ---------------------------
# Assign multiple values to multiple variables:
x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3

# Assign same value to multiple variables:
p = q = r = 0
print(p, q, r)  # Output: 0 0 0

# ---------------------------
# 5. Constants
# ---------------------------
# Python doesn't have true constants, but by convention, constants are written in UPPERCASE.
PI = 3.14159
MAX_USERS = 100

# ---------------------------
# 6. Type Casting
# ---------------------------
# You can convert variables from one type to another.
num_str = "100"
num_int = int(num_str)  # String to int
num_float = float(num_str)  # String to float
int_str = str(200)  # Int to string

print(num_int, type(num_int))
print(num_float, type(num_float))
print(int_str, type(int_str))

# ---------------------------
# 7. Deleting Variables
# ---------------------------
# Use del to delete a variable
temp = "temporary value"
del temp
# print(temp)  # This will raise an error because temp is deleted

# ---------------------------
# 8. Checking Variable Type
# ---------------------------
value = 42
print(type(value))       # <class 'int'>
print(isinstance(value, int))  # True

# ---------------------------
# 9. Variable Scope
# ---------------------------
# Global variable: declared outside any function
# Local variable: declared inside a function

global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)         # Accessible here
    print(global_var)        # Accessible here because global

my_function()
# print(local_var)  # ❌ Will cause error, local_var not accessible here

# Modifying global variables inside a function
count = 0

def increment():
    global count
    count += 1

increment()
print("Count after increment:", count)

# ---------------------------
# 10. Best Practices
# ---------------------------
# ✅ Use descriptive variable names
# ✅ Follow snake_case for variable names
# ✅ Use UPPERCASE for constants
# ✅ Avoid single-letter variable names (except in loops)
# ✅ Keep variable names meaningful

# Example:
student_name = "Hussain Ali"
student_age = 22
course_enrolled = "Python Programming"

print(f"Student: {student_name}, Age: {student_age}, Course: {course_enrolled}")
