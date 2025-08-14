"""
try_except_else_finally.py
---------------------------
This script explains and demonstrates the use of:
    - try
    - except
    - else
    - finally

The `try-except-else-finally` structure is used for handling exceptions (errors) in Python.
It allows you to gracefully manage situations where something might go wrong.
"""

# Basic Structure:
# try:
#     Code that may raise an exception
# except ExceptionType:
#     Code that runs if an exception occurs
# else:
#     Code that runs if NO exception occurs
# finally:
#     Code that runs no matter what (exception or not)

# Example 1: Division with Error Handling
def divide_numbers(a, b):
    try:
        result = a / b  # May raise ZeroDivisionError
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    else:
        print(f"✅ Division successful! Result = {result}")
    finally:
        print("🔹 This runs no matter what (clean-up, logging, etc.)")

# Running Example 1
print("Example 1: Division")
divide_numbers(10, 2)   # Successful division
print("-" * 50)
divide_numbers(10, 0)   # Division by zero error
print("=" * 70)


# Example 2: Multiple Except Blocks
def open_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"❌ The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ You don't have permission to read '{filename}'.")
    else:
        print(f"✅ File content:\n{data}")
    finally:
        print(f"🔹 Attempted to open '{filename}'.")

# Running Example 2
print("Example 2: Opening Files")
open_file("existing_file.txt")   # Works if file exists
print("-" * 50)
open_file("non_existing.txt")    # File not found
print("=" * 70)


# Example 3: Catching Any Exception
def safe_conversion(value):
    try:
        num = int(value)  # May raise ValueError
    except Exception as e:
        print(f"❌ Error occurred: {e}")
    else:
        print(f"✅ Successfully converted to integer: {num}")
    finally:
        print("🔹 Conversion attempt complete.")

# Running Example 3
print("Example 3: Type Conversion")
safe_conversion("123")   # Works fine
print("-" * 50)
safe_conversion("abc")   # Raises ValueError
print("=" * 70)


"""
📌 When to Use:
- Use `try` for risky code.
- Use `except` for handling errors gracefully.
- Use `else` for code that should only run if no error occurred.
- Use `finally` for clean-up code that must run no matter what (e.g., closing files, releasing resources).

✅ Best Practices:
- Catch specific exceptions instead of using a generic `except`.
- Use `finally` for actions like closing files, disconnecting databases, or freeing resources.
- Keep try blocks short to avoid catching unexpected errors.
"""
