"""
Topic 8 — Sets | Python for Automation Course
===============================================
Sets are UNORDERED collections with NO DUPLICATE elements.
Useful for finding unique values, comparing test cycles, and deduplication.

Concepts Covered:
    - Set creation, unordered nature, no duplicates
    - Set methods — add, remove, discard, union, intersection, difference,
      symmetric_difference, issubset, issuperset
    - Frozen sets
    - Set vs List vs Tuple — when to use which

Practice Tasks:
    1. Find common test cases using intersection()
    2. Find test cases in Cycle 1 but NOT in Cycle 2 using difference()
    3. Remove duplicate browser names using set

How to Run:
    python sets.py
"""


# ============================================================
# SECTION 1: Set Creation and Properties
# ============================================================

print("=" * 60)
print("SECTION 1: Set Creation and Properties")
print("=" * 60)

# --- Set Creation ---
# Sets are UNORDERED, MUTABLE collections with NO DUPLICATE elements
# Created with curly braces {} or set() constructor

# Method 1: Using curly braces
browsers = {"Chrome", "Firefox", "Edge", "Safari"}
print(f"Set: {browsers}")
print(f"Type: {type(browsers)}")

# Method 2: Using set() constructor
from_list = set([1, 2, 3, 4, 5])
from_string = set("hello")          # {'h', 'e', 'l', 'o'} — duplicates removed!
print(f"From list: {from_list}")
print(f"From string: {from_string}")

# IMPORTANT: {} creates an EMPTY DICT, not a set!
empty_dict = {}           # This is a dictionary!
empty_set = set()         # This is an empty set!
print(f"\n{{}} type: {type(empty_dict)}")
print(f"set() type: {type(empty_set)}")

# --- No Duplicates ---
# Sets automatically remove duplicate values
numbers_with_dupes = {1, 2, 3, 2, 1, 4, 3, 5}
print(f"\nWith dupes: {{1, 2, 3, 2, 1, 4, 3, 5}}")
print(f"Auto-deduped: {numbers_with_dupes}")  # {1, 2, 3, 4, 5}

# --- Unordered ---
# Sets have NO guaranteed order — elements may appear in any order
# You CANNOT access elements by index: browsers[0] → TypeError
print(f"\nSets are unordered: {{'A', 'B', 'C'}} → {{'B', 'C', 'A'}} (order varies)")

# Checking membership (very fast — O(1) average)
print(f"\n'Chrome' in browsers: {'Chrome' in browsers}")    # True
print(f"'Opera' in browsers:  {'Opera' in browsers}")       # False

print()


# ============================================================
# SECTION 2: Set Methods — Adding and Removing
# ============================================================

print("=" * 60)
print("SECTION 2: Adding and Removing Elements")
print("=" * 60)

# --- Adding Elements ---
test_envs = {"Dev", "Staging"}
print(f"Original: {test_envs}")

# add() — adds a single element
test_envs.add("UAT")
print(f"add('UAT'):     {test_envs}")

# Adding a duplicate — no error, no effect
test_envs.add("Dev")  # 'Dev' already exists
print(f"add('Dev'):     {test_envs}")  # No change

# --- Removing Elements ---
print("\n--- Removing ---")
test_envs = {"Dev", "Staging", "UAT", "Prod"}
print(f"Original: {test_envs}")

# remove() — removes element; RAISES KeyError if not found
test_envs.remove("UAT")
print(f"remove('UAT'):    {test_envs}")
# test_envs.remove("QA")  # KeyError: 'QA' not in set!

# discard() — removes element; NO ERROR if not found (SAFER)
test_envs.discard("QA")  # No error even though 'QA' doesn't exist
print(f"discard('QA'):    {test_envs}")  # No change, no error

# pop() — removes and returns an ARBITRARY element (sets are unordered)
removed = test_envs.pop()
print(f"pop():            removed '{removed}', remaining: {test_envs}")

# clear() — removes all elements
demo_set = {1, 2, 3}
demo_set.clear()
print(f"clear():          {demo_set}")  # set()

print()


# ============================================================
# SECTION 3: Set Operations (Mathematical)
# ============================================================
# Sets support mathematical operations: union, intersection, difference, etc.
# These are EXTREMELY useful for comparing test results across cycles!

print("=" * 60)
print("SECTION 3: Set Operations")
print("=" * 60)

cycle_1 = {"TC001", "TC002", "TC003", "TC004", "TC005"}
cycle_2 = {"TC003", "TC004", "TC005", "TC006", "TC007"}

print(f"Cycle 1: {sorted(cycle_1)}")
print(f"Cycle 2: {sorted(cycle_2)}")

