"""
Topic 15 — Python for Automation | Python for Automation Course
=================================================================
This is the CAPSTONE topic — bringing everything together for real-world
test automation. Covers pytest, Selenium concepts, Page Object Model (POM),
logging, configparser, and framework design patterns.

Concepts Covered:
    1. pytest — Test framework fundamentals
    2. pytest fixtures — Setup/Teardown
    3. pytest markers — Smoke, Regression, Skip, xfail
    4. pytest parametrize — Data-driven testing
    5. Selenium WebDriver — Overview & concepts (simulated)
    6. Page Object Model (POM) — Design pattern
    7. Logging module — Proper logging for automation
    8. configparser — Reading .ini configuration files
    9. Putting it all together — Mini framework demo

Supporting Files (in this folder):
    config.ini        → Configuration file for the framework
    test_sample.py    → Runnable pytest test file
    pages/
        __init__.py   → Pages package init
        base_page.py  → BasePage class with mock WebDriver methods

Practice Tasks:
    1. Read config.ini and display all settings
    2. Use logging module for test execution logging
    3. Build a LoginPage using POM (extends BasePage)
    4. Mini test framework: config + POM + logging + runner

How to Run:
    python automation_intro.py        → Run this learning file
    pytest test_sample.py -v          → Run pytest tests
    pytest test_sample.py -v -m smoke → Run only smoke tests

Prerequisites:
    pip install pytest pytest-html
"""

import os
import sys
import logging
import configparser
from datetime import datetime
from abc import ABC, abstractmethod


# ============================================================
# SECTION 1: pytest — Test Framework Fundamentals
# ============================================================

print("=" * 60)
print("SECTION 1: pytest Fundamentals")
print("=" * 60)

# pytest is the most popular Python testing framework.
# It's used extensively in automation for writing and running tests.

# Key features:
# - Simple assert statements (no special methods needed!)
# - Automatic test discovery (files starting with test_)
# - Fixtures for setup/teardown
# - Markers for categorizing tests
# - Parametrize for data-driven testing
# - Rich plugin ecosystem (pytest-html, allure, etc.)

# --- Test Discovery Rules ---
# pytest automatically finds tests by:
# 1. Files named test_*.py or *_test.py
# 2. Functions starting with test_
# 3. Classes starting with Test (no __init__)
# 4. Methods starting with test_ inside Test classes

print("""
  pytest Test Discovery Rules:
  ─────────────────────────────
  Files:     test_*.py or *_test.py
  Functions: test_*()
  Classes:   Test* (no __init__ method)
  Methods:   test_*() inside Test classes

  Common Commands:
  ─────────────────
  pytest                     → Run all tests
  pytest -v                  → Verbose output
  pytest -v -m smoke         → Run only @pytest.mark.smoke tests
  pytest --tb=short          → Short traceback on failures
  pytest -k "login"          → Run tests with 'login' in name
  pytest --html=report.html  → Generate HTML report
  pytest -x                  → Stop on first failure
  pytest -n auto             → Run in parallel (needs pytest-xdist)
""")


# ============================================================
# SECTION 2: pytest Fixtures (Explained)
# ============================================================

print("=" * 60)
print("SECTION 2: pytest Fixtures")
print("=" * 60)

# Fixtures provide SETUP and TEARDOWN for tests.
# They're declared with @pytest.fixture decorator.
# Tests that need them simply add the fixture name as a parameter.

print("""
  Fixture Pattern:
  ─────────────────
  @pytest.fixture
  def browser():
      # SETUP
      driver = webdriver.Chrome()
      driver.maximize_window()
      yield driver      # ← Passes driver to the test
      # TEARDOWN
      driver.quit()     # ← Runs after test, even if test fails

  def test_login(browser):   # ← Fixture injected automatically!
      browser.get("https://boodmo.com")
      assert "Boodmo" in browser.title

  Fixture Scopes:
  ─────────────────
  @pytest.fixture(scope="function")  → New for each test (default)
  @pytest.fixture(scope="class")     → New for each test class
  @pytest.fixture(scope="module")    → New for each .py file
  @pytest.fixture(scope="session")   → One for entire test run
""")

