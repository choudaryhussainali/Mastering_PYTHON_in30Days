"""
functions_basics.py

This file introduces the concept of functions in Python.
It covers:
1. What functions are.
2. Why we use functions.
3. How to define and call functions.
4. Function parameters and arguments (basic level).
5. Returning values.
6. Default parameter values.
7. Basic docstrings.
"""

# ------------------------------
# 1. What is a function?
# ------------------------------
# A function is a reusable block of code that performs a specific task.
# Instead of writing the same code again and again, we can put it inside a function
# and call that function whenever we need it.

# ------------------------------
# 2. How to define a function
# ------------------------------
# Syntax:
# def function_name(parameters):
#     """Docstring (optional)"""
#     # code
#     return value (optional)

# Example 1: A simple function with no parameters
def greet():
    """This function prints a greeting message."""
    print("Hello! Welcome to Python functions.")

# Calling the function
greet()

# ------------------------------
# 3. Function with parameters
# ------------------------------
# Parameters are variables that take values (arguments) when the function is called.

def greet_person(name):
    """Greets a person by their name."""
    print(f"Hello, {name}! How are you today?")

# Calling the function with an argument
greet_person("Hussain")
greet_person("Ali")

# ------------------------------
# 4. Function with return value
# ------------------------------
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result

# Calling the function and storing the result
sum_result = add_numbers(5, 7)
print("The sum is:", sum_result)

# ------------------------------
# 5. Default parameter values
# ------------------------------
def greet_with_default(name="Guest"):
    """Greets a person, using a default name if none is provided."""
    print(f"Hello, {name}!")

greet_with_default("Hussain")
greet_with_default()  # uses the default value "Guest"

# ------------------------------
# 6. Multiple parameters
# ------------------------------
def multiply_numbers(a, b, c):
    """Multiplies three numbers and returns the result."""
    return a * b * c

product = multiply_numbers(2, 3, 4)
print("Product:", product)

# ------------------------------
# 7. Why use functions?
# ------------------------------
# Functions make code:
# - Reusable (write once, use many times)
# - Organized (code is divided into small, logical sections)
# - Easier to debug (errors are isolated)
# - Easier to read and maintain

# Example: Without function → repetitive code
print("Without function:")
print("Sum:", 2 + 3)
print("Sum:", 4 + 5)
print("Sum:", 10 + 20)

# Example: With function → reusable
print("\nWith function:")
print("Sum:", add_numbers(2, 3))
print("Sum:", add_numbers(4, 5))
print("Sum:", add_numbers(10, 20))

# ------------------------------
# End of functions_basics.py
# ------------------------------
