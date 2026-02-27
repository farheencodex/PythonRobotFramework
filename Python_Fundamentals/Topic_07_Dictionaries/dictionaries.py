"""
Topic 7 — Dictionaries (Critical for Test Data) | Python for Automation Course
================================================================================
Dictionaries are KEY-VALUE pair collections — essential for storing test data,
configurations, API payloads/responses, element locators, and test results.

Concepts Covered:
    - Dictionary creation, key-value pairs
    - Accessing values — dict[key], dict.get(key)
    - Dictionary methods — keys(), values(), items(), update(), pop(), clear(), copy()
    - Adding, updating, and deleting key-value pairs
    - Nested dictionaries
    - Dictionary comprehension
    - Iterating over dictionaries
    - Checking if key exists — 'in' operator

Practice Tasks:
    1. Test case dict — access and update status
    2. Nested dict for 3 test cases — iterate and print
    3. Dictionary comprehension for TC IDs
    4. Merge two test result dictionaries

How to Run:
    python dictionaries.py
"""


# ============================================================
# SECTION 1: Dictionary Creation and Key-Value Pairs
# ============================================================

print("=" * 60)
print("SECTION 1: Dictionary Creation")
print("=" * 60)

# Dictionaries store data as KEY:VALUE pairs
# Keys must be UNIQUE and IMMUTABLE (str, int, tuple)
# Values can be ANY type

# Method 1: Using curly braces {} with key:value pairs
test_case = {
    "TC_ID": "TC_001",
    "Module": "Login",
    "Status": "Pass",
    "Priority": "P0"
}
print(f"Test case: {test_case}")

# Method 2: Using dict() constructor
config = dict(browser="Chrome", headless=True, timeout=30)
print(f"Config: {config}")

# Method 3: From a list of tuples
items = dict([("name", "Tayyab"), ("role", "QA Engineer"), ("exp", 5)])
print(f"From tuples: {items}")

# Method 4: Using dict.fromkeys() — all keys get same value
tc_ids = ["TC001", "TC002", "TC003"]
default_status = dict.fromkeys(tc_ids, "Not Started")
print(f"fromkeys: {default_status}")

# Empty dictionary
empty = {}
empty_v2 = dict()
print(f"Empty dict: {empty}")

# Keys must be unique — later value overwrites earlier
dupes = {"a": 1, "b": 2, "a": 99}
print(f"\nDuplicate keys: {dupes}")  # {'a': 99, 'b': 2}

print()


# ============================================================
# SECTION 2: Accessing Values
# ============================================================

print("=" * 60)
print("SECTION 2: Accessing Values")
print("=" * 60)

test_case = {
    "TC_ID": "TC_001",
    "Module": "Login",
    "Status": "Pass",
    "Priority": "P0"
}

# Method 1: dict[key] — raises KeyError if key doesn't exist
print(f"dict['TC_ID']:   {test_case['TC_ID']}")     # TC_001
print(f"dict['Status']:  {test_case['Status']}")     # Pass
# print(test_case['Duration'])  # KeyError! Key doesn't exist

# Method 2: dict.get(key) — returns None if key doesn't exist (SAFER)
print(f"\nget('TC_ID'):    {test_case.get('TC_ID')}")       # TC_001
print(f"get('Duration'): {test_case.get('Duration')}")     # None (no error!)

# get() with default value — returns default if key doesn't exist
print(f"get('Duration', 'N/A'): {test_case.get('Duration', 'N/A')}")  # N/A

# BEST PRACTICE: Use dict.get() when the key might not exist
# Use dict[key] when you're SURE the key exists (or want an error if it doesn't)

print()


# ============================================================
# SECTION 3: Dictionary Methods
# ============================================================

print("=" * 60)
print("SECTION 3: Dictionary Methods")
print("=" * 60)

test_case = {
    "TC_ID": "TC_001",
    "Module": "Login",
    "Status": "Pass",
    "Priority": "P0"
}

