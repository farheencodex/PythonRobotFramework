"""
Topic 1 — Python Basics | Python for Automation Course
=======================================================
This file covers the foundational concepts of Python programming.
Every concept is explained with inline comments so you can learn by reading the code.

Concepts Covered:
    - What is Python? Why Python for Automation?
    - First Python program — print("Hello, World!")
    - Comments — single line (#) and multi-line (''' ''')
    - Variables and dynamic typing
    - Data types — int, float, str, bool, NoneType
    - Type checking — type() and isinstance()
    - Type conversion — int(), str(), float(), bool()
    - Taking user input — input()
    - print() with formatting — f-strings, .format(), %

Practice Tasks:
    1. Name and age greeter
    2. Celsius to Fahrenheit converter
    3. All type conversions demo

How to Run:
    python python_basics.py
"""


# ============================================================
# SECTION 1: What is Python? Why Python for Automation?
# ============================================================

# Python is a high-level, interpreted, general-purpose programming language.
# It was created by Guido van Rossum and first released in 1991.

# WHY PYTHON FOR AUTOMATION?
# 1. Simple and readable syntax — easy to learn and maintain
# 2. Rich ecosystem — libraries like Selenium, pytest, requests, Robot Framework
# 3. Cross-platform — runs on Windows, macOS, Linux
# 4. Large community — extensive documentation and support
# 5. Integration-friendly — works with REST APIs, databases, CI/CD tools
# 6. Dynamic typing — write less boilerplate code
# 7. Rapid prototyping — quickly automate repetitive tasks


# ============================================================
# SECTION 2: First Python Program — print()
# ============================================================

# print() is a built-in function that outputs text to the console.
# It's the most basic way to display information.

print("Hello, World!")                   # Output: Hello, World!
print("Welcome to Python for Automation!")  # Output: Welcome to Python for Automation!

# You can print multiple values separated by commas (adds space between them)
print("Python", "is", "awesome")         # Output: Python is awesome

# You can change the separator using the 'sep' parameter
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome

# You can change the ending character using 'end' parameter
print("Hello", end=" ")                 # Does NOT add newline at end
print("World!")                          # Output: Hello World! (on same line)

# Print an empty line
print()                                  # Output: (blank line)


# ============================================================
# SECTION 3: Comments
# ============================================================

# SINGLE LINE COMMENT:
# Anything after '#' on a line is a comment — Python ignores it.
# Use comments to explain your code or temporarily disable code.

# This is a single line comment
x = 10  # This is an inline comment — explains what x is

# MULTI-LINE COMMENTS:
# Python doesn't have a dedicated multi-line comment syntax.
# We use triple quotes (''' or """) which create a multi-line string.
# When not assigned to a variable, Python ignores them.

'''
This is a multi-line comment.
It spans across multiple lines.
Python treats it as a string literal but ignores it
because it's not assigned to any variable.
'''

"""
You can also use double triple-quotes
for multi-line comments. Both work the same way.
This is commonly used for docstrings (documentation strings)
at the beginning of functions, classes, and modules.
"""

print("\n--- Comments Section Complete ---\n")


# ============================================================
# SECTION 4: Variables and Dynamic Typing
# ============================================================

# A VARIABLE is a name that refers to a value stored in memory.
# In Python, you don't need to declare the type — Python figures it out.
# This is called DYNAMIC TYPING.

# Creating variables — no need to specify type
name = "Tayyab"          # str (string) — text data
age = 25                 # int (integer) — whole numbers
height = 5.9             # float — decimal numbers
is_tester = True         # bool (boolean) — True or False
salary = None            # NoneType — represents "no value" or "nothing"

# Python is DYNAMICALLY TYPED — you can reassign a variable to a different type
my_variable = 10         # my_variable is an int
print(f"my_variable = {my_variable}, type = {type(my_variable)}")

my_variable = "Hello"    # Now my_variable is a str — no error!
print(f"my_variable = {my_variable}, type = {type(my_variable)}")

