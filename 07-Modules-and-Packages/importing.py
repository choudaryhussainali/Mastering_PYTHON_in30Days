"""
importing.py
--------------------
This file explains EVERYTHING about importing in Python — step by step.

IMPORTING in Python means bringing code (functions, classes, variables) from 
other Python files or libraries into your current program.

WHY use imports?
- Avoid rewriting the same code again and again.
- Organize your project into smaller files/modules.
- Use built-in and third-party libraries.

====================================================================
1. BASIC IMPORT
====================================================================
"""

# Example: Importing the entire math module
import math

print("Square root of 16 is:", math.sqrt(16))  # Access functions via math.<function>

"""
Note:
- You must use 'module_name.function_name' unless you import differently.
- Importing the entire module loads ALL functions/variables from it.
"""

# Example: Importing a specific function
from math import sqrt

print("Square root of 25 is:", sqrt(25))  # Now we don't need 'math.'

# Example: Importing multiple specific things
from math import pow, pi
print("2 to the power 3:", pow(2, 3))
print("Value of pi:", pi)

"""
====================================================================
2. IMPORT WITH ALIAS
====================================================================
You can rename modules/functions to make them shorter or avoid name conflicts.
"""

import numpy as np  # Common alias for NumPy
print("NumPy array:", np.array([1, 2, 3]))

from math import factorial as fact
print("Factorial of 5 is:", fact(5))

"""
====================================================================
3. IMPORTING CUSTOM MODULES (from your own files)
====================================================================
- Any Python file (.py) is a module.
- To import it, it must be in the same folder or in Python's search path.
"""

# Let's say we have a file named `my_module.py` with:
# def greet(name): return f"Hello {name}!"

import my_module  # This imports the whole file
print(my_module.greet("Hussain"))

from my_module import greet
print(greet("Ali"))

"""
====================================================================
4. IMPORTING FROM A PACKAGE
====================================================================
- A package is a folder with multiple Python files and an __init__.py file.
- Example structure:
    my_package/
        __init__.py
        module1.py
        module2.py
"""

# Example:
# from my_package import module1
# from my_package.module2 import some_function

"""
====================================================================
5. RELATIVE IMPORTS (Inside Packages)
====================================================================
- Used within a package to import from sibling/parent modules.
- Syntax:
    from . import sibling_module     # same folder
    from .. import parent_module     # parent folder
"""

"""
====================================================================
6. IMPORTING EVERYTHING (*)
====================================================================
- You can use * to import all public names from a module.
- WARNING: Not recommended because it can overwrite variables unintentionally.
"""

from math import *  # Now all math functions are available directly
print(sin(pi / 2))  # Works without 'math.'

"""
====================================================================
7. DYNAMIC IMPORTING (importlib)
====================================================================
You can import modules during runtime based on conditions.
"""

import importlib

module_name = "math"
math_module = importlib.import_module(module_name)
print("Dynamic import sqrt:", math_module.sqrt(36))

"""
====================================================================
8. CONDITIONAL IMPORTS
====================================================================
- Sometimes you import modules only if a certain condition is met.
"""

if True:
    import random
    print("Random number:", random.randint(1, 10))

"""
====================================================================
9. RELOADING MODULES
====================================================================
If a module changes during runtime, you can reload it without restarting Python.
"""

import importlib
importlib.reload(my_module)

"""
====================================================================
10. PYTHON'S MODULE SEARCH PATH
====================================================================
Python looks for modules in:
1. Current working directory
2. PYTHONPATH environment variable
3. Standard library directories
4. Site-packages (for installed libraries)
"""

import sys
print("Python search paths:", sys.path)

"""
====================================================================
11. BEST PRACTICES
====================================================================
- Import only what you need (saves memory & improves readability).
- Use aliases for long names or popular conventions (like np for numpy).
- Avoid wildcard imports (*).
- Keep imports at the top of your file.
"""

print("\n--- End of importing.py demonstration ---")