# --- Union (|) — ALL elements from BOTH sets ---
# "All test cases that appeared in either cycle"
union = cycle_1 | cycle_2                          # Using operator
union_method = cycle_1.union(cycle_2)              # Using method
print(f"\nUnion (|):        {sorted(union)}")
# ['TC001', 'TC002', 'TC003', 'TC004', 'TC005', 'TC006', 'TC007']

# --- Intersection (&) — elements in BOTH sets ---
# "Test cases that were in both cycles"
common = cycle_1 & cycle_2                         # Using operator
common_method = cycle_1.intersection(cycle_2)      # Using method
print(f"Intersection (&): {sorted(common)}")
# ['TC003', 'TC004', 'TC005']

# --- Difference (-) — elements in first set but NOT in second ---
# "Test cases in Cycle 1 that were NOT in Cycle 2"
only_cycle1 = cycle_1 - cycle_2                    # Using operator
only_cycle1_method = cycle_1.difference(cycle_2)   # Using method
print(f"Difference (C1-C2): {sorted(only_cycle1)}")
# ['TC001', 'TC002']

only_cycle2 = cycle_2 - cycle_1
print(f"Difference (C2-C1): {sorted(only_cycle2)}")
# ['TC006', 'TC007']

# --- Symmetric Difference (^) — elements in EITHER set, but NOT both ---
# "Test cases that appeared in only one cycle"
sym_diff = cycle_1 ^ cycle_2                       # Using operator
sym_diff_method = cycle_1.symmetric_difference(cycle_2)  # Using method
print(f"Symmetric Diff (^): {sorted(sym_diff)}")
# ['TC001', 'TC002', 'TC006', 'TC007']

# --- Subset and Superset ---
print("\n--- Subset and Superset ---")
p0_tests = {"TC001", "TC003"}
all_tests = {"TC001", "TC002", "TC003", "TC004", "TC005"}

# issubset() — is every element of A also in B?
print(f"P0 is subset of All?   {p0_tests.issubset(all_tests)}")    # True
print(f"P0 <= All?             {p0_tests <= all_tests}")            # True (operator)

# issuperset() — does A contain every element of B?
print(f"All is superset of P0? {all_tests.issuperset(p0_tests)}")  # True
print(f"All >= P0?             {all_tests >= p0_tests}")            # True (operator)

# isdisjoint() — do the sets have NO common elements?
set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 4, 5}
print(f"\n{{1,2,3}} disjoint {{4,5,6}}? {set_a.isdisjoint(set_b)}")  # True
print(f"{{1,2,3}} disjoint {{3,4,5}}? {set_a.isdisjoint(set_c)}")    # False

print()


# ============================================================
# SECTION 4: Frozen Sets
# ============================================================
# frozenset is an IMMUTABLE version of set — cannot add/remove elements.

print("=" * 60)
print("SECTION 4: Frozen Sets")
print("=" * 60)

# Creating a frozenset
config = frozenset(["Chrome", "Firefox", "Edge"])
print(f"Frozen set: {config}")
print(f"Type: {type(config)}")

# frozenset supports read-only operations
print(f"'Chrome' in config: {'Chrome' in config}")   # True
print(f"Length: {len(config)}")

# frozenset does NOT support add/remove
try:
    config.add("Safari")
except AttributeError as e:
    print(f"\nconfig.add() → AttributeError: {e}")

# frozenset CAN be used as dictionary key or element of another set
# (because it's immutable/hashable)
test_configs = {
    frozenset(["Chrome", "Windows"]): "config_1",
    frozenset(["Firefox", "Linux"]): "config_2",
}
print(f"\nFrozenset as dict key: {test_configs}")

# Set operations work with frozensets too
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(f"\nfs1 & fs2 = {fs1 & fs2}")    # frozenset({3})
print(f"fs1 | fs2 = {fs1 | fs2}")      # frozenset({1, 2, 3, 4, 5})

print()


# ============================================================
# SECTION 5: Set vs List vs Tuple
# ============================================================

print("=" * 60)
print("SECTION 5: Set vs List vs Tuple — When To Use Which")
print("=" * 60)

print("""
┌──────────────┬───────────┬───────────┬──────────────┐
│ Feature      │   List    │   Tuple   │    Set       │
├──────────────┼───────────┼───────────┼──────────────┤
│ Syntax       │   []      │   ()      │    {}        │
│ Ordered?     │   Yes     │   Yes     │    No        │
│ Mutable?     │   Yes     │   No      │    Yes       │
│ Duplicates?  │   Yes     │   Yes     │    No        │
│ Indexable?   │   Yes     │   Yes     │    No        │
│ Hashable?    │   No      │   Yes     │    No        │
│ Membership   │   O(n)    │   O(n)    │    O(1)      │
│ Use Case     │ Dynamic   │ Fixed     │ Unique items │
│              │ data      │ configs   │ & comparisons│
└──────────────┴───────────┴───────────┴──────────────┘

CHOOSE:
  • LIST  → When you need ordered, changeable data (test cases, URLs)
  • TUPLE → When data should not change (configs, coordinates, DB records)
  • SET   → When you need unique items or set operations (dedup, compare)
""")

