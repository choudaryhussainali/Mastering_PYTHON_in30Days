"""
collections_module.py

This script explains and demonstrates the usage of Python's built-in
`collections` module, which provides specialized container datatypes
that are alternatives to Python's general-purpose built-in containers 
like dict, list, set, and tuple.

We will cover:
1. Counter
2. namedtuple
3. deque
4. defaultdict
5. OrderedDict
"""

# Importing collections module
import collections

# -------------------------
# 1. Counter
# -------------------------
print("\n=== Counter ===")
from collections import Counter

# Counter counts the frequency of elements in an iterable
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_counter = Counter(numbers)

print("Counter result:", num_counter)  # Shows counts for each element
print("Count of 3:", num_counter[3])   # Get count of a specific element
print("Most common element:", num_counter.most_common(1))  # Returns list of most common items

# -------------------------
# 2. namedtuple
# -------------------------
print("\n=== namedtuple ===")
from collections import namedtuple

# namedtuple creates tuple-like objects with named fields
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)

print("Point p1:", p1)
print("x-coordinate:", p1.x)  # Access by name
print("y-coordinate:", p1.y)

# -------------------------
# 3. deque
# -------------------------
print("\n=== deque ===")
from collections import deque

# deque (double-ended queue) allows fast appends and pops from both ends
dq = deque([1, 2, 3])
print("Initial deque:", dq)

dq.append(4)        # Append to right
dq.appendleft(0)    # Append to left
print("After appends:", dq)

dq.pop()            # Remove from right
dq.popleft()        # Remove from left
print("After pops:", dq)

# -------------------------
# 4. defaultdict
# -------------------------
print("\n=== defaultdict ===")
from collections import defaultdict

# defaultdict automatically creates a default value if key is missing
# Example: list as default factory
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")

print("defaultdict content:", dict(dd))  # Convert to dict for nicer printing

# -------------------------
# 5. OrderedDict
# -------------------------
print("\n=== OrderedDict ===")
from collections import OrderedDict

# OrderedDict remembers the insertion order of keys (In Python 3.7+, normal dict also keeps order)
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

print("OrderedDict content:", od)

# Changing order: move_to_end
od.move_to_end("a")  # Moves key "a" to the end
print("After move_to_end:", od)

# Deleting and re-inserting
del od["b"]
od["b"] = 5
print("After deleting & reinserting 'b':", od)


"""
SUMMARY:
- Counter: Counts frequencies of elements
- namedtuple: Tuple with named fields
- deque: Fast appends/pops from both ends
- defaultdict: Auto-creates default values for missing keys
- OrderedDict: Dictionary that remembers insertion order

These are useful when working with structured or large data in Python.
"""
