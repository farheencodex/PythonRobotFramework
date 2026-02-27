"""
Topic 9 — Functions (Core to Reusability in Automation) | Python for Automation Course
========================================================================================
Functions are the building blocks of reusable, maintainable automation code.
Every page object method, test utility, and helper is a function.

Concepts Covered:
    - Defining and calling functions — def
    - Parameters and arguments
    - Default parameter values
    - *args — variable positional arguments
    - **kwargs — variable keyword arguments
    - Return statement — single and multiple return values
    - Scope — local vs global variables
    - global keyword
    - Lambda functions
    - Recursive functions (basic)
    - map(), filter(), zip() with lambda
    - Docstrings

Practice Tasks:
    1. Email validator function
    2. calculate_total() with default discount
    3. **kwargs to print test case details
    4. map() to uppercase test case IDs
    5. filter() to get failed test cases
    6. Lambda to sort by priority

How to Run:
    python functions.py
"""


# ============================================================
# SECTION 1: Defining and Calling Functions
# ============================================================

print("=" * 60)
print("SECTION 1: Defining and Calling Functions")
print("=" * 60)

# A FUNCTION is a reusable block of code that performs a specific task.
# Syntax: def function_name(parameters):
#             '''docstring'''
#             body
#             return value

# --- Defining a function ---
def greet():
    """A simple function that prints a greeting."""
    print("Hello! Welcome to Python Automation!")

# --- Calling a function ---
greet()       # Output: Hello! Welcome to Python Automation!
greet()       # You can call it multiple times

# Function with a parameter
def greet_user(name):
    """Greets a specific user."""
    print(f"Hello, {name}! Welcome aboard!")

greet_user("Tayyab")     # Output: Hello, Tayyab! Welcome aboard!
greet_user("Ali")        # Output: Hello, Ali! Welcome aboard!

# IMPORTANT TERMINOLOGY:
# PARAMETER — the variable in the function definition (name)
# ARGUMENT — the actual value passed when calling (Tayyab)

print()


# ============================================================
# SECTION 2: Parameters and Arguments
# ============================================================

print("=" * 60)
print("SECTION 2: Parameters and Arguments")
print("=" * 60)

# --- Positional arguments --- (order matters!)
def create_test_case(tc_id, title, priority):
    """Creates a test case with given details."""
    print(f"  TC: {tc_id} | {title} | Priority: {priority}")

# Arguments must be in the same order as parameters
create_test_case("TC001", "Login Test", "P0")
create_test_case("TC002", "Search Test", "P1")

# --- Keyword arguments --- (order doesn't matter!)
print()
create_test_case(priority="P0", tc_id="TC003", title="Cart Test")

# --- Default parameter values ---
print("\n--- Default Parameters ---")

def run_test(tc_id, browser="Chrome", headless=False):
    """Runs a test with configurable browser and headless mode."""
    mode = "headless" if headless else "headed"
    print(f"  Running {tc_id} on {browser} ({mode})")

run_test("TC001")                            # Uses defaults: Chrome, headed
run_test("TC002", "Firefox")                 # Override browser only
run_test("TC003", "Edge", True)              # Override both
run_test("TC004", headless=True)             # Keyword arg to skip browser

# IMPORTANT: Default parameters must come AFTER non-default ones
# def bad_func(default_param="x", required_param):  # SyntaxError!

print()


# ============================================================
# SECTION 3: *args — Variable Positional Arguments
# ============================================================
# *args lets a function accept ANY NUMBER of positional arguments.
# Inside the function, args is a TUPLE.

print("=" * 60)
print("SECTION 3: *args (Variable Positional Arguments)")
print("=" * 60)

def run_test_suite(*test_case_ids):
    """Runs a variable number of test cases."""
    print(f"  Running {len(test_case_ids)} test case(s):")
    for tc in test_case_ids:
        print(f"    → Executing: {tc}")

# Call with different number of arguments
run_test_suite("TC001")
print()
run_test_suite("TC001", "TC002", "TC003")
print()
run_test_suite("TC001", "TC002", "TC003", "TC004", "TC005")

