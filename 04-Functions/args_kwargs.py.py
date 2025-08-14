# args_kwargs.py
# ==========================
# Topic: *args and **kwargs in Python
# ==========================
# In Python, sometimes we don’t know beforehand how many arguments will be passed to a function.
# For such situations, Python provides special symbols:
#   *args   → for a variable number of positional arguments (tuple)
#   **kwargs → for a variable number of keyword arguments (dictionary)

# ---------------------------------------------------------
# 1. Using *args (Arbitrary Positional Arguments)
# ---------------------------------------------------------
# *args allows us to pass any number of positional arguments to a function.
# Inside the function, these arguments are stored in a tuple.

def sum_numbers(*args):
    """Returns the sum of all numbers passed as arguments."""
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers:", sum_numbers(2, 4, 6))        # 12
print("Sum of numbers:", sum_numbers(10, 20, 30, 40)) # 100
print("Sum of numbers:", sum_numbers())               # 0 (no arguments)


# ---------------------------------------------------------
# 2. Using **kwargs (Arbitrary Keyword Arguments)
# ---------------------------------------------------------
# **kwargs allows us to pass any number of keyword arguments to a function.
# Inside the function, these are stored in a dictionary.

def print_student_info(**kwargs):
    """Prints student details passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nStudent Info:")
print_student_info(name="Ali", age=21, course="Python Basics")

# ---------------------------------------------------------
# 3. Combining *args and **kwargs
# ---------------------------------------------------------
# We can use both in the same function.
# Order in the function definition must be:
#   1. Normal parameters
#   2. *args
#   3. **kwargs

def display_data(greeting, *args, **kwargs):
    """Displays a greeting, followed by positional and keyword data."""
    print(greeting)
    
    print("\nPositional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nDisplay Data Example:")
display_data(
    "Hello Everyone!",
    1, 2, 3,
    name="Hussain",
    topic="args and kwargs",
    difficulty="Easy"
)

# ---------------------------------------------------------
# 4. Practical Example: Building a Shopping List
# ---------------------------------------------------------
def shopping_list(*items, **prices):
    """Shows the items and their prices."""
    print("\nShopping Items:")
    for item in items:
        print(f"- {item}")
    
    print("\nItem Prices:")
    for item, price in prices.items():
        print(f"{item}: Rs.{price}")

shopping_list(
    "Milk", "Bread", "Eggs",
    Milk=150, Bread=80, Eggs=200
)

# ==========================
# Summary:
#   *args   → stores positional arguments as a tuple.
#   **kwargs → stores keyword arguments as a dictionary.
# Useful when number of inputs is unknown beforehand.
# ==========================
