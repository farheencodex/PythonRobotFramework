"""
Topic 14 — Data Structures & Algorithms Overview | Python for Automation Course
==================================================================================
Understanding DSA helps write EFFICIENT automation code — faster searches,
better data organization, optimized test data management.

Concepts Covered:
    1. Stack — LIFO (Last In, First Out)
    2. Queue — FIFO (First In, First Out)
    3. Linked List — Dynamic data storage
    4. Binary Search — Efficient searching
    5. Sorting Algorithms — Bubble Sort, Selection Sort, Python's built-in
    6. Recursion — Functions that call themselves
    7. Big O Notation — Algorithm efficiency

Practice Tasks:
    1. Stack: Browser history (back/forward)
    2. Queue: Test execution queue
    3. Binary Search: Find a test case by ID
    4. Sorting: Sort test cases by priority/duration
    5. Recursion: Directory tree traversal

How to Run:
    python dsa_overview.py
"""

import os
import time
from collections import deque


# ============================================================
# SECTION 1: Stack — LIFO (Last In, First Out)
# ============================================================

print("=" * 60)
print("SECTION 1: Stack — LIFO")
print("=" * 60)

# A STACK is like a stack of plates:
# - You add (push) plates on TOP
# - You remove (pop) plates from TOP
# - Last plate added = first plate removed → LIFO

# Python lists can be used as stacks!
# push → append()
# pop → pop()
# peek → stack[-1]

class Stack:
    """Stack implementation using a Python list."""
    
    def __init__(self):
        self._items = []  # Internal list
    
    def push(self, item):
        """Add item to the top of the stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._items.pop()
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in stack."""
        return len(self._items)
    
    def __str__(self):
        return f"Stack(top → {list(reversed(self._items))})"

# Demo: Using a stack
print("--- Stack Demo ---")
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
print(f"  After pushing A, B, C: {stack}")
print(f"  Peek (top): {stack.peek()}")
print(f"  Pop: {stack.pop()}")  # C (last in, first out)
print(f"  Pop: {stack.pop()}")  # B
print(f"  After two pops: {stack}")
print(f"  Size: {stack.size()}")

# Real-world use: Undo/Redo, Browser Back, Call Stack

print()


# ============================================================
# SECTION 2: Queue — FIFO (First In, First Out)
# ============================================================

print("=" * 60)
print("SECTION 2: Queue — FIFO")
print("=" * 60)

# A QUEUE is like a line at a store:
# - First person in line = first person served
# - Add (enqueue) at the BACK
# - Remove (dequeue) from the FRONT

# Use collections.deque for efficient queues (O(1) on both ends)

class Queue:
    """Queue implementation using collections.deque."""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        """Add item to the back of the queue."""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self._items.popleft()
    
    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in queue."""
        return len(self._items)
    
    def __str__(self):
        return f"Queue(front → {list(self._items)})"

# Demo: Using a queue
print("--- Queue Demo ---")
queue = Queue()
queue.enqueue("Task 1")
queue.enqueue("Task 2")
queue.enqueue("Task 3")
print(f"  After enqueuing 3 tasks: {queue}")
print(f"  Front: {queue.front()}")
print(f"  Dequeue: {queue.dequeue()}")  # Task 1 (first in, first out)
print(f"  Dequeue: {queue.dequeue()}")  # Task 2
print(f"  After two dequeues: {queue}")

# Real-world use: Task scheduling, Print queue, Message queues

print()


# ============================================================
# SECTION 3: Linked List
# ============================================================

print("=" * 60)
print("SECTION 3: Linked List")
print("=" * 60)

# A LINKED LIST stores data in NODES.
# Each node contains:
# 1. Data (the value)
# 2. A reference (pointer) to the NEXT node
#
# Unlike arrays/lists, linked list elements are NOT in contiguous memory.
# Advantage: O(1) insertion/deletion at known position
# Disadvantage: O(n) access (no random access by index)

class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None  # Points to the first node
    
    def append(self, data):
        """Add a node at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add a node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Remove the first node with the given data."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def search(self, data):
        """Check if data exists in the list."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def display(self):
        """Display the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " → ".join(elements) + " → None"

# Demo
print("--- Linked List Demo ---")
ll = LinkedList()
ll.append("Chrome")
ll.append("Firefox")
ll.append("Edge")
print(f"  After append: {ll.display()}")

