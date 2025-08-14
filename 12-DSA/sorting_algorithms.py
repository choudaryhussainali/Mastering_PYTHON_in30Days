"""
sorting_algs.py

Basic Sorting Algorithms in Python
---------------------------------

Sorting algorithms arrange data in a particular order (ascending/descending).

This file covers:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort

All examples use ascending order.
"""

# -----------------------
# 1. Bubble Sort
# -----------------------
def bubble_sort(arr):
    """
    Repeatedly compare adjacent elements and swap if needed.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization: Stop if already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(arr1.copy()))


# -----------------------
# 2. Selection Sort
# -----------------------
def selection_sort(arr):
    """
    Repeatedly find the minimum element and place it at the beginning.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr2 = [64, 34, 25, 12, 22, 11, 90]
print("Selection Sort:", selection_sort(arr2.copy()))


# -----------------------
# 3. Insertion Sort
# -----------------------
def insertion_sort(arr):
    """
    Build the sorted array one element at a time by inserting elements at the correct position.
    Time Complexity: O(n^2)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr3 = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:", insertion_sort(arr3.copy()))


# -----------------------
# Notes & Tips
# -----------------------
"""
- Bubble Sort: Simple but inefficient for large arrays; use early exit optimization.
- Selection Sort: Finds min element each iteration; useful when memory writes are costly.
- Insertion Sort: Efficient for small or nearly sorted arrays; stable sort.
- For large datasets, prefer built-in Python sort (Timsort): arr.sort() or sorted(arr)
"""
