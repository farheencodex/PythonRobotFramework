"""
Topic 6 — Tuples | Python for Automation Course
=================================================
Tuples are immutable sequences — once created, they cannot be changed.
Use tuples for data that should NOT be modified: config values, coordinates,
database records, and constant test data.

Concepts Covered:
    - Tuple creation and immutability
    - Indexing and slicing
    - count() and index() methods
    - Tuple unpacking
    - When to use tuple vs list
    - Nested tuples

Practice Tasks:
    1. Browser configuration tuple with unpacking
    2. Iterate over environment URLs tuple
    3. Demonstrate tuple immutability (TypeError)

How to Run:
    python tuples.py
"""


# ============================================================
# SECTION 1: Tuple Creation and Immutability
# ============================================================

print("=" * 60)
print("SECTION 1: Tuple Creation and Immutability")
print("=" * 60)

# --- Tuple Creation ---
# Tuples are created with parentheses () or just commas
# They are ORDERED and IMMUTABLE (cannot be changed after creation)

# Method 1: Using parentheses (most common)
browsers = ("Chrome", "Firefox", "Edge", "Safari")
print(f"Tuple: {browsers}")
print(f"Type: {type(browsers)}")

# Method 2: Without parentheses (comma makes it a tuple)
coordinates = 10, 20, 30
print(f"Without parentheses: {coordinates}, Type: {type(coordinates)}")

# Method 3: Single element tuple — MUST have a trailing comma!
single = ("Chrome",)       # This is a tuple with one element
not_a_tuple = ("Chrome")   # This is just a string in parentheses!
print(f"\nSingle tuple: {single}, Type: {type(single)}")
print(f"Not a tuple: {not_a_tuple}, Type: {type(not_a_tuple)}")

# Method 4: Using tuple() constructor
from_list = tuple([1, 2, 3, 4, 5])
from_string = tuple("Python")
print(f"\nFrom list: {from_list}")
print(f"From string: {from_string}")

# Empty tuple
empty = ()
empty_v2 = tuple()
print(f"Empty tuple: {empty}")

# --- Immutability ---
# Tuples CANNOT be modified after creation
# This makes them safer for constant data like configurations
config = ("Chrome", "121.0", "Windows 11")
print(f"\nConfig tuple: {config}")

# These operations would ALL raise TypeError:
# config[0] = "Firefox"    # TypeError: 'tuple' object does not support item assignment
# config.append("x")       # AttributeError: no attribute 'append'
# del config[0]             # TypeError: doesn't support item deletion

# However, you CAN:
# - Access elements (read-only)
# - Create new tuples from existing ones
# - Delete the entire tuple variable

print()


# ============================================================
# SECTION 2: Indexing and Slicing
# ============================================================
# Tuples support indexing and slicing exactly like lists and strings.

print("=" * 60)
print("SECTION 2: Indexing and Slicing")
print("=" * 60)

env_urls = (
    "https://dev.boodmo.com",
    "https://staging.boodmo.com",
    "https://uat.boodmo.com",
    "https://preprod.boodmo.com",
    "https://www.boodmo.com"
)

# Indexing
print(f"First URL:  {env_urls[0]}")       # dev
print(f"Last URL:   {env_urls[-1]}")      # prod (www)
print(f"Third URL:  {env_urls[2]}")       # uat

# Slicing
print(f"\nFirst 3:    {env_urls[:3]}")     # dev, staging, UAT
print(f"Last 2:     {env_urls[-2:]}")      # preprod, prod
print(f"Middle:     {env_urls[1:4]}")      # staging, uat, preprod
print(f"Reversed:   {env_urls[::-1]}")     # Reversed tuple

# Length
print(f"\nTotal environments: {len(env_urls)}")

print()


# ============================================================
# SECTION 3: Tuple Methods — count() and index()
# ============================================================
# Tuples have only 2 methods (much fewer than lists — because they're immutable!)

print("=" * 60)
print("SECTION 3: count() and index()")
print("=" * 60)

test_results = ("Pass", "Fail", "Pass", "Pass", "Blocked", "Fail", "Pass")
print(f"Results: {test_results}")

# count() — how many times a value appears
print(f"\ncount('Pass'):    {test_results.count('Pass')}")      # 4
print(f"count('Fail'):    {test_results.count('Fail')}")      # 2
print(f"count('Blocked'): {test_results.count('Blocked')}")   # 1
print(f"count('Skip'):    {test_results.count('Skip')}")      # 0

# index() — returns the index of the FIRST occurrence
print(f"\nindex('Pass'):    {test_results.index('Pass')}")      # 0
print(f"index('Fail'):    {test_results.index('Fail')}")      # 1
print(f"index('Blocked'): {test_results.index('Blocked')}")   # 4

# index() with start and stop parameters
print(f"index('Pass', 1): {test_results.index('Pass', 1)}")   # 2 (search from index 1)

# index() raises ValueError if not found:
# test_results.index('Skip')  # ValueError: tuple.index(x): x not in tuple

