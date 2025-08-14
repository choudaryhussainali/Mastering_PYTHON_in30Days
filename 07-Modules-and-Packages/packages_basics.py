"""
packages_basics.py
===================

This file explains **Python Packages** in detail with theory, examples, and best practices.
It is part of the "Modules and Packages" folder in your Python learning repo.

-------------------------------------------------------
1. What is a Package?
-------------------------------------------------------
- A **package** is a way of organizing related Python modules into a single directory.
- Technically, a package is just a **folder containing a special file named `__init__.py`**.
- Packages allow you to group related code into a hierarchical structure.

Example folder structure:
my_project/
    my_package/
        __init__.py       # Marks this folder as a package
        module1.py
        module2.py

You can then use:
    import my_package.module1
    from my_package import module2

-------------------------------------------------------
2. Why use Packages?
-------------------------------------------------------
✅ Better organization for large projects.
✅ Avoids name conflicts between modules.
✅ Makes code reusable and maintainable.
✅ Allows hierarchical imports (nested folders).

-------------------------------------------------------
3. Creating and Using a Package
-------------------------------------------------------
Step 1: Create a folder for the package.
Step 2: Add an empty `__init__.py` file.
Step 3: Add Python modules (.py files) inside.

Example:
math_tools/
    __init__.py
    addition.py
    subtraction.py

addition.py:
    def add(a, b):
        return a + b

subtraction.py:
    def subtract(a, b):
        return a - b

main.py (outside package):
    import math_tools.addition
    print(math_tools.addition.add(3, 2))

Or:
    from math_tools.addition import add
    print(add(3, 2))

-------------------------------------------------------
4. __init__.py
-------------------------------------------------------
- This file can be empty OR can include initialization code for the package.
- You can also define what should be imported when someone uses:
    from my_package import *

Example `__init__.py`:
    from .addition import add
    from .subtraction import subtract

    __all__ = ['add', 'subtract']

-------------------------------------------------------
5. Nested Packages
-------------------------------------------------------
Packages can contain other packages (sub-packages).

Example:
my_project/
    data_tools/
        __init__.py
        cleaners/
            __init__.py
            text_cleaner.py
        processors/
            __init__.py
            number_processor.py

Import example:
    from data_tools.cleaners.text_cleaner import clean_text

-------------------------------------------------------
6. Import Styles in Packages
-------------------------------------------------------
1️⃣ Absolute Import:
    from my_package.module1 import function1

2️⃣ Relative Import:
    from .module1 import function1   # Same directory
    from ..subpackage.module2 import function2  # Parent directory

⚠ Relative imports only work inside a package (not from main script).

-------------------------------------------------------
7. Practical Example in a Single File
-------------------------------------------------------
# Imagine our package is called "shapes"
# Inside shapes/__init__.py we define:
# from .circle import area as circle_area
# from .square import area as square_area

# circle.py:
# def area(radius):
#     return 3.14 * radius ** 2

# square.py:
# def area(side):
#     return side ** 2

# main.py:
# from shapes import circle_area, square_area
# print(circle_area(5))  # 78.5
# print(square_area(4))  # 16

-------------------------------------------------------
8. Best Practices for Packages
-------------------------------------------------------
✔ Use clear, descriptive names for packages and modules.
✔ Keep related functionality together in one package.
✔ Use `__init__.py` to simplify imports.
✔ Avoid circular imports (modules importing each other).
✔ Keep package hierarchy clean and logical.

-------------------------------------------------------
9. When to Use Packages vs Modules
-------------------------------------------------------
- Use a **module** when your related functions/classes can fit in one file.
- Use a **package** when you have multiple related modules and need organization.

-------------------------------------------------------
Summary:
-------------------------------------------------------
📦 A package is a folder with `__init__.py` that contains related modules.
📦 It helps organize large projects and avoid naming conflicts.
📦 You can have nested packages for more structure.
📦 `__init__.py` can control what is exposed when importing.

"""

# ----------------------------------------------
# DEMO: Creating a fake package inside this file
# ----------------------------------------------

# Simulating a package "math_package" with two modules: addition and subtraction
# Normally, these would be in separate files, but here we'll define them as classes/functions for demonstration.

# Simulated addition.py
class addition:
    @staticmethod
    def add(a, b):
        return a + b

# Simulated subtraction.py
class subtraction:
    @staticmethod
    def subtract(a, b):
        return a - b

# Simulated __init__.py behavior
# In a real package, __init__.py would import these functions/classes
class math_package:
    add = addition.add
    subtract = subtraction.subtract


# Using the simulated package
if __name__ == "__main__":
    print("Addition:", math_package.add(10, 5))       # 15
    print("Subtraction:", math_package.subtract(10, 5))  # 5

