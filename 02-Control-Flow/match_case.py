# match_cases.py
"""
Title: Python match-case Statements (Pattern Matching)
Description:
    This file explains the 'match-case' statement in Python in detail.
    Pattern matching using 'match-case' was introduced in Python 3.10
    and is somewhat similar to 'switch-case' statements in other languages.
    
    It allows you to match a value against multiple patterns and
    execute code depending on which pattern matches.

Topics Covered:
    1. Introduction to match-case
    2. Basic syntax
    3. Simple example
    4. Using multiple values in one case
    5. Using the default case (case _)
    6. Matching with if conditions (guards)
    7. Summary

Note:
    match-case is **case-sensitive** when comparing strings.
    Always make sure your Python version is 3.10 or higher.
"""

# 1. Introduction to match-case
# ------------------------------
# The 'match' keyword starts the pattern matching block.
# The 'case' keyword checks for a specific value or pattern.
# 'case _' acts like a default or "else" statement (matches anything).

# 2. Basic Syntax:
"""
match variable:
    case value1:
        # code if variable == value1
    case value2:
        # code if variable == value2
    case _:
        # default case if no other matches
"""

# 3. Simple example
print("=== Simple match-case example ===")
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":  # Multiple values in one case
        print("It's weekend!")
    case _:
        print("Midweek days are busy.")

# 4. Using multiple values in one case
# ------------------------------------
print("\n=== Multiple values in one case ===")
color = "green"

match color:
    case "red" | "blue" | "green":
        print("This color is in our primary list.")
    case _:
        print("This is some other color.")

# 5. Default case with case _
# ---------------------------
# '_' means "match anything" and is used as the default if no other case matches.
print("\n=== Default case example ===")
fruit = "banana"

match fruit:
    case "apple":
        print("An apple a day keeps the doctor away!")
    case "mango":
        print("Sweet mangoes are in season.")
    case _:
        print("Unknown fruit.")

# 6. Matching with if conditions (guards)
# ---------------------------------------
# You can add an 'if' condition to a case to add extra checks.
print("\n=== match-case with condition (guard) ===")
number = 15

match number:
    case n if n < 0:
        print("Negative number.")
    case n if n == 0:
        print("Zero.")
    case n if n % 2 == 0:
        print("Positive even number.")
    case _:
        print("Positive odd number.")

# 7. Summary:
"""
- match-case is like switch-case but more powerful.
- case _ works like a default case.
- You can combine multiple values using '|'.
- Guards (if conditions) allow more complex matching.
- Works with Python 3.10+ only.
"""

