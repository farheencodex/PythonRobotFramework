"""
Topic 2 — Operators | Python for Automation Course
====================================================
This file covers all Python operators with commented explanations.

Concepts Covered:
    - Arithmetic operators — +, -, *, /, //, %, **
    - Comparison operators — ==, !=, >, <, >=, <=
    - Logical operators — and, or, not
    - Assignment operators — =, +=, -=, *=, /=
    - Bitwise operators (overview) — &, |, ^, ~, <<, >>
    - Identity operators — is, is not
    - Membership operators — in, not in

Practice Tasks:
    1. Check if a number is even or odd
    2. Membership operators with test case statuses
    3. All comparison operators demo

How to Run:
    python operators.py
"""


# ============================================================
# SECTION 1: Arithmetic Operators
# ============================================================
# Arithmetic operators perform mathematical calculations.

a = 15
b = 4

print("=" * 60)
print("SECTION 1: Arithmetic Operators")
print("=" * 60)
print(f"a = {a}, b = {b}")
print()

# Addition (+) — adds two numbers
print(f"a + b  = {a + b}")       # Output: 19

# Subtraction (-) — subtracts right from left
print(f"a - b  = {a - b}")       # Output: 11

# Multiplication (*) — multiplies two numbers
print(f"a * b  = {a * b}")       # Output: 60

# Division (/) — divides and returns a FLOAT (always)
print(f"a / b  = {a / b}")       # Output: 3.75

# Floor Division (//) — divides and returns INTEGER part only (rounds DOWN)
print(f"a // b = {a // b}")      # Output: 3

# Modulus (%) — returns the REMAINDER of division
print(f"a % b  = {a % b}")       # Output: 3 (15 ÷ 4 = 3 remainder 3)

# Exponentiation (**) — raises to the power
print(f"a ** b = {a ** b}")      # Output: 50625 (15⁴)

# PRACTICAL USE CASES IN AUTOMATION:
# - % (modulus): Check if number is even/odd, pagination logic
# - // (floor div): Calculate number of full pages in pagination
# - ** (power): Exponential backoff for retry delays

# String operations with arithmetic operators
print("\n--- Arithmetic with Strings ---")
print("Hello " + "World")        # Concatenation: "Hello World"
print("Ha" * 3)                   # Repetition: "HaHaHa"

print()


# ============================================================
# SECTION 2: Comparison (Relational) Operators
# ============================================================
# Comparison operators compare two values and return True or False.
# Used heavily in test assertions and conditional logic.

x = 10
y = 20

print("=" * 60)
print("SECTION 2: Comparison Operators")
print("=" * 60)
print(f"x = {x}, y = {y}")
print()

# Equal to (==) — checks if values are equal
print(f"x == y  → {x == y}")     # Output: False

# Not equal to (!=) — checks if values are NOT equal
print(f"x != y  → {x != y}")     # Output: True

# Greater than (>)
print(f"x > y   → {x > y}")      # Output: False

# Less than (<)
print(f"x < y   → {x < y}")      # Output: True

# Greater than or equal to (>=)
print(f"x >= y  → {x >= y}")     # Output: False
print(f"x >= 10 → {x >= 10}")    # Output: True

# Less than or equal to (<=)
print(f"x <= y  → {x <= y}")     # Output: True
print(f"y <= 20 → {y <= 20}")    # Output: True

# IMPORTANT: == vs = 
# = is ASSIGNMENT (puts a value into a variable)
# == is COMPARISON (checks if two values are equal)

# Comparison with strings (lexicographic / alphabetical order)
print("\n--- String Comparison ---")
print(f"'apple' == 'apple' → {'apple' == 'apple'}")  # True
print(f"'apple' < 'banana' → {'apple' < 'banana'}")  # True (a comes before b)
print(f"'Apple' == 'apple' → {'Apple' == 'apple'}")  # False (case-sensitive!)

# Chained comparisons (Python allows this — very readable!)
age = 25
print(f"\n18 <= {age} <= 65 → {18 <= age <= 65}")    # True (is age between 18 and 65?)

print()


# ============================================================
# SECTION 3: Logical Operators
# ============================================================
# Logical operators combine boolean expressions.
# Used in complex conditions — e.g., "if logged in AND has permission"

print("=" * 60)
print("SECTION 3: Logical Operators")
print("=" * 60)

# and — Returns True only if BOTH conditions are True
print(f"True and True   → {True and True}")     # True
print(f"True and False  → {True and False}")     # False
print(f"False and True  → {False and True}")     # False
print(f"False and False → {False and False}")    # False

# or — Returns True if AT LEAST ONE condition is True
print(f"\nTrue or True   → {True or True}")      # True
print(f"True or False  → {True or False}")       # True
print(f"False or True  → {False or True}")       # True
print(f"False or False → {False or False}")      # False

# not — Reverses the boolean value
print(f"\nnot True  → {not True}")               # False
print(f"not False → {not False}")                # True

# PRACTICAL EXAMPLE: Automation condition
is_logged_in = True
has_permission = False
print(f"\nis_logged_in = {is_logged_in}, has_permission = {has_permission}")
print(f"Can access dashboard? {is_logged_in and has_permission}")  # False

