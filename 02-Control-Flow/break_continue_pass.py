"""
break_continue_pass.py

This file explains the three loop control statements in Python:
1. break
2. continue
3. pass

These statements control the flow of loops and help in handling specific conditions
without breaking the logic of the program.
"""

# -----------------------------
# 1. BREAK STATEMENT
# -----------------------------
"""
The `break` statement stops the loop immediately, even if the loop condition is still True.
It exits only the loop in which it is used.
"""

print("Example 1: break statement")
for i in range(1, 6):
    if i == 4:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

# Output:
# i=1
# i=2
# i=3
# Breaking the loop at i=4

# -----------------------------
# 2. CONTINUE STATEMENT
# -----------------------------
"""
The `continue` statement skips the rest of the code inside the current iteration
and moves to the next iteration of the loop.
"""

print("\nExample 2: continue statement")
for i in range(1, 6):
    if i == 3:
        print("Skipping number", i)
        continue
    print("i =", i)

# Output:
# i=1
# i=2
# Skipping number 3
# i=4
# i=5

# -----------------------------
# 3. PASS STATEMENT
# -----------------------------
"""
The `pass` statement does nothing. It is used as a placeholder when syntax requires
a statement but you do not want to execute any code.
"""

print("\nExample 3: pass statement")
for i in range(1, 4):
    if i == 2:
        pass  # Placeholder, does nothing
    print("i =", i)

# Output:
# i=1
# i=2
# i=3

# -----------------------------
# 4. BREAK AND CONTINUE TOGETHER
# -----------------------------
print("\nExample 4: break and continue together")
for i in range(1, 6):
    if i == 2:
        print("Skipping", i)
        continue
    if i == 5:
        print("Breaking at", i)
        break
    print("i =", i)

# Output:
# i=1
# Skipping 2
# i=3
# i=4
# Breaking at 5

# -----------------------------
# 5. WHILE LOOP WITH BREAK AND CONTINUE
# -----------------------------
print("\nExample 5: while loop with break and continue")
n = 0
while n < 5:
    n += 1
    if n == 2:
        print("Skipping", n)
        continue
    if n == 4:
        print("Breaking at", n)
        break
    print("n =", n)

# Output:
# n=1
# Skipping 2
# n=3
# Breaking at 4

# -----------------------------
# Summary
# -----------------------------
"""
- break: exits the loop immediately
- continue: skips current iteration and moves to next
- pass: does nothing (used as placeholder)
- You can use these statements in both for and while loops.
- Proper use of these statements makes loops flexible and efficient.
"""
