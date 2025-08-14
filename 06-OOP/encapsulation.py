"""
Encapsulation in Python
------------------------
Encapsulation is one of the main principles of Object-Oriented Programming (OOP).  
It is the concept of wrapping data (variables) and methods (functions) together into a single unit (class), 
while restricting access to some parts of the object to protect the integrity of the data.

In Python, encapsulation is implemented by:
1. Public members     -> Accessible from anywhere.
2. Protected members  -> Prefix with a single underscore (_) — should be accessed only inside the class and subclasses.
3. Private members    -> Prefix with double underscores (__) — name-mangled and cannot be accessed directly from outside.

Benefits of Encapsulation:
- Data protection (no accidental modification).
- Control over how data is modified.
- Improves maintainability and modularity.
- Makes the code more secure and less error-prone.
"""

# ----------------------------
# Example 1: Basic Encapsulation
# ----------------------------

class Car:
    def __init__(self, brand, speed):
        self.brand = brand             # Public attribute
        self._speed = speed            # Protected attribute (convention: use with caution outside)
        self.__engine_number = "EN12345"  # Private attribute

    # Public method to display details
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self._speed} km/h")
        # Accessing private attribute inside the class is allowed
        print(f"Engine Number: {self.__engine_number}")

    # Public method to update speed safely
    def set_speed(self, new_speed):
        if new_speed > 0:
            self._speed = new_speed
            print(f"Speed updated to {self._speed} km/h")
        else:
            print("Speed must be positive.")

    # Private method (only used internally)
    def __start_engine(self):
        print("Engine started!")

    # Public method that uses the private method
    def start_car(self):
        self.__start_engine()
        print("Car is ready to drive!")


# Create object
car1 = Car("Toyota", 120)

# Accessing public method
car1.display_info()

# Accessing public attribute directly (allowed)
print("\nPublic Access ->", car1.brand)

# Accessing protected attribute (possible but not recommended)
print("Protected Access ->", car1._speed)

# Accessing private attribute directly (will cause AttributeError)
# print(car1.__engine_number)  # ❌ This will throw an error

# Accessing private attribute indirectly (name mangling)
print("Private Access using Name Mangling ->", car1._Car__engine_number)

# Using public method to update protected attribute safely
car1.set_speed(150)

# Starting the car (uses a private method internally)
car1.start_car()


# ----------------------------
# Example 2: Encapsulation in Banking System
# ----------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance              # Private attribute

    # Getter method to safely view balance
    def get_balance(self):
        return f"Account Balance: ${self.__balance}"

    # Setter method to safely deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Setter method to safely withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# Create account
account1 = BankAccount("Hussain Ali", 500)

# Access balance using getter (safe)
print("\n", account1.get_balance())

# Deposit money safely
account1.deposit(200)
print(account1.get_balance())

# Withdraw money safely
account1.withdraw(100)
print(account1.get_balance())

# Trying to directly access private attribute (will fail)
# print(account1.__balance)  # ❌ AttributeError

# Accessing private attribute using name mangling (not recommended)
print("Force Access Private ->", account1._BankAccount__balance)


# ----------------------------
# Summary:
# ----------------------------
# - Public members: Free access everywhere.
# - Protected members: Should be accessed only inside the class or subclasses.
# - Private members: Cannot be accessed directly; use getters/setters for control.
# - Encapsulation protects data and ensures controlled modification.