# Safe way to check before calling index()
search_val = "Skip"
if search_val in test_results:
    print(f"index('{search_val}'): {test_results.index(search_val)}")
else:
    print(f"'{search_val}' not found in tuple")

print()


# ============================================================
# SECTION 4: Tuple Unpacking
# ============================================================
# Unpacking assigns each element of a tuple to a separate variable.
# This is one of the most powerful features of tuples!

print("=" * 60)
print("SECTION 4: Tuple Unpacking")
print("=" * 60)

# Basic unpacking — number of variables must match number of elements
browser_config = ("Chrome", "121.0", "Windows 11")

# Traditional way — accessing by index
print(f"browser_config[0] = {browser_config[0]}")
print(f"browser_config[1] = {browser_config[1]}")
print(f"browser_config[2] = {browser_config[2]}")

# Unpacking — cleaner and more readable
browser_name, version, os_name = browser_config
print(f"\nUnpacked: browser={browser_name}, version={version}, OS={os_name}")

# Unpacking with * (star) — capture remaining elements
scores = (95, 82, 73, 91, 68, 77)
first, second, *rest = scores
print(f"\nfirst={first}, second={second}, rest={rest}")
# first=95, second=82, rest=[73, 91, 68, 77]

# Star in the middle
first, *middle, last = scores
print(f"first={first}, middle={middle}, last={last}")
# first=95, middle=[82, 73, 91, 68], last=77

# Ignoring values with _ (underscore)
name, _, city = ("Tayyab", 25, "Mumbai")
print(f"name={name}, city={city}")  # 25 is ignored

# Swap variables using tuple unpacking (no temp variable needed!)
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a  # Swap using tuple unpacking
print(f"After swap:  a={a}, b={b}")

# Unpacking in loops
test_data = [
    ("TC001", "Login Test", "Pass"),
    ("TC002", "Search Test", "Fail"),
    ("TC003", "Cart Test", "Pass"),
]

print("\nTest Results (unpacked in loop):")
for tc_id, name, status in test_data:
    icon = "✓" if status == "Pass" else "✗"
    print(f"  {icon} {tc_id}: {name} → {status}")

# Function returning multiple values (returned as tuple)
def get_test_stats(results):
    """Returns pass count and fail count as a tuple."""
    pass_count = results.count("Pass")
    fail_count = results.count("Fail")
    return pass_count, fail_count  # Returns a tuple!

results = ("Pass", "Fail", "Pass", "Pass", "Fail")
passed, failed = get_test_stats(results)  # Unpack the returned tuple
print(f"\nStats: {passed} passed, {failed} failed")

print()


# ============================================================
# SECTION 5: Tuple vs List — When to Use Which
# ============================================================

print("=" * 60)
print("SECTION 5: Tuple vs List")
print("=" * 60)

print("""
┌──────────────────┬──────────────────────┬──────────────────────┐
│ Feature          │ Tuple                │ List                 │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Syntax           │ ()                   │ []                   │
│ Mutable?         │ No (immutable)       │ Yes (mutable)        │
│ Methods          │ 2 (count, index)     │ 11+ methods          │
│ Performance      │ Faster               │ Slower               │
│ Memory           │ Less memory          │ More memory          │
│ As dict key?     │ Yes                  │ No                   │
│ Hashable?        │ Yes (if elements are)│ No                   │
└──────────────────┴──────────────────────┴──────────────────────┘

USE TUPLE FOR:
  • Configuration that shouldn't change (browser, version, OS)
  • Database rows / API response records
  • Dictionary keys (lists can't be dict keys!)
  • Function arguments and return values
  • Data integrity — prevent accidental modification

USE LIST FOR:
  • Collections that need to grow/shrink (test case list)
  • Data that needs sorting, filtering, or modification
  • Dynamic test data that changes during execution
""")

