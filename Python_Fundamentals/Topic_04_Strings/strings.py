"""
Topic 4 — Strings (Critical for Automation) | Python for Automation Course
===========================================================================
Strings are used EVERYWHERE in automation — URLs, locators, test data, logs,
assertions, API payloads, file paths, and more. Master strings thoroughly!

Concepts Covered:
    - String creation, indexing, slicing
    - String immutability
    - String methods (20+ methods)
    - String formatting — f-strings, .format(), %s
    - String concatenation and repetition
    - Multi-line strings
    - Escape characters
    - Raw strings
    - String comparison

Practice Tasks:
    1. URL parsing — strip, extract domain, uppercase
    2. Email validation using string methods
    3. Split CSV test data string into list
    4. f-string formatted test report line

How to Run:
    python strings.py
"""


# ============================================================
# SECTION 1: String Creation, Indexing, and Slicing
# ============================================================

print("=" * 60)
print("SECTION 1: String Creation, Indexing, and Slicing")
print("=" * 60)

# --- String Creation ---
# Strings can be created with single quotes, double quotes, or triple quotes
single = 'Hello'              # Single quotes
double = "Hello"              # Double quotes — both are identical
triple_single = '''Hello'''   # Triple single quotes
triple_double = """Hello"""   # Triple double quotes

# All produce the same string
print(f"All equal: {single == double == triple_single == triple_double}")  # True

# When to use which?
# - Single quotes: Most common for simple strings
# - Double quotes: When string contains single quote — "It's Python"
# - Triple quotes: For multi-line strings or strings with both quote types

contains_single = "It's a test"         # Double quotes avoid escaping
contains_double = 'He said "hello"'     # Single quotes avoid escaping
contains_both = """It's a "test" case"""  # Triple quotes handle both

print(contains_single)
print(contains_double)
print(contains_both)

# --- Indexing ---
# Each character in a string has a position (index), starting from 0.
# You can also use NEGATIVE indexing, which counts from the end.

text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5    ← Positive index (left to right)
#      -6 -5 -4 -3 -2 -1   ← Negative index (right to left)

print(f"\ntext = '{text}'")
print(f"text[0]  = '{text[0]}'")    # P — first character
print(f"text[1]  = '{text[1]}'")    # y — second character
print(f"text[-1] = '{text[-1]}'")   # n — last character
print(f"text[-2] = '{text[-2]}'")   # o — second to last

# --- Slicing ---
# Syntax: string[start:stop:step]
# - start: included (default 0)
# - stop: excluded (default end)
# - step: increment (default 1)

url = "https://www.boodmo.com"
print(f"\nurl = '{url}'")

print(f"url[0:5]    = '{url[0:5]}'")      # 'https' — characters 0 to 4
print(f"url[8:]     = '{url[8:]}'")        # 'www.boodmo.com' — from index 8 to end
print(f"url[:5]     = '{url[:5]}'")        # 'https' — from start to index 4
print(f"url[-3:]    = '{url[-3:]}'")       # 'com' — last 3 characters
print(f"url[::2]    = '{url[::2]}'")       # Every 2nd character
print(f"url[::-1]   = '{url[::-1]}'")      # Reversed string

# Practical: Extract protocol from URL
protocol = url[:url.index("://")]          # 'https'
print(f"Protocol: {protocol}")

print()


# ============================================================
# SECTION 2: String Immutability
# ============================================================
# Strings in Python are IMMUTABLE — you CANNOT change them after creation.
# Any "modification" creates a NEW string.

print("=" * 60)
print("SECTION 2: String Immutability")
print("=" * 60)

name = "Python"
print(f"Original: {name}")

# This would cause an error:
# name[0] = "J"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string
new_name = "J" + name[1:]  # "J" + "ython" = "Jython"
print(f"Modified: {new_name}")
print(f"Original unchanged: {name}")  # Original is still "Python"

# Using replace() — also creates a new string
replaced = name.replace("P", "J")
print(f"Replaced: {replaced}")
print(f"Original unchanged: {name}")  # Still "Python"

