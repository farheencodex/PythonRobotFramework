"""
Topic 3 — Control Flow | Python for Automation Course
======================================================
This file covers conditional statements and loops — the backbone of program logic.

Concepts Covered:
    - if, elif, else statements
    - Nested if statements
    - Ternary (inline) if expression
    - for loop — with range(), iterating over lists, strings, dictionaries
    - while loop — with break, continue, pass
    - else with loops
    - Nested loops

Practice Tasks:
    1. Test case result grading based on marks
    2. Iterate over a list of URLs
    3. Login retry loop (while with counter)
    4. Multiplication table using nested loops

How to Run:
    python control_flow.py
"""


# ============================================================
# SECTION 1: if, elif, else Statements
# ============================================================
# Conditional statements let your program make decisions.
# The code block under the matching condition gets executed.
# Python uses INDENTATION (4 spaces) to define code blocks — no braces {}!

print("=" * 60)
print("SECTION 1: if, elif, else Statements")
print("=" * 60)

# Basic if statement — executes block only if condition is True
temperature = 38
if temperature > 37:
    print(f"Temperature is {temperature}°C — Fever detected!")  # This runs

# if-else — two branches: one for True, one for False
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult.")   # This runs
else:
    print(f"Age {age}: You are a minor.")

# if-elif-else — multiple conditions checked in order
# Python checks each condition from top to bottom.
# The FIRST matching condition's block runs; the rest are skipped.
score = 75

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")  # Output: Score: 75 → Grade: B

# IMPORTANT: Only ONE block executes even if multiple conditions are true
# For example, score 75 is also >= 60 and >= 50, but only the first match (>= 70) runs

print()


# ============================================================
# SECTION 2: Nested if Statements
# ============================================================
# You can put if statements inside other if statements — this is "nesting".
# Use nesting when you need to check a second condition only if the first is true.

print("=" * 60)
print("SECTION 2: Nested if Statements")
print("=" * 60)

is_logged_in = True
user_role = "admin"

if is_logged_in:
    print("User is logged in.")
    
    # Nested if — only checked if outer condition is True
    if user_role == "admin":
        print("Access granted: Admin Dashboard")
    elif user_role == "tester":
        print("Access granted: Test Dashboard")
    else:
        print("Access granted: User Dashboard")
else:
    print("Please log in first.")

# TIP: Avoid deep nesting (more than 2-3 levels). If your code is deeply nested,
# consider using functions or restructuring with early returns.

# Example of avoiding deep nesting (better approach):
print("\n--- Better approach (flat structure with 'and') ---")
if is_logged_in and user_role == "admin":
    print("Admin access granted!")
elif is_logged_in:
    print("User access granted!")
else:
    print("Please log in!")

print()


# ============================================================
# SECTION 3: Ternary (Inline) if Expression
# ============================================================
# A one-line shorthand for simple if-else statements.
# Syntax: value_if_true IF condition ELSE value_if_false

print("=" * 60)
print("SECTION 3: Ternary (Inline) if Expression")
print("=" * 60)

age = 25

# Traditional if-else (3 lines)
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(f"Traditional: {status}")

# Ternary expression (1 line) — does the same thing
status = "Adult" if age >= 18 else "Minor"
print(f"Ternary: {status}")

# More examples
score = 85
result = "Pass" if score >= 60 else "Fail"
print(f"Score {score} → {result}")

# Ternary in f-strings
tc_status = "Fail"
print(f"Test case {'PASSED ✓' if tc_status == 'Pass' else 'FAILED ✗'}")

# Nested ternary (possible but less readable — use sparingly)
marks = 92
grade = "A+" if marks >= 90 else ("A" if marks >= 80 else "B")
print(f"Marks {marks} → Grade: {grade}")

print()


# ============================================================
# SECTION 4: for Loop
# ============================================================
# for loops iterate over sequences (lists, strings, tuples, dicts, ranges).
# Each iteration, the loop variable takes the next value from the sequence.

print("=" * 60)
print("SECTION 4: for Loop")
print("=" * 60)

# --- for with range() ---
# range(stop) — generates numbers from 0 to stop-1
# range(start, stop) — generates numbers from start to stop-1
# range(start, stop, step) — with step increment

print("--- range() examples ---")

# range(5) → 0, 1, 2, 3, 4
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()  # newline

