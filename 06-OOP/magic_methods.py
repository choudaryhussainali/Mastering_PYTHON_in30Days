"""
magic_methods.py
================

This file explains EVERYTHING about **Magic Methods** (also called "dunder methods")
in Python.

Magic methods are special methods in Python that have double underscores
at the beginning and end of their names, like `__init__`, `__str__`, and `__add__`.

They are "magical" because they allow you to customize the behavior of your
objects in ways that integrate deeply with Python's built-in features.

You have already used some magic methods without realizing it — for example:
- `__init__` runs automatically when creating an object.
- `__str__` controls what is printed when you do `print(object)`.
- `__len__` lets your object work with `len(object)`.
- `__add__` lets you use the `+` operator on your object.

Think of magic methods as **"hooks"** that let you define how your custom class
behaves when used with Python syntax like arithmetic, comparison, iteration, etc.

----------------------------------------------------------------------
REAL-LIFE ANALOGY
----------------------------------------------------------------------
Imagine you are designing a "Robot".
By default, the robot knows how to stand and blink.  
But if you want it to:
- Dance when someone plays music 🎵
- Wave when someone says "hello" 👋
- Speak politely when asked something 🗣️

…you need to program these "special reactions".
Magic methods are like those special reactions for Python objects.

----------------------------------------------------------------------
COMMON CATEGORIES OF MAGIC METHODS
----------------------------------------------------------------------

1. **Object Initialization & Representation**
    - `__init__(self, ...)` → Called when creating a new object.
    - `__repr__(self)` → Developer-friendly representation of the object.
    - `__str__(self)` → User-friendly representation of the object.

2. **Comparison Magic Methods**
    - `__eq__(self, other)` → self == other
    - `__ne__(self, other)` → self != other
    - `__lt__(self, other)` → self < other
    - `__gt__(self, other)` → self > other
    - `__le__(self, other)` → self <= other
    - `__ge__(self, other)` → self >= other

3. **Arithmetic Magic Methods**
    - `__add__(self, other)` → self + other
    - `__sub__(self, other)` → self - other
    - `__mul__(self, other)` → self * other
    - `__truediv__(self, other)` → self / other
    - `__floordiv__(self, other)` → self // other
    - `__mod__(self, other)` → self % other
    - `__pow__(self, other)` → self ** other

4. **Length, Indexing & Iteration**
    - `__len__(self)` → len(self)
    - `__getitem__(self, index)` → self[index]
    - `__setitem__(self, index, value)` → self[index] = value
    - `__delitem__(self, index)` → del self[index]
    - `__iter__(self)` → Makes the object iterable
    - `__next__(self)` → Gets next item in iteration

5. **Context Manager Methods**
    - `__enter__(self)` → Runs at the start of `with` block
    - `__exit__(self, exc_type, exc_value, traceback)` → Runs at the end of `with` block

----------------------------------------------------------------------
EXAMPLES
----------------------------------------------------------------------
"""

# 1. Object initialization and string representation
class Person:
    def __init__(self, name, age):
        self.name = name  # called automatically when object is created
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"  # user-friendly print

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"  # developer-friendly print


p1 = Person("Alice", 25)
print(str(p1))   # Calls __str__()
print(repr(p1))  # Calls __repr__()

# 2. Comparison magic methods
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __eq__(self, other):
        return self.volume == other.volume

    def __lt__(self, other):
        return self.volume < other.volume


box1 = Box(100)
box2 = Box(150)
print(box1 == box2)  # Calls __eq__()
print(box1 < box2)   # Calls __lt__()

# 3. Arithmetic magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)  # vector addition

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Calls __add__()

# 4. Iteration magic methods
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # iterable returns itself

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


for num in MyRange(1, 5):
    print(num, end=" ")  # Outputs: 1 2 3 4


# 5. Context manager magic methods
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()


with FileOpener("test.txt", "w") as f:
    f.write("Hello, Magic Methods!")


"""
----------------------------------------------------------------------
SUMMARY:
----------------------------------------------------------------------
- Magic methods let you define how your object reacts to built-in Python operations.
- They start and end with double underscores, like `__init__`, `__add__`, etc.
- Categories: object creation/representation, comparisons, arithmetic, iteration,
  context managers, and more.
- They make your custom classes work seamlessly with Python syntax.

💡 TIP:
If you ever wonder "Can I make my object work with X syntax?", check the Python
docs for a magic method that supports it.
"""