# See test_sample.py for working fixture examples!


# ============================================================
# SECTION 3: pytest Markers
# ============================================================

print("=" * 60)
print("SECTION 3: pytest Markers")
print("=" * 60)

print("""
  Markers categorize tests for selective execution:
  ───────────────────────────────────────────────────
  @pytest.mark.smoke       → Quick sanity tests
  @pytest.mark.regression  → Full regression tests
  @pytest.mark.skip        → Skip this test
  @pytest.mark.xfail       → Expected to fail (known bug)
  @pytest.mark.parametrize → Data-driven test

  Running marked tests:
  ───────────────────────
  pytest -m smoke           → Only smoke tests
  pytest -m "not regression"→ Skip regression tests
  pytest -m "smoke or sanity" → Either marker

  Custom markers should be registered in pytest.ini:
  ─────────────────────────────────────────────────────
  [pytest]
  markers =
      smoke: Quick sanity tests
      regression: Full regression tests
""")


# ============================================================
# SECTION 4: Selenium WebDriver — Overview
# ============================================================

print("=" * 60)
print("SECTION 4: Selenium WebDriver Overview")
print("=" * 60)

# Selenium automates web browsers for testing.
# Key components:
# - WebDriver — controls the browser
# - Locators — find elements on the page
# - Actions — click, type, wait, etc.

print("""
  Selenium Setup:
  ─────────────────
  pip install selenium webdriver-manager

  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  Basic Usage:
  ─────────────
  driver = webdriver.Chrome()
  driver.get("https://boodmo.com")
  
  # Find elements
  element = driver.find_element(By.ID, "search-input")
  element = driver.find_element(By.XPATH, "//button[@type='submit']")
  element = driver.find_element(By.CSS_SELECTOR, ".login-btn")
  
  # Interact
  element.click()
  element.send_keys("brake pad")
  text = element.text
  
  # Wait for element
  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.presence_of_element_located((By.ID, "results")))
  
  driver.quit()

  Locator Strategies:
  ─────────────────────
  By.ID            → Fastest, most reliable
  By.NAME          → By name attribute
  By.CLASS_NAME    → By CSS class
  By.TAG_NAME      → By HTML tag
  By.CSS_SELECTOR  → Flexible CSS selector
  By.XPATH         → Most flexible, can traverse DOM
  By.LINK_TEXT     → Exact link text
  By.PARTIAL_LINK_TEXT → Partial link text
""")


# ============================================================
# SECTION 5: Page Object Model (POM)
# ============================================================

print("=" * 60)
print("SECTION 5: Page Object Model (POM)")
print("=" * 60)

# POM is a design pattern that:
# 1. Creates a CLASS for each web page
# 2. Stores element locators as class variables
# 3. Provides methods for page interactions
# 4. Tests use page objects, NOT raw Selenium calls

# Benefits:
# - Reduces code duplication
# - Easy maintenance (change locator in one place)
# - Readable tests (english-like method names)
# - Reusable page objects across tests

print("""
  POM Structure:
  ────────────────
  pages/
  ├── __init__.py
  ├── base_page.py        → Common methods (click, type, wait)
  ├── login_page.py       → Login page locators + methods
  ├── search_page.py      → Search page locators + methods
  └── cart_page.py         → Cart page locators + methods

  tests/
  ├── conftest.py          → Shared fixtures
  ├── test_login.py        → Login tests (use LoginPage)
  ├── test_search.py       → Search tests (use SearchPage)
  └── test_cart.py         → Cart tests (use CartPage)

  Example:
  ──────────
  class LoginPage(BasePage):
      USERNAME_INPUT = (By.ID, "username")
      PASSWORD_INPUT = (By.ID, "password")
      LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")

      def login(self, username, password):
          self.type_text(self.USERNAME_INPUT, username)
          self.type_text(self.PASSWORD_INPUT, password)
          self.click(self.LOGIN_BUTTON)

  # Test:
  def test_login(browser):
      login_page = LoginPage(browser)
      login_page.open()
      login_page.login("user@test.com", "pass123")
      assert login_page.is_logged_in()
""")