ll.prepend("Safari")
print(f"  After prepend Safari: {ll.display()}")

ll.delete("Firefox")
print(f"  After delete Firefox: {ll.display()}")

pos = ll.search("Edge")
print(f"  Search 'Edge': found at position {pos}")
pos = ll.search("Opera")
print(f"  Search 'Opera': position {pos} (not found)")

print()


# ============================================================
# SECTION 4: Binary Search
# ============================================================

print("=" * 60)
print("SECTION 4: Binary Search")
print("=" * 60)

# Binary Search works on SORTED data.
# Instead of checking every item (linear search, O(n)),
# it repeatedly divides the search space in half → O(log n)

# How it works:
# 1. Look at the MIDDLE element
# 2. If target == middle → found!
# 3. If target < middle → search LEFT half
# 4. If target > middle → search RIGHT half
# 5. Repeat until found or search space is empty

def binary_search(sorted_list, target):
    """
    Binary search on a sorted list.
    
    Args:
        sorted_list: A sorted list of comparable elements
        target: The value to find
    
    Returns:
        int: Index of the target, or -1 if not found
    """
    left = 0
    right = len(sorted_list) - 1
    steps = 0
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"    Step {steps}: left={left}, right={right}, mid={mid}, "
              f"value={sorted_list[mid]}")
        
        if sorted_list[mid] == target:
            print(f"    Found '{target}' at index {mid} in {steps} steps!")
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    print(f"    '{target}' not found after {steps} steps.")
    return -1

# Demo
sorted_ids = ["TC_001", "TC_002", "TC_003", "TC_004", "TC_005",
              "TC_006", "TC_007", "TC_008", "TC_009", "TC_010"]

print(f"  Sorted list: {sorted_ids}")
print(f"\n  Searching for 'TC_007':")
binary_search(sorted_ids, "TC_007")

print(f"\n  Searching for 'TC_002':")
binary_search(sorted_ids, "TC_002")

# Compare: Linear search would check every item from start
# List of 1000 items: linear = ~500 avg steps, binary = ~10 steps!
# List of 1,000,000: linear = ~500,000, binary = ~20 steps!

print()


# ============================================================
# SECTION 5: Sorting Algorithms
# ============================================================

print("=" * 60)
print("SECTION 5: Sorting Algorithms")
print("=" * 60)

# --- Bubble Sort --- O(n²)
# Compares adjacent elements and swaps if out of order.
# Repeats until no swaps needed.
# Simple but SLOW for large datasets.

def bubble_sort(arr):
    """Bubble Sort — O(n²) time complexity."""
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    swaps = 0
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swaps += 1
                swapped = True
        if not swapped:
            break  # Already sorted!
    
    return arr, swaps

print("--- Bubble Sort ---")
data = [64, 34, 25, 12, 22, 11, 90]
print(f"  Before: {data}")
sorted_data, swap_count = bubble_sort(data)
print(f"  After:  {sorted_data}")
print(f"  Swaps:  {swap_count}")


# --- Selection Sort --- O(n²)
# Finds the minimum element and puts it at the beginning.
# Repeats for the remaining unsorted portion.

def selection_sort(arr):
    """Selection Sort — O(n²) time complexity."""
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(f"\n--- Selection Sort ---")
data = [64, 34, 25, 12, 22, 11, 90]
print(f"  Before: {data}")
print(f"  After:  {selection_sort(data)}")


# --- Python's Built-in Sort --- O(n log n) — TimSort
# ALWAYS use this in production! It's highly optimized.

print(f"\n--- Python's Built-in sort() ---")
data = [64, 34, 25, 12, 22, 11, 90]
print(f"  sorted({data}) = {sorted(data)}")
print(f"  sorted(reverse=True) = {sorted(data, reverse=True)}")

# Sort objects by a key
test_results = [
    {"name": "Login", "duration": 5.2, "priority": "P0"},
    {"name": "Search", "duration": 2.1, "priority": "P1"},
    {"name": "Cart", "duration": 8.3, "priority": "P0"},
    {"name": "Profile", "duration": 1.5, "priority": "P2"},
]

# Sort by duration
by_duration = sorted(test_results, key=lambda x: x["duration"])
print(f"\n  Sorted by duration:")
for t in by_duration:
    print(f"    {t['name']:10s} {t['duration']:.1f}s ({t['priority']})")

