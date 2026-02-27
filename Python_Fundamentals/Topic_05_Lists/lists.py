"""
Topic 5 — Lists (Most Used in Automation) | Python for Automation Course
=========================================================================
Lists are the MOST used data structure in automation — storing test cases,
browser lists, URLs, test data rows, element locators, and more.

Concepts Covered:
    - List creation, indexing, negative indexing, slicing
    - List mutability
    - List methods — append, insert, extend, remove, pop, clear, sort, reverse,
      index, count, copy
    - len(), min(), max(), sum()
    - List comprehension
    - Nested lists
    - Iterating over a list
    - Checking membership with 'in'

Practice Tasks:
    1. Create and manipulate a test case list
    2. Filter failed test cases using list comprehension
    3. Remove duplicates using set conversion
    4. Find second-highest execution time

How to Run:
    python lists.py
"""


# ============================================================
# SECTION 1: List Creation, Indexing, and Slicing
# ============================================================

print("=" * 60)
print("SECTION 1: List Creation, Indexing, and Slicing")
print("=" * 60)

# --- List Creation ---
# Lists are ordered, mutable collections enclosed in square brackets []
# They can contain ANY data type and can mix types (though not recommended)

empty_list = []                          # Empty list
numbers = [1, 2, 3, 4, 5]               # List of integers
browsers = ["Chrome", "Firefox", "Edge"]  # List of strings
mixed = [1, "hello", 3.14, True, None]   # Mixed types (possible but avoid)
nested = [[1, 2], [3, 4], [5, 6]]       # Nested list (list of lists)

# Using list() constructor
from_range = list(range(1, 6))           # [1, 2, 3, 4, 5]
from_string = list("Python")             # ['P', 'y', 't', 'h', 'o', 'n']

print(f"Numbers: {numbers}")
print(f"Browsers: {browsers}")
print(f"From range: {from_range}")
print(f"From string: {from_string}")

# --- Indexing ---
# Lists use 0-based indexing (same as strings)
tc_ids = ["TC001", "TC002", "TC003", "TC004", "TC005"]
#          [0]      [1]      [2]      [3]      [4]      ← positive
#          [-5]     [-4]     [-3]     [-2]     [-1]     ← negative

print(f"\ntc_ids = {tc_ids}")
print(f"tc_ids[0]  = {tc_ids[0]}")      # TC001 — first element
print(f"tc_ids[2]  = {tc_ids[2]}")      # TC003 — third element
print(f"tc_ids[-1] = {tc_ids[-1]}")     # TC005 — last element
print(f"tc_ids[-2] = {tc_ids[-2]}")     # TC004 — second to last

# --- Slicing ---
# Syntax: list[start:stop:step]
print(f"\ntc_ids[1:4]  = {tc_ids[1:4]}")    # ['TC002', 'TC003', 'TC004']
print(f"tc_ids[:3]   = {tc_ids[:3]}")       # ['TC001', 'TC002', 'TC003']
print(f"tc_ids[2:]   = {tc_ids[2:]}")       # ['TC003', 'TC004', 'TC005']
print(f"tc_ids[::2]  = {tc_ids[::2]}")      # ['TC001', 'TC003', 'TC005'] — every 2nd
print(f"tc_ids[::-1] = {tc_ids[::-1]}")     # Reversed list

print()


# ============================================================
# SECTION 2: List Mutability
# ============================================================
# Unlike strings, lists ARE MUTABLE — you CAN change elements in-place.

print("=" * 60)
print("SECTION 2: List Mutability")
print("=" * 60)

statuses = ["Pass", "Fail", "Pass", "Blocked"]
print(f"Original: {statuses}")

# Change an element by index
statuses[1] = "Pass"  # Changed "Fail" to "Pass" at index 1
print(f"After statuses[1] = 'Pass': {statuses}")

# Change a slice (replace multiple elements)
statuses[2:4] = ["Fail", "Skip"]
print(f"After slice replacement: {statuses}")

# Delete an element using del
del statuses[0]
print(f"After del statuses[0]: {statuses}")

print()


# ============================================================
# SECTION 3: List Methods
# ============================================================

print("=" * 60)
print("SECTION 3: List Methods")
print("=" * 60)

# --- Adding Elements ---
print("--- Adding Elements ---")

tc_list = ["TC001", "TC002", "TC003"]
print(f"Original: {tc_list}")

