"""
Closures in Python
------------------

A **closure** is a function that remembers the variables from its enclosing scope 
even after the scope has finished executing.

Closures are created when:
1. A nested function (inner function) is defined inside another function (outer function).
2. The inner function references variables from the outer function.
3. The outer function returns the inner function.

Why Closures are Useful?
------------------------
- They allow data to be associated with functions.
- Useful for maintaining state without using global variables or classes.
- Helps with data hiding and encapsulation.

Structure of a Closure:
-----------------------
def outer():
    # variable in outer function
    def inner():
        # inner function uses outer variable
    return inner
"""

# Example 1: Basic Closure
def outer_function(message):
    """
    This function returns another function (inner_function)
    that remembers the value of 'message'.
    """
    def inner_function():
        print(f"Message: {message}")
    return inner_function  # Returning inner function without calling it

# Create closures
closure_hello = outer_function("Hello, World!")
closure_python = outer_function("Python is powerful!")

# Call closures
closure_hello()   # Output: Message: Hello, World!
closure_python()  # Output: Message: Python is powerful!


# Example 2: Closure as a Function Factory
def power_of(exponent):
    """
    Returns a function that calculates 'base' raised to the 'exponent'.
    The 'exponent' value is remembered by the returned function.
    """
    def power(base):
        return base ** exponent
    return power

# Create specialized functions using closure
square = power_of(2)  # remembers exponent = 2
cube = power_of(3)    # remembers exponent = 3

print(square(4))  # Output: 16
print(cube(2))    # Output: 8


# Example 3: Using Closures for Data Hiding
def counter():
    """
    Returns a function that keeps track of how many times it has been called.
    The variable 'count' is private and only accessible through the inner function.
    """
    count = 0  # variable hidden from outside
    def increment():
        nonlocal count  # to modify 'count' from outer scope
        count += 1
        return count
    return increment

# Create a counter function
my_counter = counter()

print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3


"""
Key Points:
-----------
1. Closures help preserve state between function calls.
2. Variables in outer scope are remembered by the inner function.
3. Use 'nonlocal' keyword to modify outer scope variables in closure.
4. Closures are commonly used in decorators, callbacks, and function factories.
"""
