# sets.py
# ---------------------------
# Topic: Sets in Python
# ---------------------------
# A set is an unordered collection of unique elements.
# - It does not allow duplicate values.
# - Elements can be of different data types.
# - Sets are useful when you want to store unique items and perform mathematical set operations like union, intersection, etc.
#
# Syntax:
# my_set = {element1, element2, element3, ...}
#
# NOTE: Sets are unordered, so they do not support indexing or slicing.

# ---------------------------
# 1. Creating Sets
# ---------------------------

# Creating a simple set
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Creating a set from a list (duplicates will be removed automatically)
numbers = set([1, 2, 3, 2, 1])
print("Numbers set (from list):", numbers)

# Creating an empty set (IMPORTANT: Use set(), not {} for empty sets)
empty_set = set()
print("Empty set:", empty_set)

# ---------------------------
# 2. Properties of Sets
# ---------------------------
# - No duplicates
# - Unordered (output order may be different from insertion order)
# - Can store different types of data

mixed_set = {1, "apple", 3.14, True}
print("Mixed set:", mixed_set)

# ---------------------------
# 3. Adding and Removing Elements
# ---------------------------

# Adding a single element
fruits.add("orange")
print("After adding 'orange':", fruits)

# Adding multiple elements
fruits.update(["mango", "grape"])
print("After adding multiple elements:", fruits)

# Removing an element (will give an error if the element is not found)
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Discarding an element (no error if not found)
fruits.discard("banana")  # banana is already removed, so no error
print("After discarding 'banana':", fruits)

# Removing and returning a random element
removed_item = fruits.pop()
print("Removed item:", removed_item)
print("Fruits after pop:", fruits)

# Clearing all elements
fruits.clear()
print("Fruits after clear:", fruits)

# ---------------------------
# 4. Set Operations
# ---------------------------

# Creating sets for operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (A ∪ B) - Elements from both sets, no duplicates
print("Union:", A.union(B))

# Intersection (A ∩ B) - Elements common to both sets
print("Intersection:", A.intersection(B))

# Difference (A - B) - Elements in A but not in B
print("Difference (A - B):", A.difference(B))

# Symmetric Difference (A △ B) - Elements in either A or B, but not both
print("Symmetric Difference:", A.symmetric_difference(B))

# ---------------------------
# 5. Membership Test
# ---------------------------
print("Is 3 in A?", 3 in A)
print("Is 7 in A?", 7 in A)

# ---------------------------
# 6. Copying Sets
# ---------------------------
copy_A = A.copy()
print("Copied set A:", copy_A)

# ---------------------------
# Summary:
# - Sets store unique, unordered elements.
# - They support mathematical set operations like union, intersection, difference, and symmetric difference.
# - Good for removing duplicates and performing membership tests quickly.
