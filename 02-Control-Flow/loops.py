"""
loops.py

This file covers the concept of loops in Python in complete detail.
Loops are used to execute a block of code repeatedly as long as a certain condition is met.
There are mainly two types of loops in Python:
1. for loop
2. while loop

We will also cover:
- Loop structure
- Loop examples
- Nested loops
- Loop control statements (break, continue, pass)
- Infinite loops
- Using loops with else clause
"""

# -----------------------------
# 1. FOR LOOP
# -----------------------------
"""
The `for` loop in Python is used to iterate over a sequence (list, tuple, string, range, etc.).
It executes the block of code for each element in the sequence.
"""

# Example: Basic for loop
print("Example: Basic for loop over a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: Using range() with for loop
print("\nExample: for loop with range()")
for i in range(5):
    print("Number:", i)  # Will print 0 to 4

# Example: for loop with custom start, stop, step
print("\nExample: range(start, stop, step)")
for num in range(2, 11, 2):  # Prints even numbers from 2 to 10
    print(num)

# -----------------------------
# 2. WHILE LOOP
# -----------------------------
"""
The `while` loop keeps executing as long as a condition is True.
Be careful to ensure the loop condition will eventually become False to avoid infinite loops.
"""

# Example: Basic while loop
print("\nExample: while loop")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Example: Infinite while loop with break
print("\nExample: infinite loop with break")
i = 0
while True:
    print("i =", i)
    i += 1
    if i == 3:
        break  # Exit loop when i becomes 3

# -----------------------------
# 3. LOOP CONTROL STATEMENTS
# -----------------------------
"""
Python provides special statements to control the flow inside loops:
1. break    → Exits the loop immediately
2. continue → Skips the current iteration and moves to the next
3. pass     → Does nothing, acts as a placeholder
"""

# break example
print("\nExample: break statement")
for num in range(1, 10):
    if num == 5:
        break  # Stop when number is 5
    print(num)

# continue example
print("\nExample: continue statement")
for num in range(1, 6):
    if num == 3:
        continue  # Skip number 3
    print(num)

# pass example
print("\nExample: pass statement")
for num in range(1, 4):
    if num == 2:
        pass  # Placeholder, does nothing
    print(num)

# -----------------------------
# 4. NESTED LOOPS
# -----------------------------
"""
A loop inside another loop is called a nested loop.
The inner loop runs completely for each iteration of the outer loop.
"""

# Example: Nested for loops
print("\nExample: Nested loops")
for x in range(1, 4):
    for y in range(1, 3):
        print(f"x={x}, y={y}")

# -----------------------------
# 5. ELSE WITH LOOPS
# -----------------------------
"""
In Python, loops can have an else clause.
The else block is executed after the loop finishes normally (without break).
"""

# Example: else in for loop
print("\nExample: else with for loop")
for num in range(3):
    print(num)
else:
    print("Loop finished without break.")

# Example: else with while loop
print("\nExample: else with while loop")
n = 0
while n < 3:
    print("n =", n)
    n += 1
else:
    print("While loop finished without break.")