# Sort by priority
by_priority = sorted(test_results, key=lambda x: x["priority"])
print(f"\n  Sorted by priority:")
for t in by_priority:
    print(f"    {t['name']:10s} {t['duration']:.1f}s ({t['priority']})")

print()


# ============================================================
# SECTION 6: Recursion
# ============================================================

print("=" * 60)
print("SECTION 6: Recursion")
print("=" * 60)

# RECURSION = a function that calls ITSELF.
# Every recursive function needs:
# 1. BASE CASE — when to stop (prevents infinite loop!)
# 2. RECURSIVE CASE — the function calls itself with a smaller input

# --- Factorial ---
# n! = n × (n-1) × (n-2) × ... × 1
# 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    """Calculate factorial recursively."""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print("--- Factorial ---")
for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")

# --- Fibonacci ---
# Each number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    """Generate the nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\n--- Fibonacci ---")
fib_series = [fibonacci(i) for i in range(10)]
print(f"  First 10: {fib_series}")

# --- Recursion vs Iteration ---
print(f"\n--- Recursion vs Iteration ---")
# Iterative factorial (often more efficient)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"  Recursive 10! = {factorial(10)}")
print(f"  Iterative 10! = {factorial_iterative(10)}")
print(f"  Same result? {factorial(10) == factorial_iterative(10)}")

# NOTE: Recursion can cause StackOverflow for deep recursion.
# Python's default recursion limit is 1000.
# Use iteration for large inputs.

print()


# ============================================================
# SECTION 7: Big O Notation
# ============================================================

print("=" * 60)
print("SECTION 7: Big O Notation")
print("=" * 60)

# Big O describes HOW PERFORMANCE SCALES with input size.
# It tells you the WORST-CASE scenario.

# Common complexities (fastest to slowest):
# ───────────────────────────────────────────
# O(1)       → Constant   → Same time regardless of size
#              Example: dict lookup, list index access
#
# O(log n)   → Logarithmic → Halves the problem each step
#              Example: Binary search
#
# O(n)       → Linear     → Time grows proportionally with input
#              Example: Loop through a list, linear search
#
# O(n log n) → Linearithmic → Optimal comparison sort
#              Example: Python's sorted(), merge sort
#
# O(n²)      → Quadratic  → Nested loops
#              Example: Bubble sort, compare every pair
#
# O(2^n)     → Exponential → Very slow!
#              Example: Naive recursive Fibonacci

print("  Big O Complexity Table:")
print(f"  {'Notation':<12} {'Name':<15} {'n=100':<12} {'n=1000':<12} {'Example'}")
print(f"  {'-'*70}")
print(f"  {'O(1)':<12} {'Constant':<15} {'1':<12} {'1':<12} dict[key]")
print(f"  {'O(log n)':<12} {'Logarithmic':<15} {'~7':<12} {'~10':<12} binary search")
print(f"  {'O(n)':<12} {'Linear':<15} {'100':<12} {'1000':<12} for loop")
print(f"  {'O(n log n)':<12} {'Linearithmic':<15} {'~664':<12} {'~9966':<12} sorted()")
print(f"  {'O(n²)':<12} {'Quadratic':<15} {'10,000':<12} {'1,000,000':<12} bubble sort")
print(f"  {'O(2^n)':<12} {'Exponential':<15} {'1.27e30':<12} {'Too big!':<12} naive fib")

# Practical demo: Timing different approaches
print(f"\n--- Timing: Linear vs Binary Search ---")

sorted_data = list(range(100000))  # 100,000 items
target = 87654

# Linear search
start = time.time()
for item in sorted_data:
    if item == target:
        break
linear_time = time.time() - start

