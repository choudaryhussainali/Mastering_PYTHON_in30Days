"""
arrays_basics.py
----------------
Basic operations on arrays (lists in Python).

In Python, we use lists to simulate arrays.
"""

# Creating an array (list in Python)
arr = [10, 20, 30, 40, 50]
print("Initial array:", arr)

# Accessing elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Insertion
arr.append(60)  # Add at the end
print("After append:", arr)

arr.insert(2, 25)  # Insert at index 2
print("After inserting 25 at index 2:", arr)

# Deletion
arr.remove(40)  # Remove by value
print("After removing 40:", arr)

deleted_value = arr.pop(3)  # Remove by index
print(f"Deleted value at index 3: {deleted_value}")
print("Array after pop:", arr)

# Updating elements
arr[1] = 22
print("After updating index 1 to 22:", arr)

# Traversal
print("Traversing array:")
for element in arr:
    print(element)

# Searching
if 30 in arr:
    print("30 found in array")
else:
    print("30 not found in array")

# Sorting
arr.sort()
print("Sorted array:", arr)

# Reversing
arr.reverse()
print("Reversed array:", arr)
