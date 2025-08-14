"""
polymorphism.py

Polymorphism in Python:
-----------------------
The term "polymorphism" comes from Greek, meaning "many forms".
In programming, it refers to the ability of a function, method, or operator 
to behave differently based on the object or data type it is applied to.

In Python OOP, polymorphism allows us to define methods in the child class
with the same name as in the parent class, but with different behaviors.
It can also be seen when different classes have methods with the same name
but unrelated inheritance — yet Python treats them interchangeably.

Why it matters:
---------------
Polymorphism makes code more flexible, reusable, and easier to extend.
You can write generic functions that work with different types of objects,
as long as they implement the same method name.
"""

# =========================
# 1. Polymorphism with Functions
# =========================

# A single function can take different types of objects and behave accordingly.
def add(a, b):
    """
    Demonstrates function polymorphism.
    Works with numbers (addition) and strings (concatenation).
    """
    return a + b  # '+' works differently for different data types

print("Function Polymorphism Examples:")
print(add(3, 5))       # Integer addition -> 8
print(add("Hi, ", "Ali"))  # String concatenation -> "Hi, Ali"
print(add([1, 2], [3, 4])) # List concatenation -> [1, 2, 3, 4]
print("-" * 50)


# =========================
# 2. Polymorphism with Class Methods
# =========================

class Dog:
    def speak(self):
        return "Woof! 🐶"

class Cat:
    def speak(self):
        return "Meow! 🐱"

class Cow:
    def speak(self):
        return "Moo! 🐄"

# A function that works with ANY object having a 'speak' method
def animal_sound(animal):
    """
    This function doesn't care which class the object belongs to.
    As long as it has a 'speak' method, it will work.
    """
    print(animal.speak())

print("Class Method Polymorphism Examples:")
for creature in [Dog(), Cat(), Cow()]:
    animal_sound(creature)
print("-" * 50)


# =========================
# 3. Polymorphism in Inheritance
# =========================

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly high in the sky.")

class Penguin(Bird):
    def flight(self):
        print("Penguins cannot fly, they swim instead.")

print("Polymorphism via Inheritance:")
for bird in [Sparrow(), Penguin()]:
    bird.intro()   # Same method from parent
    bird.flight()  # Overridden method behaves differently
print("-" * 50)


# =========================
# 4. Real-world Example: Payment System
# =========================

class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden.")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}."

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}."

class CryptoPayment(Payment):
    def process_payment(self, amount):
        return f"Processing cryptocurrency payment of ${amount}."

def complete_purchase(payment_method, amount):
    """
    This function works with ANY payment method object
    that implements 'process_payment'.
    """
    print(payment_method.process_payment(amount))

print("Real-world Payment Example with Polymorphism:")
methods = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]
for method in methods:
    complete_purchase(method, 100)
print("-" * 50)


# =========================
# 5. Built-in Polymorphism in Python
# =========================

# len() behaves differently for strings, lists, tuples, etc.
print("Built-in Function Polymorphism Examples:")
print(len("Hello"))        # String length -> 5
print(len([1, 2, 3]))      # List length -> 3
print(len((10, 20, 30, 40)))  # Tuple length -> 4

# '+' works for numbers, strings, lists...
print(5 + 10)           # Integer addition
print("AI " + "Engineer") # String concatenation
print([1, 2] + [3, 4])  # List concatenation


"""
Key Takeaways:
--------------
1. Polymorphism allows one interface to be used for different underlying forms.
2. Reduces code duplication and increases flexibility.
3. Works with:
   - Functions (same function name, different data types)
   - Class methods (same method name in different classes)
   - Inheritance (method overriding)
   - Built-in functions/operators
4. You don't need to know the exact type of object — 
   you just call the method, and Python resolves the correct one.
"""
