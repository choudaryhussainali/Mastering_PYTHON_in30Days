"""
=======================================
FILE HANDLING IN PYTHON - read_write_text.py
=======================================

This script covers everything about reading and writing **text files** in Python:
1. Opening files in different modes
2. Writing to files
3. Reading from files
4. Working with `with` statement (best practice)
5. Reading line-by-line
6. Appending to files
7. Handling file paths
8. Exception handling for file operations

---------------------------------------
FILE MODES:
---------------------------------------
'r'  -> Read (default mode) - file must exist
'w'  -> Write - creates new file or overwrites existing
'a'  -> Append - creates file if it doesn't exist
'r+' -> Read and write
'w+' -> Write and read (overwrites file)
'a+' -> Append and read

NOTE: By default, files are opened in text mode.
For binary files, add 'b' to the mode ('rb', 'wb', etc.)
"""

import os

# -------------------------------
# 1. Writing to a file
# -------------------------------

# Method 1: Using open() and close()
file_path = "sample.txt"
f = open(file_path, "w")  # 'w' creates/overwrites the file
f.write("Hello, World!\n")
f.write("This is the first file write example.\n")
f.close()  # Always close the file when done

# Method 2: Using 'with' (Best Practice)
# 'with' automatically closes the file after the block
with open(file_path, "w") as file:
    file.write("Overwritten with new content.\n")
    file.write("Python file handling is easy!\n")

# -------------------------------
# 2. Reading from a file
# -------------------------------

# Read the entire file as a single string
with open(file_path, "r") as file:
    content = file.read()
    print("=== Reading Entire File ===")
    print(content)

# -------------------------------
# 3. Reading line by line
# -------------------------------

# Method 1: Using for loop
with open(file_path, "r") as file:
    print("=== Reading Line by Line ===")
    for line in file:
        print(line.strip())  # strip() removes \n

# Method 2: Using readlines()
with open(file_path, "r") as file:
    lines = file.readlines()
    print("=== List of Lines ===")
    print(lines)

# Method 3: Using readline()
with open(file_path, "r") as file:
    print("=== Reading Single Line ===")
    first_line = file.readline()
    print(first_line.strip())

# -------------------------------
# 4. Appending to a file
# -------------------------------
with open(file_path, "a") as file:
    file.write("Appended line 1.\n")
    file.write("Appended line 2.\n")

# Show updated content
with open(file_path, "r") as file:
    print("=== After Appending ===")
    print(file.read())

# -------------------------------
# 5. Using absolute paths
# -------------------------------
absolute_path = os.path.abspath(file_path)
print(f"Absolute Path of file: {absolute_path}")

# -------------------------------
# 6. Exception handling
# -------------------------------
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File does not exist!")
except IOError:
    print("Error: An I/O error occurred!")

# -------------------------------
# 7. Writing list of strings to file
# -------------------------------
lines_to_write = [
    "Line 1: Python is powerful.\n",
    "Line 2: File handling is essential.\n",
    "Line 3: Practice makes perfect.\n"
]

with open("list_example.txt", "w") as file:
    file.writelines(lines_to_write)

print("List of strings written to 'list_example.txt'.")

# -------------------------------
# 8. Reading file safely if it exists
# -------------------------------
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print("=== Safe File Read ===")
        print(file.read())
else:
    print(f"{file_path} does not exist.")

"""
---------------------------------------
KEY BEST PRACTICES:
---------------------------------------
✅ Always use 'with open(...)' instead of manually closing files.
✅ Handle exceptions for missing files.
✅ Use absolute paths when working with files outside your script folder.
✅ For large files, read line-by-line instead of reading the whole file at once.
✅ Be careful with 'w' mode as it overwrites existing files.
"""