my_variable = 3.14       # Now my_variable is a float
print(f"my_variable = {my_variable}, type = {type(my_variable)}")

# VARIABLE NAMING RULES:
# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, digits (0-9), and underscores
# 3. Cannot start with a digit
# 4. Cannot use Python keywords (if, else, for, while, class, etc.)
# 5. Case-sensitive — 'Name' and 'name' are different variables

# NAMING CONVENTIONS (best practices):
# - Use snake_case for variables and functions: my_variable, test_case_id
# - Use PascalCase for classes: TestCase, LoginPage
# - Use UPPER_CASE for constants: MAX_RETRIES, BASE_URL
# - Use descriptive names: test_status (good) vs ts (bad)

first_name = "Tayyab"    # snake_case — good practice
lastName = "Ahmed"       # camelCase — works but not Pythonic
MAX_RETRIES = 3          # UPPER_CASE — indicates a constant

# Multiple assignment — assign multiple variables in one line
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")  # Output: a=1, b=2, c=3

# Same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")  # Output: x=0, y=0, z=0

print("\n--- Variables Section Complete ---\n")


# ============================================================
# SECTION 5: Data Types
# ============================================================

# Python has several built-in data types. The most common ones are:

# 1. int — Integer (whole numbers, positive or negative, no decimals)
count = 100
negative_num = -42
big_number = 1_000_000   # Underscores for readability (same as 1000000)
print(f"int examples: {count}, {negative_num}, {big_number}")

# 2. float — Floating point (numbers with decimals)
price = 19.99
pi = 3.14159
scientific = 2.5e3       # Scientific notation: 2.5 × 10³ = 2500.0
print(f"float examples: {price}, {pi}, {scientific}")

# 3. str — String (text data, enclosed in quotes)
greeting = "Hello"        # Double quotes
language = 'Python'       # Single quotes — both work the same
multiline = """This is
a multi-line
string"""                 # Triple quotes for multi-line strings
print(f"str examples: {greeting}, {language}")
print(f"Multi-line string:\n{multiline}")

# 4. bool — Boolean (True or False)
# Note: True and False are capitalized in Python!
is_active = True
is_deleted = False
print(f"bool examples: is_active={is_active}, is_deleted={is_deleted}")

# Booleans are actually integers: True = 1, False = 0
print(f"True + True = {True + True}")    # Output: 2
print(f"True * 10 = {True * 10}")        # Output: 10
print(f"False + 5 = {False + 5}")        # Output: 5

# 5. NoneType — Represents the absence of a value
result = None
print(f"NoneType example: result={result}")  # Output: result=None

# None is NOT the same as 0, False, or empty string ""
# None means "no value assigned" or "nothing"

print("\n--- Data Types Section Complete ---\n")


# ============================================================
# SECTION 6: Type Checking — type() and isinstance()
# ============================================================

# type() — Returns the type of a value/variable
print("--- type() examples ---")
print(type(42))            # Output: <class 'int'>
print(type(3.14))          # Output: <class 'float'>
print(type("Hello"))       # Output: <class 'str'>
print(type(True))          # Output: <class 'bool'>
print(type(None))          # Output: <class 'NoneType'>
print(type([1, 2, 3]))     # Output: <class 'list'>

# isinstance() — Checks if a value is of a specific type (returns True/False)
# More flexible than type() because it also checks inheritance
print("\n--- isinstance() examples ---")
print(isinstance(42, int))          # Output: True
print(isinstance(3.14, float))      # Output: True
print(isinstance("Hello", str))     # Output: True
print(isinstance(True, bool))       # Output: True
print(isinstance(True, int))        # Output: True (bool is a subclass of int!)
print(isinstance(None, type(None))) # Output: True

# isinstance() can check against multiple types using a tuple
value = 42
print(isinstance(value, (int, float)))  # Output: True (is it int OR float?)

# PRACTICAL USE CASE: Validate test data types before processing
test_data = "TC001"
if isinstance(test_data, str):
    print(f"Valid test case ID: {test_data}")
else:
    print("Error: Test case ID must be a string!")

