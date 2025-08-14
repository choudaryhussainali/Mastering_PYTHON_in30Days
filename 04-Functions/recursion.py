# recursion.py

"""
Recursion in Python
-------------------
Recursion is when a function calls itself directly or indirectly.
It's like looking into two mirrors facing each other — the reflection keeps going.

Recursion is often used for:
1. Breaking big problems into smaller ones.
2. Working with tasks that have a repeated pattern (e.g., factorial, Fibonacci).
3. Tree or graph traversal.

Important:
- Every recursion must have a BASE CASE (stopping condition).
- Without a base case, recursion will cause infinite calls → leads to RecursionError.

"""

# Example 1: Factorial using recursion
def factorial(n):
    """
    Calculates factorial of a number using recursion.
    Factorial formula:
        n! = n × (n-1) × (n-2) × ... × 1
    Base case:
        factorial(0) = 1
    """
    if n == 0:
        return 1  # base case
    return n * factorial(n - 1)  # recursive call


# Example 2: Fibonacci sequence using recursion
def fibonacci(n):
    """
    Returns nth Fibonacci number using recursion.
    Fibonacci sequence:
        0, 1, 1, 2, 3, 5, 8, ...
    Base cases:
        fibonacci(0) = 0
        fibonacci(1) = 1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive call


# Example 3: Sum of list elements using recursion
def sum_list(lst):
    """
    Recursively calculates the sum of a list of numbers.
    Base case: If list has 1 element, return it.
    """
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_list(lst[1:])  # recursive call


# Example 4: Countdown using recursion
def countdown(n):
    """
    Recursively counts down from n to 0.
    """
    if n < 0:
        return  # base case
    print(n)
    countdown(n - 1)  # recursive call


print("Factorial of 5:", factorial(5))         # 120
print("Fibonacci of 6:", fibonacci(6))         # 8
print("Sum of list [1,2,3,4]:", sum_list([1, 2, 3, 4]))  # 10
print("Countdown from 5:")
countdown(5)
