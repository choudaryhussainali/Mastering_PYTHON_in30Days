# Day 1: Introduction to Python
# File: introduction.py

"""
Welcome to Day 1 of "Mastering Python in 30 Days"!

In this file, we will:
- Understand what Python is and why it is popular
- Learn how to write and run our first Python program
- Cover Python's basic syntax, indentation, and comments
"""

# -------------------------------
# 1. What is Python?
# -------------------------------
# Python is a high-level, interpreted programming language.
# It is known for its simple syntax, readability, and vast library support.
# Python is used in:
# - Web Development
# - Data Science & Machine Learning
# - Automation
# - Game Development
# - IoT and more...

# -------------------------------
# 2. Writing our first Python program
# -------------------------------

print("Hello, World!")  # This will display text on the screen

# -------------------------------
# 3. Comments in Python
# -------------------------------
# Single-line comment: Starts with "#"
"""
Multi-line comment: Written between triple quotes
They are often used for documentation purposes.
"""

# -------------------------------
# 4. Python Syntax and Indentation
# -------------------------------
# Python uses indentation (spaces or tabs) to define code blocks.
# Unlike other languages that use curly braces { }, Python relies on indentation.

if True:
    print("This is indented properly.")
    print("Python requires consistent indentation.")
# If indentation is incorrect, Python will throw an IndentationError.

# -------------------------------
# 5. Variables and Data Types
# -------------------------------
# Variables store data values.
# Python is dynamically typed, meaning you don't need to declare variable types.

name = "Hussain"      # String
age = 22              # Integer
height = 5.9          # Float
is_student = True     # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# -------------------------------
# 6. Checking Data Types
# -------------------------------
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))# <class 'bool'>

# -------------------------------
# 7. Taking User Input
# -------------------------------
# Uncomment the following lines to try taking input from the user:
# user_name = input("Enter your name: ")
# print("Hello,", user_name)

# -------------------------------
# 8. Summary
# -------------------------------
"""
Today, you learned:
1. What Python is and where it is used
2. How to print output
3. Single-line and multi-line comments
4. Python syntax & indentation rules
5. Variables and data types
6. How to check a variable's data type
7. Taking input from the user

Tomorrow, we will dive into Python's operators and expressions!
"""
