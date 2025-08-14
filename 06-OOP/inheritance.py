"""
inheritance.py
-----------------
This file explains **Inheritance** in Python OOP.

🔹 What is Inheritance?
Inheritance is a mechanism where a **child class** (subclass) can **reuse**
the properties and methods of a **parent class** (superclass).

Why use Inheritance?
- Avoid code duplication
- Build hierarchical relationships
- Extend or modify parent functionality
- Promote reusability and maintainability

Syntax:
    class Parent:
        ...
    class Child(Parent):
        ...

Types of Inheritance in Python:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance (combination of above)
"""

# 1️⃣ SINGLE INHERITANCE
print("----- Single Inheritance Example -----")

class Animal:
    """Parent class"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    """Child class inheriting from Animal"""
    def speak(self):
        return f"{self.name} barks."

# Using classes
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks


# 2️⃣ MULTIPLE INHERITANCE
print("\n----- Multiple Inheritance Example -----")

class Walker:
    def walk(self):
        return "Walking..."

class Swimmer:
    def swim(self):
        return "Swimming..."

class Amphibian(Walker, Swimmer):
    pass

frog = Amphibian()
print(frog.walk())  # Output: Walking...
print(frog.swim())  # Output: Swimming...


# 3️⃣ MULTILEVEL INHERITANCE
print("\n----- Multilevel Inheritance Example -----")

class Vehicle:
    def start(self):
        return "Vehicle started."

class Car(Vehicle):
    def drive(self):
        return "Car is driving."

class ElectricCar(Car):
    def charge(self):
        return "Car is charging."

tesla = ElectricCar()
print(tesla.start())   # Vehicle started.
print(tesla.drive())   # Car is driving.
print(tesla.charge())  # Car is charging.


# 4️⃣ HIERARCHICAL INHERITANCE
print("\n----- Hierarchical Inheritance Example -----")

class Shape:
    def area(self):
        return "Calculating area..."

class Circle(Shape):
    def area(self):
        return "Area = π × r²"

class Square(Shape):
    def area(self):
        return "Area = side × side"

circle = Circle()
square = Square()
print(circle.area())  # Area = π × r²
print(square.area())  # Area = side × side


# 5️⃣ USING super()
print("\n----- super() Example -----")

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # Call parent constructor
        self.employee_id = employee_id

    def info(self):
        return f"Name: {self.name}, ID: {self.employee_id}"

emp = Employee("Alice", 101)
print(emp.info())  # Name: Alice, ID: 101


# 6️⃣ METHOD RESOLUTION ORDER (MRO)
print("\n----- Method Resolution Order Example -----")

class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass

obj = D()
print(obj.show())   # Class B
print(D.mro())      # MRO order: D → B → C → A → object


"""
💡 Summary:
- Child classes automatically have access to parent methods unless overridden.
- Use `super()` to call parent methods/constructors.
- Multiple inheritance is possible but can be tricky due to MRO.
- Avoid deep/messy inheritance trees — prefer composition if possible.
"""
