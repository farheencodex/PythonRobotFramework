"""
Topic 11 — Exception Handling | Python for Automation Course
=============================================================
Exception handling is ESSENTIAL for automation — tests fail, files go missing,
elements aren't found, APIs return errors. Proper exception handling makes
your scripts robust and prevents random crashes.

Concepts Covered:
    1. What are Exceptions? (common exception types)
    2. try / except — catching exceptions
    3. try / except / else — success path
    4. try / except / finally — always-execute block
    5. Catching multiple exception types
    6. Raising exceptions with raise
    7. Custom exception classes
    8. Exception chaining (from keyword)
    9. Best practices for exception handling

Practice Tasks:
    1. Safe division calculator with input validation
    2. File reader with graceful error handling
    3. Custom exceptions: InvalidBrowserError, ElementNotFoundError
    4. Retry mechanism using exceptions

How to Run:
    python exception_handling.py
"""

import os
import time
import random


# ============================================================
# SECTION 1: What are Exceptions?
# ============================================================

print("=" * 60)
print("SECTION 1: What are Exceptions?")
print("=" * 60)

# An EXCEPTION is an error that occurs DURING program execution.
# If not handled, it CRASHES the program.

# Common exception types in Python:
# ─────────────────────────────────────────────────────────────
# TypeError        → Wrong data type operation
# ValueError       → Right type, wrong value
# KeyError         → Key not found in dictionary
# IndexError       → List index out of range
# FileNotFoundError→ File doesn't exist
# ZeroDivisionError→ Division by zero
# AttributeError   → Object doesn't have the attribute
# ImportError      → Module not found
# NameError        → Variable not defined
# RuntimeError     → General runtime error

# In automation:
# NoSuchElementException → Selenium can't find element
# TimeoutException       → Wait timed out
# StaleElementException  → Element is no longer in DOM

# Let's see some exceptions (commented out so they don't crash):
# print(1 / 0)            # ZeroDivisionError
# int("hello")            # ValueError
# {"a": 1}["b"]           # KeyError
# [1, 2, 3][10]           # IndexError
# open("no_such_file.txt")  # FileNotFoundError

print("Exceptions are errors that occur during runtime.")
print("Without handling, they crash your program!\n")


# ============================================================
# SECTION 2: try / except — Catching Exceptions
# ============================================================

print("=" * 60)
print("SECTION 2: try / except")
print("=" * 60)

# The try block lets you TEST code for errors.
# The except block handles the error if one occurs.

# --- Basic try/except ---
print("--- Basic try/except ---")
try:
    result = 10 / 0  # This will cause ZeroDivisionError
except ZeroDivisionError:
    print("  Error: Cannot divide by zero!")

# Without try/except, the above would crash the entire script.
# With try/except, we handle it gracefully and continue.

# --- Catching the error message ---
print("\n--- Capturing error details ---")
try:
    number = int("not_a_number")  # ValueError
except ValueError as e:
    # 'e' contains the error message
    print(f"  Error caught: {e}")
    print(f"  Error type: {type(e).__name__}")

# --- Catching generic Exception ---
print("\n--- Generic Exception handler ---")
try:
    data = {"name": "Tayyab"}
    value = data["email"]  # KeyError — key doesn't exist
except Exception as e:
    # Exception catches ANY exception type
    print(f"  Caught: {type(e).__name__}: {e}")

# NOTE: Catching generic Exception is useful as a safety net,
# but prefer catching SPECIFIC exceptions when possible.

print()


# ============================================================
# SECTION 3: try / except / else
# ============================================================

print("=" * 60)
print("SECTION 3: try / except / else")
print("=" * 60)

# The 'else' block runs ONLY if no exception was raised in try.
# Use it for code that should run only when try succeeds.

print("--- else block (success path) ---")

values = ["42", "hello", "100"]

for val in values:
    try:
        number = int(val)
    except ValueError:
        print(f"  '{val}' → Error: Not a valid integer!")
    else:
        # Runs only when try succeeds (no exception)
        doubled = number * 2
        print(f"  '{val}' → Converted to {number}, doubled = {doubled}")

