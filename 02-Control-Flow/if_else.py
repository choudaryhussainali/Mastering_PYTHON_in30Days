# if-else.py
# --------------------------
# Topic: If-Else Statements in Python
# --------------------------
# In Python, "if-else" is used to make decisions in the program.
# It allows us to execute certain code only if a condition is True,
# and run alternative code if the condition is False.

# Syntax:
# if condition:
#     # code to run if condition is True
# else:
#     # code to run if condition is False

# Note: 
# - Indentation (spaces) is VERY important in Python.
# - The condition must be an expression that returns True or False.

# --------------------------
# Example 1: Simple if-else
# --------------------------
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")

# Output: You are eligible to vote.
# Explanation: age (18) is greater than or equal to 18, so the if block runs.


# --------------------------
# Example 2: Checking Even or Odd
# --------------------------
number = 7

if number % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

# Output: The number is ODD.
# Explanation: 7 % 2 is 1 (not equal to 0), so the else block runs.


# --------------------------
# Example 3: Comparing two numbers
# --------------------------
a = 10
b = 20

if a > b:
    print("a is greater than b")
else:
    print("a is NOT greater than b")

# Output: a is NOT greater than b
# Explanation: 10 is less than 20, so else block executes.


# --------------------------
# Example 4: Taking user input
# --------------------------
# The input() function takes input as a string, so we convert it to int for comparison.
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("Welcome! You are an adult.")
else:
    print("Sorry! You are underage.")

# Try running this and entering values like 15 or 20 to see different outputs.


# --------------------------
# Points to Remember:
# --------------------------
# 1. Python uses indentation instead of curly braces {} to define code blocks.
# 2. The else part is optional. If you only want to check and do something when True, you can skip else.
# 3. Comparison operators we can use here:
#    ==  (equal to)
#    !=  (not equal to)
#    >   (greater than)
#    <   (less than)
#    >=  (greater than or equal to)
#    <=  (less than or equal to)
# 4. If the condition is False and no else is provided, Python just skips the block.
