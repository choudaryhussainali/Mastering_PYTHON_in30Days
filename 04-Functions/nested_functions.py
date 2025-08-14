# nested_functions.py
# Demonstrating how functions can be defined inside other functions.

def outer_function():
    """Outer function that contains an inner function."""

    def inner_function():
        """Inner function accessible only inside the outer function."""
        print("Hello from the inner function!")

    print("Hello from the outer function!")
    inner_function()  # Calling the inner function inside the outer function


# Example 1: Calling the outer function, which also calls the inner function
outer_function()


# Example 2: Returning an inner function
def multiplier(n):
    """Outer function that returns a function to multiply by n."""
    def multiply(x):
        return x * n
    return multiply


# Create multiplier functions
times_two = multiplier(2)
times_five = multiplier(5)

print(times_two(10))  # Output: 20
print(times_five(10))  # Output: 50
