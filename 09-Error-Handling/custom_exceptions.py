"""
custom_exceptions.py

This file explains everything about creating and using CUSTOM EXCEPTIONS in Python.

────────────────────────────────────────
📌 WHAT ARE CUSTOM EXCEPTIONS?
────────────────────────────────────────
- In Python, we can raise built-in exceptions (like ValueError, TypeError).
- Sometimes, these built-in exceptions are not enough for our specific needs.
- Custom exceptions are user-defined error classes that help make code more readable,
  organized, and meaningful.
- We create them by subclassing (inheriting) from Python's built-in `Exception` class.

────────────────────────────────────────
📌 WHY USE CUSTOM EXCEPTIONS?
────────────────────────────────────────
1. Provide meaningful error names for specific problems.
2. Make debugging easier.
3. Help other developers understand what went wrong.
4. Allow structured exception handling.

────────────────────────────────────────
📌 HOW TO CREATE A CUSTOM EXCEPTION?
────────────────────────────────────────
- Syntax:
    class MyCustomError(Exception):
        pass

- Best Practice: 
  - Inherit from `Exception` (not `BaseException`, because that’s reserved for system exits).
  - Optionally define `__init__` to accept custom error messages or extra data.
"""

# ──────────────────────────────────────
# 1️⃣ BASIC CUSTOM EXCEPTION
# ──────────────────────────────────────
class MyCustomError(Exception):
    """A simple custom exception without extra logic."""
    pass


# ──────────────────────────────────────
# 2️⃣ CUSTOM EXCEPTION WITH MESSAGE
# ──────────────────────────────────────
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Provided age: {age}")


# ──────────────────────────────────────
# 3️⃣ MULTIPLE CUSTOM EXCEPTIONS
# ──────────────────────────────────────
class BankError(Exception):
    """Base class for all banking-related errors."""
    pass

class InsufficientFundsError(BankError):
    """Raised when withdrawal amount is greater than balance."""
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds! Balance: {balance}, Withdrawal: {amount}")

class NegativeDepositError(BankError):
    """Raised when deposit amount is negative."""
    def __init__(self, amount):
        super().__init__(f"Deposit amount cannot be negative: {amount}")


# ──────────────────────────────────────
# 4️⃣ USING CUSTOM EXCEPTIONS
# ──────────────────────────────────────
def check_age(age):
    """Validates the provided age."""
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    return f"Age {age} is valid."

def withdraw(balance, amount):
    """Withdraws amount from balance."""
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

def deposit(balance, amount):
    """Deposits amount to balance."""
    if amount < 0:
        raise NegativeDepositError(amount)
    return balance + amount


# ──────────────────────────────────────
# 5️⃣ DEMONSTRATION OF USAGE
# ──────────────────────────────────────
if __name__ == "__main__":
    # Example 1: Simple Custom Exception
    try:
        raise MyCustomError("This is my custom error!")
    except MyCustomError as e:
        print("Caught MyCustomError:", e)

    print("-" * 50)

    # Example 2: Age validation
    try:
        print(check_age(150))  # Invalid age
    except InvalidAgeError as e:
        print("Caught InvalidAgeError:", e)

    print("-" * 50)

    # Example 3: Banking Operations
    balance = 1000
    try:
        balance = withdraw(balance, 1500)  # More than balance
    except InsufficientFundsError as e:
        print("Caught InsufficientFundsError:", e)

    print("-" * 50)

    try:
        balance = deposit(balance, -200)  # Negative deposit
    except NegativeDepositError as e:
        print("Caught NegativeDepositError:", e)

    print("-" * 50)

    # Successful operations
    try:
        balance = deposit(balance, 500)
        balance = withdraw(balance, 200)
        print(f"Final Balance: {balance}")
    except BankError as e:
        print("Bank Error:", e)

"""
────────────────────────────────────────
📌 BEST PRACTICES FOR CUSTOM EXCEPTIONS
────────────────────────────────────────
✅ Inherit from Exception (not BaseException).
✅ Keep exception names descriptive and end with 'Error'.
✅ Group related exceptions under a base custom exception class.
✅ Provide meaningful error messages.
✅ Use them to make code cleaner and easier to debug.

────────────────────────────────────────
📌 REAL-WORLD EXAMPLES
────────────────────────────────────────
- Web apps: `InvalidCredentialsError`, `PermissionDeniedError`
- Banking systems: `OverdraftError`, `AccountNotFoundError`
- Data processing: `InvalidFileFormatError`, `MissingDataError`
"""