# ============================================================
# SECTION 6: Logging Module
# ============================================================

print("=" * 60)
print("SECTION 6: Logging Module")
print("=" * 60)

# Python's logging module is much better than print() for automation:
# - Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# - Write to files AND console simultaneously
# - Timestamps, formatting, rotation
# - Standard across the industry

# --- Configure logging ---
# Create a logger for this module
logger = logging.getLogger("automation")
logger.setLevel(logging.DEBUG)

# Console handler — shows INFO and above
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("  %(asctime)s | %(levelname)-8s | %(message)s",
                                   datefmt="%H:%M:%S")
console_handler.setFormatter(console_format)

# File handler — logs everything (DEBUG and above)
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "test_execution.log")
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
file_handler.setFormatter(file_format)

# Add handlers to logger (avoid duplicate handlers)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# --- Log levels ---
print("\n--- Logging Levels ---")
logger.debug("This is a DEBUG message (detailed, for developers)")     # Not shown in console
logger.info("This is an INFO message (general information)")
logger.warning("This is a WARNING message (something might be wrong)")
logger.error("This is an ERROR message (something went wrong!)")
logger.critical("This is a CRITICAL message (system is failing!)")

# --- Logging in automation ---
print("\n--- Simulated Test Execution Log ---")
logger.info("=" * 40)
logger.info("Test Suite: Boodmo Smoke Tests")
logger.info("Environment: Staging")
logger.info("Browser: Chrome v121.0")
logger.info("=" * 40)
logger.info("Starting test: Login with valid credentials")
logger.debug("Navigating to https://staging.boodmo.com/login")
logger.debug("Finding element: #username")
logger.info("Entering username: testuser@boodmo.com")
logger.debug("Finding element: #password")
logger.info("Entering password: ********")
logger.debug("Finding element: .login-button")
logger.info("Clicking login button")
logger.info("Verifying dashboard is displayed")
logger.info("Test PASSED: Login with valid credentials")
logger.info("-" * 40)

print(f"\n  Log file created: {log_file}")

print()


# ============================================================
# SECTION 7: configparser — Reading .ini Files
# ============================================================

print("=" * 60)
print("SECTION 7: configparser — .ini Files")
print("=" * 60)

# configparser reads .ini configuration files.
# Great for storing environment settings, browser configs, etc.

config_path = os.path.join(script_dir, "config.ini")

# --- Reading config.ini ---
config = configparser.ConfigParser()
config.read(config_path)

print("--- Reading config.ini ---")
print(f"\n  Sections: {config.sections()}")

# Access DEFAULT section values
print(f"\n  [DEFAULT]")
print(f"    Browser:       {config['DEFAULT']['browser']}")
print(f"    Headless:      {config['DEFAULT']['headless']}")
print(f"    Implicit Wait: {config['DEFAULT']['implicit_wait']}s")

# Access environment-specific settings
print(f"\n  [STAGING]")
print(f"    Base URL:  {config['STAGING']['base_url']}")
print(f"    Username:  {config['STAGING']['username']}")

print(f"\n  [PRODUCTION]")
print(f"    Base URL:  {config['PRODUCTION']['base_url']}")

# Access with fallback
timeout = config.getint("DEFAULT", "explicit_wait", fallback=30)
headless = config.getboolean("DEFAULT", "headless", fallback=False)
print(f"\n  Explicit Wait (int): {timeout}")
print(f"  Headless (bool): {headless}")

# --- Using config in automation ---
print("\n--- Config Usage Pattern ---")

