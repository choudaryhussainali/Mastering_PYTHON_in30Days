"""
dict_comprehension.py
----------------------
This file covers Dictionary Comprehensions in Python:
    - Basic syntax
    - Filtering with conditions
    - Nested comprehensions
    - Real-life examples

Dictionary Comprehension:
-------------------------
A concise way to create dictionaries in Python using a single line of code.

Syntax:
--------
    {key_expression: value_expression for item in iterable if condition}

Benefits:
---------
- More concise than loops
- Easier to read for small transformations
- Combines creation & transformation in one step
"""

# 1. Basic dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Basic squares dict:", squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# 2. Dictionary comprehension with condition (filtering)
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares dict:", even_squares)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# 3. Converting two lists into a dictionary
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
student_scores = {name: score for name, score in zip(names, scores)}
print("Student scores dict:", student_scores)
# Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}


# 4. Dictionary comprehension with transformation
prices_in_usd = {"apple": 1.0, "banana": 0.5, "orange": 0.8}
exchange_rate = 280  # 1 USD = 280 PKR
prices_in_pkr = {item: round(price * exchange_rate, 2) for item, price in prices_in_usd.items()}
print("Prices in PKR:", prices_in_pkr)
# Output: {'apple': 280.0, 'banana': 140.0, 'orange': 224.0}


# 5. Filtering dictionary based on value
high_scores = {name: score for name, score in student_scores.items() if score >= 80}
print("High scores:", high_scores)
# Output: {'Alice': 85, 'Bob': 92}


# 6. Nested dictionary comprehension
nested_dict = {x: {y: x*y for y in range(1, 4)} for x in range(1, 4)}
print("Nested dictionary:", nested_dict)
# Output: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}


# 7. Real-life Example: Word length mapping
words = ["hello", "world", "python", "rocks"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)
# Output: {'hello': 5, 'world': 5, 'python': 6, 'rocks': 5}


# 8. Dictionary comprehension with enumerate (index mapping)
indexed_names = {index: name for index, name in enumerate(names)}
print("Indexed names:", indexed_names)
# Output: {0: 'Alice', 1: 'Bob', 2: 'Charlie'}


"""
Best Practices:
---------------
- Use dictionary comprehensions for simple transformations.
- Avoid overly complex expressions for readability.
- Useful for filtering, mapping, and quick dictionary creation.

Real-world Use Cases:
---------------------
- Converting API JSON data into dictionaries
- Filtering user data based on conditions
- Transforming values (currency conversion, normalization, etc.)
"""
