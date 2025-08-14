"""
parameters_arguments.py

This script explains **parameters** and **arguments** in Python functions.

We will cover:
1. What parameters and arguments are.
2. Positional arguments.
3. Keyword arguments.
4. Default parameter values.
5. Mixing positional and keyword arguments.
6. Rules and best practices.

NOTE: We are not using any advanced concepts yet (like *args/**kwargs or type hints)
since they will come later.
"""

# 1. Defining parameters vs. arguments
# ------------------------------------
# Parameters: The variables you define in the function definition.
# Arguments:  The actual values you pass when calling the function.

def greet(name, message):
    """Function with two parameters: name and message."""
    print(f"Hello {name}, {message}")

# Here, 'name' and 'message' are PARAMETERS.
# Now let's call the function with ARGUMENTS.
greet("Alice", "Welcome to Python!")  # "Alice" and "Welcome to Python!" are ARGUMENTS.


# 2. Positional Arguments
# -----------------------
# These are matched to parameters in the order they appear.

def display_info(first_name, last_name):
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")

# Arguments are matched by position:
display_info("John", "Doe")  # first_name="John", last_name="Doe"


# 3. Keyword Arguments
# --------------------
# You can specify which parameter gets which value using the parameter name.

display_info(last_name="Smith", first_name="Jane")  # Order doesn't matter here.


# 4. Default Parameter Values
# ---------------------------
# You can give parameters default values, so you don’t have to provide them every time.

def introduce(name, country="Pakistan"):
    print(f"My name is {name} and I am from {country}")

introduce("Ali")  # Uses default for country
introduce("Sara", "Canada")  # Overrides default


# 5. Mixing Positional and Keyword Arguments
# ------------------------------------------
# Rule: Positional arguments must come before keyword arguments.

def student_info(name, age, city="Lahore"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Correct:
student_info("Hassan", 21)
student_info("Zara", 19, city="Karachi")

# Incorrect (will cause an error):
# student_info(name="Hassan", 21)  # ❌ SyntaxError


# 6. Summary
# ----------
# - Parameters: placeholders in function definition.
# - Arguments: actual values passed to the function.
# - Positional arguments: matched by order.
# - Keyword arguments: matched by parameter name.
# - Default values: make parameters optional.
# - Rule: Positional arguments → Keyword arguments → *args/**kwargs (later).