# Performance comparison
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(f"List size:  {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
print("Tuples use less memory!\n")

# Tuple as dictionary key (list cannot be used as key)
# This is because tuples are hashable (immutable) and lists are not
test_env = {
    ("Chrome", "Windows"): "https://chrome-win.test.com",
    ("Firefox", "Linux"): "https://firefox-linux.test.com",
    ("Safari", "macOS"): "https://safari-mac.test.com",
}
print("Tuples as dict keys:")
for (browser, os_name), url in test_env.items():
    print(f"  {browser} on {os_name} → {url}")

print()


# ============================================================
# SECTION 6: Nested Tuples
# ============================================================

print("=" * 60)
print("SECTION 6: Nested Tuples")
print("=" * 60)

# Tuples can contain other tuples
test_matrix = (
    ("TC001", "Login", "Pass", 2.5),
    ("TC002", "Search", "Fail", 5.1),
    ("TC003", "Cart", "Pass", 3.2),
)

print("Test Matrix (nested tuples):")
print(f"{'TC ID':<8} | {'Module':<10} | {'Status':<8} | {'Time (s)'}")
print("-" * 45)

for row in test_matrix:
    tc_id, module, status, time = row
    print(f"{tc_id:<8} | {module:<10} | {status:<8} | {time}")

# Accessing nested elements
print(f"\nFirst test case: {test_matrix[0]}")
print(f"First TC status: {test_matrix[0][2]}")
print(f"Second TC time:  {test_matrix[1][3]}")

# Tuple concatenation — creates a NEW tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"\nConcatenation: {tuple1} + {tuple2} = {combined}")

# Tuple repetition
repeated = ("Test",) * 3
print(f"Repetition: {repeated}")  # ('Test', 'Test', 'Test')

print()


# ============================================================
# PRACTICE TASK 1: Browser Configuration Unpacking
# ============================================================
# Task: Store browser config as a tuple and access values using unpacking

print("=" * 60)
print("PRACTICE TASK 1: Browser Configuration Unpacking")
print("=" * 60)

# Browser configuration as a tuple (should not change during test)
browser_config = ("Chrome", "121.0", "Windows 11")
print(f"Browser config tuple: {browser_config}")

# Access each value using unpacking
browser_name, browser_version, operating_system = browser_config

print(f"\nBrowser:          {browser_name}")
print(f"Version:          {browser_version}")
print(f"Operating System: {operating_system}")

# Use in a practical context
print(f"\nTest Environment: {browser_name} v{browser_version} on {operating_system}")

# Multiple configurations
all_configs = (
    ("Chrome", "121.0", "Windows 11"),
    ("Firefox", "122.0", "Ubuntu 22.04"),
    ("Safari", "17.0", "macOS Sonoma"),
    ("Edge", "121.0", "Windows 11"),
)

print("\nAll Test Configurations:")
print(f"{'#':<3} | {'Browser':<10} | {'Version':<10} | {'OS':<15}")
print("-" * 45)
for i, (name, ver, os_name) in enumerate(all_configs, 1):
    print(f"{i:<3} | {name:<10} | {ver:<10} | {os_name:<15}")


# ============================================================
# PRACTICE TASK 2: Iterate Over Environment URLs
# ============================================================
# Task: Create a tuple of 5 test environment URLs and iterate over them

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Iterate Over Environment URLs")
print("=" * 60)

# Environment URLs as a tuple (should NOT change during testing)
env_urls = (
    "https://dev.boodmo.com",
    "https://qa.boodmo.com",
    "https://staging.boodmo.com",
    "https://uat.boodmo.com",
    "https://www.boodmo.com"
)

env_names = ("Development", "QA", "Staging", "UAT", "Production")

print(f"\nTotal environments: {len(env_urls)}")
print("\nEnvironment URL Mapping:")
print(f"{'#':<3} | {'Environment':<15} | {'URL'}")
print("-" * 55)

for i, (name, url) in enumerate(zip(env_names, env_urls), 1):
    print(f"{i:<3} | {name:<15} | {url}")

# Practical: Simulate navigating to each environment
print("\nSimulated Test Run:")
for name, url in zip(env_names, env_urls):
    print(f"  → Navigating to {name}: {url}")
    # In real automation: driver.get(url)
    print(f"    ✓ Page loaded successfully")


# ============================================================
# PRACTICE TASK 3: Demonstrate Tuple Immutability (TypeError)
# ============================================================
# Task: Show that tuples cannot be modified

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Tuple Immutability Demo")
print("=" * 60)

config = ("Chrome", "121.0", "Windows 11")
print(f"Original tuple: {config}")

# Attempt 1: Try to change an element
print("\nAttempt 1: config[0] = 'Firefox'")
try:
    config[0] = "Firefox"
except TypeError as e:
    print(f"  ✗ TypeError: {e}")

# Attempt 2: Try to append
print("\nAttempt 2: config.append('headless')")
try:
    config.append("headless")
except AttributeError as e:
    print(f"  ✗ AttributeError: {e}")

# Attempt 3: Try to delete an element
print("\nAttempt 3: del config[0]")
try:
    del config[0]
except TypeError as e:
    print(f"  ✗ TypeError: {e}")

# Attempt 4: Try to extend
print("\nAttempt 4: config += ('extra',)")
# This actually works, but creates a NEW tuple (doesn't modify original)
original_id = id(config)
config = config + ("headless",)  # Creates a brand new tuple
new_id = id(config)
print(f"  Result: {config}")
print(f"  Same object? {original_id == new_id}")  # False — it's a new tuple!

# IMPORTANT CAVEAT: If a tuple contains a MUTABLE object (like a list),
# the list inside CAN be modified!
print("\nCaveat: Mutable objects inside tuples CAN be modified!")
mixed_tuple = ("TC001", ["Pass", "Fail"])
print(f"Before: {mixed_tuple}")
mixed_tuple[1].append("Blocked")  # Modifying the LIST inside the tuple
print(f"After:  {mixed_tuple}")   # The list changed, but the tuple reference didn't

print("\n✓ Tuple itself is immutable, but mutable contents can change!")

print("\n--- Topic 6 Complete! ---")