# append() — adds ONE element to the END
tc_list.append("TC004")
print(f"append('TC004'):  {tc_list}")     # ['TC001', 'TC002', 'TC003', 'TC004']

# insert() — adds element at a SPECIFIC position
tc_list.insert(1, "TC001a")               # Insert at index 1
print(f"insert(1,'TC001a'): {tc_list}")   # ['TC001', 'TC001a', 'TC002', 'TC003', 'TC004']

# extend() — adds ALL elements from another list to the end
new_tcs = ["TC005", "TC006"]
tc_list.extend(new_tcs)
print(f"extend({new_tcs}): {tc_list}")

# IMPORTANT: append vs extend
demo = [1, 2, 3]
demo.append([4, 5])   # Adds the LIST as a single element → [1, 2, 3, [4, 5]]
print(f"\nappend([4,5]): {demo}")  # Nested list!

demo = [1, 2, 3]
demo.extend([4, 5])   # Adds EACH element individually → [1, 2, 3, 4, 5]
print(f"extend([4,5]): {demo}")   # Flat list!

# --- Removing Elements ---
print("\n--- Removing Elements ---")

fruits = ["apple", "banana", "cherry", "banana", "date"]
print(f"Original: {fruits}")

# remove() — removes the FIRST occurrence of a value
fruits.remove("banana")
print(f"remove('banana'): {fruits}")      # Removes first 'banana' only

# pop() — removes and RETURNS element at index (default: last)
last = fruits.pop()                        # Removes 'date'
print(f"pop(): {fruits}, removed: {last}")

second = fruits.pop(1)                     # Removes element at index 1
print(f"pop(1): {fruits}, removed: {second}")

# clear() — removes ALL elements
demo = [1, 2, 3]
demo.clear()
print(f"clear(): {demo}")                 # []

# --- Sorting ---
print("\n--- Sorting ---")

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")

# sort() — sorts the list IN-PLACE (modifies the original list)
numbers.sort()
print(f"sort(): {numbers}")               # [1, 2, 3, 5, 8, 9]

# sort() in descending order
numbers.sort(reverse=True)
print(f"sort(reverse=True): {numbers}")   # [9, 8, 5, 3, 2, 1]

# sorted() — returns a NEW sorted list (original unchanged)
original = [5, 2, 8, 1]
sorted_list = sorted(original)
print(f"\nsorted({original}): {sorted_list}")
print(f"Original unchanged: {original}")

# Sort strings (alphabetical)
browsers = ["Firefox", "Chrome", "Edge", "Safari"]
browsers.sort()
print(f"\nSorted browsers: {browsers}")

# Sort with key function — sort by length
browsers.sort(key=len)
print(f"Sorted by length: {browsers}")

# --- reverse() ---
print("\n--- reverse() ---")
items = [1, 2, 3, 4, 5]
items.reverse()                           # Reverses in-place
print(f"reverse(): {items}")              # [5, 4, 3, 2, 1]

# --- Search Methods ---
print("\n--- Search Methods ---")

data = ["Pass", "Fail", "Pass", "Blocked", "Pass"]
print(f"data = {data}")

# index() — returns the index of first occurrence
print(f"index('Fail'): {data.index('Fail')}")    # 1
# print(data.index('Skip'))  # ValueError if not found!

# count() — returns number of occurrences
print(f"count('Pass'): {data.count('Pass')}")    # 3
print(f"count('Skip'): {data.count('Skip')}")    # 0

# --- copy() ---
print("\n--- copy() ---")
original = [1, 2, 3]
copied = original.copy()                  # Creates a SHALLOW copy
copied.append(4)
print(f"Original: {original}")            # [1, 2, 3] — unchanged
print(f"Copied:   {copied}")             # [1, 2, 3, 4]

# WARNING: Without copy(), assignment creates a REFERENCE (not a copy)
ref = original                            # ref points to SAME list
ref.append(99)
print(f"\nAfter ref.append(99):")
print(f"original: {original}")            # [1, 2, 3, 99] — ALSO changed!
print(f"ref:      {ref}")                # [1, 2, 3, 99]

print()


# ============================================================
# SECTION 4: Built-in Functions with Lists
# ============================================================

print("=" * 60)
print("SECTION 4: Built-in Functions — len, min, max, sum")
print("=" * 60)

exec_times = [2.5, 1.8, 4.2, 0.9, 3.1, 2.0]
print(f"Execution times: {exec_times}")

