"""
queues.py

Queue Implementation in Python
------------------------------
A Queue is a linear data structure that follows the FIFO principle:
    First In → First Out

Operations:
-----------
1. enqueue(item) - Add an element to the rear of the queue
2. dequeue()     - Remove and return the front element
3. peek()        - Get the front element without removing it
4. is_empty()    - Check if the queue is empty
5. size()        - Get the number of elements in the queue
"""

# -----------------------
# Approach 1: Using Python list
# -----------------------

class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# -----------------------
# Approach 2: Using collections.deque (Recommended)
# -----------------------
from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.queue.popleft()
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# -----------------------
# Example usage
# -----------------------
if __name__ == "__main__":
    print("Queue using list:")
    q1 = QueueList()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print("Front element:", q1.peek())
    q1.dequeue()
    q1.dequeue()
    print("Queue size:", q1.size())
    print("Is queue empty?", q1.is_empty())

    print("\nQueue using deque:")
    q2 = QueueDeque()
    q2.enqueue(100)
    q2.enqueue(200)
    q2.enqueue(300)
    print("Front element:", q2.peek())
    q2.dequeue()
    q2.dequeue()
    print("Queue size:", q2.size())
    print("Is queue empty?", q2.is_empty())
