"""
Topic 13 — Modules and Packages | Python for Automation Course
================================================================
Modules and packages are how Python organizes reusable code.
In automation, you'll use built-in modules (os, json, csv), third-party
packages (selenium, pytest), and your OWN custom modules.

Concepts Covered:
    1. What are Modules? (import, from...import, aliases)
    2. Built-in modules overview (os, sys, math, random, datetime)
    3. The import system — how Python finds modules
    4. Creating your own modules
    5. What are Packages? (__init__.py, folder structure)
    6. Using your custom package (test_utils)
    7. Third-party packages (pip, requirements.txt)
    8. __name__ == "__main__" guard
    9. Module best practices

Practice Tasks:
    1. Use os module to explore the project structure
    2. Use datetime for test timing/reporting
    3. Import and use custom test_utils package
    4. Create a test runner using custom modules

Custom Package (included in this folder):
    test_utils/
        __init__.py   — Package init (imports + re-exports)
        utils.py      — Utility functions (generate_test_id, log_result)

How to Run:
    cd Topic_13_Modules_and_Packages
    python modules_demo.py
"""

# ============================================================
# SECTION 1: What are Modules?
# ============================================================

print("=" * 60)
print("SECTION 1: What are Modules?")
print("=" * 60)

# A MODULE is simply a .py file containing Python code.
# You IMPORT modules to use their functions, classes, and variables.

# --- Three ways to import ---

# Method 1: import the entire module
import os                # Now use: os.path.exists(), os.getcwd(), etc.

# Method 2: import specific items
from datetime import datetime, timedelta  # Just datetime and timedelta

# Method 3: import with an alias
import json as j         # Use j.load(), j.dumps() instead of json.load()

# Method 4 (avoid!): import everything
# from os import *       # Imports ALL names — pollutes namespace!

print("  Module imported!")
print(f"  os module location: {os.__file__}")
print(f"  Current time: {datetime.now().strftime('%H:%M:%S')}")

print()


# ============================================================
# SECTION 2: Built-in Modules Overview
# ============================================================

print("=" * 60)
print("SECTION 2: Built-in Modules")
print("=" * 60)

# --- os module — Operating System interface ---
print("--- os module ---")
print(f"  Current directory: {os.getcwd()}")
print(f"  Platform: {os.name}")  # 'nt' for Windows, 'posix' for Linux/Mac

# --- sys module — System-specific parameters ---
import sys
print(f"\n--- sys module ---")
print(f"  Python version: {sys.version.split()[0]}")
print(f"  Platform: {sys.platform}")
print(f"  Path entries: {len(sys.path)}")

# --- math module — Mathematical functions ---
import math
print(f"\n--- math module ---")
print(f"  pi = {math.pi}")
print(f"  sqrt(144) = {math.sqrt(144)}")
print(f"  ceil(4.2) = {math.ceil(4.2)}")
print(f"  floor(4.8) = {math.floor(4.8)}")

# --- random module — Random number generation ---
import random
print(f"\n--- random module ---")
print(f"  random.randint(1, 100) = {random.randint(1, 100)}")
print(f"  random.choice(['Chrome', 'Firefox', 'Edge']) = {random.choice(['Chrome', 'Firefox', 'Edge'])}")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"  random.shuffle([1,2,3,4,5]) = {items}")

# --- datetime module — Date and time ---
print(f"\n--- datetime module ---")
now = datetime.now()
print(f"  Now: {now}")
print(f"  Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Tomorrow: {(now + timedelta(days=1)).strftime('%Y-%m-%d')}")
print(f"  1 hour from now: {(now + timedelta(hours=1)).strftime('%H:%M:%S')}")

# --- string module — String constants ---
import string
print(f"\n--- string module ---")
print(f"  ascii_lowercase: {string.ascii_lowercase}")
print(f"  digits: {string.digits}")
print(f"  punctuation: {string.punctuation}")

print()


# ============================================================
# SECTION 3: The Import System
# ============================================================

print("=" * 60)
print("SECTION 3: How Python Finds Modules")
print("=" * 60)

# When you do 'import xyz', Python searches in this order:
# 1. Built-in modules (sys, os, etc.)
# 2. Current directory
# 3. Directories in sys.path (includes site-packages for pip installs)
# 4. PYTHONPATH environment variable

print("Python module search path:")
for i, path in enumerate(sys.path[:5]):  # First 5 entries
    print(f"  {i+1}. {path}")
