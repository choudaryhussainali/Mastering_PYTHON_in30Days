"""
input-outputs.py
================
This file explains Python's input and output operations in detail.
It covers:
    - Displaying output using print()
    - Formatting output
    - Taking input from the user using input()
    - Type conversion of inputs
    - Output to files
    - Input from files
"""

# ----------------------------
# 1. PRINTING OUTPUT (print function)
# ----------------------------
print("Hello, World!")  # Basic output
print("Python", "is", "fun")  # Multiple arguments
print("Python", "is", "fun", sep="-")  # Custom separator
print("Welcome", end="!")  # Custom end (default is '\n')
print(" Let's start learning.")  # Continues on same line

# Printing variables
name = "Hussain"
age = 21
print("My name is", name, "and I am", age, "years old.")

# ----------------------------
# 2. FORMATTING OUTPUT
# ----------------------------

# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# Using format() method
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name))

# Formatting numbers
pi = 3.1415926535
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
print("Pi rounded to 3 decimal places: {:.3f}".format(pi))

# ----------------------------
# 3. TAKING INPUT FROM USER
# ----------------------------

# Basic input (returns string)
# user_name = input("Enter your name: ")
# print("Hello,", user_name)

# Example with integer conversion
# user_age = int(input("Enter your age: "))
# print("You will be", user_age + 1, "next year.")

# Example with float conversion
# user_height = float(input("Enter your height in meters: "))
# print("Your height in centimeters is:", user_height * 100)

# ----------------------------
# 4. MULTIPLE INPUTS IN ONE LINE
# ----------------------------

# Example: Getting multiple integers from user
# x, y = map(int, input("Enter two numbers separated by space: ").split())
# print("Sum:", x + y)

# Example: Getting multiple strings
# first_name, last_name = input("Enter your first and last name: ").split()
# print(f"Full Name: {first_name} {last_name}")

# ----------------------------
# 5. OUTPUT TO FILE
# ----------------------------
with open("output.txt", "w") as file:
    file.write("This is written to a file.\n")
    file.write(f"Name: {name}, Age: {age}\n")

# Append data to file
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")

# ----------------------------
# 6. INPUT FROM FILE
# ----------------------------
# First, let's create a file for reading
with open("sample.txt", "w") as file:
    file.write("Line 1: Hello World\n")
    file.write("Line 2: Python is awesome\n")
    file.write("Line 3: File reading example\n")

# Reading the entire file content
with open("sample.txt", "r") as file:
    content = file.read()
print("\nFile Content:\n", content)

# Reading line by line
with open("sample.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Reading all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
print("\nList of lines:", lines)

# ----------------------------
# 7. ADVANCED PRINTING
# ----------------------------
# Printing in a loop
for i in range(1, 6):
    print(f"Number {i}")

# Printing with alignment
print(f"{'Name':<10} {'Age':>3}")
print(f"{'Ali':<10} {21:>3}")
print(f"{'Sara':<10} {19:>3}")

# ----------------------------
# END OF FILE
# ----------------------------