# Performance comparison: membership check
import time

# Create large collections
large_list = list(range(100000))
large_set = set(range(100000))

# Search for an element near the end
target = 99999

# List membership time
start = time.perf_counter()
for _ in range(1000):
    _ = target in large_list
list_time = time.perf_counter() - start

# Set membership time
start = time.perf_counter()
for _ in range(1000):
    _ = target in large_set
set_time = time.perf_counter() - start

print(f"Membership check (1000 iterations):")
print(f"  List: {list_time:.4f}s")
print(f"  Set:  {set_time:.6f}s")
print(f"  Set is ~{list_time/set_time:.0f}x faster!")

print()


# ============================================================
# PRACTICE TASK 1: Common Test Cases Using intersection()
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Common Test Cases (intersection)")
print("=" * 60)

# Test cases executed in two different test cycles
cycle_1_tests = {"TC001", "TC002", "TC003", "TC004", "TC005", "TC006"}
cycle_2_tests = {"TC004", "TC005", "TC006", "TC007", "TC008", "TC009"}

print(f"Cycle 1: {sorted(cycle_1_tests)}")
print(f"Cycle 2: {sorted(cycle_2_tests)}")

# Find common test cases using intersection
common_tests = cycle_1_tests.intersection(cycle_2_tests)
# Same as: common_tests = cycle_1_tests & cycle_2_tests

print(f"\nCommon test cases: {sorted(common_tests)}")
print(f"Number of common TCs: {len(common_tests)}")

# Practical analysis
print(f"\nAnalysis:")
print(f"  Total unique TCs across both cycles: {len(cycle_1_tests | cycle_2_tests)}")
print(f"  TCs in Cycle 1 only:    {sorted(cycle_1_tests - cycle_2_tests)}")
print(f"  TCs in Cycle 2 only:    {sorted(cycle_2_tests - cycle_1_tests)}")
print(f"  TCs in both cycles:     {sorted(common_tests)}")


# ============================================================
# PRACTICE TASK 2: Test Cases in Cycle 1 but NOT in Cycle 2
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Difference — Cycle 1 Only")
print("=" * 60)

# Using the same sets from Task 1
only_in_cycle1 = cycle_1_tests.difference(cycle_2_tests)
# Same as: only_in_cycle1 = cycle_1_tests - cycle_2_tests

print(f"Cycle 1 tests: {sorted(cycle_1_tests)}")
print(f"Cycle 2 tests: {sorted(cycle_2_tests)}")
print(f"\nTCs in Cycle 1 but NOT in Cycle 2: {sorted(only_in_cycle1)}")
print(f"Count: {len(only_in_cycle1)} test case(s)")

# These are test cases that were dropped from Cycle 2
# or were specific to Cycle 1 only
print("\nThese test cases need review — why were they not in Cycle 2?")
for tc in sorted(only_in_cycle1):
    print(f"  ⚠️ {tc} — executed in Cycle 1 only")

# Also show what's new in Cycle 2
only_in_cycle2 = cycle_2_tests - cycle_1_tests
print(f"\nNew TCs added in Cycle 2: {sorted(only_in_cycle2)}")
for tc in sorted(only_in_cycle2):
    print(f"  ✚ {tc} — new in Cycle 2")


# ============================================================
# PRACTICE TASK 3: Remove Duplicate Browser Names
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Remove Duplicates Using Set")
print("=" * 60)

# List with duplicate browser names
browser_list = ["Chrome", "Firefox", "Chrome", "Edge", "Firefox"]
print(f"Original list: {browser_list}")
print(f"List length:   {len(browser_list)}")

# Convert to set to remove duplicates
unique_browsers = set(browser_list)
print(f"\nUnique set:    {unique_browsers}")
print(f"Set length:    {len(unique_browsers)}")

# Convert back to list if you need indexing
unique_list = list(unique_browsers)
print(f"Back to list:  {unique_list}")

# Preserving order (if needed)
unique_ordered = list(dict.fromkeys(browser_list))
print(f"Ordered unique: {unique_ordered}")

# Duplicates removed
duplicates_count = len(browser_list) - len(unique_browsers)
print(f"\nDuplicates removed: {duplicates_count}")

# Bonus: Find which items were duplicated
from collections import Counter
counts = Counter(browser_list)
duplicated = {item: count for item, count in counts.items() if count > 1}
print(f"Duplicated items: {duplicated}")

print("\n--- Topic 8 Complete! ---")