# Why use else instead of putting code at end of try?
# Because code at the end of try could ALSO raise exceptions
# and you'd accidentally catch those too.

print()


# ============================================================
# SECTION 4: try / except / finally
# ============================================================

print("=" * 60)
print("SECTION 4: try / except / finally")
print("=" * 60)

# The 'finally' block ALWAYS runs, whether or not an exception occurred.
# Use it for CLEANUP operations: closing files, closing browsers, etc.

print("--- finally block (always runs) ---")

def simulate_browser_test(url, should_fail=False):
    """Simulate opening a browser, running a test, and closing the browser."""
    print(f"\n  Opening browser...")
    try:
        print(f"  Navigating to: {url}")
        if should_fail:
            raise ConnectionError("Failed to connect to server!")
        print(f"  Test passed!")
    except ConnectionError as e:
        print(f"  Test failed: {e}")
    finally:
        # ALWAYS runs — even if exception occurred!
        print(f"  Closing browser... (finally block)")
        print(f"  Browser closed.")

# Test 1: Success
print("Test 1 (success):")
simulate_browser_test("https://boodmo.com")

# Test 2: Failure — browser still gets closed!
print("\nTest 2 (failure):")
simulate_browser_test("https://boodmo.com/broken", should_fail=True)

# --- Full try/except/else/finally ---
print("\n\n--- Complete structure ---")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("  Division by zero!")
else:
    print(f"  Success! Result = {result}")
finally:
    print(f"  Cleanup complete (always runs).")

# Order: try → except (if error) OR else (if no error) → finally (always)

print()


# ============================================================
# SECTION 5: Catching Multiple Exception Types
# ============================================================

print("=" * 60)
print("SECTION 5: Multiple Exception Types")
print("=" * 60)

# --- Method 1: Separate except blocks ---
print("--- Method 1: Separate except blocks ---")

def process_data(value, key):
    """Process data with multiple potential errors."""
    try:
        data = {"name": "Tayyab", "age": 28}
        result = int(data[key])     # Could raise KeyError or ValueError
        answer = 100 / result       # Could raise ZeroDivisionError
        return answer
    except KeyError as e:
        print(f"  KeyError: Key {e} not found in data!")
    except ValueError as e:
        print(f"  ValueError: {e}")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: Cannot divide by zero!")
    return None

process_data(None, "email")  # KeyError
process_data(None, "name")   # ValueError (can't convert "Tayyab" to int)

# --- Method 2: Tuple of exception types ---
print("\n--- Method 2: Tuple of exception types ---")

def safe_convert(value):
    """Convert value to float, handling multiple error types."""
    try:
        return float(value)
    except (ValueError, TypeError) as e:
        # Catches BOTH ValueError and TypeError
        print(f"  Cannot convert {value!r}: {type(e).__name__}: {e}")
        return None

safe_convert("3.14")     # Success
safe_convert("hello")    # ValueError
safe_convert(None)       # TypeError

print()


# ============================================================
# SECTION 6: Raising Exceptions with raise
# ============================================================

print("=" * 60)
print("SECTION 6: Raising Exceptions")
print("=" * 60)

# Use 'raise' to intentionally throw an exception.
# Use this to enforce input validation and business rules.

def set_browser(browser_name):
    """Set browser — raises ValueError for unsupported browsers."""
    supported = ["Chrome", "Firefox", "Edge"]
    if browser_name not in supported:
        raise ValueError(f"Browser '{browser_name}' is not supported! "
                        f"Choose from: {supported}")
    print(f"  Browser set to: {browser_name}")
    return browser_name

# Valid browser
set_browser("Chrome")

# Invalid browser — caught with try/except
try:
    set_browser("Opera")
except ValueError as e:
    print(f"  Caught: {e}")

# --- Re-raising exceptions ---
print("\n--- Re-raising exceptions ---")

def validate_url(url):
    """Validate URL — re-raise with additional context."""
    try:
        if not url.startswith(("http://", "https://")):
            raise ValueError(f"Invalid URL: {url}")
    except ValueError:
        print(f"  Logging error before re-raising...")
        raise  # Re-raise the same exception

try:
    validate_url("boodmo.com")  # Missing https://
except ValueError as e:
    print(f"  Final catch: {e}")