if len(sys.path) > 5:
    print(f"  ... and {len(sys.path) - 5} more entries")

# You can add directories to sys.path:
# sys.path.insert(0, "/path/to/my/modules")

print()


# ============================================================
# SECTION 4: Creating Your Own Modules
# ============================================================

print("=" * 60)
print("SECTION 4: Creating Custom Modules")
print("=" * 60)

# Any .py file can be a module!
# If you have a file called 'helpers.py' with a function 'greet()'
# you can do: from helpers import greet

# For this demo, we'll create a module inline (just for illustration)
# In practice, you'd have separate .py files.

# Example module structure for an automation project:
# my_framework/
# ├── config.py          → Configuration settings
# ├── helpers.py         → Utility functions
# ├── pages/
# │   ├── __init__.py
# │   ├── base_page.py   → BasePage class
# │   └── login_page.py  → LoginPage class
# ├── tests/
# │   ├── __init__.py
# │   └── test_login.py  → Test cases
# └── reports/
#     └── reporter.py    → Report generation

print("  Module structure explained above (see comments)")
print("  Key idea: each .py file = one module")
print("  Organize related modules into packages (folders with __init__.py)")

print()


# ============================================================
# SECTION 5: What are Packages?
# ============================================================

print("=" * 60)
print("SECTION 5: Packages (__init__.py)")
print("=" * 60)

# A PACKAGE is a folder containing:
# 1. __init__.py — makes the folder a package (can be empty)
# 2. One or more .py module files

# The __init__.py runs when the package is imported.
# It can:
# - Be empty (just marks folder as package)
# - Import and re-export items for convenience
# - Set package-level variables

# Our custom package structure:
# test_utils/
# ├── __init__.py     → Package initializer
# └── utils.py        → Utility functions
#
# With __init__.py re-exports, users can do:
#   from test_utils import generate_test_id
# Instead of:
#   from test_utils.utils import generate_test_id

print("  Packages = folders with __init__.py")
print("  __init__.py makes Python treat the folder as a package")
print("  See test_utils/ folder for a working example")

print()


# ============================================================
# SECTION 6: Using Custom Package (test_utils)
# ============================================================

print("=" * 60)
print("SECTION 6: Using Custom test_utils Package")
print("=" * 60)

# Add the current script's directory to sys.path so Python finds test_utils
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Now import from our custom package
from test_utils import generate_test_id, log_result, TestStatus
from test_utils import PACKAGE_NAME, VERSION
from test_utils.utils import format_duration

print(f"  Package: {PACKAGE_NAME} v{VERSION}")

# --- Using generate_test_id() ---
print(f"\n--- generate_test_id() ---")
for _ in range(5):
    test_id = generate_test_id()
    print(f"  {test_id}")

# With custom prefix and length
bug_id = generate_test_id(prefix="BUG", length=6)
print(f"  Bug ID: {bug_id}")

# --- Using TestStatus ---
print(f"\n--- TestStatus ---")
print(f"  All statuses: {TestStatus.all_statuses()}")
print(f"  Is 'PASS' valid? {TestStatus.is_valid('PASS')}")
print(f"  Is 'MAYBE' valid? {TestStatus.is_valid('MAYBE')}")

# --- Using log_result() ---
print(f"\n--- log_result() ---")
log_result("TC_001", "Login Test", TestStatus.PASS, duration=2.5)
log_result("TC_002", "Search Test", TestStatus.FAIL, duration=5.1,
           error_msg="Search button not found")
log_result("TC_003", "Cart Test", TestStatus.SKIP,
           error_msg="Cart module not ready")

# --- Using format_duration() ---
print(f"\n--- format_duration() ---")
durations = [0.05, 0.5, 2.3, 45.7, 125.3]
for d in durations:
    print(f"  {d:>7.2f}s → {format_duration(d)}")

print()


# ============================================================
# SECTION 7: Third-Party Packages (pip)
# ============================================================

print("=" * 60)
print("SECTION 7: Third-Party Packages")
print("=" * 60)

# pip is Python's package manager — installs packages from PyPI.
#
# Common commands:
#   pip install selenium          → Install a package
#   pip install -r requirements.txt → Install from file
#   pip list                      → List installed packages
#   pip show selenium             → Show package info
#   pip uninstall selenium        → Remove a package
#   pip freeze > requirements.txt → Save current packages