# keys() — returns all keys
print(f"keys():   {list(test_case.keys())}")
# ['TC_ID', 'Module', 'Status', 'Priority']

# values() — returns all values
print(f"values(): {list(test_case.values())}")
# ['TC_001', 'Login', 'Pass', 'P0']

# items() — returns all key-value pairs as tuples
print(f"items():  {list(test_case.items())}")
# [('TC_ID', 'TC_001'), ('Module', 'Login'), ...]

# update() — adds/updates multiple key-value pairs from another dict
test_case.update({"Status": "Fail", "Bug_ID": "BUG-123"})
print(f"\nAfter update(): {test_case}")
# Status changed to Fail, Bug_ID added

# pop() — removes a key and returns its value
removed_value = test_case.pop("Bug_ID")
print(f"pop('Bug_ID'): {removed_value}")
print(f"After pop:     {test_case}")

# pop() with default — no error if key doesn't exist
safe_pop = test_case.pop("NonExistent", "default_value")
print(f"pop('NonExistent', 'default'): {safe_pop}")

# popitem() — removes and returns the LAST key-value pair
last_item = test_case.popitem()
print(f"\npopitem(): {last_item}")
print(f"After popitem: {test_case}")

# copy() — shallow copy
original = {"a": 1, "b": 2}
copied = original.copy()
copied["c"] = 3
print(f"\nOriginal: {original}")  # Unchanged
print(f"Copied:   {copied}")     # Has 'c'

# clear() — removes all items
demo = {"x": 1, "y": 2}
demo.clear()
print(f"\nAfter clear(): {demo}")  # {}

# setdefault() — returns value if key exists, otherwise sets default
config = {"browser": "Chrome"}
config.setdefault("browser", "Firefox")   # Key exists → returns existing value
config.setdefault("headless", False)       # Key doesn't exist → adds it
print(f"\nsetdefault: {config}")
# {'browser': 'Chrome', 'headless': False}

print()


# ============================================================
# SECTION 4: Adding, Updating, and Deleting
# ============================================================

print("=" * 60)
print("SECTION 4: Adding, Updating, and Deleting")
print("=" * 60)

env_config = {"browser": "Chrome", "timeout": 30}
print(f"Original: {env_config}")

# Adding a new key-value pair
env_config["base_url"] = "https://boodmo.com"
print(f"Added:    {env_config}")

# Updating an existing value
env_config["timeout"] = 60
print(f"Updated:  {env_config}")

# Deleting using del
del env_config["timeout"]
print(f"Deleted:  {env_config}")

# Deleting using pop()
url = env_config.pop("base_url")
print(f"Popped:   {env_config}, removed value: {url}")

print()


# ============================================================
# SECTION 5: Nested Dictionaries
# ============================================================
# Dictionaries can contain other dictionaries — perfect for structured test data!

print("=" * 60)
print("SECTION 5: Nested Dictionaries")
print("=" * 60)

# Nested dict — each test case is a dict inside the main dict
test_suite = {
    "TC_001": {
        "title": "Verify Login",
        "module": "Authentication",
        "status": "Pass",
        "priority": "P0",
        "execution_time": 2.5
    },
    "TC_002": {
        "title": "Verify Search",
        "module": "Search",
        "status": "Fail",
        "priority": "P1",
        "execution_time": 5.1
    },
    "TC_003": {
        "title": "Verify Cart",
        "module": "Cart",
        "status": "Pass",
        "priority": "P0",
        "execution_time": 3.2
    }
}

# Accessing nested values
print(f"TC_001 title:  {test_suite['TC_001']['title']}")
print(f"TC_002 status: {test_suite['TC_002']['status']}")
print(f"TC_003 time:   {test_suite['TC_003']['execution_time']}s")

# Updating nested values
test_suite["TC_002"]["status"] = "Pass"
test_suite["TC_002"]["bug_id"] = None  # Bug resolved
print(f"\nTC_002 after update: {test_suite['TC_002']}")

