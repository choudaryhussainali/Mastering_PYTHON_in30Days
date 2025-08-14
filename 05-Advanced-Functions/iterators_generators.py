"""
decorators.py

A decorator in Python is a function that takes another function as input,
adds some functionality to it, and returns the new function — without
modifying the original function's code directly.

Decorators are very powerful and are often used for:
    - Logging
    - Access control / authentication
    - Caching
    - Timing functions
    - Debugging
    - Pre/post-processing data

In short: "Wrap a function, enhance it, return it."
"""

# ------------------------------
# 1. BASIC DECORATOR
# ------------------------------

def my_decorator(func):
    """A simple decorator that prints messages before and after a function call."""
    def wrapper():
        print(">>> Before the function runs...")
        func()
        print(">>> After the function runs...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

# Usage
print("=== BASIC DECORATOR ===")
say_hello()
print()


# ------------------------------
# 2. DECORATOR WITH ARGUMENTS
# ------------------------------

def greet_decorator(func):
    """Decorator that wraps a function with a friendly greeting."""
    def wrapper(name):
        print(f"👋 Hello, {name}!")
        func(name)
        print(f"👋 Goodbye, {name}!")
    return wrapper

@greet_decorator
def show_name(name):
    print(f"You are inside the function: {name}")

print("=== DECORATOR WITH ARGUMENTS ===")
show_name("Hussain")
print()


# ------------------------------
# 3. DECORATOR THAT RETURNS VALUES
# ------------------------------

def double_result(func):
    """Decorator that doubles the result of a function."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print("=== DECORATOR THAT RETURNS VALUES ===")
print(add(5, 3))  # (5+3) * 2 = 16
print()


# ------------------------------
# 4. DECORATOR WITH ANY NUMBER OF ARGUMENTS
# ------------------------------

def log_function_call(func):
    """Logs the function name and arguments."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def multiply(a, b, c=1):
    return a * b * c

print("=== DECORATOR WITH ANY NUMBER OF ARGUMENTS ===")
print(multiply(2, 3, c=4))
print()


# ------------------------------
# 5. CHAINING MULTIPLE DECORATORS
# ------------------------------

def make_bold(func):
    """Wraps the text in <b> tags."""
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_italic(func):
    """Wraps the text in <i> tags."""
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@make_bold
@make_italic
def get_text():
    return "Hello"

print("=== CHAINING MULTIPLE DECORATORS ===")
print(get_text())  # <b><i>Hello</i></b>
print()


# ------------------------------
# 6. USING functools.wraps
# ------------------------------

from functools import wraps

def proper_decorator(func):
    """Example showing why functools.wraps is important."""
    @wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        """Wrapper function docstring"""
        print("Running the decorated function...")
        return func(*args, **kwargs)
    return wrapper

@proper_decorator
def original_function():
    """This is the original function's docstring."""
    print("Inside original function!")

print("=== USING functools.wraps ===")
original_function()
print("Function name:", original_function.__name__)
print("Docstring:", original_function.__doc__)
print()


# ------------------------------
# 7. PRACTICAL EXAMPLE: TIMING A FUNCTION
# ------------------------------

import time

def timing_decorator(func):
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} executed in {end - start:.4f} seconds")
        return value
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    print("Finished slow function.")

print("=== PRACTICAL: TIMING FUNCTION ===")
slow_function()
print()


# ------------------------------
# SUMMARY
# ------------------------------
"""
- Decorators are a Python feature that lets you modify or extend the behavior of functions without changing their code.
- They work by taking a function as input, defining an inner function (wrapper), and returning it.
- Common use cases:
    * Logging
    * Authentication
    * Caching
    * Performance measurement
    * Code reusability
"""