print()


# ============================================================
# SECTION 7: Custom Exception Classes
# ============================================================

print("=" * 60)
print("SECTION 7: Custom Exceptions")
print("=" * 60)

# Custom exceptions make your code MORE READABLE and SPECIFIC.
# Always inherit from Exception (or a subclass of Exception).

class AutomationError(Exception):
    """Base exception for all automation errors."""
    pass

class BrowserNotSupportedError(AutomationError):
    """Raised when an unsupported browser is specified."""
    def __init__(self, browser, supported=None):
        self.browser = browser
        self.supported = supported or ["Chrome", "Firefox", "Edge"]
        message = (f"Browser '{browser}' is not supported. "
                  f"Supported: {', '.join(self.supported)}")
        super().__init__(message)

class ElementNotFoundError(AutomationError):
    """Raised when a web element is not found."""
    def __init__(self, locator, timeout=10):
        self.locator = locator
        self.timeout = timeout
        message = f"Element '{locator}' not found after {timeout}s wait."
        super().__init__(message)

class LoginFailedError(AutomationError):
    """Raised when login fails."""
    def __init__(self, username, reason="Invalid credentials"):
        self.username = username
        self.reason = reason
        message = f"Login failed for '{username}': {reason}"
        super().__init__(message)

# Using custom exceptions
print("--- Custom Exception Demo ---")

def launch_browser(name):
    supported = ["Chrome", "Firefox", "Edge"]
    if name not in supported:
        raise BrowserNotSupportedError(name, supported)
    print(f"  Launched: {name}")

def find_element(locator, timeout=10):
    # Simulate element not found
    raise ElementNotFoundError(locator, timeout)

def perform_login(username, password):
    if password != "correct_password":
        raise LoginFailedError(username, "Password incorrect")
    print(f"  Login successful for {username}")

# Test each custom exception
try:
    launch_browser("Safari")
except BrowserNotSupportedError as e:
    print(f"  Caught: {e}")
    print(f"  Browser: {e.browser}")
    print(f"  Supported: {e.supported}")

print()
try:
    find_element("//input[@id='search']")
except ElementNotFoundError as e:
    print(f"  Caught: {e}")
    print(f"  Locator: {e.locator}")
    print(f"  Timeout: {e.timeout}s")

print()
try:
    perform_login("tayyab", "wrong_pass")
except LoginFailedError as e:
    print(f"  Caught: {e}")

# Exception hierarchy — catching parent catches all children
print("\n--- Catching the parent class ---")
try:
    launch_browser("Opera")
except AutomationError as e:
    # Catches BrowserNotSupportedError (and any AutomationError subclass)
    print(f"  Caught AutomationError: {type(e).__name__}: {e}")

print()


# ============================================================
# SECTION 8: Exception Chaining (from keyword)
# ============================================================

print("=" * 60)
print("SECTION 8: Exception Chaining")
print("=" * 60)

# Use 'from' to chain exceptions — shows the original cause.

def read_config(filename):
    """Read config file — chains FileNotFoundError into a custom error."""
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as original:
        raise AutomationError(
            f"Config file '{filename}' is missing. "
            f"Please create it before running tests."
        ) from original

try:
    read_config("nonexistent_config.ini")
except AutomationError as e:
    print(f"  AutomationError: {e}")
    print(f"  Original cause: {type(e.__cause__).__name__}: {e.__cause__}")

print()


# ============================================================
# SECTION 9: Best Practices
# ============================================================

print("=" * 60)
print("SECTION 9: Best Practices")
print("=" * 60)

# 1. Catch SPECIFIC exceptions, not generic Exception
#    Bad:  except Exception:
#    Good: except ValueError:

# 2. Don't use bare except:
#    Bad:  except:          (catches EVERYTHING including KeyboardInterrupt)
#    Good: except Exception: (at minimum, be this specific)

# 3. Use finally for cleanup
#    Always close files, browsers, database connections in finally

# 4. Don't silently swallow exceptions
#    Bad:  except ValueError: pass
#    Good: except ValueError as e: logger.error(f"Error: {e}")

# 5. Use custom exceptions for domain-specific errors
#    Makes code more readable and debugging easier