# Iterating over nested dict
print(f"\n{'TC ID':<8} | {'Title':<18} | {'Module':<15} | {'Status':<8} | {'Time'}")
print("-" * 70)
for tc_id, details in test_suite.items():
    print(f"{tc_id:<8} | {details['title']:<18} | {details['module']:<15} | "
          f"{details['status']:<8} | {details['execution_time']}s")

# Adding a new test case to the suite
test_suite["TC_004"] = {
    "title": "Verify Checkout",
    "module": "Checkout",
    "status": "Not Run",
    "priority": "P0",
    "execution_time": 0
}
print(f"\nTotal test cases: {len(test_suite)}")

print()


# ============================================================
# SECTION 6: Dictionary Comprehension
# ============================================================
# Create dictionaries using a concise one-line syntax.
# Syntax: {key_expr: value_expr FOR item IN iterable IF condition}

print("=" * 60)
print("SECTION 6: Dictionary Comprehension")
print("=" * 60)

# Basic — create a dict of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From a list — create TC_ID to status mapping
tc_ids = ["TC001", "TC002", "TC003", "TC004"]
status_dict = {tc: "Pass" for tc in tc_ids}
print(f"Status dict: {status_dict}")

# With condition — only even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform keys/values
original = {"name": "tayyab", "city": "mumbai", "role": "qa"}
uppercased = {k: v.upper() for k, v in original.items()}
print(f"Uppercased values: {uppercased}")

# From two lists using zip()
keys = ["browser", "version", "os"]
values = ["Chrome", "121.0", "Windows 11"]
config = {k: v for k, v in zip(keys, values)}
print(f"From zip: {config}")

# Invert a dictionary (swap keys and values)
status_map = {"TC001": "Pass", "TC002": "Fail", "TC003": "Pass"}
inverted = {}
for tc, status in status_map.items():
    inverted.setdefault(status, []).append(tc)
print(f"Grouped by status: {inverted}")

print()


# ============================================================
# SECTION 7: Iterating Over Dictionaries
# ============================================================

print("=" * 60)
print("SECTION 7: Iterating Over Dictionaries")
print("=" * 60)

test_case = {
    "TC_ID": "TC_001",
    "Module": "Login",
    "Status": "Pass",
    "Priority": "P0",
    "Time": 2.5
}

# Method 1: Iterate over keys (default)
print("Keys:")
for key in test_case:  # Same as: for key in test_case.keys()
    print(f"  {key}")

# Method 2: Iterate over values
print("\nValues:")
for value in test_case.values():
    print(f"  {value}")

# Method 3: Iterate over key-value pairs (MOST COMMON)
print("\nKey-Value pairs:")
for key, value in test_case.items():
    print(f"  {key}: {value}")

print()


# ============================================================
# SECTION 8: Checking if Key Exists
# ============================================================

print("=" * 60)
print("SECTION 8: Checking Key Existence")
print("=" * 60)

config = {"browser": "Chrome", "headless": True, "timeout": 30}

# Using 'in' operator — checks KEYS only
print(f"'browser' in config:  {'browser' in config}")    # True
print(f"'Chrome' in config:   {'Chrome' in config}")     # False (Chrome is a value!)
print(f"'retries' in config:  {'retries' in config}")    # False

# Practical: Safe access pattern
if "timeout" in config:
    print(f"\nTimeout is set to: {config['timeout']}")
else:
    print("\nTimeout not configured, using default.")

# Check if value exists (must check .values())
print(f"\n'Chrome' in config.values(): {'Chrome' in config.values()}")  # True

print()


# ============================================================
# PRACTICE TASK 1: Test Case Dict — Access and Update
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Test Case Dictionary Operations")
print("=" * 60)

# Create the test case dictionary
test_case = {
    "TC_ID": "TC_001",
    "Module": "Login",
    "Status": "Pass",
    "Priority": "P0"
}
print(f"Original: {test_case}")

