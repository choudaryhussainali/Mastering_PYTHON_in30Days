"""
classes_objects.py
===================

A COMPLETE GUIDE TO CLASSES & OBJECTS IN PYTHON
------------------------------------------------
Think of a *class* as a **blueprint** and an *object* as a **real-world thing built from that blueprint**.

For example:
    - A class could be "Car" (design)
    - An object could be "My red Toyota Corolla" (actual instance)

We use classes to group **data** (attributes) and **functions** (methods) together
to represent a concept in programming.

In Python:
    - Class names use PascalCase by convention (e.g., Car, Person, Animal)
    - Objects are created from classes
"""

# -----------------------------
# 1. DEFINING A SIMPLE CLASS
# -----------------------------
class Car:
    # Class Attribute (shared by ALL objects of this class)
    wheels = 4  # Every car has 4 wheels

    # Constructor method (__init__) — called automatically when creating a new object
    def __init__(self, brand, model, year):
        """
        The __init__ method initializes (sets up) the object with given values.
        'self' refers to the current object being created.
        """
        self.brand = brand    # Instance Attribute
        self.model = model    # Instance Attribute
        self.year = year      # Instance Attribute

    # Instance Method — works on a single object (uses 'self')
    def display_info(self):
        """Displays car details."""
        return f"{self.year} {self.brand} {self.model} with {Car.wheels} wheels"

    # Instance Method — performs an action
    def honk(self):
        """Car horn sound."""
        return f"{self.brand} says Beep Beep!"

# -----------------------------
# 2. CREATING OBJECTS
# -----------------------------
my_car = Car("Toyota", "Corolla", 2020)
your_car = Car("Honda", "Civic", 2019)

# Calling methods
print(my_car.display_info())   # "2020 Toyota Corolla with 4 wheels"
print(your_car.honk())         # "Honda says Beep Beep!"

# -----------------------------
# 3. INSTANCE ATTRIBUTES vs CLASS ATTRIBUTES
# -----------------------------
"""
Instance Attributes:
    - Belong to a specific object
    - Defined using 'self.attribute_name'
    - Can be different for each object

Class Attributes:
    - Belong to the class itself
    - Shared by ALL objects
    - Accessed using ClassName.attribute
"""
print(Car.wheels)    # Access class attribute via class
print(my_car.wheels) # Can also access via object (not recommended to modify this way)

# Changing class attribute
Car.wheels = 6
print(my_car.display_info())  # Now both cars show 6 wheels

# Changing instance attribute (affects only that object)
my_car.brand = "Tesla"
print(my_car.display_info())  # Tesla instead of Toyota

# -----------------------------
# 4. ADDING ATTRIBUTES DYNAMICALLY
# -----------------------------
# You can add attributes to an object at runtime
my_car.color = "Red"  # This attribute exists only for my_car
print(my_car.color)
# print(your_car.color)  # ❌ Will cause AttributeError

# -----------------------------
# 5. DELETING ATTRIBUTES OR OBJECTS
# -----------------------------
# Delete an attribute
del my_car.color
# Delete an object completely
del your_car
# print(your_car)  # ❌ NameError: 'your_car' is not defined

# -----------------------------
# 6. REAL-LIFE ANALOGY
# -----------------------------
"""
Class = House Blueprint
Object = A specific built house

A class is NOT a real object by itself.
It only describes how the object will look and behave.
"""

# -----------------------------
# 7. SPECIAL METHODS
# -----------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Defines string representation for print()."""
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        """Defines representation in interactive shell."""
        return f"Person('{self.name}', {self.age})"

# Creating a Person object
p1 = Person("Alice", 25)
print(p1)  # Calls __str__
print([p1])  # Calls __repr__

# -----------------------------
# 8. SUMMARY OF KEY POINTS
# -----------------------------
"""
- Class: Blueprint for creating objects
- Object: Instance of a class
- Attributes: Variables inside a class (instance or class-level)
- Methods: Functions inside a class
- self: Refers to the current object
- __init__: Constructor for initialization
- Class attributes are shared, instance attributes are unique
- Attributes can be added/removed dynamically
- Special methods (__str__, __repr__, etc.) customize object behavior
"""

# -----------------------------
# 9. QUICK PRACTICE
# -----------------------------
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating and using objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())  # Buddy says Woof!
print(dog2.bark())  # Lucy says Woof!
print(Dog.species)  # Canis familiaris