# Binary search
start = time.time()
left, right = 0, len(sorted_data) - 1
while left <= right:
    mid = (left + right) // 2
    if sorted_data[mid] == target:
        break
    elif sorted_data[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
binary_time = time.time() - start

print(f"  List size: {len(sorted_data):,}")
print(f"  Linear search: {linear_time*1000:.3f}ms")
print(f"  Binary search: {binary_time*1000:.3f}ms")
if linear_time > 0 and binary_time > 0:
    ratio = linear_time / binary_time if binary_time > 0 else float('inf')
    print(f"  Binary is ~{ratio:.0f}x faster!")

print()


# ============================================================
# PRACTICE TASK 1: Browser History Stack
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Browser History Stack")
print("=" * 60)

class BrowserHistory:
    """Browser navigation history using a Stack."""
    
    def __init__(self, homepage="https://boodmo.com"):
        self.back_stack = Stack()    # Pages to go back to
        self.forward_stack = Stack()  # Pages to go forward to
        self.current_page = homepage
        print(f"  🏠 Home: {homepage}")
    
    def navigate(self, url):
        """Navigate to a new URL."""
        self.back_stack.push(self.current_page)
        self.current_page = url
        # Clear forward history (can't go forward after new navigation)
        self.forward_stack = Stack()
        print(f"  → Navigate: {url}")
    
    def back(self):
        """Go back to the previous page."""
        if self.back_stack.is_empty():
            print(f"  ← Back: No history!")
            return
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"  ← Back: {self.current_page}")
    
    def forward(self):
        """Go forward to the next page."""
        if self.forward_stack.is_empty():
            print(f"  → Forward: No forward history!")
            return
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"  → Forward: {self.current_page}")
    
    def current(self):
        print(f"  📍 Current: {self.current_page}")

# Demo
browser = BrowserHistory()
browser.navigate("https://boodmo.com/search")
browser.navigate("https://boodmo.com/product/123")
browser.navigate("https://boodmo.com/cart")
browser.current()

print()
browser.back()   # → /product/123
browser.back()   # → /search
browser.back()   # → / (home)
browser.back()   # No history!
browser.current()

print()
browser.forward()  # → /search
browser.forward()  # → /product/123
browser.current()


# ============================================================
# PRACTICE TASK 2: Test Execution Queue
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Test Execution Queue")
print("=" * 60)

class TestExecutionQueue:
    """A queue for managing test case execution order."""
    
    def __init__(self):
        self.queue = Queue()
        self.completed = []
    
    def add_test(self, test_id, test_name, priority="P1"):
        """Add a test to the queue."""
        self.queue.enqueue({
            "id": test_id,
            "name": test_name,
            "priority": priority,
            "status": "Queued"
        })
        print(f"  + Queued: [{test_id}] {test_name}")
    
    def execute_next(self):
        """Execute the next test in the queue."""
        if self.queue.is_empty():
            print(f"  Queue is empty — all tests executed!")
            return None
        
        test = self.queue.dequeue()
        test["status"] = "Pass" if hash(test["name"]) % 3 != 0 else "Fail"
        self.completed.append(test)
        
        icon = "✓" if test["status"] == "Pass" else "✗"
        print(f"  {icon} Executed: [{test['id']}] {test['name']} → {test['status']}")
        return test
    
    def execute_all(self):
        """Execute all tests in the queue."""
        print(f"\n  Executing all {self.queue.size()} tests...")
        while not self.queue.is_empty():
            self.execute_next()
    
    def summary(self):
        """Print execution summary."""
        total = len(self.completed)
        passed = sum(1 for t in self.completed if t["status"] == "Pass")
        failed = total - passed
        print(f"\n  Summary: {total} total | {passed} pass | {failed} fail")

# Demo
test_queue = TestExecutionQueue()
test_queue.add_test("TC_001", "Login Test", "P0")
test_queue.add_test("TC_002", "Search Test", "P1")
test_queue.add_test("TC_003", "Cart Test", "P0")
test_queue.add_test("TC_004", "Checkout Test", "P0")
test_queue.add_test("TC_005", "Profile Test", "P2")

test_queue.execute_all()
test_queue.summary()


# ============================================================
# PRACTICE TASK 3: Binary Search for Test Cases
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Binary Search — Find Test Case")
print("=" * 60)

# Sorted test case database
test_database = [
    {"id": "TC_001", "name": "Login Valid", "module": "Auth"},
    {"id": "TC_002", "name": "Login Invalid", "module": "Auth"},
    {"id": "TC_003", "name": "Signup", "module": "Auth"},
    {"id": "TC_004", "name": "Search Products", "module": "Search"},
    {"id": "TC_005", "name": "Filter Results", "module": "Search"},
    {"id": "TC_006", "name": "Add to Cart", "module": "Cart"},
    {"id": "TC_007", "name": "Update Quantity", "module": "Cart"},
    {"id": "TC_008", "name": "Remove Item", "module": "Cart"},
    {"id": "TC_009", "name": "Checkout", "module": "Order"},
    {"id": "TC_010", "name": "Payment", "module": "Order"},
]

