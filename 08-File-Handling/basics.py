# file_handling_basics.py
"""
File Handling Basics in Python
==============================
This file explains the basics of working with files in Python — opening,
reading, writing, appending, and closing files — step-by-step with examples.
"""

# ---------------------------
# 1. Opening a File
# ---------------------------
"""
In Python, the `open()` function is used to open a file.
Syntax:
    open(file, mode)

Modes:
    "r"  -> Read mode (default). Opens file for reading. Error if file not found.
    "w"  -> Write mode. Creates a new file or overwrites existing one.
    "a"  -> Append mode. Writes at the end of file without deleting existing data.
    "x"  -> Create mode. Creates new file, error if file exists.
    "b"  -> Binary mode (use with other modes like "rb" or "wb").
    "t"  -> Text mode (default).
"""

# Example: Opening a file in read mode
try:
    f = open("example.txt", "r")  # Tries to open existing file
    print("File opened successfully!")
    f.close()  # Always close after use
except FileNotFoundError:
    print("example.txt not found. Create it first to read.")

# ---------------------------
# 2. Writing to a File
# ---------------------------
"""
When writing ("w"), Python creates the file if it doesn't exist,
or clears existing content before writing new data.
"""
with open("example.txt", "w") as file:
    file.write("Hello, this is a new file.\n")
    file.write("We are learning file handling in Python.\n")
print("Data written to example.txt successfully!")

# ---------------------------
# 3. Reading from a File
# ---------------------------
"""
You can read file content in several ways:
    read()     -> Reads the whole file as a string.
    readline() -> Reads one line at a time.
    readlines()-> Reads all lines into a list.
"""
with open("example.txt", "r") as file:
    print("\nReading entire file content:")
    content = file.read()
    print(content)

# Reading line-by-line
with open("example.txt", "r") as file:
    print("Reading line-by-line:")
    line = file.readline()
    while line:
        print(line.strip())  # strip() removes newlines
        line = file.readline()

# ---------------------------
# 4. Appending to a File
# ---------------------------
"""
Append mode ("a") lets you add content without deleting existing data.
"""
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")
print("Data appended successfully!")

# ---------------------------
# 5. Reading Files as Lists
# ---------------------------
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nFile content as a list:")
    print(lines)

# ---------------------------
# 6. File Paths
# ---------------------------
"""
By default, Python looks for files in the current directory.
For other locations, provide absolute or relative paths.

Example:
    open("C:/Users/YourName/Documents/file.txt", "r")
"""

# ---------------------------
# 7. 'with' Statement Advantage
# ---------------------------
"""
The 'with' statement automatically closes the file after the block ends,
even if an error occurs — making it safer than manual open/close.
"""

# ---------------------------
# 8. Summary
# ---------------------------
"""
1. Use open() with correct mode.
2. Always close the file or use 'with'.
3. Be aware that "w" overwrites files and "a" appends.
4. Use read(), readline(), readlines() for reading content.
5. Handle FileNotFoundError when reading.
"""