# *args with regular parameters
def log_results(tester_name, *results):
    """Logs test results for a tester."""
    print(f"\n  Tester: {tester_name}")
    print(f"  Results: {results}")
    for i, result in enumerate(results, 1):
        print(f"    Test {i}: {result}")

log_results("Tayyab", "Pass", "Fail", "Pass", "Pass")

# Unpacking a list into *args
tc_list = ["TC001", "TC002", "TC003"]
run_test_suite(*tc_list)  # Unpacks the list into separate arguments

print()


# ============================================================
# SECTION 4: **kwargs — Variable Keyword Arguments
# ============================================================
# **kwargs lets a function accept ANY NUMBER of keyword arguments.
# Inside the function, kwargs is a DICTIONARY.

print("=" * 60)
print("SECTION 4: **kwargs (Variable Keyword Arguments)")
print("=" * 60)

def print_test_details(**details):
    """Prints all test case details dynamically."""
    print("  Test Case Details:")
    for key, value in details.items():
        # Convert key from snake_case to Title Case for display
        display_key = key.replace("_", " ").title()
        print(f"    {display_key}: {value}")

print_test_details(
    tc_id="TC_001",
    title="Login Test",
    status="Pass",
    priority="P0",
    execution_time=2.5,
    assigned_to="Tayyab"
)

# Combining regular params, *args, and **kwargs
print("\n--- Combining all parameter types ---")

def configure_test(env, *browsers, **options):
    """Configure test with environment, browsers, and options."""
    print(f"  Environment: {env}")
    print(f"  Browsers: {browsers}")
    print(f"  Options: {options}")

configure_test(
    "Staging",                          # Regular param
    "Chrome", "Firefox", "Edge",        # *args
    headless=True, timeout=30, retries=3  # **kwargs
)

print()


# ============================================================
# SECTION 5: Return Statement
# ============================================================

print("=" * 60)
print("SECTION 5: Return Statement")
print("=" * 60)

# --- Single return value ---
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(10, 20)
print(f"add(10, 20) = {result}")     # 30

# --- Multiple return values (returned as a tuple) ---
def get_test_stats(results):
    """Returns pass count, fail count, and pass percentage."""
    total = len(results)
    passed = results.count("Pass")
    failed = results.count("Fail")
    percentage = (passed / total) * 100 if total > 0 else 0
    return passed, failed, percentage  # Returns a tuple