# range(1, 6) → 1, 2, 3, 4, 5
print("range(1, 6):", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(0, 10, 2) → 0, 2, 4, 6, 8 (step of 2)
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# range(10, 0, -1) → 10, 9, 8, ..., 1 (counting down)
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# --- for with lists ---
print("\n--- Iterating over lists ---")
browsers = ["Chrome", "Firefox", "Edge", "Safari"]

# Simple iteration
for browser in browsers:
    print(f"Testing on: {browser}")

# With index using enumerate()
print()
for index, browser in enumerate(browsers):
    print(f"Browser {index + 1}: {browser}")

# With enumerate starting from a custom number
print()
for index, browser in enumerate(browsers, start=1):  # Start counting from 1
    print(f"#{index} → {browser}")

# --- for with strings ---
print("\n--- Iterating over strings ---")
word = "Python"
for char in word:
    print(char, end="-")      # Output: P-y-t-h-o-n-
print()

# --- for with dictionaries ---
print("\n--- Iterating over dictionaries ---")
test_config = {"browser": "Chrome", "headless": True, "timeout": 30}

# Iterate over keys (default)
print("Keys:")
for key in test_config:
    print(f"  {key}")

# Iterate over values
print("Values:")
for value in test_config.values():
    print(f"  {value}")

# Iterate over key-value pairs
print("Key-Value pairs:")
for key, value in test_config.items():
    print(f"  {key}: {value}")

print()


# ============================================================
# SECTION 5: while Loop
# ============================================================
# while loops repeat as long as a condition is True.
# Be careful: if the condition never becomes False, you get an INFINITE LOOP!

print("=" * 60)
print("SECTION 5: while Loop")
print("=" * 60)

# Basic while loop — counting from 1 to 5
print("--- Basic while loop ---")
counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # Don't forget to update the counter or you'll loop forever!

# --- break — exits the loop immediately ---
print("\n--- break example ---")
print("Searching for 'Firefox' in browser list...")
browsers = ["Chrome", "Firefox", "Edge", "Safari"]
for browser in browsers:
    if browser == "Firefox":
        print(f"Found {browser}! Stopping search.")
        break  # Exit loop immediately
    print(f"Checking: {browser}...")
# Output: Checking: Chrome... → Found Firefox! Stopping search.

# --- continue — skips to the next iteration ---
print("\n--- continue example ---")
print("Printing only passing test cases:")
results = ["Pass", "Fail", "Pass", "Blocked", "Pass", "Fail"]
for result in results:
    if result != "Pass":
        continue  # Skip non-pass results, go to next iteration
    print(f"  ✓ {result}")

# --- pass — does nothing (placeholder) ---
print("\n--- pass example ---")
# pass is used as a placeholder when you need a statement but don't want to do anything
for i in range(5):
    if i == 3:
        pass  # TODO: Handle case when i is 3 (to be implemented later)
    else:
        print(f"  Processing item {i}")

# PRACTICAL USE: pass in empty class/function definitions during development
# class LoginPage:
#     pass  # Will implement later

print()


# ============================================================
# SECTION 6: else with Loops
# ============================================================
# Python's unique feature: 'else' block after for/while loops.
# The else block runs only if the loop completed WITHOUT hitting 'break'.

print("=" * 60)
print("SECTION 6: else with Loops")
print("=" * 60)

# Example 1: Loop completes normally → else runs
print("--- Loop without break (else runs) ---")
test_cases = ["TC001", "TC002", "TC003"]
search_for = "TC999"

for tc in test_cases:
    if tc == search_for:
        print(f"Found {search_for}!")
        break
else:
    # This runs because the loop completed without finding TC999
    print(f"{search_for} not found in the test suite.")

# Example 2: Loop hits break → else does NOT run
print("\n--- Loop with break (else skipped) ---")
search_for = "TC002"

for tc in test_cases:
    if tc == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found.")  # This does NOT run

print()


# ============================================================
# SECTION 7: Nested Loops
# ============================================================
# Loops inside loops — the inner loop runs completely for each iteration of the outer loop.

print("=" * 60)
print("SECTION 7: Nested Loops")
print("=" * 60)

# Example: Testing on multiple browsers across multiple environments
browsers = ["Chrome", "Firefox"]
environments = ["Dev", "Staging", "Prod"]

print("Test Matrix:")
for browser in browsers:
    for env in environments:
        print(f"  → Testing {browser} on {env}")

# Example: Creating a simple grid
print("\nGrid Pattern:")
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()  # New line after each row
# Output:
# * * * *
# * * * *
# * * * *

print()


# ============================================================
# PRACTICE TASK 1: Test Case Result Grading
# ============================================================
# Task: if marks >= 90: "Pass with Distinction", elif >= 60: "Pass", else: "Fail"

print("=" * 60)
print("PRACTICE TASK 1: Test Case Result Grading")
print("=" * 60)

# Simulating test scores for multiple test cases
test_scores = {
    "TC_001": 95,
    "TC_002": 72,
    "TC_003": 88,
    "TC_004": 45,
    "TC_005": 60,
    "TC_006": 33,
    "TC_007": 91,
}

print(f"\n{'TC ID':<10} | {'Score':>5} | {'Result':<25}")
print("-" * 45)

# Counters for summary
distinction_count = 0
pass_count = 0
fail_count = 0

for tc_id, marks in test_scores.items():
    # Check marks and assign result
    if marks >= 90:
        result = "Pass with Distinction ⭐"
        distinction_count += 1
    elif marks >= 60:
        result = "Pass ✓"
        pass_count += 1
    else:
        result = "Fail ✗"
        fail_count += 1
    
    print(f"{tc_id:<10} | {marks:>5} | {result}")

# Print summary
print("-" * 45)
print(f"\nSummary: {distinction_count} Distinction, {pass_count} Pass, {fail_count} Fail")
print(f"Total: {len(test_scores)} test cases")


# ============================================================
# PRACTICE TASK 2: Iterate Over a List of URLs
# ============================================================
# Task: Write a for loop to iterate over a list of 5 URLs and print each one

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Iterate Over URLs")
print("=" * 60)

# List of 5 URLs to test
urls = [
    "https://www.boodmo.com",
    "https://www.boodmo.com/login",
    "https://www.boodmo.com/search?q=brake",
    "https://www.boodmo.com/cart",
    "https://www.boodmo.com/checkout"
]

# Simple iteration with index
print("\nURL Navigation Sequence:")
for index, url in enumerate(urls, start=1):
    print(f"  Step {index}: Navigate to → {url}")

# Practical: Check URL patterns
print("\nURL Analysis:")
for url in urls:
    # Check if URL contains query parameters
    has_params = "?" in url
    # Extract the path
    path = url.split("boodmo.com")[-1] if "boodmo.com" in url else "/"
    
    print(f"  URL: {url}")
    print(f"    Path: {path or '/'}")
    print(f"    Has parameters: {has_params}")
    print()


# ============================================================
# PRACTICE TASK 3: Login Retry Loop
# ============================================================
# Task: Write a while loop that retries a failed login attempt up to 3 times

print("=" * 60)
print("PRACTICE TASK 3: Login Retry Loop")
print("=" * 60)

import random  # We'll use this to simulate random login results

max_retries = 3
attempt = 0
login_successful = False

print("\nSimulating login attempts (randomly succeeds or fails):")
print("-" * 40)

# Seed random for reproducible results in demo
random.seed(42)

while attempt < max_retries and not login_successful:
    attempt += 1
    print(f"\nAttempt {attempt}/{max_retries}:")
    
    # Simulate a login attempt (randomly succeeds or fails)
    # In real automation, this would be actual login code
    login_result = random.choice([True, False, False])  # 33% chance of success
    
    if login_result:
        login_successful = True
        print(f"  ✓ Login SUCCESSFUL on attempt {attempt}!")
    else:
        print(f"  ✗ Login FAILED on attempt {attempt}.")
        
        if attempt < max_retries:
            print(f"  ↻ Retrying... ({max_retries - attempt} attempts remaining)")
        else:
            print(f"  ⚠️  Maximum retries ({max_retries}) exhausted!")

# Final status
print("\n" + "-" * 40)
if login_successful:
    print(f"Final Result: Login succeeded after {attempt} attempt(s).")
else:
    print(f"Final Result: Login failed after {attempt} attempt(s). Aborting test.")


# ============================================================
# PRACTICE TASK 4: Multiplication Table Using Nested Loops
# ============================================================
# Task: Print a multiplication table using nested loops

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Multiplication Table (Nested Loops)")
print("=" * 60)

# Print multiplication table from 1 to 10
table_size = 10

# Print header row
print(f"\n{'×':>4}", end="")
for col in range(1, table_size + 1):
    print(f"{col:>5}", end="")
print()  # newline
print("-" * (4 + 5 * table_size))

# Print each row
for row in range(1, table_size + 1):
    print(f"{row:>4}", end="")       # Row number
    for col in range(1, table_size + 1):
        product = row * col
        print(f"{product:>5}", end="")
    print()  # newline after each row

# Simpler version — multiplication table for a single number
print("\n--- Single Number Table ---")
number = 7
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"  {number} × {i:>2} = {number * i:>3}")

print("\n--- Topic 3 Complete! ---")