# SHORT-CIRCUIT EVALUATION:
# 'and' stops at the first False (no need to check further)
# 'or' stops at the first True (no need to check further)
print("\n--- Short-circuit evaluation ---")
print(f"False and (1/0) → Python won't evaluate 1/0 because False and anything = False")
result = False and "this won't matter"
print(f"Result: {result}")  # False — second operand was never evaluated

print()


# ============================================================
# SECTION 4: Assignment Operators
# ============================================================
# Assignment operators assign and optionally modify values.

print("=" * 60)
print("SECTION 4: Assignment Operators")
print("=" * 60)

# Simple assignment (=)
count = 10
print(f"count = {count}")        # 10

# Add and assign (+=) — same as: count = count + 5
count += 5
print(f"count += 5  → {count}")  # 15

# Subtract and assign (-=) — same as: count = count - 3
count -= 3
print(f"count -= 3  → {count}")  # 12

# Multiply and assign (*=) — same as: count = count * 2
count *= 2
print(f"count *= 2  → {count}")  # 24

# Divide and assign (/=) — same as: count = count / 4
count /= 4
print(f"count /= 4  → {count}")  # 6.0

# Floor divide and assign (//=)
count = 15
count //= 4
print(f"count //= 4 → {count}")  # 3

# Modulus and assign (%=)
count = 15
count %= 4
print(f"count %= 4  → {count}")  # 3

# Exponent and assign (**=)
count = 2
count **= 3
print(f"count **= 3 → {count}")  # 8

# PRACTICAL USE: Incrementing test counters
pass_count = 0
fail_count = 0
pass_count += 1  # Test passed — increment counter
pass_count += 1  # Another test passed
fail_count += 1  # Test failed
print(f"\nTest Results: {pass_count} passed, {fail_count} failed")

print()


# ============================================================
# SECTION 5: Bitwise Operators (Overview)
# ============================================================
# Bitwise operators work on binary representations of integers.
# Less common in everyday automation but useful to know.

print("=" * 60)
print("SECTION 5: Bitwise Operators (Overview)")
print("=" * 60)

a = 5   # Binary: 0101
b = 3   # Binary: 0011
print(f"a = {a} (binary: {a:04b})")
print(f"b = {b} (binary: {b:04b})")
print()

# AND (&) — 1 only if both bits are 1
print(f"a & b  = {a & b}  (binary: {a & b:04b})")    # 1 (0001)

# OR (|) — 1 if at least one bit is 1
print(f"a | b  = {a | b}  (binary: {a | b:04b})")    # 7 (0111)

# XOR (^) — 1 if bits are different
print(f"a ^ b  = {a ^ b}  (binary: {a ^ b:04b})")    # 6 (0110)

# NOT (~) — Inverts all bits (returns -(n+1))
print(f"~a     = {~a}  (inverts all bits)")            # -6

# Left shift (<<) — Shifts bits left, fills with 0s (multiplies by 2^n)
print(f"a << 1 = {a << 1}  (binary: {a << 1:04b})")  # 10 (1010)

# Right shift (>>) — Shifts bits right (divides by 2^n)
print(f"a >> 1 = {a >> 1}  (binary: {a >> 1:04b})")  # 2 (0010)

print()


# ============================================================
# SECTION 6: Identity Operators
# ============================================================
# Identity operators check if two variables point to the SAME OBJECT in memory.
# 'is' checks identity (same object), '==' checks equality (same value).

print("=" * 60)
print("SECTION 6: Identity Operators")
print("=" * 60)

# 'is' — Returns True if both variables refer to the SAME object
# 'is not' — Returns True if they refer to DIFFERENT objects

a = [1, 2, 3]
b = [1, 2, 3]
c = a  # c points to the SAME object as a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a (c points to same object as a)")
print()

# == checks VALUE equality
print(f"a == b → {a == b}")      # True — same values

# 'is' checks if they're the SAME OBJECT in memory
print(f"a is b → {a is b}")      # False — different objects with same values

# c points to the same object as a
print(f"a is c → {a is c}")      # True — same object in memory

# 'is not' — opposite of 'is'
print(f"a is not b → {a is not b}")  # True — different objects

# BEST PRACTICE: Use 'is' only for None, True, False comparisons
result = None
print(f"\nresult is None → {result is None}")      # ✅ Correct way
print(f"result == None → {result == None}")         # ⚠️ Works but not recommended

print()


# ============================================================
# SECTION 7: Membership Operators
# ============================================================
# Membership operators check if a value exists IN a sequence (list, tuple, string, dict, set).
# Very useful in automation for checking test results!

print("=" * 60)
print("SECTION 7: Membership Operators")
print("=" * 60)

# 'in' — Returns True if value is found in the sequence
# 'not in' — Returns True if value is NOT found in the sequence

