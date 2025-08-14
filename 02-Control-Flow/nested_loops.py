"""
nested_loops.py

This file explains Nested Loops in Python in detail.

Nested loops are loops inside another loop.
- The **outer loop** runs once for each iteration of the **inner loop**.
- Useful for working with grids, tables, patterns, or multi-dimensional data.

We will cover:
1. Basic nested for loops
2. Nested while loops
3. Nested for inside while
4. Practical examples
"""

# -----------------------------
# 1. Basic nested for loops
# -----------------------------
print("Example 1: Nested for loop (simple numbers)")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")

# Output Explanation:
# Outer loop i=1 → inner loop runs j=1,2,3
# Outer loop i=2 → inner loop runs j=1,2,3
# Outer loop i=3 → inner loop runs j=1,2,3

# -----------------------------
# 2. Nested while loops
# -----------------------------
print("\nExample 2: Nested while loop")
x = 1
while x <= 3:  # Outer loop
    y = 1
    while y <= 2:  # Inner loop
        print(f"x={x}, y={y}")
        y += 1
    x += 1

# -----------------------------
# 3. Nested for inside while
# -----------------------------
print("\nExample 3: For loop inside while loop")
a = 1
while a <= 2:  # Outer while loop
    for b in range(1, 4):  # Inner for loop
        print(f"a={a}, b={b}")
    a += 1

# -----------------------------
# 4. Practical Example: Multiplication Table
# -----------------------------
print("\nExample 4: Multiplication table using nested loops")
for i in range(1, 6):  # 1 to 5
    for j in range(1, 6):  # 1 to 5
        print(f"{i*j}", end="\t")  # Tab space for alignment
    print()  # Newline after each row

# -----------------------------
# 5. Practical Example: Printing Patterns
# -----------------------------
print("\nExample 5: Star (*) pattern")
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")  # Print stars in one row
    print()  # Newline after each row

"""
Output:
*
**
***
****
"""

# -----------------------------
# 6. Tips and Best Practices
# -----------------------------
"""
1. Avoid too many levels of nesting — it makes code harder to read.
2. Use meaningful variable names for outer and inner loops.
3. Keep inner loop logic simple.
4. Remember: the inner loop completes all iterations for every single iteration of the outer loop.
5. You can mix for and while loops if needed, but avoid unnecessary complexity.
"""

