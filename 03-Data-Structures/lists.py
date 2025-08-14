# lists.py
# Python Lists - Basics to Advanced

# A list is an ordered, mutable collection that can store elements of any type.
# Lists are defined using square brackets [].

# -----------------------
# 1. Creating Lists
# -----------------------
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", True, 3.14]
nested_list = [[1, 2], [3, 4], [5, 6]]

print("Empty List:", empty_list)
print("Numbers:", numbers)
print("Mixed:", mixed)
print("Nested List:", nested_list)

# -----------------------
# 2. Accessing Elements
# -----------------------
print("First element:", numbers[0])   # Index starts at 0
print("Last element:", numbers[-1])   # Negative index = from the end
print("Slice [1:4]:", numbers[1:4])   # Elements from index 1 to 3

# -----------------------
# 3. Modifying Lists
# -----------------------
numbers[0] = 100
print("After modification:", numbers)

# Adding elements
numbers.append(6)  # Add at end
numbers.insert(2, 200)  # Insert at index 2
print("After adding:", numbers)

# Removing elements
numbers.remove(200)   # Remove first occurrence
popped = numbers.pop()  # Remove last element
print("Removed element:", popped)
print("After removing:", numbers)

# -----------------------
# 4. Iterating Through Lists
# -----------------------
for num in numbers:
    print("Item:", num)

# With index
for index, value in enumerate(numbers):
    print(f"Index {index} => Value {value}")

# -----------------------
# 5. Common List Methods
# -----------------------
letters = ["a", "b", "c"]
letters.extend(["d", "e"])  # Add multiple elements
print("Extended list:", letters)

letters.reverse()
print("Reversed list:", letters)

letters.sort()
print("Sorted list:", letters)

# -----------------------
# 6. List Comprehensions
# -----------------------
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# -----------------------
# 7. Copying Lists
# -----------------------
copy_list = numbers.copy()  # Creates a new list
print("Copied list:", copy_list)

# -----------------------
# 8. Nested Lists Access
# -----------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix element [1][2]:", matrix[1][2])  # Row 1, Col 2
