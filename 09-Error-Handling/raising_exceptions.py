"""
raising_exceptions.py

This file covers how to raise exceptions in Python.

💡 In Python, you can manually trigger (raise) an exception when you detect an error
condition in your code, even if Python itself wouldn't normally raise one.
"""

# Example 1: Raising a built-in exception
def divide(a, b):
    """Divide two numbers, but raise an exception if divisor is zero."""
    if b == 0:
        # Manually raise a ZeroDivisionError
        raise ZeroDivisionError("You cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)


# Example 2: Raising a built-in exception with 'ValueError'
def set_age(age):
    """Set age but ensure it's a positive integer."""
    if age <= 0:
        raise ValueError("Age must be greater than zero.")
    print(f"Age set to: {age}")

try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)


# Example 3: Raising a custom exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(number):
    """Raise a custom exception if number is negative."""
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print(f"Number {number} is positive.")

try:
    check_positive(-10)
except NegativeNumberError as e:
    print("Custom Error:", e)


# Example 4: Raising multiple exceptions in the same function
def process_input(value):
    """Validate input for different error conditions."""
    if not isinstance(value, int):
        raise TypeError("Value must be an integer.")
    if value < 0:
        raise NegativeNumberError("Value cannot be negative.")
    if value > 100:
        raise ValueError("Value cannot be greater than 100.")
    print(f"Processing value: {value}")

try:
    process_input("abc")  # This will raise TypeError
except (TypeError, NegativeNumberError, ValueError) as e:
    print("Validation Error:", e)


# Example 5: Raising an exception inside another exception (Exception chaining)
def outer_function():
    try:
        int("abc")  # This will raise a ValueError
    except ValueError as e:
        # Raise another exception but keep the original cause
        raise RuntimeError("Failed in outer_function") from e

try:
    outer_function()
except RuntimeError as e:
    print("Chained Exception:", e)
    print("Original Cause:", e.__cause__)


"""
📌 Summary:
- Use `raise` to manually trigger an exception.
- You can raise both built-in exceptions and custom exceptions.
- Exceptions can be chained using `from` to preserve the original error.
- Raising exceptions is useful for input validation, enforcing rules, and signaling errors early.
"""