print()


# ============================================================
# SECTION 3: String Methods
# ============================================================
# Python provides 40+ built-in string methods. Here are the most important ones.

print("=" * 60)
print("SECTION 3: String Methods")
print("=" * 60)

# --- Case Conversion Methods ---
print("--- Case Conversion ---")
text = "hello World PYTHON"

print(f"upper()      : '{text.upper()}'")       # 'HELLO WORLD PYTHON'
print(f"lower()      : '{text.lower()}'")       # 'hello world python'
print(f"title()      : '{text.title()}'")       # 'Hello World Python'
print(f"capitalize() : '{text.capitalize()}'")  # 'Hello world python' (only first char)
print(f"swapcase()   : '{text.swapcase()}'")    # 'HELLO wORLD python'

# --- Whitespace Methods ---
print("\n--- Whitespace Handling ---")
messy = "   Hello World   "
print(f"Original     : '{messy}'")
print(f"strip()      : '{messy.strip()}'")      # Remove whitespace from BOTH sides
print(f"lstrip()     : '{messy.lstrip()}'")     # Remove whitespace from LEFT only
print(f"rstrip()     : '{messy.rstrip()}'")     # Remove whitespace from RIGHT only

# strip() can also remove specific characters
url_messy = "///path/to/page///"
print(f"strip('/')   : '{url_messy.strip('/')}'")   # 'path/to/page'

# --- Search Methods ---
print("\n--- Search Methods ---")
text = "Test Case TC_001 has status PASS"

print(f"find('TC')       : {text.find('TC')}")         # 10 — index where 'TC' starts
print(f"find('XYZ')      : {text.find('XYZ')}")        # -1 — not found (no error)
# print(f"index('XYZ')   : {text.index('XYZ')}")       # Would raise ValueError!
print(f"count('s')       : {text.count('s')}")          # 3 — number of occurrences
print(f"startswith('Test'): {text.startswith('Test')}")  # True
print(f"endswith('PASS') : {text.endswith('PASS')}")     # True
print(f"endswith('FAIL') : {text.endswith('FAIL')}")     # False

# --- Replace Method ---
print("\n--- replace() ---")
text = "Status: FAIL"
new_text = text.replace("FAIL", "PASS")  # Replace FAIL with PASS
print(f"Original : '{text}'")
print(f"Replaced : '{new_text}'")

# Replace with count limit
text = "a-b-c-d-e"
print(f"Replace first 2 '-': '{text.replace('-', '_', 2)}'")  # 'a_b_c-d-e'

# --- Split and Join ---
print("\n--- split() and join() ---")

# split() — breaks string into a LIST using a delimiter
csv_data = "TC001,TC002,TC003,TC004"
tc_list = csv_data.split(",")       # Split by comma
print(f"split(','): {tc_list}")     # ['TC001', 'TC002', 'TC003', 'TC004']

sentence = "Python is great for automation"
words = sentence.split()            # Split by whitespace (default)
print(f"split(): {words}")          # ['Python', 'is', 'great', 'for', 'automation']

# split with maxsplit — limit the number of splits
text = "one:two:three:four"
print(f"split(':', 2): {text.split(':', 2)}")  # ['one', 'two', 'three:four']

# join() — combines a LIST into a string using a delimiter
tc_list = ["TC001", "TC002", "TC003"]
joined = ", ".join(tc_list)         # Join with comma+space
print(f"join(): '{joined}'")        # 'TC001, TC002, TC003'

joined_dash = "-".join(tc_list)
print(f"join('-'): '{joined_dash}'")  # 'TC001-TC002-TC003'

# Practical: Build a URL path
path_parts = ["https:", "", "www.boodmo.com", "search"]
url = "/".join(path_parts)
print(f"URL: {url}")

