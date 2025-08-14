"""
modules_basics.py
=================
In Python, a MODULE is simply a file containing Python code (functions, classes, variables).
You can import this file into another Python file to reuse its code.

Why use modules?
----------------
✅ To organize code into separate files.
✅ To reuse code without rewriting it.
✅ To improve maintainability and readability.
✅ To avoid huge files with everything in one place.

📌 Built-in modules → Provided by Python (e.g., math, random, datetime)
📌 User-defined modules → Created by you
📌 External modules → Installed using pip (e.g., requests, pandas)
"""

# -----------------------------
# 1. IMPORTING A BUILT-IN MODULE
# -----------------------------

import math  # math module provides mathematical functions

print("Square root of 16:", math.sqrt(16))
print("Value of Pi:", math.pi)
print("Factorial of 5:", math.factorial(5))


# -----------------------------
# 2. IMPORTING WITH ALIAS
# -----------------------------
import random as rnd  # alias for shorter name

print("Random number between 1 and 10:", rnd.randint(1, 10))


# -----------------------------
# 3. IMPORTING SPECIFIC FUNCTIONS
# -----------------------------
from datetime import date, datetime

today = date.today()
now = datetime.now()

print("Today's date:", today)
print("Current time:", now)


# -----------------------------
# 4. USER-DEFINED MODULE EXAMPLE
# -----------------------------
# Step 1: Create a file named `my_module.py` with some code:
"""
# my_module.py
def greet(name):
    return f"Hello, {name}!"

pi_value = 3.14159
"""

# Step 2: Import and use it
# from my_module import greet, pi_value
# print(greet("Hussain"))
# print("Pi value from my_module:", pi_value)


# -----------------------------
# 5. RENAMING IMPORTED FUNCTIONS
# -----------------------------
# from math import factorial as fact
# print("Factorial of 6:", fact(6))


# -----------------------------
# 6. USING ALL FUNCTIONS FROM A MODULE (Not Recommended)
# -----------------------------
# from math import *
# print(sqrt(25))  # Works, but pollutes namespace


# -----------------------------
# 7. CHECKING ALL ATTRIBUTES/FUNCTIONS IN A MODULE
# -----------------------------
print("\nAll attributes in math module:")
print(dir(math))


# -----------------------------
# 8. RELOADING A MODULE (Advanced)
# -----------------------------
# Sometimes useful if you modify a module without restarting Python
# import importlib
# import my_module
# importlib.reload(my_module)


# -----------------------------
# 9. THE __name__ VARIABLE
# -----------------------------
# Each Python file has a special variable __name__.
# If the file is run directly, __name__ == "__main__".
# If imported, __name__ == module name.

def test_func():
    print("test_func is running!")

if __name__ == "__main__":
    print("\nRunning modules_basics.py directly")
    test_func()
else:
    print("\nmodules_basics.py has been imported")
