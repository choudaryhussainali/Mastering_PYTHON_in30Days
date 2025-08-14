"""
comments.py
------------
This file explains and demonstrates how to use comments in Python in detail.

Comments in Python are non-executable lines in your code. They are ignored by the Python interpreter 
and are used to explain, clarify, or document the code for human readers.

Python supports:
1. Single-line comments
2. Multi-line comments (using multiple # or docstrings for documentation)
3. Inline comments

Why are comments important?
---------------------------
- Make code more readable.
- Explain logic and purpose of code.
- Help in debugging and revisiting code later.
- Facilitate teamwork in large projects.
"""

# ----------------------------
# 1. Single-line Comments
# ----------------------------
# This is a single-line comment.
# You use the '#' symbol at the start of the comment.
# The Python interpreter ignores everything after '#'.

print("Hello, World!")  # This prints a greeting message


# ----------------------------
# 2. Inline Comments
# ----------------------------
# Inline comments appear on the same line as code.
# Keep inline comments short and relevant.

x = 10  # Initializing variable x with value 10
y = 5   # Initializing variable y with value 5

# Adding two numbers and printing the result
print(x + y)  # Expected output: 15


# ----------------------------
# 3. Multi-line Comments
# ----------------------------
# Python does not have a specific multi-line comment syntax like some languages.
# You can create multi-line comments by:
#    - Using multiple single-line comments (preferred for real comments)
#    - Using triple quotes (''' or """), usually for docstrings, but can also be used for block comments

# Example of multi-line using multiple single-line comments:
# This code block calculates
# the sum of two numbers and prints the result.

a = 7
b = 3
print(a + b)


# Example of multi-line using triple quotes:
"""
This is a multi-line comment using triple double-quotes.
The Python interpreter technically treats this as a multi-line string.
If it is not assigned to any variable or used in the code, it acts like a comment.
However, using triple quotes for comments is discouraged unless used as docstrings.
"""

'''
This is another example using triple single-quotes.
Again, use this primarily for documentation (docstrings).
'''


# ----------------------------
# 4. Docstrings (Documentation Strings)
# ----------------------------
# Docstrings are used to document functions, classes, and modules.
# They are enclosed in triple quotes and are accessible at runtime using __doc__.

def greet(name):
    """
    This function greets the person whose name is provided.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}!")

# Printing the docstring of the greet function
print(greet.__doc__)


# ----------------------------
# Best Practices for Comments
# ----------------------------
# 1. Keep comments concise and relevant.
# 2. Do not state the obvious:
#    ❌ x = x + 1  # Add 1 to x
# 3. Update comments if code changes.
# 4. Use comments to explain *why*, not just *what*.
# 5. Follow the PEP 8 guidelines:
#    - One space after '#'
#    - Limit comment lines to 72 characters

# Example of bad vs good comment:
# ❌ Bad:  # Increment x by 1
# ✅ Good: # Increase counter to move to the next step in the loop