# --- Checking Methods (return True/False) ---
print("\n--- Checking Methods ---")
print(f"'12345'.isdigit()    : {'12345'.isdigit()}")      # True — all digits?
print(f"'Hello'.isalpha()    : {'Hello'.isalpha()}")      # True — all letters?
print(f"'Hello123'.isalnum() : {'Hello123'.isalnum()}")   # True — all letters or digits?
print(f"'hello'.islower()    : {'hello'.islower()}")      # True — all lowercase?
print(f"'HELLO'.isupper()    : {'HELLO'.isupper()}")      # True — all uppercase?
print(f"'   '.isspace()      : {'   '.isspace()}")        # True — all whitespace?

print()


# ============================================================
# SECTION 4: String Formatting
# ============================================================

print("=" * 60)
print("SECTION 4: String Formatting")
print("=" * 60)

tc_id = "TC_001"
status = "PASS"
execution_time = 2.567
date = "26-Feb-2026"

# f-strings (PREFERRED) — Python 3.6+
# Put 'f' before the string and embed expressions in {curly braces}
print("--- f-strings (Recommended) ---")
print(f"Test Case {tc_id} has status: {status} and executed on {date}")
print(f"Execution time: {execution_time:.2f} seconds")   # 2 decimal places
print(f"Status: {status.lower()}")                        # Call methods inside {}
print(f"{'PASS' if status == 'PASS' else 'FAIL':>10}")  # Right-align in 10 chars

# .format() method
print("\n--- .format() method ---")
print("Test Case {} has status: {}".format(tc_id, status))
print("Test Case {id} has status: {s}".format(id=tc_id, s=status))

# % formatting (legacy — you'll see it in older code)
print("\n--- % formatting (legacy) ---")
print("Test Case %s has status: %s" % (tc_id, status))
print("Execution time: %.2f seconds" % execution_time)

print()


# ============================================================
# SECTION 5: String Concatenation and Repetition
# ============================================================

print("=" * 60)
print("SECTION 5: Concatenation and Repetition")
print("=" * 60)

# Concatenation (+) — joining strings together
first_name = "Tayyab"
last_name = "Ahmed"
full_name = first_name + " " + last_name  # Must add space manually
print(f"Concatenation: {full_name}")

# Repetition (*) — repeating strings
divider = "=-" * 30
print(f"Repetition: {divider}")
print("Ha" * 5)  # HaHaHaHaHa

# IMPORTANT: You can only concatenate string with string!
# age = 25
# print("Age: " + age)  # TypeError! Must convert: str(age)
age = 25
print("Age: " + str(age))  # Works — converted int to str

# Better approach: Use f-strings instead of concatenation
print(f"Age: {age}")        # Cleaner and handles type conversion automatically

print()


# ============================================================
# SECTION 6: Multi-line Strings
# ============================================================

print("=" * 60)
print("SECTION 6: Multi-line Strings")
print("=" * 60)

# Triple quotes allow strings to span multiple lines
query = """
SELECT tc_id, status, execution_time
FROM test_results
WHERE status = 'FAIL'
ORDER BY execution_time DESC
"""
print("SQL Query:")
print(query)

# Multi-line strings preserve all formatting, including indentation
html_template = """<html>
    <head><title>Test Report</title></head>
    <body>
        <h1>Test Results</h1>
        <p>Status: PASS</p>
    </body>
</html>"""
print("HTML Template:")
print(html_template)

# Line continuation with backslash (NOT multi-line string, just continuation)
long_url = "https://www.boodmo.com/search?" \
           "q=brake+pad&" \
           "category=brakes&" \
           "page=1"
print(f"\nLong URL: {long_url}")

print()


# ============================================================
# SECTION 7: Escape Characters
# ============================================================

print("=" * 60)
print("SECTION 7: Escape Characters")
print("=" * 60)

# Escape characters start with backslash (\) and represent special characters

print("\\n  → Newline:")
print("Line 1\nLine 2")           # \n = new line

print("\n\\t  → Tab:")
print("Column1\tColumn2\tColumn3")  # \t = tab

print("\n\\\\  → Backslash:")
print("C:\\Users\\tayya\\Documents")    # \\ = literal backslash

print("\n\\'  → Single quote:")
print('It\'s Python')              # \' = literal single quote