print("\n--- Type Checking Section Complete ---\n")


# ============================================================
# SECTION 7: Type Conversion (Casting)
# ============================================================

# Python allows converting between types using built-in functions.

# int() — Convert to integer
print("--- int() conversions ---")
print(int(3.99))          # float → int: 3 (truncates, does NOT round)
print(int("42"))          # str → int: 42 (string must contain a valid number)
print(int(True))          # bool → int: 1
print(int(False))         # bool → int: 0
# print(int("hello"))     # ERROR! Cannot convert non-numeric string to int

# float() — Convert to float
print("\n--- float() conversions ---")
print(float(42))          # int → float: 42.0
print(float("3.14"))      # str → float: 3.14
print(float("42"))        # str → float: 42.0
print(float(True))        # bool → float: 1.0

# str() — Convert to string
print("\n--- str() conversions ---")
print(str(42))            # int → str: "42"
print(str(3.14))          # float → str: "3.14"
print(str(True))          # bool → str: "True"
print(str(None))          # NoneType → str: "None"
print(str([1, 2, 3]))     # list → str: "[1, 2, 3]"

# bool() — Convert to boolean
print("\n--- bool() conversions ---")
# TRUTHY values (convert to True):
print(bool(1))            # Non-zero int → True
print(bool(3.14))         # Non-zero float → True
print(bool("Hello"))      # Non-empty string → True
print(bool([1, 2]))       # Non-empty list → True

# FALSY values (convert to False):
print(bool(0))            # Zero → False
print(bool(0.0))          # Zero float → False
print(bool(""))           # Empty string → False
print(bool([]))           # Empty list → False
print(bool(None))         # None → False

print("\n--- Type Conversion Section Complete ---\n")


# ============================================================
# SECTION 8: Taking User Input — input()
# ============================================================

# input() reads a line of text from the user and returns it as a STRING.
# Whatever the user types is ALWAYS returned as a string, even if they type a number.

# IMPORTANT: input() calls are commented out below so this file can run
# without user interaction. Uncomment them to try interactive mode.

# --- Interactive version (uncomment to try) ---
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# user_age = input("Enter your age: ")  # Returns a STRING like "25"
# user_age = int(user_age)               # Must convert to int for math operations
# print(f"In 5 years, you will be {user_age + 5} years old.")

# --- Non-interactive version (hardcoded for demonstration) ---
user_name = "Tayyab"     # Simulating input("Enter your name: ")
user_age = "25"          # Simulating input("Enter your age: ") — note: it's a string!

print(f"Simulated input — Name: {user_name}, Age: {user_age}")
print(f"Age is a string: {type(user_age)}")

# Convert string to int for calculations
user_age_int = int(user_age)
print(f"After conversion — Age: {user_age_int}, Type: {type(user_age_int)}")
print(f"In 5 years, you will be {user_age_int + 5} years old.")

print("\n--- User Input Section Complete ---\n")


# ============================================================
# SECTION 9: print() with Formatting
# ============================================================

# There are 3 main ways to format strings in Python:

name = "Tayyab"
age = 25
score = 95.678

# METHOD 1: f-strings (f"...") — PREFERRED, Python 3.6+
# Put 'f' before the string and use {variable_name} inside
print("--- f-strings (Recommended) ---")
print(f"Hello, {name}! You are {age} years old.")
print(f"Score: {score:.2f}")                    # Format float to 2 decimal places
print(f"Score: {score:.1f}")                    # Format float to 1 decimal place
print(f"Name in uppercase: {name.upper()}")     # Call methods inside f-string
print(f"2 + 3 = {2 + 3}")                       # Expressions inside f-string
print(f"{'Pass' if score > 50 else 'Fail'}")    # Ternary inside f-string

# Padding and alignment with f-strings
print(f"{'Left':<20}|")      # Left-align in 20 chars
print(f"{'Center':^20}|")    # Center-align in 20 chars
print(f"{'Right':>20}|")     # Right-align in 20 chars

