"""
try_except.py

This file explains Python's try-except block in detail with examples.
Error handling is essential to prevent your program from crashing due to unexpected issues.
"""

# ----------------------------
# Basic try-except
# ----------------------------
try:
    x = int("10")  # Valid conversion
    y = int("abc")  # This will raise ValueError
except ValueError as e:
    print("ValueError occurred:", e)

# ----------------------------
# Multiple except blocks
# ----------------------------
try:
    num = 10 / 0  # This raises ZeroDivisionError
except ValueError:
    print("This is a value error")
except ZeroDivisionError:
    print("Cannot divide by zero")

# ----------------------------
# Handling multiple errors in one except
# ----------------------------
try:
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
except (IndexError, KeyError) as e:
    print(f"An indexing/key error occurred: {e}")

# ----------------------------
# Using else block
# ----------------------------
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result =", result)

# ----------------------------
# Using finally block
# ----------------------------
try:
    file = open("test.txt", "w")
    file.write("Hello, Python!")
except IOError:
    print("Error while writing to file")
finally:
    file.close()  # Always executed
    print("File closed")

# ----------------------------
# Nested try-except
# ----------------------------
try:
    a = int(input("Enter a number: "))
    try:
        result = 10 / a
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero")
except ValueError:
    print("Outer: Invalid input, please enter a number")

# ----------------------------
# Custom error raising
# ----------------------------
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Custom Error:", e)