print(f"len()  = {len(exec_times)}")      # 6 — number of elements
print(f"min()  = {min(exec_times)}")      # 0.9 — smallest value
print(f"max()  = {max(exec_times)}")      # 4.2 — largest value
print(f"sum()  = {sum(exec_times)}")      # 14.5 — total sum
print(f"avg    = {sum(exec_times) / len(exec_times):.2f}")  # Average

# With strings
names = ["Charlie", "Alice", "Bob"]
print(f"\nmin({names}) = {min(names)}")    # Alice (alphabetical)
print(f"max({names}) = {max(names)}")      # Charlie

print()


# ============================================================
# SECTION 5: List Comprehension
# ============================================================
# List comprehension provides a concise way to create lists.
# Syntax: [expression FOR item IN iterable IF condition]

print("=" * 60)
print("SECTION 5: List Comprehension")
print("=" * 60)

# Basic — create a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")              # [1, 4, 9, 16, 25]

# With condition — only even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens: {evens}")                  # [2, 4, 6, 8, 10]

# Transform strings — convert to uppercase
tc_ids = ["tc001", "tc002", "tc003"]
upper_ids = [tc.upper() for tc in tc_ids]
print(f"Uppercase: {upper_ids}")          # ['TC001', 'TC002', 'TC003']

# Filter and transform — get lengths of long words
words = ["Python", "is", "great", "for", "automation", "testing"]
long_words = [w for w in words if len(w) > 4]
print(f"Long words (>4 chars): {long_words}")

# Ternary in comprehension
scores = [85, 42, 91, 55, 73, 30]
results = ["Pass" if s >= 60 else "Fail" for s in scores]
print(f"Scores:  {scores}")
print(f"Results: {results}")

# Nested comprehension — flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flat:   {flat}")                  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# PRACTICAL: Generate test data
test_urls = [f"https://boodmo.com/page/{i}" for i in range(1, 6)]
print(f"URLs: {test_urls}")

print()


# ============================================================
# SECTION 6: Nested Lists
# ============================================================

print("=" * 60)
print("SECTION 6: Nested Lists")
print("=" * 60)

# Lists can contain other lists — creating rows and columns (like a table)
test_results = [
    ["TC001", "Login Test", "Pass"],
    ["TC002", "Search Test", "Fail"],
    ["TC003", "Cart Test", "Pass"],
    ["TC004", "Checkout Test", "Blocked"]
]

# Access elements: list[row][column]
print(f"All results: {test_results}")
print(f"First row: {test_results[0]}")         # ['TC001', 'Login Test', 'Pass']
print(f"TC002 status: {test_results[1][2]}")   # 'Fail' (row 1, column 2)

# Iterate over nested list
print(f"\n{'TC ID':<10} | {'Test Name':<15} | {'Status'}")
print("-" * 40)
for row in test_results:
    tc_id, name, status = row  # Unpacking
    print(f"{tc_id:<10} | {name:<15} | {status}")

print()


# ============================================================
# SECTION 7: Iterating Over Lists & Membership
# ============================================================

print("=" * 60)
print("SECTION 7: Iterating and Membership")
print("=" * 60)

browsers = ["Chrome", "Firefox", "Edge", "Safari"]

# Method 1: Direct iteration
print("Direct iteration:")
for browser in browsers:
    print(f"  {browser}")

# Method 2: With index using enumerate
print("\nWith enumerate:")
for i, browser in enumerate(browsers, 1):
    print(f"  {i}. {browser}")

# Method 3: Using range and len (C-style — less Pythonic)
print("\nWith range(len()):")
for i in range(len(browsers)):
    print(f"  browsers[{i}] = {browsers[i]}")

# Membership check with 'in'
print(f"\n'Chrome' in browsers: {'Chrome' in browsers}")    # True
print(f"'Opera' in browsers: {'Opera' in browsers}")        # False
print(f"'Opera' not in browsers: {'Opera' not in browsers}")# True

print()


# ============================================================
# PRACTICE TASK 1: Test Case List Manipulation
# ============================================================
# Task: Create a list of test cases, add 2 more using append() and extend(),
# then sort and print

print("=" * 60)
print("PRACTICE TASK 1: Test Case List Manipulation")
print("=" * 60)

# Step 1: Create initial list
test_cases = ["TC001", "TC002", "TC003"]
print(f"Initial list: {test_cases}")

# Step 2: Add one using append()
test_cases.append("TC004")
print(f"After append('TC004'): {test_cases}")

