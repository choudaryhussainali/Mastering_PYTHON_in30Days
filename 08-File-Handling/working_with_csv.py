"""
working_with_csv.py

This script explains how to work with CSV (Comma-Separated Values) files in Python.

We will cover:
1. What is a CSV file?
2. Reading CSV files
3. Writing CSV files
4. Appending data to CSV files
5. Reading into dictionaries
6. Writing from dictionaries
7. Common CSV pitfalls and tips
"""

import csv

# ----------------------------------------------------
# 1. WHAT IS A CSV FILE?
# ----------------------------------------------------
# - A CSV (Comma-Separated Values) file stores tabular data in plain text format.
# - Each row is on a new line, and each value is separated by a delimiter (commonly a comma ',').
# - Example content:
#     Name, Age, Country
#     Alice, 25, USA
#     Bob, 30, UK
# - CSV files are widely used for data exchange between applications (Excel, databases, etc.)

# ----------------------------------------------------
# 2. WRITING TO A CSV FILE
# ----------------------------------------------------
# Let's create a CSV file and write some data to it.
people_data = [
    ["Name", "Age", "Country"],
    ["Alice", 25, "USA"],
    ["Bob", 30, "UK"],
    ["Charlie", 28, "Canada"]
]

with open("people.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(people_data)  # Write multiple rows at once

print("✅ 'people.csv' created and written successfully.")

# ----------------------------------------------------
# 3. READING A CSV FILE
# ----------------------------------------------------
# Reading data back from the file
with open("people.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\n📂 Reading CSV file content:")
    for row in reader:
        print(row)  # Each row is a list of strings

# ----------------------------------------------------
# 4. APPENDING DATA TO A CSV FILE
# ----------------------------------------------------
# Adding a new record without overwriting the file
with open("people.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["David", 35, "Australia"])

print("\n✅ Data appended to 'people.csv'.")

# ----------------------------------------------------
# 5. READING CSV FILE INTO DICTIONARIES
# ----------------------------------------------------
# Sometimes, you want data with keys (column names).
with open("people.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\n📂 Reading CSV as dictionaries:")
    for row in reader:
        print(row)  # Each row is an OrderedDict with column names as keys

# ----------------------------------------------------
# 6. WRITING DICTIONARIES TO CSV
# ----------------------------------------------------
people_dict_data = [
    {"Name": "Emma", "Age": 22, "Country": "Germany"},
    {"Name": "Liam", "Age": 29, "Country": "France"}
]

with open("people_dict.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "Country"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write column names
    writer.writerows(people_dict_data)  # Write data rows

print("\n✅ 'people_dict.csv' created successfully.")

# ----------------------------------------------------
# 7. COMMON PITFALLS AND TIPS
# ----------------------------------------------------
# - Always open CSV files with newline="" to avoid blank lines in Windows.
# - Specify encoding (e.g., utf-8) to handle special characters.
# - Use DictReader and DictWriter for easier handling with named columns.
# - If your CSV uses a different delimiter (e.g., semicolon ';'), pass it like:
#     csv.reader(file, delimiter=';')
# - For very large CSV files, consider using the `pandas` library for faster processing.

print("\n💡 CSV handling demo completed successfully.")