# 6. Keep try blocks small
#    Only wrap the code that might raise the specific exception

# 7. Use else for success code
#    Separates the "try this risky thing" from "do this if it worked"

print("Best Practices Summary:")
print("  1. Catch SPECIFIC exceptions")
print("  2. Never use bare except:")
print("  3. Use finally for cleanup")
print("  4. Don't silently swallow exceptions")
print("  5. Use custom exceptions for domain errors")
print("  6. Keep try blocks small")
print("  7. Use else for success path code")

print()


# ============================================================
# PRACTICE TASK 1: Safe Division Calculator
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Safe Division Calculator")
print("=" * 60)

def safe_divide(a, b):
    """
    Safely divide a by b with comprehensive error handling.
    
    Args:
        a: Numerator (should be numeric)
        b: Denominator (should be numeric, non-zero)
    
    Returns:
        float: Result of division, or None if error occurred
    """
    try:
        # Convert to float (handles string inputs)
        num_a = float(a)
        num_b = float(b)
        result = num_a / num_b
    except ValueError as e:
        print(f"  ✗ ValueError: Cannot convert to number — {e}")
        return None
    except ZeroDivisionError:
        print(f"  ✗ ZeroDivisionError: Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        print(f"  ✗ TypeError: Invalid types — {e}")
        return None
    else:
        # Only runs if no exception occurred
        print(f"  ✓ {num_a} / {num_b} = {result:.4f}")
        return result
    finally:
        print(f"  [Calculation attempt completed]")

# Test cases
print("Test 1: Normal division")
safe_divide(10, 3)

print("\nTest 2: Division by zero")
safe_divide(10, 0)

print("\nTest 3: Invalid string input")
safe_divide("ten", 5)

print("\nTest 4: None input")
safe_divide(None, 5)

print("\nTest 5: Negative numbers")
safe_divide(-15, 4)


# ============================================================
# PRACTICE TASK 2: File Reader with Error Handling
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: File Reader with Error Handling")
print("=" * 60)

def read_file_safely(filepath):
    """
    Read a file with comprehensive error handling.
    Handles: FileNotFoundError, PermissionError, UnicodeDecodeError
    """
    file_handle = None
    try:
        print(f"  Attempting to open: {filepath}")
        file_handle = open(filepath, "r", encoding="utf-8")
        content = file_handle.read()
    except FileNotFoundError:
        print(f"  ✗ File not found: {filepath}")
        print(f"    → Check if the file path is correct.")
        return None
    except PermissionError:
        print(f"  ✗ Permission denied: {filepath}")
        print(f"    → Check file permissions.")
        return None
    except UnicodeDecodeError:
        print(f"  ✗ Cannot decode file: {filepath}")
        print(f"    → File may be binary or have different encoding.")
        return None
    else:
        line_count = len(content.splitlines())
        print(f"  ✓ File read successfully! ({line_count} lines, {len(content)} chars)")
        return content
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"  [File handle closed]")

# Test with a non-existent file
print("\nTest 1: Non-existent file")
read_file_safely("nonexistent_file.txt")

# Test with the current file (this script itself)
print("\nTest 2: Reading this script")
script_path = os.path.abspath(__file__)
content = read_file_safely(script_path)
if content:
    # Show first 3 lines
    lines = content.splitlines()[:3]
    for line in lines:
        print(f"    | {line}")
    print(f"    | ... ({len(content.splitlines()) - 3} more lines)")


# ============================================================
# PRACTICE TASK 3: Custom Exceptions for Automation
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Custom Exceptions — Automation Framework")
print("=" * 60)

# Define the exception hierarchy
class FrameworkError(Exception):
    """Base exception for the automation framework."""
    pass

class InvalidBrowserError(FrameworkError):
    """Raised when an invalid browser is specified."""
    def __init__(self, browser):
        self.browser = browser
        super().__init__(f"Invalid browser: '{browser}'. "
                        f"Supported: Chrome, Firefox, Edge")

class ElementNotFoundError(FrameworkError):
    """Raised when a page element cannot be located."""
    def __init__(self, locator, page="Unknown"):
        self.locator = locator
        self.page = page
        super().__init__(f"Element '{locator}' not found on {page} page.")