# Access individual values
print(f"\nTC ID:    {test_case['TC_ID']}")
print(f"Module:   {test_case['Module']}")
print(f"Status:   {test_case['Status']}")
print(f"Priority: {test_case['Priority']}")

# Update the status
test_case["Status"] = "Fail"
print(f"\nAfter status update: {test_case}")

# Add new fields
test_case["Bug_ID"] = "BUG-456"
test_case["Assigned_To"] = "Tayyab"
print(f"After adding fields: {test_case}")

# Print formatted
print(f"\n{'Field':<15} | {'Value'}")
print("-" * 35)
for key, value in test_case.items():
    print(f"{key:<15} | {value}")


# ============================================================
# PRACTICE TASK 2: Nested Dict — 3 Test Cases
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Nested Dictionary Iteration")
print("=" * 60)

# Nested dictionary for 3 test cases
test_suite = {
    "TC_001": {
        "description": "Verify user can login with valid credentials",
        "status": "Pass"
    },
    "TC_002": {
        "description": "Verify search returns relevant results",
        "status": "Fail"
    },
    "TC_003": {
        "description": "Verify items can be added to cart",
        "status": "Pass"
    }
}

# Iterate and print all test cases
print("\nTest Suite Report:")
print(f"{'TC ID':<8} | {'Status':<8} | {'Description'}")
print("-" * 65)

for tc_id, details in test_suite.items():
    status_icon = "✓" if details["status"] == "Pass" else "✗"
    print(f"{tc_id:<8} | {status_icon} {details['status']:<5} | {details['description']}")

# Summary
total = len(test_suite)
passed = sum(1 for d in test_suite.values() if d["status"] == "Pass")
failed = total - passed
print(f"\nTotal: {total} | Passed: {passed} | Failed: {failed}")


# ============================================================
# PRACTICE TASK 3: Dictionary Comprehension for TC IDs
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Dictionary Comprehension")
print("=" * 60)

# Given list of TC IDs, create a dict with {tc_id: "Pass"} for each
tc_ids = ["TC_001", "TC_002", "TC_003", "TC_004", "TC_005"]

# Dictionary comprehension
result_dict = {tc_id: "Pass" for tc_id in tc_ids}
print(f"Input list: {tc_ids}")
print(f"Result dict: {result_dict}")

# More complex: With index-based status
status_dict = {
    tc_id: ("Pass" if i % 2 == 0 else "Fail")
    for i, tc_id in enumerate(tc_ids)
}
print(f"\nAlternating status: {status_dict}")

# Print formatted
print(f"\n{'TC ID':<10} | {'Status'}")
print("-" * 22)
for tc_id, status in result_dict.items():
    print(f"{tc_id:<10} | {status}")


# ============================================================
# PRACTICE TASK 4: Merge Two Test Result Dictionaries
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Merge Dictionaries with update()")
print("=" * 60)

# Test results from two different modules
login_results = {
    "TC_001": "Pass",
    "TC_002": "Fail",
    "TC_003": "Pass"
}

search_results = {
    "TC_004": "Pass",
    "TC_005": "Fail",
    "TC_006": "Pass"
}

print(f"Login results:  {login_results}")
print(f"Search results: {search_results}")

# Method 1: Using update() — modifies the first dict
all_results = login_results.copy()  # Copy first to preserve original
all_results.update(search_results)
print(f"\nMerged (update): {all_results}")

# Method 2: Using ** unpacking (Python 3.5+)
merged = {**login_results, **search_results}
print(f"Merged (**):     {merged}")

# Method 3: Using | operator (Python 3.9+)
merged_v3 = login_results | search_results
print(f"Merged (|):      {merged_v3}")

# Verify originals are unchanged
print(f"\nOriginal login:  {login_results}")
print(f"Original search: {search_results}")

# Summary of merged results
total = len(all_results)
passed = sum(1 for s in all_results.values() if s == "Pass")
failed = total - passed
print(f"\nMerged Summary: {total} total, {passed} passed, {failed} failed")

print("\n--- Topic 7 Complete! ---")
