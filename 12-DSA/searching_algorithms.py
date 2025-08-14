"""
searching_algs.py

Linear Search & Binary Search in Python
---------------------------------------

Searching algorithms help us find elements in a data structure efficiently.

1️⃣ Linear Search (Sequential Search):
    - Traverse the list element by element
    - Time Complexity: O(n)
    - Works on both sorted and unsorted lists

2️⃣ Binary Search:
    - Requires a **sorted list**
    - Divide and conquer approach
    - Time Complexity: O(log n)
"""

# -----------------------
# 1. Linear Search
# -----------------------
def linear_search(arr, target):
    """
    Returns index of target if found, else -1
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage of Linear Search
arr = [10, 23, 45, 70, 11, 15]
target = 45
index = linear_search(arr, target)
print(f"Linear Search: {target} found at index {index}" if index != -1 else f"{target} not found")


# -----------------------
# 2. Binary Search (Iterative)
# -----------------------
def binary_search_iterative(arr, target):
    """
    Returns index of target if found, else -1
    List must be sorted
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage of Binary Search (Iterative)
sorted_arr = [11, 15, 23, 45, 70]
target = 23
index = binary_search_iterative(sorted_arr, target)
print(f"Binary Search (Iterative): {target} found at index {index}" if index != -1 else f"{target} not found")


# -----------------------
# 3. Binary Search (Recursive)
# -----------------------
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage of Binary Search (Recursive)
target = 45
index = binary_search_recursive(sorted_arr, target, 0, len(sorted_arr)-1)
print(f"Binary Search (Recursive): {target} found at index {index}" if index != -1 else f"{target} not found")


# -----------------------
# 4. Notes & Tips
# -----------------------
"""
- Linear Search is simple but inefficient for large datasets.
- Binary Search is much faster but requires sorted data.
- Always ensure the list is sorted before using binary search.
- Binary search can be implemented iteratively or recursively.
"""