class TestSetupError(FrameworkError):
    """Raised when test setup fails."""
    def __init__(self, test_name, reason):
        self.test_name = test_name
        self.reason = reason
        super().__init__(f"Setup failed for '{test_name}': {reason}")

# Simulate a test framework using these exceptions
class SimpleTestRunner:
    """A simple test runner that demonstrates custom exceptions."""
    
    SUPPORTED_BROWSERS = ["Chrome", "Firefox", "Edge"]
    
    def __init__(self, browser):
        if browser not in self.SUPPORTED_BROWSERS:
            raise InvalidBrowserError(browser)
        self.browser = browser
        self.results = []
    
    def find_element(self, locator, page="Main"):
        """Simulate finding an element."""
        # Simulate: element found only if locator contains 'valid'
        if "valid" not in locator.lower():
            raise ElementNotFoundError(locator, page)
        return f"Found: {locator}"
    
    def run_test(self, test_name, locators):
        """Run a simulated test."""
        print(f"\n  Running: {test_name}")
        try:
            for loc in locators:
                result = self.find_element(loc, "Login")
                print(f"    ✓ {result}")
            self.results.append((test_name, "PASS"))
            print(f"    → Test PASSED")
        except ElementNotFoundError as e:
            self.results.append((test_name, "FAIL"))
            print(f"    ✗ {e}")
            print(f"    → Test FAILED")

# Demo
print("--- Setting up test runner ---")

# Test with invalid browser
try:
    runner = SimpleTestRunner("Safari")
except InvalidBrowserError as e:
    print(f"  Caught: {e}")
    print(f"  Bad browser: {e.browser}")

# Test with valid browser
runner = SimpleTestRunner("Chrome")
print(f"  Runner created with: {runner.browser}")

# Run tests with various locators
runner.run_test("Valid Elements Test", ["valid_username", "valid_password"])
runner.run_test("Invalid Element Test", ["valid_username", "submit_btn"])
runner.run_test("All Invalid Test", ["login_button"])

# Summary
print("\n  --- Test Results ---")
for name, status in runner.results:
    icon = "✓" if status == "PASS" else "✗"
    print(f"    {icon} {name}: {status}")


# ============================================================
# PRACTICE TASK 4: Retry Mechanism with Exceptions
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Retry Mechanism")
print("=" * 60)

def retry(func, max_attempts=3, delay=0.5):
    """
    Retry a function up to max_attempts times.
    Waits 'delay' seconds between retries.
    
    Args:
        func: Callable to retry
        max_attempts: Maximum number of attempts
        delay: Seconds to wait between retries
    
    Returns:
        The result of the function if successful
    
    Raises:
        The last exception if all attempts fail
    """
    last_exception = None
    
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"  Attempt {attempt}/{max_attempts}...")
            result = func()
            print(f"  ✓ Success on attempt {attempt}!")
            return result
        except Exception as e:
            last_exception = e
            print(f"  ✗ Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                print(f"    Waiting {delay}s before retry...")
                time.sleep(delay)
    
    # All attempts failed
    print(f"  ✗ All {max_attempts} attempts failed!")
    raise last_exception

# Simulate a flaky operation (fails randomly)
attempt_counter = {"count": 0}

def flaky_api_call():
    """Simulates an API call that succeeds on the 3rd attempt."""
    attempt_counter["count"] += 1
    if attempt_counter["count"] < 3:
        raise ConnectionError("Server timeout — try again.")
    return {"status": "ok", "data": "Test results"}

# Use the retry mechanism
print("--- Retry with flaky API ---")
try:
    result = retry(flaky_api_call, max_attempts=5, delay=0.3)
    print(f"  Result: {result}")
except ConnectionError as e:
    print(f"  Final failure: {e}")

# Simulate an operation that always fails
print("\n--- Retry with always-failing operation ---")

def always_fails():
    raise TimeoutError("Element not clickable!")

try:
    retry(always_fails, max_attempts=3, delay=0.2)
except TimeoutError as e:
    print(f"  Gave up after retries: {e}")

print("\n--- Topic 11 Complete! ---")