class FrameworkConfig:
    """Reads config.ini and provides typed access to settings."""
    
    def __init__(self, config_file):
        self._config = configparser.ConfigParser()
        self._config.read(config_file)
        self.environment = "STAGING"  # Default environment
    
    @property
    def browser(self):
        return self._config.get("DEFAULT", "browser")
    
    @property
    def headless(self):
        return self._config.getboolean("DEFAULT", "headless")
    
    @property
    def base_url(self):
        return self._config.get(self.environment, "base_url")
    
    @property
    def username(self):
        return self._config.get(self.environment, "username")
    
    @property
    def timeout(self):
        return self._config.getint("DEFAULT", "explicit_wait")

fw_config = FrameworkConfig(config_path)
print(f"  Browser:  {fw_config.browser}")
print(f"  Headless: {fw_config.headless}")
print(f"  Base URL: {fw_config.base_url}")
print(f"  Username: {fw_config.username}")
print(f"  Timeout:  {fw_config.timeout}s")

print()


# ============================================================
# SECTION 8: Putting It All Together
# ============================================================

print("=" * 60)
print("SECTION 8: Mini Automation Framework")
print("=" * 60)

# This section demonstrates how all concepts work together
# in a real automation framework.

# Add pages directory to path
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from pages.base_page import BasePage


# --- LoginPage (POM) ---
class LoginPage(BasePage):
    """Login Page Object — extends BasePage."""
    
    # Locators (in real Selenium, these would be tuples)
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = ".login-btn"
    ERROR_MESSAGE = ".error-msg"
    DASHBOARD_HEADER = "#dashboard-header"
    
    def __init__(self, driver_name="Chrome"):
        super().__init__(driver_name)
        self.login_url = fw_config.base_url + "/login"
        logger.info("LoginPage initialized")
    
    def open(self):
        """Navigate to login page."""
        self.open_url(self.login_url)
        return self
    
    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, username, password):
        """Complete login flow."""
        logger.info(f"Logging in as: {username}")
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        logger.info("Login completed")
        return self
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_dashboard_displayed(self):
        return self.is_element_displayed(self.DASHBOARD_HEADER)


# --- SearchPage (POM) ---
class SearchPage(BasePage):
    """Search Page Object — extends BasePage."""
    
    SEARCH_INPUT = "#search-input"
    SEARCH_BUTTON = ".search-btn"
    RESULTS_CONTAINER = "#search-results"
    RESULT_ITEMS = ".result-item"
    
    def __init__(self, driver_name="Chrome"):
        super().__init__(driver_name)
        self.search_url = fw_config.base_url + "/search"
        logger.info("SearchPage initialized")
    
    def open(self):
        self.open_url(self.search_url)
        return self
    
    def search(self, query):
        """Perform a search."""
        logger.info(f"Searching for: {query}")
        self.open()
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self
    
    def has_results(self):
        return self.is_element_displayed(self.RESULTS_CONTAINER)


# --- Mini Test Runner ---
class TestResult:
    """Represents a single test result."""
    def __init__(self, name, status, duration=0, error=None):
        self.name = name
        self.status = status
        self.duration = duration
        self.error = error