# METHOD 2: .format() — Older but still widely used
print("\n--- .format() method ---")
print("Hello, {}! You are {} years old.".format(name, age))
print("Hello, {0}! You are {1} years old. {0} is great!".format(name, age))  # Indexed
print("Hello, {n}! You are {a} years old.".format(n=name, a=age))  # Named
print("Score: {:.2f}".format(score))             # Float formatting

# METHOD 3: % formatting — Oldest style (C-style)
print("\n--- % formatting (legacy) ---")
print("Hello, %s! You are %d years old." % (name, age))  # %s=string, %d=integer
print("Score: %.2f" % score)                              # %f=float with 2 decimals
# %s = string, %d = integer, %f = float, %x = hexadecimal

print("\n--- Formatting Section Complete ---\n")


# ============================================================
# PRACTICE TASK 1: Name and Age Greeter
# ============================================================
# Task: Write a program that takes a user's name and age as input
# and prints: "Hello Tayyab, you are 25 years old."

print("=" * 60)
print("PRACTICE TASK 1: Name and Age Greeter")
print("=" * 60)

# --- Interactive version (uncomment to try) ---
# name_input = input("Enter your name: ")
# age_input = input("Enter your age: ")

# --- Non-interactive (hardcoded) ---
name_input = "Tayyab"
age_input = "25"

# Using f-string (preferred method)
print(f"Hello {name_input}, you are {age_input} years old.")

# Using .format()
print("Hello {}, you are {} years old.".format(name_input, age_input))

# Using % formatting
print("Hello %s, you are %s years old." % (name_input, age_input))


# ============================================================
# PRACTICE TASK 2: Celsius to Fahrenheit Converter
# ============================================================
# Task: Write a program that converts temperature from Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Celsius to Fahrenheit Converter")
print("=" * 60)

# --- Interactive version (uncomment to try) ---
# celsius_input = input("Enter temperature in Celsius: ")
# celsius = float(celsius_input)

# --- Non-interactive (hardcoded) ---
celsius = 37.0  # Normal body temperature in Celsius

# Calculate Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")  # Formatted to 2 decimals

# Let's also try with a few more temperatures
test_temps = [0, 100, -40, 20, 37]
print("\nConversion Table:")
print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)
for temp_c in test_temps:
    temp_f = (temp_c * 9/5) + 32
    print(f"{temp_c:>10}°C | {temp_f:>10.2f}°F")


# ============================================================
# PRACTICE TASK 3: All Type Conversions Demo
# ============================================================
# Task: Demonstrate all type conversions with examples.

print("\n" + "=" * 60)
print("PRACTICE TASK 3: All Type Conversions Demo")
print("=" * 60)

print("\n--- Converting TO int ---")
values_to_int = [3.7, "42", True, False, 0.0]
for val in values_to_int:
    try:
        converted = int(val)
        print(f"int({val!r:>10}) = {converted:>5}  |  {type(val).__name__:>5} → int")
    except (ValueError, TypeError) as e:
        print(f"int({val!r:>10}) = ERROR: {e}")

print("\n--- Converting TO float ---")
values_to_float = [42, "3.14", True, False, "100"]
for val in values_to_float:
    try:
        converted = float(val)
        print(f"float({val!r:>10}) = {converted:>8}  |  {type(val).__name__:>5} → float")
    except (ValueError, TypeError) as e:
        print(f"float({val!r:>10}) = ERROR: {e}")

print("\n--- Converting TO str ---")
values_to_str = [42, 3.14, True, False, None, [1, 2]]
for val in values_to_str:
    converted = str(val)
    print(f"str({val!r:>10}) = {converted!r:>12}  |  {type(val).__name__:>9} → str")

print("\n--- Converting TO bool ---")
values_to_bool = [0, 1, -1, 0.0, 3.14, "", "Hello", None, [], [1], {}, {"a": 1}]
for val in values_to_bool:
    converted = bool(val)
    label = "TRUTHY" if converted else "FALSY"
    print(f"bool({val!r:>12}) = {str(converted):>5}  ({label})")

print("\n--- Topic 1 Complete! ---")
