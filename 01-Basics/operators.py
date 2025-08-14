# ==========================
# Python Operators Tutorial
# ==========================
# In Python, operators are special symbols that perform operations on variables and values.
# We can classify operators into several types:
# 1. Arithmetic Operators
# 2. Comparison (Relational) Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators

# ---------------------------
# 1. Arithmetic Operators
# ---------------------------

a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)        # Adds two numbers
print("Subtraction:", a - b)     # Subtracts two numbers
print("Multiplication:", a * b)  # Multiplies two numbers
print("Division:", a / b)        # Divides and returns a float
print("Floor Division:", a // b) # Divides and returns an integer
print("Modulus:", a % b)         # Returns remainder
print("Exponentiation:", a ** b) # Power calculation (a^b)

# ---------------------------
# 2. Comparison Operators
# ---------------------------
# These operators compare two values and return a Boolean result (True or False).

print("\nComparison Operators:")
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

# ---------------------------
# 3. Assignment Operators
# ---------------------------
# These operators assign values to variables, with optional arithmetic.

x = 5
print("\nAssignment Operators:")
x += 3  # x = x + 3
print("After += :", x)
x -= 2  # x = x - 2
print("After -= :", x)
x *= 4  # x = x * 4
print("After *= :", x)
x /= 2  # x = x / 2
print("After /= :", x)
x //= 2 # x = x // 2
print("After //= :", x)
x %= 3  # x = x % 3
print("After %= :", x)
x **= 2 # x = x ** 2
print("After **= :", x)

# ---------------------------
# 4. Logical Operators
# ---------------------------
# Used to combine conditional statements.

p = True
q = False

print("\nLogical Operators:")
print("AND:", p and q)   # True if both p and q are True
print("OR:", p or q)     # True if at least one is True
print("NOT:", not p)     # Inverts the Boolean value

# ---------------------------
# 5. Bitwise Operators
# ---------------------------
# These work on bits (binary representation of numbers).

m = 5  # (in binary: 0101)
n = 3  # (in binary: 0011)

print("\nBitwise Operators:")
print("Bitwise AND:", m & n)    # 0101 & 0011 = 0001 (1)
print("Bitwise OR:", m | n)     # 0101 | 0011 = 0111 (7)
print("Bitwise XOR:", m ^ n)    # 0101 ^ 0011 = 0110 (6)
print("Bitwise NOT:", ~m)       # ~(0101) = -(m+1) = -6
print("Bitwise Left Shift:", m << 1) # 0101 << 1 = 1010 (10)
print("Bitwise Right Shift:", m >> 1) # 0101 >> 1 = 0010 (2)

# ---------------------------
# 6. Membership Operators
# ---------------------------
# Used to test if a sequence contains a value.

numbers = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("Is 3 in list?:", 3 in numbers)
print("Is 10 not in list?:", 10 not in numbers)

# ---------------------------
# 7. Identity Operators
# ---------------------------
# Compare object memory locations (not values).

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("\nIdentity Operators:")
print("x is z:", x is z)         # True because z refers to the same object as x
print("x is y:", x is y)         # False because they are different objects with the same content
print("x is not y:", x is not y) # True

# ---------------------------
# Summary:
# Operators in Python make it possible to perform various operations such as arithmetic, 
# comparisons, logical evaluations, bitwise calculations, and object checks.