# Commonly used packages in automation:
# - selenium       → Web browser automation
# - pytest          → Testing framework
# - requests        → HTTP/API testing
# - openpyxl        → Excel file handling
# - allure-pytest   → Beautiful test reports
# - webdriver-manager → Auto-manages browser drivers

print("  Third-party packages install via pip:")
print("    pip install selenium")
print("    pip install pytest")
print("    pip install -r requirements.txt")
print()
print("  requirements.txt lists all project dependencies.")
print("  See the project root for our requirements.txt")

print()


# ============================================================
# SECTION 8: __name__ == "__main__" Guard
# ============================================================

print("=" * 60)
print('SECTION 8: __name__ == "__main__"')
print("=" * 60)

# Every Python module has a special variable __name__
# - When you RUN the file directly:     __name__ == "__main__"
# - When you IMPORT it from elsewhere:  __name__ == "module_name"

# This is used to prevent code from running when the file is imported.

print(f"  Current __name__ = '{__name__}'")

# Example pattern:
# def main():
#     """Main entry point."""
#     run_tests()
#
# if __name__ == "__main__":
#     main()  # Only runs when executed directly, not when imported

# Why this matters:
# If someone does 'import modules_demo', the main() code won't run.
# This makes your module IMPORTABLE without side effects.

print()


# ============================================================
# SECTION 9: Module Best Practices
# ============================================================

print("=" * 60)
print("SECTION 9: Module Best Practices")
print("=" * 60)

print("""
  1. One module = one responsibility
     (Don't put everything in one file)

  2. Use descriptive module names
     Good: test_helpers.py, page_objects.py
     Bad:  stuff.py, misc.py

  3. Group related modules into packages
     pages/, tests/, utils/ etc.

  4. Use __init__.py to simplify imports

  5. Use if __name__ == "__main__": guard

  6. Import order (PEP 8):
     a) Standard library (os, sys, json)
     b) Third-party (selenium, pytest)
     c) Local/custom (from test_utils import ...)

  7. Avoid circular imports
     (Module A imports B, and B imports A → error!)

  8. Use requirements.txt for dependencies
""")


# ============================================================
# PRACTICE TASK 1: Explore Project with os Module
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Project Explorer with os")
print("=" * 60)

def explore_project(root_dir, indent=0):
    """Recursively explore and display project structure."""
    prefix = "  " * indent
    items = sorted(os.listdir(root_dir))
    
    for item in items:
        full_path = os.path.join(root_dir, item)
        
        # Skip __pycache__ and hidden files
        if item.startswith("__pycache__") or item.startswith("."):
            continue
        
        if os.path.isdir(full_path):
            print(f"{prefix}📁 {item}/")
            explore_project(full_path, indent + 1)
        else:
            size = os.path.getsize(full_path)
            ext = os.path.splitext(item)[1]
            icon = {"py": "🐍", ".csv": "📊", ".json": "📋", ".txt": "📝",
                    ".md": "📖", ".ini": "⚙️"}.get(ext, "📄")
            print(f"{prefix}{icon} {item} ({size:,} bytes)")

project_root = os.path.dirname(script_dir)
print(f"\n  Project: {os.path.basename(project_root)}")
print(f"  Path: {project_root}\n")
explore_project(project_root)


# ============================================================
# PRACTICE TASK 2: Test Timing with datetime
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Test Timing with datetime")
print("=" * 60)

import time

def timed_test(test_name, duration_simulate=None):
    """Simulate a test and measure its duration."""
    start = datetime.now()
    
    print(f"\n  ▶ {test_name}")
    print(f"    Started: {start.strftime('%H:%M:%S.%f')[:-3]}")
    
    # Simulate test execution
    if duration_simulate:
        time.sleep(duration_simulate)
    
    end = datetime.now()
    elapsed = (end - start).total_seconds()
    
    print(f"    Ended:   {end.strftime('%H:%M:%S.%f')[:-3]}")
    print(f"    Duration: {format_duration(elapsed)}")
    
    return elapsed

# Run timed tests
print("  Running timed tests...")
total_time = 0

total_time += timed_test("Login Test", 0.1)
total_time += timed_test("Search Test", 0.05)
total_time += timed_test("Cart Test", 0.15)

print(f"\n  Total execution time: {format_duration(total_time)}")


# ============================================================
# PRACTICE TASK 3: Import & Use Custom Package
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Using test_utils Package")
print("=" * 60)

# Already imported above — demonstrate comprehensive usage
print("\nGenerating test suite with custom IDs:")