class MiniFramework:
    """Mini automation framework — ties everything together."""
    
    def __init__(self, config_file):
        self.config = FrameworkConfig(config_file)
        self.results = []
        self.start_time = None
        logger.info("Framework initialized")
        logger.info(f"Browser: {self.config.browser}")
        logger.info(f"Environment: {self.config.environment}")
        logger.info(f"Base URL: {self.config.base_url}")
    
    def run_test(self, test_name, test_func):
        """Run a single test and capture the result."""
        logger.info(f"{'─'*40}")
        logger.info(f"RUNNING: {test_name}")
        start = datetime.now()
        
        try:
            test_func()
            elapsed = (datetime.now() - start).total_seconds()
            result = TestResult(test_name, "PASS", elapsed)
            logger.info(f"PASSED: {test_name} ({elapsed:.2f}s)")
        except AssertionError as e:
            elapsed = (datetime.now() - start).total_seconds()
            result = TestResult(test_name, "FAIL", elapsed, str(e))
            logger.error(f"FAILED: {test_name} — {e}")
        except Exception as e:
            elapsed = (datetime.now() - start).total_seconds()
            result = TestResult(test_name, "ERROR", elapsed, str(e))
            logger.error(f"ERROR: {test_name} — {e}")
        
        self.results.append(result)
    
    def run_suite(self, suite_name, tests):
        """Run a suite of tests."""
        self.start_time = datetime.now()
        logger.info(f"{'='*50}")
        logger.info(f"SUITE: {suite_name}")
        logger.info(f"Tests: {len(tests)}")
        logger.info(f"{'='*50}")
        
        for test_name, test_func in tests:
            self.run_test(test_name, test_func)
        
        self._print_report(suite_name)
    
    def _print_report(self, suite_name):
        """Print test execution report."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "PASS")
        failed = sum(1 for r in self.results if r.status == "FAIL")
        errors = sum(1 for r in self.results if r.status == "ERROR")
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        print(f"\n  {'╔' + '═'*56 + '╗'}")
        print(f"  ║ {'TEST EXECUTION REPORT':^54s} ║")
        print(f"  {'╠' + '═'*56 + '╣'}")
        print(f"  ║ Suite:       {suite_name:<42s} ║")
        print(f"  ║ Environment: {self.config.base_url:<42s} ║")
        print(f"  ║ Browser:     {self.config.browser:<42s} ║")
        print(f"  ║ Duration:    {elapsed:.2f}s{' '*(39-len(f'{elapsed:.2f}s'))} ║")
        print(f"  {'╠' + '═'*56 + '╣'}")
        print(f"  ║ Total: {total:<4d} │ Pass: {passed:<4d} │ Fail: {failed:<4d} │ Error: {errors:<4d}║")
        
        rate = (passed / total * 100) if total > 0 else 0
        bar_len = 30
        filled = int(bar_len * passed / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  ║ Rate: [{bar}] {rate:5.1f}%     ║")
        print(f"  {'╠' + '═'*56 + '╣'}")
        
        for r in self.results:
            icon = {"PASS": "✓", "FAIL": "✗", "ERROR": "⚠"}[r.status]
            line = f"{icon} {r.name} ({r.duration:.2f}s)"
            print(f"  ║ {line:<54s} ║")
            if r.error:
                err_line = f"    Error: {r.error[:46]}"
                print(f"  ║ {err_line:<54s} ║")
        
        print(f"  {'╚' + '═'*56 + '╝'}")
        
        logger.info(f"{'='*50}")
        logger.info(f"REPORT: {passed}/{total} passed ({rate:.1f}%)")
        logger.info(f"{'='*50}")


# ============================================================
# PRACTICE TASK 1: Config Reader Demo
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Config Reader")
print("=" * 60)

def read_all_config(config_file):
    """Read and display all configuration settings."""
    parser = configparser.ConfigParser()
    parser.read(config_file)
    
    print(f"\n  Configuration from: {os.path.basename(config_file)}")
    
    for section in parser.sections():
        print(f"\n  [{section}]")
        for key, value in parser.items(section):
            print(f"    {key:<20s} = {value}")
    
    return parser

read_all_config(config_path)


# ============================================================
# PRACTICE TASK 2: Logging Demo
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: Structured Logging")
print("=" * 60)

def simulate_test_with_logging(test_name, should_pass=True):
    """Simulate a test execution with proper logging."""
    test_logger = logging.getLogger("automation.test")
    
    test_logger.info(f"Starting: {test_name}")
    test_logger.debug(f"Opening browser: {fw_config.browser}")
    test_logger.debug(f"Navigating to: {fw_config.base_url}")
    
    if should_pass:
        test_logger.info(f"Assertions passed for: {test_name}")
        test_logger.info(f"RESULT: {test_name} → PASS")
    else:
        test_logger.error(f"Assertion failed: Expected True, got False")
        test_logger.error(f"RESULT: {test_name} → FAIL")
    
    test_logger.debug("Closing browser")
    test_logger.info(f"Completed: {test_name}")

simulate_test_with_logging("Verify Login", should_pass=True)
simulate_test_with_logging("Verify Cart", should_pass=False)


# ============================================================
# PRACTICE TASK 3: LoginPage POM Demo
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: LoginPage POM Demo")
print("=" * 60)

print("\n--- Login with valid credentials ---")
login_page = LoginPage("Chrome")
login_page.login(fw_config.username, "Test@123")
print(f"  Dashboard displayed: {login_page.is_dashboard_displayed()}")

print("\n--- Search for a product ---")
search_page = SearchPage("Chrome")
search_page.search("brake pad")
print(f"  Results found: {search_page.has_results()}")


# ============================================================
# PRACTICE TASK 4: Mini Framework — Full Demo
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: Mini Framework Demo")
print("=" * 60)

# Define test functions
def test_login_valid():
    """Test: Login with valid credentials."""
    page = LoginPage()
    page.login(fw_config.username, "Test@123")
    assert page.is_dashboard_displayed(), "Dashboard not displayed after login!"

def test_login_invalid():
    """Test: Login with invalid credentials."""
    page = LoginPage()
    page.login("invalid@test.com", "wrong")
    # This will pass in our mock (because mock always returns True)
    assert page.is_dashboard_displayed()

def test_search():
    """Test: Search functionality."""
    page = SearchPage()
    page.search("brake pad")
    assert page.has_results(), "No search results found!"

def test_checkout_failure():
    """Test: Checkout (will fail with assertion)."""
    # Simulate a failing test
    cart_total = 0
    assert cart_total > 0, "Cart is empty — cannot checkout!"

def test_api_error():
    """Test: API call (will raise error)."""
    raise ConnectionError("API endpoint not reachable!")

# Run the framework
framework = MiniFramework(config_path)
framework.run_suite("Boodmo Smoke Tests", [
    ("Login with valid credentials", test_login_valid),
    ("Login with invalid credentials", test_login_invalid),
    ("Search for products", test_search),
    ("Checkout process", test_checkout_failure),
    ("API health check", test_api_error),
])

# Show log file content
print(f"\n--- Log file: {log_file} ---")
with open(log_file, "r") as f:
    lines = f.readlines()
    print(f"  ({len(lines)} lines logged)")
    # Show last 10 lines
    for line in lines[-10:]:
        print(f"  {line.rstrip()}")

print(f"\n{'='*60}")
print("🎉 CONGRATULATIONS! All 15 Topics Complete!")
print("=" * 60)
print("""
  You have covered:
  ──────────────────
  ✓ Topic 01: Python Basics
  ✓ Topic 02: Operators
  ✓ Topic 03: Control Flow
  ✓ Topic 04: Strings
  ✓ Topic 05: Lists
  ✓ Topic 06: Tuples
  ✓ Topic 07: Dictionaries
  ✓ Topic 08: Sets
  ✓ Topic 09: Functions
  ✓ Topic 10: OOP
  ✓ Topic 11: Exception Handling
  ✓ Topic 12: File Handling
  ✓ Topic 13: Modules & Packages
  ✓ Topic 14: DSA Overview
  ✓ Topic 15: Python for Automation

  Next Steps:
  ────────────
  1. Run: pytest test_sample.py -v
  2. Install Selenium: pip install selenium webdriver-manager
  3. Build real page objects with actual WebDriver
  4. Create a proper test framework with conftest.py
  5. Add reporting with pytest-html or Allure
""")

print("--- Topic 15 Complete! ---")