results = ["Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]
pass_count, fail_count, pass_pct = get_test_stats(results)
print(f"\nStats: {pass_count} passed, {fail_count} failed, {pass_pct:.1f}% pass rate")

# --- Return None implicitly ---
def greet_only(name):
    """Function without explicit return — returns None."""
    print(f"Hello, {name}!")
    # No return statement → returns None implicitly

result = greet_only("World")
print(f"Return value: {result}")     # None

# --- Early return (guard clause) ---
def divide(a, b):
    """Divides a by b with safety check."""
    if b == 0:
        return "Error: Division by zero!"  # Early return
    return a / b

print(f"\ndivide(10, 3) = {divide(10, 3)}")
print(f"divide(10, 0) = {divide(10, 0)}")

print()


# ============================================================
# SECTION 6: Scope — Local vs Global Variables
# ============================================================

print("=" * 60)
print("SECTION 6: Variable Scope")
print("=" * 60)

# GLOBAL variable — defined outside any function
global_var = "I am global"

def demo_scope():
    # LOCAL variable — defined inside a function
    local_var = "I am local"
    print(f"  Inside function: global_var = {global_var}")  # Can READ global
    print(f"  Inside function: local_var = {local_var}")

demo_scope()
print(f"Outside function: global_var = {global_var}")
# print(local_var)  # NameError! local_var doesn't exist outside the function

# --- global keyword ---
# Use 'global' to MODIFY a global variable inside a function
print("\n--- global keyword ---")

counter = 0   # Global variable

def increment():
    global counter   # Declare that we want to modify the global 'counter'
    counter += 1
    print(f"  Counter inside function: {counter}")

print(f"Counter before: {counter}")
increment()   # Counter becomes 1
increment()   # Counter becomes 2
increment()   # Counter becomes 3
print(f"Counter after:  {counter}")

# BEST PRACTICE: Avoid global variables in automation!
# Pass values as parameters and return results instead.
# Global state makes tests unpredictable and hard to debug.

print()


# ============================================================
# SECTION 7: Lambda Functions
# ============================================================
# Lambda functions are small, anonymous (unnamed) functions.
# Syntax: lambda parameters: expression

print("=" * 60)
print("SECTION 7: Lambda Functions")
print("=" * 60)

# Regular function
def square(x):
    return x ** 2

# Same thing as lambda
square_lambda = lambda x: x ** 2

print(f"Regular function: square(5) = {square(5)}")
print(f"Lambda function:  square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"add(3, 7) = {add(3, 7)}")

# Lambda with conditional
status = lambda score: "Pass" if score >= 60 else "Fail"
print(f"status(85) = {status(85)}")
print(f"status(45) = {status(45)}")

# Lambda is most useful as an argument to other functions (sort, map, filter)
# See Sections 8 and 9 below

print()


# ============================================================
# SECTION 8: Recursive Functions (Basic)
# ============================================================
# A recursive function calls ITSELF. It must have a BASE CASE to stop.

print("=" * 60)
print("SECTION 8: Recursive Functions")
print("=" * 60)

# Factorial: n! = n × (n-1) × (n-2) × ... × 1
# 5! = 5 × 4 × 3 × 2 × 1 = 120
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:           # Base case — stops the recursion
        return 1
    return n * factorial(n - 1)   # Recursive case — calls itself

print(f"factorial(5) = {factorial(5)}")     # 120
print(f"factorial(10) = {factorial(10)}")   # 3628800

# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the sum of the two before it
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFirst 10 Fibonacci numbers:")
fib_nums = [fibonacci(i) for i in range(10)]
print(f"  {fib_nums}")

# CAUTION: Recursive functions can be slow for large inputs
# and may hit Python's recursion limit (default: 1000)
# For production code, prefer iterative solutions or memoization

print()


# ============================================================
# SECTION 9: map(), filter(), zip() with Lambda
# ============================================================

print("=" * 60)
print("SECTION 9: map(), filter(), zip()")
print("=" * 60)

# --- map() --- applies a function to EVERY element of an iterable
print("--- map() ---")

# Convert list of TC IDs to uppercase
tc_ids = ["tc001", "tc002", "tc003", "tc004"]
upper_ids = list(map(str.upper, tc_ids))       # Using built-in method
print(f"map(upper): {upper_ids}")

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"map(square): {squares}")               # [1, 4, 9, 16, 25]

# map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda a, b: a + b, list1, list2))
print(f"map(add): {sums}")                     # [11, 22, 33]

# --- filter() --- keeps elements where the function returns True
print("\n--- filter() ---")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(even): {evens}")                # [2, 4, 6, 8, 10]

# Filter failed test cases
results = [("TC001", "Pass"), ("TC002", "Fail"), ("TC003", "Pass"), ("TC004", "Fail")]
failed = list(filter(lambda x: x[1] == "Fail", results))
print(f"filter(failed): {failed}")             # [('TC002', 'Fail'), ('TC004', 'Fail')]

# --- zip() --- combines multiple iterables element-by-element
print("\n--- zip() ---")

tc_ids = ["TC001", "TC002", "TC003"]
statuses = ["Pass", "Fail", "Pass"]
times = [2.5, 5.1, 1.8]

# zip creates tuples of corresponding elements
zipped = list(zip(tc_ids, statuses, times))
print(f"zip(): {zipped}")

# Common use: Create a dictionary from two lists
tc_status = dict(zip(tc_ids, statuses))
print(f"dict(zip()): {tc_status}")

# Iterate over zipped data
print("\nTest Results:")
for tc_id, status, time in zip(tc_ids, statuses, times):
    print(f"  {tc_id}: {status} ({time}s)")

print()


# ============================================================
# SECTION 10: Docstrings
# ============================================================

print("=" * 60)
print("SECTION 10: Docstrings")
print("=" * 60)

# Docstrings are string literals at the beginning of a function/class/module.
# They document what the code does, its parameters, and return values.

def calculate_pass_rate(total, passed):
    """
    Calculate the test pass rate as a percentage.
    
    Args:
        total (int): Total number of test cases executed.
        passed (int): Number of test cases that passed.
    
    Returns:
        float: Pass rate as a percentage (0.0 to 100.0).
    
    Raises:
        ValueError: If total is 0 or negative.
    
    Example:
        >>> calculate_pass_rate(10, 8)
        80.0
    """
    if total <= 0:
        raise ValueError("Total must be a positive number")
    return (passed / total) * 100

# Access the docstring
print(f"Function docstring:\n{calculate_pass_rate.__doc__}")

# Use the function
rate = calculate_pass_rate(10, 8)
print(f"\nPass rate: {rate}%")

# help() uses docstrings
print("\n--- help() output ---")
help(calculate_pass_rate)

print()


# ============================================================
# PRACTICE TASK 1: Email Validator Function
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Email Validator")
print("=" * 60)

def is_valid_email(email):
    """
    Validates if an email address is valid.
    
    Rules:
        - Must contain exactly one '@' symbol
        - Must end with '.com' or '.in'
        - Must have text before '@'
        - Must have text between '@' and the domain extension
    
    Args:
        email (str): Email address to validate.
    
    Returns:
        bool: True if email is valid, False otherwise.
    """
    # Check if @ exists and appears exactly once
    if email.count("@") != 1:
        return False
    
    # Check if it ends with .com or .in
    if not (email.endswith(".com") or email.endswith(".in")):
        return False
    
    # Split at @ and check both parts have content
    local, domain = email.split("@")
    if len(local) == 0 or len(domain) < 4:  # domain needs at least "x.in"
        return False
    
    return True

# Test with various email addresses
test_emails = [
    "testuser@gmail.com",
    "admin@company.in",
    "invalid.email.com",     # Missing @
    "@gmail.com",            # Nothing before @
    "user@.com",             # Nothing between @ and .com
    "tayyab@boodmo.com",
    "test@@double.com",      # Double @
    "user@domain.org",       # Wrong extension
]

print(f"\n{'Email':<30} | {'Valid?'}")
print("-" * 45)
for email in test_emails:
    result = is_valid_email(email)
    icon = "✓" if result else "✗"
    print(f"{email:<30} | {icon} {result}")


# ============================================================
# PRACTICE TASK 2: calculate_total() with Default Discount
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: calculate_total() with Default Discount")
print("=" * 60)

def calculate_total(price, qty, discount=0):
    """
    Calculate total price with optional discount.
    
    Args:
        price (float): Price per unit.
        qty (int): Quantity of items.
        discount (float): Discount percentage (0-100). Default is 0.
    
    Returns:
        float: Total price after discount.
    """
    subtotal = price * qty
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount
    return total

# Without discount (uses default 0)
total1 = calculate_total(100, 5)
print(f"calculate_total(100, 5)         = ₹{total1:.2f}")

# With 10% discount
total2 = calculate_total(100, 5, 10)
print(f"calculate_total(100, 5, 10)     = ₹{total2:.2f}")

# With 25% discount using keyword
total3 = calculate_total(price=250, qty=3, discount=25)
print(f"calculate_total(250, 3, 25)     = ₹{total3:.2f}")

# Detailed breakdown
print(f"\nDetailed Calculation:")
price, qty, discount = 500, 2, 15
subtotal = price * qty
disc_amount = subtotal * (discount / 100)
total = calculate_total(price, qty, discount)
print(f"  Price: ₹{price} × {qty} = ₹{subtotal}")
print(f"  Discount: {discount}% = -₹{disc_amount:.2f}")
print(f"  Total: ₹{total:.2f}")


# ============================================================
# PRACTICE TASK 3: **kwargs to Print Test Case Details
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: **kwargs Test Details Printer")
print("=" * 60)

def print_tc_details(**kwargs):
    """
    Prints test case details dynamically using **kwargs.
    Accepts any number of keyword arguments.
    
    Example:
        print_tc_details(tc_id="TC001", status="Pass")
    """
    print("\n  ┌─── Test Case Details ───┐")
    for key, value in kwargs.items():
        formatted_key = key.replace("_", " ").title()
        print(f"  │ {formatted_key:<18}: {value}")
    print(f"  └{'─' * 25}┘")

# Call with different sets of keyword arguments
print_tc_details(
    tc_id="TC_001",
    title="Verify Login",
    status="Pass",
    priority="P0"
)

print_tc_details(
    tc_id="TC_002",
    title="Verify Search",
    module="Search",
    status="Fail",
    bug_id="BUG-789",
    assigned_to="Tayyab",
    execution_time="5.2s"
)


# ============================================================
# PRACTICE TASK 4: map() to Uppercase TC IDs
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: map() — Uppercase TC IDs")
print("=" * 60)

# List of test case IDs in mixed/lowercase
tc_ids = ["tc_001", "tc_002", "Tc_003", "TC_004", "tc_005"]
print(f"Original:    {tc_ids}")

# Use map() to convert all to uppercase
upper_ids = list(map(str.upper, tc_ids))
print(f"Uppercased:  {upper_ids}")

# Alternative: map with lambda
upper_ids_v2 = list(map(lambda tc: tc.upper(), tc_ids))
print(f"Via lambda:  {upper_ids_v2}")

# Bonus: Add prefix using map
prefixed = list(map(lambda tc: f"REGRESSION_{tc.upper()}", tc_ids))
print(f"Prefixed:    {prefixed}")


# ============================================================
# PRACTICE TASK 5: filter() — Get Failed Test Cases
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 5: filter() — Failed Test Cases")
print("=" * 60)

# List of (tc_id, status) tuples
all_results = [
    ("TC001", "Pass"),
    ("TC002", "Fail"),
    ("TC003", "Pass"),
    ("TC004", "Fail"),
    ("TC005", "Pass"),
    ("TC006", "Fail"),
]

print(f"All results: {all_results}")

# Filter failed test cases using filter() and lambda
failed_tests = list(filter(lambda x: x[1] == "Fail", all_results))
print(f"\nFailed tests: {failed_tests}")

# Extract just the TC IDs of failed tests
failed_ids = [tc_id for tc_id, _ in failed_tests]
print(f"Failed IDs:   {failed_ids}")

# Also get passed tests
passed_tests = list(filter(lambda x: x[1] == "Pass", all_results))
print(f"Passed tests: {passed_tests}")

# Summary
print(f"\nTotal: {len(all_results)} | Passed: {len(passed_tests)} | Failed: {len(failed_tests)}")


# ============================================================
# PRACTICE TASK 6: Lambda to Sort by Priority
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 6: Lambda Sort by Priority")
print("=" * 60)

# Test cases with priority
test_cases = [
    {"id": "TC001", "title": "Login Test", "priority": "P2"},
    {"id": "TC002", "title": "Checkout Test", "priority": "P0"},
    {"id": "TC003", "title": "Search Test", "priority": "P1"},
    {"id": "TC004", "title": "Profile Test", "priority": "P3"},
    {"id": "TC005", "title": "Cart Test", "priority": "P0"},
]

print("Before sorting:")
for tc in test_cases:
    print(f"  {tc['id']}: {tc['title']} [{tc['priority']}]")

# Sort by priority using lambda as key function
# P0 < P1 < P2 < P3 (string comparison works here!)
sorted_tcs = sorted(test_cases, key=lambda tc: tc["priority"])

print("\nAfter sorting by priority:")
for tc in sorted_tcs:
    print(f"  {tc['id']}: {tc['title']} [{tc['priority']}]")

# Sort by priority (descending) and then by title
sorted_desc = sorted(test_cases, key=lambda tc: (tc["priority"], tc["title"]), reverse=True)
print("\nSorted by priority (desc):")
for tc in sorted_desc:
    print(f"  {tc['id']}: {tc['title']} [{tc['priority']}]")

print("\n--- Topic 9 Complete! ---")