# With lists
browsers = ["Chrome", "Firefox", "Edge", "Safari"]
print(f"browsers = {browsers}")
print(f"'Chrome' in browsers    → {'Chrome' in browsers}")       # True
print(f"'Opera' in browsers     → {'Opera' in browsers}")        # False
print(f"'Opera' not in browsers → {'Opera' not in browsers}")    # True

# With strings
url = "https://www.boodmo.com/search?q=brake"
print(f"\nurl = '{url}'")
print(f"'boodmo' in url → {'boodmo' in url}")                    # True
print(f"'amazon' in url → {'amazon' in url}")                    # False

# With dictionaries (checks KEYS only, not values)
test_config = {"browser": "Chrome", "headless": True, "timeout": 30}
print(f"\ntest_config = {test_config}")
print(f"'browser' in test_config  → {'browser' in test_config}")  # True (key exists)
print(f"'Chrome' in test_config   → {'Chrome' in test_config}")   # False (Chrome is a VALUE, not key)

# With tuples
statuses = ("Pass", "Fail", "Blocked", "Skip")
print(f"\n'Pass' in {statuses}   → {'Pass' in statuses}")         # True
print(f"'Error' in {statuses}  → {'Error' in statuses}")          # False

print()


# ============================================================
# PRACTICE TASK 1: Even or Odd Checker
# ============================================================
# Task: Write a program to check if a number is even or odd using % operator

print("=" * 60)
print("PRACTICE TASK 1: Even or Odd Checker")
print("=" * 60)

# A number is EVEN if it's divisible by 2 (remainder is 0)
# A number is ODD if it's NOT divisible by 2 (remainder is 1)

# --- Interactive version (uncomment to try) ---
# number = int(input("Enter a number: "))

# --- Non-interactive (hardcoded) ---
numbers_to_check = [10, 7, 0, -3, 42, 99]

for number in numbers_to_check:
    # The modulus operator (%) gives the remainder of division
    if number % 2 == 0:
        print(f"{number:>4} is EVEN  (remainder: {number % 2})")
    else:
        print(f"{number:>4} is ODD   (remainder: {number % 2})")


# ============================================================
# PRACTICE TASK 2: Membership Operators with Test Case Statuses
# ============================================================
# Task: Demonstrate 'in' and 'not in' with a list of test case statuses

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Membership Operators with Test Statuses")
print("=" * 60)

# List of test case statuses from a test execution report
test_statuses = ["Pass", "Fail", "Blocked", "Skip"]
print(f"Test statuses: {test_statuses}")

# Check if various statuses exist in the list
statuses_to_check = ["Pass", "Fail", "Error", "Timeout", "Skip", "Blocked", "In Progress"]

print(f"\n{'Status':<15} | {'in list?':<10} | {'not in list?':<12}")
print("-" * 45)

for status in statuses_to_check:
    in_list = status in test_statuses
    not_in_list = status not in test_statuses
    indicator = "✓ Found" if in_list else "✗ Not found"
    print(f"{status:<15} | {str(in_list):<10} | {str(not_in_list):<12} | {indicator}")

# Practical use: Check if a test case failed
current_status = "Fail"
if current_status in test_statuses:
    print(f"\nStatus '{current_status}' is a valid status.")
else:
    print(f"\nStatus '{current_status}' is NOT a valid status!")

# Check if status indicates a problem
problem_statuses = ["Fail", "Blocked"]
if current_status in problem_statuses:
    print(f"⚠️ WARNING: Test case has status '{current_status}' — needs attention!")


# ============================================================
# PRACTICE TASK 3: All Comparison Operators Demo
# ============================================================
# Task: Write a program using all comparison operators to compare two numbers

print("\n" + "=" * 60)
print("PRACTICE TASK 3: All Comparison Operators Demo")
print("=" * 60)

# --- Interactive version (uncomment to try) ---
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# --- Non-interactive (hardcoded) ---
test_pairs = [(10, 20), (20, 20), (30, 10), (-5, 5), (0, 0)]

for num1, num2 in test_pairs:
    print(f"\nComparing num1={num1} and num2={num2}:")
    print(f"  {num1} == {num2}  → {num1 == num2}")   # Equal to
    print(f"  {num1} != {num2}  → {num1 != num2}")   # Not equal to
    print(f"  {num1} >  {num2}  → {num1 > num2}")    # Greater than
    print(f"  {num1} <  {num2}  → {num1 < num2}")    # Less than
    print(f"  {num1} >= {num2}  → {num1 >= num2}")   # Greater than or equal
    print(f"  {num1} <= {num2}  → {num1 <= num2}")   # Less than or equal

# BONUS: Automation-relevant comparison
print("\n--- Automation Example: Response Time Check ---")
response_time_ms = 1500
max_allowed_ms = 2000

print(f"Response time: {response_time_ms}ms")
print(f"Max allowed:   {max_allowed_ms}ms")

if response_time_ms <= max_allowed_ms:
    print(f"✓ PASS — Response time ({response_time_ms}ms) is within limit ({max_allowed_ms}ms)")
else:
    print(f"✗ FAIL — Response time ({response_time_ms}ms) exceeds limit ({max_allowed_ms}ms)")

print("\n--- Topic 2 Complete! ---")
