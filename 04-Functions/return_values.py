"""
return_values.py

Topic: Returning values from functions in Python
------------------------------------------------
When we call a function, it can either:
    1. Just perform some action (like printing)
    2. Or send a result back to the caller using the `return` statement.

The `return` statement:
    - Ends the function immediately
    - Sends data back to where the function was called
    - Can return any type of data (numbers, strings, lists, etc.)
    - A function can return multiple values (as a tuple)

Why use return values?
    - To reuse results instead of printing them directly.
    - To use the result in other calculations.
"""

# Example 1: Function that returns a single value
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add_numbers(5, 3)
print("Sum is:", result)  # We can store and reuse the result


# Example 2: Function that returns multiple values
def math_operations(a, b):
    """Return sum, difference, and product of two numbers."""
    return a + b, a - b, a * b  # This returns a tuple

sum_result, diff_result, prod_result = math_operations(10, 4)
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)


# Example 3: Returning different data types
def get_user_info():
    """Return a dictionary with user details."""
    return {
        "name": "Ali",
        "age": 21,
        "country": "Pakistan"
    }

user = get_user_info()
print("User Info:", user)


# Example 4: Returning None explicitly
def greet_user(name):
    """Greet the user and return None."""
    print(f"Hello, {name}!")
    return None

greet_user("Hussain")  # Prints greeting but returns None


# Example 5: Using return to stop execution early
def safe_divide(a, b):
    """Divide a by b, but stop if b is zero."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return  # Stops the function without a value (returns None)
    return a / b

print("Division result:", safe_divide(10, 2))
print("Division result:", safe_divide(5, 0))  # Early return stops execution
