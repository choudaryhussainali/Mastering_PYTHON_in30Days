"""
nested-if.py
-----------------
This file explains the concept of "Nested if" statements in Python.

A "nested if" is an if statement inside another if statement.
It allows you to check multiple conditions in a structured, step-by-step way.

Think of it like this:
    - You check one condition first.
    - If it’s true, THEN you check another condition inside it.
    - You can keep nesting more if statements as needed.

Use Cases:
    1. Multi-step decisions (e.g., security checks, eligibility criteria).
    2. Breaking large decision-making into smaller steps.
    3. Creating a logical hierarchy of checks.

Syntax:
--------
if condition1:
    # if condition1 is True, then check another condition
    if condition2:
        # if condition2 is also True
        # do something
    else:
        # condition2 was False
else:
    # condition1 was False
"""

# Example 1: Simple Nested if
age = 20
citizenship = "Pakistan"

if age >= 18:
    print("Step 1: Age requirement passed.")
    if citizenship == "Pakistan":
        print("Step 2: Citizenship requirement passed.")
        print("✅ You are eligible to vote.")
    else:
        print("❌ Citizenship requirement not met.")
else:
    print("❌ Age requirement not met.")

# --------------------------------------------

# Example 2: Multi-level nesting
temperature = 30
is_raining = False
has_umbrella = True

if temperature > 25:
    print("It's a warm day.")
    if is_raining:
        print("It’s raining.")
        if has_umbrella:
            print("You can go outside with your umbrella.")
        else:
            print("Better stay inside to avoid getting wet.")
    else:
        print("No rain today — perfect for going outside!")
else:
    print("It's a cool or cold day.")

# --------------------------------------------

# Example 3: Nested if for grading system
marks = 85

if marks >= 50:
    print("You passed the exam.")
    if marks >= 80:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("You failed the exam.")

"""
Best Practices for Nested if:
1. Use nested ifs only when conditions depend on each other.
2. Avoid too much nesting — it makes code harder to read.
3. Consider combining conditions using logical operators (and, or)
   when possible, instead of excessive nesting.
4. Indentation is important in Python — each nested block should be indented consistently.
"""