def find_test_case(database, target_id):
    """Find a test case by ID using binary search."""
    left = 0
    right = len(database) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        mid_id = database[mid]["id"]
        
        if mid_id == target_id:
            print(f"  Found in {comparisons} comparisons!")
            tc = database[mid]
            print(f"  ID: {tc['id']}, Name: {tc['name']}, Module: {tc['module']}")
            return database[mid]
        elif mid_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"  Not found after {comparisons} comparisons.")
    return None

# Search for various test cases
for tc_id in ["TC_006", "TC_001", "TC_010", "TC_011"]:
    print(f"\n  Searching for {tc_id}:")
    find_test_case(test_database, tc_id)


# ============================================================
# PRACTICE TASK 4: Sort Test Cases by Priority/Duration
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Sorting Test Cases")
print("=" * 60)

test_cases = [
    {"id": "TC_001", "name": "Login", "priority": "P0", "duration": 5.2},
    {"id": "TC_002", "name": "Search", "priority": "P1", "duration": 2.1},
    {"id": "TC_003", "name": "Cart", "priority": "P0", "duration": 8.3},
    {"id": "TC_004", "name": "Profile", "priority": "P2", "duration": 1.5},
    {"id": "TC_005", "name": "Checkout", "priority": "P0", "duration": 12.0},
    {"id": "TC_006", "name": "Settings", "priority": "P2", "duration": 0.8},
    {"id": "TC_007", "name": "Logout", "priority": "P1", "duration": 1.2},
]

def print_test_list(tests, title):
    print(f"\n  --- {title} ---")
    print(f"  {'ID':<10} {'Name':<12} {'Priority':<10} {'Duration'}")
    print(f"  {'-'*42}")
    for tc in tests:
        print(f"  {tc['id']:<10} {tc['name']:<12} {tc['priority']:<10} {tc['duration']:.1f}s")

# Sort by priority (P0 first)
by_priority = sorted(test_cases, key=lambda x: x["priority"])
print_test_list(by_priority, "Sorted by Priority")

# Sort by duration (fastest first)
by_duration = sorted(test_cases, key=lambda x: x["duration"])
print_test_list(by_duration, "Sorted by Duration (fastest first)")

# Sort by duration (slowest first)
by_duration_desc = sorted(test_cases, key=lambda x: x["duration"], reverse=True)
print_test_list(by_duration_desc, "Sorted by Duration (slowest first)")

# Sort by priority, then by duration
by_priority_duration = sorted(test_cases, key=lambda x: (x["priority"], x["duration"]))
print_test_list(by_priority_duration, "Sorted by Priority → Duration")


# ============================================================
# PRACTICE TASK 5: Recursive Directory Traversal
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 5: Recursive Directory Traversal")
print("=" * 60)

def list_files_recursive(directory, indent=0, max_depth=3):
    """
    Recursively list all files and directories.
    
    Args:
        directory: Root directory to start from
        indent: Current indentation level
        max_depth: Maximum recursion depth
    """
    if indent > max_depth:
        print("  " + "  " * indent + "... (max depth reached)")
        return
    
    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        print("  " + "  " * indent + "(permission denied)")
        return
    
    file_count = 0
    dir_count = 0
    
    for item in items:
        # Skip hidden and cache files
        if item.startswith((".", "__pycache__")):
            continue
        
        full_path = os.path.join(directory, item)
        prefix = "  " * (indent + 1)
        
        if os.path.isdir(full_path):
            dir_count += 1
            print(f"  {prefix}📁 {item}/")
            list_files_recursive(full_path, indent + 1, max_depth)
        else:
            file_count += 1
            size = os.path.getsize(full_path)
            print(f"  {prefix}📄 {item} ({size:,} bytes)")
    
    return file_count, dir_count

# Traverse the project
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

print(f"\n  Project: {os.path.basename(project_root)}")
print(f"  Root: {project_root}")
print()
list_files_recursive(project_root)

print("\n--- Topic 14 Complete! ---")