print("\n\\\"  → Double quote:")
print("He said \"Hello\"")         # \" = literal double quote

# \r = carriage return (moves cursor to beginning of line)
# \0 = null character
# \b = backspace

print()


# ============================================================
# SECTION 8: Raw Strings
# ============================================================
# Raw strings (prefix r"") treat backslashes as literal characters.
# Extremely useful for file paths and regular expressions!

print("=" * 60)
print("SECTION 8: Raw Strings")
print("=" * 60)

# Without raw string — backslashes get interpreted
print("Normal string: C:\\new_folder\\test")   # \\n would become newline without \\

# With raw string — backslashes are literal
print(r"Raw string   : C:\new_folder\test")    # \n stays as \n

# File paths — raw strings make them easier
file_path = r"C:\Users\tayya\Downloads\test_data.csv"
print(f"File path: {file_path}")

# Regular expressions — raw strings are essential
import re
pattern = r"\d{3}-\d{3}-\d{4}"  # Phone number pattern: 123-456-7890
print(f"Regex pattern: {pattern}")

print()


# ============================================================
# SECTION 9: String Comparison
# ============================================================

print("=" * 60)
print("SECTION 9: String Comparison")
print("=" * 60)

# Strings are compared lexicographically (dictionary/alphabetical order)
# Each character is compared by its Unicode code point

print(f"'apple' == 'apple'  → {'apple' == 'apple'}")    # True — exact match
print(f"'apple' == 'Apple'  → {'apple' == 'Apple'}")    # False — case sensitive!
print(f"'apple' != 'banana' → {'apple' != 'banana'}")   # True — different
print(f"'apple' < 'banana'  → {'apple' < 'banana'}")    # True — 'a' < 'b'
print(f"'Apple' < 'apple'   → {'Apple' < 'apple'}")    # True — uppercase < lowercase

# Case-insensitive comparison — convert both to same case
str1 = "Pass"
str2 = "PASS"
print(f"\n'{str1}' == '{str2}' → {str1 == str2}")                      # False
print(f"Case-insensitive:  → {str1.lower() == str2.lower()}")          # True

# PRACTICAL: Assert test status (case-insensitive)
expected = "pass"
actual = "PASS"
assert actual.lower() == expected.lower(), f"Expected {expected}, got {actual}"
print("Assertion passed: Status matches (case-insensitive)")

print()


# ============================================================
# PRACTICE TASK 1: URL Parsing
# ============================================================
# Task: Given a URL " https://www.boodmo.com/search?q=brake ",
# strip whitespace, extract the domain name, and convert to uppercase

print("=" * 60)
print("PRACTICE TASK 1: URL Parsing")
print("=" * 60)

url = "  https://www.boodmo.com/search?q=brake  "
print(f"Original URL: '{url}'")

# Step 1: Strip whitespace from both sides
url_clean = url.strip()
print(f"After strip(): '{url_clean}'")

# Step 2: Extract the domain name
# Method 1: Using split()
# Split by '//' to get everything after protocol, then split by '/' to get domain
domain = url_clean.split("//")[1].split("/")[0]
print(f"Domain extracted: '{domain}'")

# Method 2: Using find() and slicing
start = url_clean.find("//") + 2           # Start after '//'
end = url_clean.find("/", start)           # Find next '/' after domain
domain_v2 = url_clean[start:end]
print(f"Domain (method 2): '{domain_v2}'")

# Step 3: Convert domain to uppercase
domain_upper = domain.upper()
print(f"Domain uppercase: '{domain_upper}'")

# Bonus: Extract query parameter
if "?" in url_clean:
    query = url_clean.split("?")[1]
    param_name, param_value = query.split("=")
    print(f"Query parameter: {param_name} = {param_value}")


# ============================================================
# PRACTICE TASK 2: Email Validation
# ============================================================
# Task: Check if email "testuser@gmail.com" contains @ and ends with .com

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Email Validation")
print("=" * 60)

