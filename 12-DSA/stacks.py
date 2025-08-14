"""
stack.py

Stack Implementation in Python
------------------------------

A Stack is a linear data structure that follows the LIFO principle:
    Last In → First Out

Operations:
-----------
1. push(item) - Add an element to the top of the stack
2. pop()      - Remove and return the top element
3. peek()     - Get the top element without removing it
4. is_empty() - Check if the stack is empty
5. size()     - Get the number of elements in the stack
"""

# -----------------------
# Approach 1: Using Python List
# -----------------------
class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------
# Approach 2: Using collections.deque (Recommended)
# -----------------------
from collections import deque

class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------
# Example Usage
# -----------------------
if __name__ == "__main__":
    print("Stack using list:")
    s1 = StackList()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print("Top element:", s1.peek())
    s1.pop()
    print("Stack size:", s1.size())
    print("Is stack empty?", s1.is_empty())

    print("\nStack using deque:")
    s2 = StackDeque()
    s2.push(100)
    s2.push(200)
    s2.push(300)
    print("Top element:", s2.peek())
    s2.pop()
    print("Stack size:", s2.size())
    print("Is stack empty?", s2.is_empty())