# Step 3: Add two more using extend()
test_cases.extend(["TC005", "TC006"])
print(f"After extend(['TC005', 'TC006']): {test_cases}")

# Step 4: Sort the list
test_cases.sort()
print(f"After sort(): {test_cases}")

# Step 5: Print each with index
print("\nFinal Test Case List:")
for i, tc in enumerate(test_cases, 1):
    print(f"  {i}. {tc}")

print(f"\nTotal test cases: {len(test_cases)}")


# ============================================================
# PRACTICE TASK 2: Filter Failed Test Cases
# ============================================================
# Task: Use list comprehension to filter only failed test cases

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Filter Failed Test Cases")
print("=" * 60)

# List of tuples: (TC_ID, Status)
all_results = [
    ("TC001", "Pass"),
    ("TC002", "Fail"),
    ("TC003", "Pass"),
    ("TC004", "Fail"),
]

print(f"All results: {all_results}")

# List comprehension to filter only failed test cases
failed_cases = [tc_id for tc_id, status in all_results if status == "Fail"]
print(f"Failed cases: {failed_cases}")    # ['TC002', 'TC004']

# Alternative: Get full failed records
failed_records = [(tc_id, status) for tc_id, status in all_results if status == "Fail"]
print(f"Failed records: {failed_records}")

# Bonus: Get passed cases
passed_cases = [tc_id for tc_id, status in all_results if status == "Pass"]
print(f"Passed cases: {passed_cases}")    # ['TC001', 'TC003']

# Summary
print(f"\nSummary: {len(passed_cases)} passed, {len(failed_cases)} failed "
      f"out of {len(all_results)} total")


# ============================================================
# PRACTICE TASK 3: Remove Duplicates Using Set Conversion
# ============================================================
# Task: Remove duplicate test case IDs from a list

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Remove Duplicates")
print("=" * 60)

# List with duplicate TC IDs
tc_ids_with_dupes = ["TC001", "TC002", "TC003", "TC001", "TC004", "TC002", "TC005", "TC003"]
print(f"With duplicates: {tc_ids_with_dupes}")
print(f"Count: {len(tc_ids_with_dupes)}")

# Method 1: Convert to set (loses order)
unique_set = set(tc_ids_with_dupes)
unique_list_v1 = list(unique_set)
print(f"\nMethod 1 (set): {sorted(unique_list_v1)}")

# Method 2: Using dict.fromkeys() (preserves order)
unique_list_v2 = list(dict.fromkeys(tc_ids_with_dupes))
print(f"Method 2 (dict, order preserved): {unique_list_v2}")

# Method 3: Manual loop (preserves order)
unique_list_v3 = []
for tc in tc_ids_with_dupes:
    if tc not in unique_list_v3:
        unique_list_v3.append(tc)
print(f"Method 3 (manual): {unique_list_v3}")

print(f"\nDuplicates removed: {len(tc_ids_with_dupes) - len(unique_list_v2)} items")
print(f"Unique count: {len(unique_list_v2)}")


# ============================================================
# PRACTICE TASK 4: Find Second-Highest Execution Time
# ============================================================
# Task: Find the second-highest execution time from a list

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Second-Highest Execution Time")
print("=" * 60)

exec_times = [2.5, 4.2, 1.8, 4.2, 3.1, 0.9, 3.7]
print(f"Execution times: {exec_times}")

# Method 1: Sort and pick second element
sorted_times = sorted(exec_times, reverse=True)
print(f"Sorted (desc): {sorted_times}")

# Handle case where highest might have duplicates
unique_sorted = sorted(set(exec_times), reverse=True)
print(f"Unique sorted: {unique_sorted}")

if len(unique_sorted) >= 2:
    second_highest = unique_sorted[1]
    print(f"\nSecond-highest execution time: {second_highest} seconds")
else:
    print("Not enough unique values to find second highest!")

# Method 2: Without sorting (more efficient for large lists — O(n))
first = second = float('-inf')  # Start with negative infinity
for time in exec_times:
    if time > first:
        second = first  # Previous first becomes second
        first = time
    elif time > second and time != first:
        second = time

print(f"Method 2 — Highest: {first}, Second-highest: {second}")

# Method 3: Using heapq (efficient for finding top-N)
import heapq
top_2 = heapq.nlargest(2, set(exec_times))
print(f"Method 3 (heapq) — Top 2: {top_2}, Second-highest: {top_2[1]}")

print("\n--- Topic 5 Complete! ---")