test_suite = []
test_names = [
    "Verify login with valid credentials",
    "Verify login with invalid password",
    "Verify search returns results",
    "Verify add to cart",
    "Verify checkout process",
]

# Generate unique IDs for each test
for name in test_names:
    tc_id = generate_test_id()
    # Simulate random status
    status = random.choice([TestStatus.PASS, TestStatus.PASS, TestStatus.PASS, TestStatus.FAIL])
    duration = random.uniform(0.5, 5.0)
    error = "Assertion failed" if status == TestStatus.FAIL else None
    
    result = log_result(tc_id, name, status, duration, error)
    test_suite.append(result)

# Summary
passed = sum(1 for t in test_suite if t["status"] == TestStatus.PASS)
failed = sum(1 for t in test_suite if t["status"] == TestStatus.FAIL)
total = len(test_suite)
print(f"\n  Summary: {total} total | {passed} passed | {failed} failed")
print(f"  Pass rate: {passed/total*100:.1f}%")


# ============================================================
# PRACTICE TASK 4: Mini Test Runner
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Mini Test Runner")
print("=" * 60)

class MiniTestRunner:
    """A minimal test runner using our custom modules."""
    
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.results = []
        self.start_time = None
        self.end_time = None
    
    def run_test(self, test_func, test_name):
        """Run a single test function and capture result."""
        tc_id = generate_test_id()
        start = datetime.now()
        
        try:
            test_func()
            elapsed = (datetime.now() - start).total_seconds()
            result = log_result(tc_id, test_name, TestStatus.PASS, elapsed)
        except AssertionError as e:
            elapsed = (datetime.now() - start).total_seconds()
            result = log_result(tc_id, test_name, TestStatus.FAIL, elapsed,
                              error_msg=str(e))
        except Exception as e:
            elapsed = (datetime.now() - start).total_seconds()
            result = log_result(tc_id, test_name, TestStatus.ERROR, elapsed,
                              error_msg=str(e))
        
        self.results.append(result)
    
    def run_suite(self, tests):
        """Run a list of (test_func, test_name) tuples."""
        self.start_time = datetime.now()
        print(f"\n  ╔{'═'*50}╗")
        print(f"  ║ {'Running: ' + self.suite_name:^48s} ║")
        print(f"  ╚{'═'*50}╝\n")
        
        for test_func, test_name in tests:
            self.run_test(test_func, test_name)
        
        self.end_time = datetime.now()
        self._print_summary()
    
    def _print_summary(self):
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == TestStatus.PASS)
        failed = sum(1 for r in self.results if r["status"] == TestStatus.FAIL)
        errors = sum(1 for r in self.results if r["status"] == TestStatus.ERROR)
        elapsed = (self.end_time - self.start_time).total_seconds()
        
        print(f"\n  {'─'*50}")
        print(f"  Suite: {self.suite_name}")
        print(f"  Time:  {format_duration(elapsed)}")
        print(f"  Total: {total} | Pass: {passed} | Fail: {failed} | Error: {errors}")
        rate = (passed / total * 100) if total > 0 else 0
        bar_len = 30
        filled = int(bar_len * passed / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  Rate:  [{bar}] {rate:.1f}%")
        print(f"  {'─'*50}")

# Define test functions
def test_login_valid():
    """Test: Login with valid credentials."""
    assert 2 + 2 == 4  # Simulates pass
    time.sleep(0.05)

def test_login_invalid():
    """Test: Login with invalid credentials."""
    assert "error" in "error message displayed"  # Simulates pass
    time.sleep(0.03)

def test_search():
    """Test: Search functionality."""
    results = [1, 2, 3]
    assert len(results) > 0  # Pass
    time.sleep(0.04)

def test_cart_failure():
    """Test: Add to cart (will fail)."""
    cart_items = []
    assert len(cart_items) > 0, "Cart is empty after adding item!"  # FAIL

def test_checkout_error():
    """Test: Checkout (will raise error)."""
    raise ConnectionError("Payment gateway timeout!")

# Run the test suite
runner = MiniTestRunner("Boodmo Smoke Tests")
runner.run_suite([
    (test_login_valid, "Login with valid credentials"),
    (test_login_invalid, "Login with invalid credentials"),
    (test_search, "Search returns results"),
    (test_cart_failure, "Add to cart"),
    (test_checkout_error, "Checkout process"),
])

print("\n--- Topic 13 Complete! ---")
