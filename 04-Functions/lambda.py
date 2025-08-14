"""
lambda.py

This file explains and demonstrates the use of lambda functions in Python.

A lambda function is a small, anonymous function that can have any number of arguments
but can only contain a single expression. It’s useful when you need a short function
and don’t want to formally define it using 'def'.

Syntax:
    lambda arguments: expression

Important:
- Lambdas can have multiple arguments but only one expression.
- They return the result of that single expression automatically.
- Mostly used for short, throwaway functions, or as arguments to other functions like 'map', 'filter', or 'sorted'.
"""

# ------------------------------------
# 1. Basic Lambda Example
# ------------------------------------
# A lambda function to add 10 to a number
add_ten = lambda x: x + 10
print("Add 10 to 5:", add_ten(5))  # Output: 15

# A lambda function to multiply two numbers
multiply = lambda a, b: a * b
print("Multiply 4 and 6:", multiply(4, 6))  # Output: 24


# ------------------------------------
# 2. Using Lambda inside another function
# ------------------------------------
def apply_operation(x, func):
    """
    Applies a given function to the value x.
    """
    return func(x)

result = apply_operation(7, lambda num: num ** 2)  # Square the number
print("Square of 7:", result)  # Output: 49


# ------------------------------------
# 3. Sorting with Lambda
# ------------------------------------
# Suppose we have a list of tuples (name, age)
people = [
    ("Ali", 25),
    ("Hassan", 30),
    ("Zain", 22)
]

# Sort by age using a lambda function as the key
sorted_people = sorted(people, key=lambda person: person[1])
print("Sorted by age:", sorted_people)


# ------------------------------------
# 4. Using Lambda with filter()
# ------------------------------------
# Get only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4, 6]


# ------------------------------------
# 5. Using Lambda with map()
# ------------------------------------
# Double each number in the list
doubled = list(map(lambda n: n * 2, numbers))
print("Doubled numbers:", doubled)  # Output: [2, 4, 6, 8, 10, 12]


# ------------------------------------
# 6. Using Lambda with reduce()
# ------------------------------------
from functools import reduce

# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)  # Output: 720


# ------------------------------------
# Key Points Recap
# ------------------------------------
"""
- Lambda functions are anonymous functions defined with 'lambda' keyword.
- Syntax: lambda args: expression
- Automatically return the result of the expression.
- Best used for short, simple operations.
- Commonly used with functions like map(), filter(), reduce(), or as sorting keys.
"""
