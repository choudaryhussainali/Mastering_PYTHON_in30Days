"""
list_comprehension.py
----------------------
A complete guide to Python list comprehensions with examples,
from beginner-friendly to advanced usage.
"""

# -----------------------
# 1. Basic List Comprehension
# -----------------------
# Syntax: [expression for item in iterable]

# Example: Squares of numbers 0–9
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)


# -----------------------
# 2. With Condition
# -----------------------
# Syntax: [expression for item in iterable if condition]

# Example: Even numbers between 0–20
evens = [x for x in range(21) if x % 2 == 0]
print("Even numbers:", evens)


# -----------------------
# 3. With If–Else in Expression
# -----------------------
# Example: Label numbers as 'Even' or 'Odd'
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print("Labels:", labels)


# -----------------------
# 4. Nested Loops
# -----------------------
# Syntax: [expression for item1 in iterable1 for item2 in iterable2]

# Example: Cartesian product of two lists
list1 = [1, 2, 3]
list2 = ["A", "B"]
pairs = [(x, y) for x in list1 for y in list2]
print("Pairs:", pairs)


# -----------------------
# 5. Working with Strings
# -----------------------
# Example: Extract vowels from a string
text = "Python Comprehensions"
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print("Vowels:", vowels)


# -----------------------
# 6. Using Functions
# -----------------------
def square(n):
    return n * n

nums = [1, 2, 3, 4]
squared_nums = [square(n) for n in nums]
print("Squared via function:", squared_nums)


# -----------------------
# 7. Flatten a Nested List
# -----------------------
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)


# -----------------------
# 8. Advanced: Multiple Conditions
# -----------------------
# Example: Numbers divisible by both 2 and 3
divisible = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print("Divisible by 2 and 3:", divisible)


# -----------------------
# 9. List Comprehension with Enumerate
# -----------------------
words = ["Python", "Java", "C++"]
indexed_words = [f"{i}: {word}" for i, word in enumerate(words)]
print("Indexed words:", indexed_words)


# -----------------------
# 10. Dictionary to List Conversion
# -----------------------
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
passed_students = [name for name, score in student_scores.items() if score >= 80]
print("Students who passed:", passed_students)