emails_to_check = [
    "testuser@gmail.com",
    "admin@company.in",
    "invalidemailgmail.com",     # Missing @
    "user@domain.org",
    "test@.com",                 # Invalid but has @ and .com
    "hello@boodmo.com",
]

print(f"\n{'Email':<30} | {'Has @':>6} | {'Ends .com':>10} | {'Valid':>6}")
print("-" * 65)

for email in emails_to_check:
    has_at = "@" in email
    ends_com = email.endswith(".com") or email.endswith(".in")
    
    # Basic validation: must have @ AND end with .com or .in
    is_valid = has_at and ends_com
    
    # Additional check: @ should not be the first character
    if has_at:
        at_pos = email.index("@")
        if at_pos == 0:
            is_valid = False
    
    status = "✓ Valid" if is_valid else "✗ Invalid"
    print(f"{email:<30} | {str(has_at):>6} | {str(ends_com):>10} | {status:>8}")


# ============================================================
# PRACTICE TASK 3: Split CSV Test Data
# ============================================================
# Task: Split a comma-separated test data string into a list

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Split CSV Test Data")
print("=" * 60)

# Comma-separated test case IDs
csv_string = "TC001,TC002,TC003,TC004"
print(f"CSV String: '{csv_string}'")

# Split into a list using comma as delimiter
tc_list = csv_string.split(",")
print(f"After split: {tc_list}")

# Process each test case
print(f"\nTotal test cases: {len(tc_list)}")
for index, tc_id in enumerate(tc_list, start=1):
    print(f"  {index}. {tc_id}")

# Bonus: Join them back with a different delimiter
joined_pipe = " | ".join(tc_list)
print(f"\nJoined with pipe: '{joined_pipe}'")

# Bonus: More complex CSV with spaces
csv_messy = " TC001 , TC002 , TC003 , TC004 "
tc_list_clean = [tc.strip() for tc in csv_messy.split(",")]
print(f"\nMessy CSV: '{csv_messy}'")
print(f"Cleaned list: {tc_list_clean}")


# ============================================================
# PRACTICE TASK 4: f-string Formatted Test Report Line
# ============================================================
# Task: Use f-string to print:
# "Test Case TC_001 has status: PASS and executed on 26-Feb-2026"

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Formatted Test Report Line")
print("=" * 60)

# Test case data
tc_id = "TC_001"
status = "PASS"
execution_date = "26-Feb-2026"
execution_time = 3.456  # seconds
tester = "Tayyab"

# Using f-string (preferred method)
print(f"\nTest Case {tc_id} has status: {status} and executed on {execution_date}")

# Enhanced version with more details
print(f"\n{'='*50}")
print(f"  Test Report Entry")
print(f"{'='*50}")
print(f"  TC ID    : {tc_id}")
print(f"  Status   : {status}")
print(f"  Date     : {execution_date}")
print(f"  Time     : {execution_time:.2f} seconds")
print(f"  Tester   : {tester}")
print(f"  Result   : {'✓ PASSED' if status == 'PASS' else '✗ FAILED'}")
print(f"{'='*50}")

# Generating multiple report lines
print("\nBatch Test Report:")
test_cases = [
    ("TC_001", "PASS", 2.34),
    ("TC_002", "FAIL", 5.67),
    ("TC_003", "PASS", 1.23),
    ("TC_004", "PASS", 3.89),
    ("TC_005", "FAIL", 8.12),
]

print(f"\n{'TC ID':<10} | {'Status':<8} | {'Time (s)':<10} | {'Date'}")
print("-" * 50)
for tc, st, time_taken in test_cases:
    status_icon = "✓" if st == "PASS" else "✗"
    print(f"{tc:<10} | {status_icon} {st:<5} | {time_taken:<10.2f} | {execution_date}")

# Summary
pass_count = sum(1 for _, s, _ in test_cases if s == "PASS")
fail_count = len(test_cases) - pass_count
print(f"\nSummary: {pass_count} Passed, {fail_count} Failed out of {len(test_cases)} total")

print("\n--- Topic 4 Complete! ---")
