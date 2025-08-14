# set_comprehension.py
# Demonstrating Python set comprehensions

# Basic example: Squaring numbers
numbers = [1, 2, 2, 3, 4, 4, 5]
squared_set = {n ** 2 for n in numbers}
print("Squared set (duplicates removed):", squared_set)

# Using condition in set comprehension
even_squared_set = {n ** 2 for n in numbers if n % 2 == 0}
print("Even squared set:", even_squared_set)

# Creating a set of first letters from words
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
print("First letters set:", first_letters)

# Creating a set of unique lowercase characters from a string
sentence = "Set Comprehension in PYTHON"
char_set = {char.lower() for char in sentence if char.isalpha()}
print("Unique characters in lowercase:", char_set)

# Example with mathematical operation
multiples_of_three = {x for x in range(1, 31) if x % 3 == 0}
print("Multiples of three from 1 to 30:", multiples_of_three)

# Nested set comprehension: Flatten and filter unique values
matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
flattened_unique = {num for row in matrix for num in row if num > 2}
print("Flattened unique numbers > 2:", flattened_unique)
