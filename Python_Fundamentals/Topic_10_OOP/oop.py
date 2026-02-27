"""
Topic 10 — Object-Oriented Programming (OOP) | Python for Automation Course
=============================================================================
OOP is CRITICAL for automation framework design — Page Object Model, test base
classes, config managers, and reporting all use OOP extensively.

Concepts Covered:
    Classes and Objects:
        - Class definition, __init__() constructor
        - Instance variables and methods
        - self keyword
        - Creating multiple objects
    
    The 4 Pillars of OOP:
        - Encapsulation — bundling data + methods, private variables
        - Inheritance — child class inherits from parent
        - Polymorphism — same method, different behavior
        - Abstraction — hide implementation, expose interface
    
    Additional Concepts:
        - __str__() and __repr__() magic methods
        - Class variables vs instance variables
        - @classmethod and @staticmethod
        - super() keyword
        - Method overriding
        - Multiple inheritance (overview)
        - Abstract classes using ABC module

Practice Tasks:
    1. TestCase class with execute(), mark_pass(), mark_fail(), __str__()
    2. BasePage → LoginPage inheritance hierarchy
    3. Encapsulation with __password and getter/setter
    4. BrowserConfig with @classmethod and @staticmethod
    5. Abstract BaseTest with LoginTest and SearchTest subclasses

How to Run:
    python oop.py
"""

from abc import ABC, abstractmethod  # For abstract classes


# ============================================================
# SECTION 1: Classes and Objects
# ============================================================

print("=" * 60)
print("SECTION 1: Classes and Objects")
print("=" * 60)

# A CLASS is a blueprint for creating objects.
# An OBJECT is an instance of a class — a specific thing created from the blueprint.

# Think of it like:
# Class = "Car" blueprint → Object = your specific Honda Civic
# Class = "TestCase" blueprint → Object = specific test case TC_001

# --- Class Definition ---
class Browser:
    """A class representing a web browser for testing."""
    
    # __init__() is the CONSTRUCTOR — called when creating a new object
    # 'self' refers to the specific object being created
    def __init__(self, name, version):
        # Instance variables — unique to each object
        self.name = name          # Each browser has its own name
        self.version = version    # Each browser has its own version
        self.is_open = False      # Default state
    
    # Instance method — a function that belongs to the object
    def open(self):
        """Opens the browser."""
        self.is_open = True
        print(f"  {self.name} v{self.version} opened.")
    
    def close(self):
        """Closes the browser."""
        self.is_open = False
        print(f"  {self.name} closed.")
    
    def navigate(self, url):
        """Navigates to a URL."""
        if self.is_open:
            print(f"  {self.name} navigating to: {url}")
        else:
            print(f"  Error: {self.name} is not open!")

# --- Creating Objects (Instances) ---
# Each object is independent — changing one doesn't affect others
chrome = Browser("Chrome", "121.0")
firefox = Browser("Firefox", "122.0")

print(f"chrome.name = {chrome.name}")
print(f"firefox.name = {firefox.name}")

# Calling methods on objects
chrome.open()
chrome.navigate("https://boodmo.com")
chrome.close()

print()
firefox.navigate("https://boodmo.com")  # Error — not opened yet
firefox.open()
firefox.navigate("https://boodmo.com")  # Works now

# 'self' explained:
# When you call chrome.open(), Python automatically passes chrome as 'self'
# So self.name inside open() refers to chrome.name = "Chrome"
# When firefox.open() is called, self.name = "Firefox"

print()


# ============================================================
# SECTION 2: The 4 Pillars of OOP
# ============================================================

# ──────────────────────────────────────────────────────────────
# PILLAR 1: ENCAPSULATION
# ──────────────────────────────────────────────────────────────
# Bundle data and methods together. Hide internal implementation details.
# Use private variables (__var) to prevent direct access.

print("=" * 60)
print("PILLAR 1: Encapsulation")
print("=" * 60)

class UserAccount:
    """Demonstrates encapsulation with private attributes."""
    
    def __init__(self, username, password):
        self.username = username        # Public — accessible from outside
        self.__password = password      # Private — NOT accessible from outside
        self.__login_attempts = 0       # Private — internal tracking
    
    def get_password(self):
        """Getter — safe way to access private data."""
        # Return masked version for security
        return "*" * len(self.__password)
    
    def set_password(self, old_password, new_password):
        """Setter — safe way to modify private data with validation."""
        if old_password == self.__password:
            if len(new_password) >= 8:
                self.__password = new_password
                print(f"  Password updated for {self.username}.")
            else:
                print("  Error: Password must be at least 8 characters!")
        else:
            print("  Error: Old password is incorrect!")
    
    def login(self, password):
        """Attempt to login with password."""
        self.__login_attempts += 1
        if password == self.__password:
            print(f"  ✓ Login successful for {self.username}!")
            return True
        else:
            print(f"  ✗ Login failed! (Attempt {self.__login_attempts})")
            return False

user = UserAccount("tayyab", "SecureP@ss123")

# Public attribute — accessible
print(f"Username: {user.username}")

# Private attribute — NOT directly accessible
# print(user.__password)  # AttributeError!
print(f"Password: {user.get_password()}")  # Safe access via getter

# Login attempts
user.login("wrong_pass")
user.login("SecureP@ss123")

# Change password
user.set_password("SecureP@ss123", "NewP@ss456")
user.set_password("SecureP@ss123", "short")  # Will fail — old pass wrong
user.set_password("NewP@ss456", "short")     # Will fail — too short

# Name mangling — Python actually renames __var to _ClassName__var
# You CAN access it, but you SHOULDN'T (it violates encapsulation)
# print(user._UserAccount__password)  # Works but DON'T do this!

print()


# ──────────────────────────────────────────────────────────────
# PILLAR 2: INHERITANCE
# ──────────────────────────────────────────────────────────────
# Child class inherits attributes and methods from parent class.
# This promotes code REUSE — don't repeat yourself (DRY principle)!

print("=" * 60)
print("PILLAR 2: Inheritance")
print("=" * 60)

# Parent (base) class
class Animal:
    """Parent class representing a generic animal."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        print(f"  {self.name} makes a sound.")
    
    def info(self):
        print(f"  {self.name} is a {self.species}.")

# Child class — inherits from Animal
class Dog(Animal):  # Dog inherits from Animal
    """Child class — inherits all of Animal's methods and adds its own."""
    
    def __init__(self, name, breed):
        # super() calls the parent's __init__ method
        super().__init__(name, species="Dog")
        self.breed = breed  # New attribute specific to Dog
    
    # Override parent's speak method
    def speak(self):
        print(f"  {self.name} says: Woof! Woof!")
    
    # New method specific to Dog
    def fetch(self, item):
        print(f"  {self.name} fetches the {item}!")

# Child class — another child
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def speak(self):
        print(f"  {self.name} says: Meow!")

# Using inheritance
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Orange")

dog.info()      # Inherited from Animal
dog.speak()     # Overridden in Dog
dog.fetch("ball")  # Dog-specific method

cat.info()      # Inherited from Animal
cat.speak()     # Overridden in Cat

# isinstance() checks — inheritance aware
print(f"\ndog is a Dog?    {isinstance(dog, Dog)}")       # True
print(f"dog is an Animal? {isinstance(dog, Animal)}")    # True (Dog inherits Animal)
print(f"cat is a Dog?     {isinstance(cat, Dog)}")       # False

print()


# ──────────────────────────────────────────────────────────────
# PILLAR 3: POLYMORPHISM
# ──────────────────────────────────────────────────────────────
# Same method name, different behavior in different classes.
# "Poly" = many, "morph" = forms → many forms!

print("=" * 60)
print("PILLAR 3: Polymorphism")
print("=" * 60)

class WebElement:
    """Base class for web elements."""
    def __init__(self, locator):
        self.locator = locator
    
    def click(self):
        print(f"  Clicking element: {self.locator}")

class Button(WebElement):
    def click(self):
        print(f"  Clicking BUTTON: {self.locator}")
        print(f"  → Button click event fired!")

class Link(WebElement):
    def click(self):
        print(f"  Clicking LINK: {self.locator}")
        print(f"  → Navigating to linked page...")

class Checkbox(WebElement):
    def __init__(self, locator):
        super().__init__(locator)
        self.checked = False
    
    def click(self):
        self.checked = not self.checked
        state = "checked" if self.checked else "unchecked"
        print(f"  Clicking CHECKBOX: {self.locator}")
        print(f"  → Checkbox is now {state}")

# Polymorphism in action — same method name, different behavior
elements = [
    Button("submit-btn"),
    Link("home-link"),
    Checkbox("remember-me"),
    Button("cancel-btn"),
]

print("Clicking all elements (polymorphism):")
for element in elements:
    element.click()  # Same method name, different behavior!
    print()


# ──────────────────────────────────────────────────────────────
# PILLAR 4: ABSTRACTION
# ──────────────────────────────────────────────────────────────
# Hide complex implementation, expose simple interface.
# Use abstract classes to define a contract that subclasses must follow.

print("=" * 60)
print("PILLAR 4: Abstraction")
print("=" * 60)

class Shape(ABC):
    """Abstract class — cannot be instantiated directly.
    Subclasses MUST implement all abstract methods."""
    
    @abstractmethod
    def area(self):
        """Calculate the area. Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter. Must be implemented by subclasses."""
        pass
    
    # Regular (non-abstract) methods CAN have implementation
    def describe(self):
        print(f"  Shape: {self.__class__.__name__}")
        print(f"  Area: {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot create an instance of abstract class:
# shape = Shape()  # TypeError: Can't instantiate abstract class

# Can create instances of concrete subclasses:
circle = Circle(5)
rect = Rectangle(4, 6)

circle.describe()
print()
rect.describe()

print()


# ============================================================
# SECTION 3: __str__() and __repr__() Magic Methods
# ============================================================

print("=" * 60)
print("SECTION 3: __str__() and __repr__()")
print("=" * 60)

class TestCase:
    def __init__(self, tc_id, title, status="Not Run"):
        self.tc_id = tc_id
        self.title = title
        self.status = status
    
    def __str__(self):
        """Human-readable representation — used by print() and str()."""
        return f"[{self.tc_id}] {self.title} — Status: {self.status}"
    
    def __repr__(self):
        """Developer-friendly representation — used in debugger and repr()."""
        return f"TestCase('{self.tc_id}', '{self.title}', '{self.status}')"

tc = TestCase("TC001", "Login Test", "Pass")

# __str__ is used by print()
print(f"str:  {tc}")           # [TC001] Login Test — Status: Pass

# __repr__ is used by repr() and in debugger
print(f"repr: {repr(tc)}")     # TestCase('TC001', 'Login Test', 'Pass')

# In a list, __repr__ is used
test_cases = [
    TestCase("TC001", "Login", "Pass"),
    TestCase("TC002", "Search", "Fail"),
]
print(f"\nList: {test_cases}")  # Shows repr for each

print()


# ============================================================
# SECTION 4: Class Variables vs Instance Variables
# ============================================================

print("=" * 60)
print("SECTION 4: Class vs Instance Variables")
print("=" * 60)

class TestSuite:
    # CLASS VARIABLE — shared by ALL instances
    total_suites = 0
    
    def __init__(self, name):
        # INSTANCE VARIABLE — unique to each instance
        self.name = name
        self.test_count = 0
        
        # Increment the class variable (shared counter)
        TestSuite.total_suites += 1
    
    def add_test(self):
        self.test_count += 1  # Modifies instance variable

# Create multiple instances
suite1 = TestSuite("Login Suite")
suite2 = TestSuite("Search Suite")
suite3 = TestSuite("Cart Suite")

suite1.add_test()
suite1.add_test()
suite2.add_test()

# Instance variables are unique to each object
print(f"suite1.test_count = {suite1.test_count}")  # 2
print(f"suite2.test_count = {suite2.test_count}")  # 1
print(f"suite3.test_count = {suite3.test_count}")  # 0

# Class variable is shared
print(f"\nTotal suites created: {TestSuite.total_suites}")  # 3 (shared!)

print()


# ============================================================
# SECTION 5: @classmethod and @staticmethod
# ============================================================

print("=" * 60)
print("SECTION 5: @classmethod and @staticmethod")
print("=" * 60)

class BrowserConfig:
    """Browser configuration manager using class/static methods."""
    
    # Class variable — default config
    DEFAULT_BROWSER = "Chrome"
    SUPPORTED_BROWSERS = ["Chrome", "Firefox", "Edge", "Safari"]
    
    def __init__(self, browser, version, headless=False):
        self.browser = browser
        self.version = version
        self.headless = headless
    
    @classmethod
    def get_default_browser(cls):
        """
        @classmethod receives the CLASS (cls) as first argument.
        Can access/modify class-level attributes.
        Often used as alternative constructors.
        """
        return cls.DEFAULT_BROWSER
    
    @classmethod
    def from_string(cls, config_string):
        """Alternative constructor — create from string like 'Chrome-121.0'."""
        browser, version = config_string.split("-")
        return cls(browser, version)
    
    @staticmethod
    def is_supported_browser(name):
        """
        @staticmethod doesn't receive class or instance.
        It's a utility function that logically belongs to the class
        but doesn't need access to class/instance data.
        """
        return name in BrowserConfig.SUPPORTED_BROWSERS
    
    def __str__(self):
        mode = "headless" if self.headless else "headed"
        return f"{self.browser} v{self.version} ({mode})"

# Using @classmethod
default = BrowserConfig.get_default_browser()
print(f"Default browser: {default}")

# Using @classmethod as alternative constructor
config = BrowserConfig.from_string("Firefox-122.0")
print(f"From string: {config}")

# Using @staticmethod
print(f"\nIs Chrome supported? {BrowserConfig.is_supported_browser('Chrome')}")   # True
print(f"Is Opera supported?  {BrowserConfig.is_supported_browser('Opera')}")    # False

# Regular usage
chrome = BrowserConfig("Chrome", "121.0", headless=True)
print(f"\nConfig: {chrome}")

print()


# ============================================================
# SECTION 6: super() Keyword
# ============================================================

print("=" * 60)
print("SECTION 6: super() Keyword")
print("=" * 60)

# super() is used to call methods from the PARENT class.
# Most commonly used in __init__ to initialize parent attributes.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"  Vehicle.__init__({make}, {model}, {year})")
    
    def describe(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        # super() calls the parent's __init__
        super().__init__(make, model, year)  # Initialize parent attributes
        self.battery_kwh = battery_kwh       # Add child-specific attribute
        print(f"  ElectricCar.__init__(battery={battery_kwh}kWh)")
    
    def describe(self):
        # Override parent method but also USE parent's implementation
        base = super().describe()  # Call parent's describe()
        return f"{base} (Electric, {self.battery_kwh}kWh)"

tesla = ElectricCar("Tesla", "Model 3", 2024, 75)
print(f"\n{tesla.describe()}")

print()


# ============================================================
# SECTION 7: Method Overriding & Multiple Inheritance
# ============================================================

print("=" * 60)
print("SECTION 7: Method Overriding & Multiple Inheritance")
print("=" * 60)

# --- Method Overriding ---
# Child class provides its own implementation of a parent's method

class Logger:
    def log(self, message):
        print(f"  LOG: {message}")

class FileLogger(Logger):
    def log(self, message):
        # Override parent's log — writes to file instead of console
        print(f"  FILE LOG: {message} (would write to file)")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"  CONSOLE LOG: [{message}]")

# Each subclass has different behavior for log()
loggers = [Logger(), FileLogger(), ConsoleLogger()]
for logger in loggers:
    logger.log("Test started")

# --- Multiple Inheritance (overview) ---
print("\n--- Multiple Inheritance ---")

class Printable:
    def print_details(self):
        print(f"  Printable: {self}")

class Serializable:
    def to_dict(self):
        return self.__dict__

class Config(Printable, Serializable):
    """Inherits from BOTH Printable and Serializable."""
    def __init__(self, browser, timeout):
        self.browser = browser
        self.timeout = timeout
    
    def __str__(self):
        return f"Config(browser={self.browser}, timeout={self.timeout})"

config = Config("Chrome", 30)
config.print_details()              # From Printable
print(f"  Dict: {config.to_dict()}")  # From Serializable

# MRO — Method Resolution Order (how Python decides which method to call)
print(f"\n  MRO: {[c.__name__ for c in Config.__mro__]}")

print()


# ============================================================
# PRACTICE TASK 1: TestCase Class
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: TestCase Class")
print("=" * 60)

class TestCase:
    """
    Represents a test case with execution capabilities.
    
    Attributes:
        tc_id (str): Test case identifier
        title (str): Test case title/description
        status (str): Current status (Not Run, Pass, Fail)
        priority (str): Priority level (P0, P1, P2, P3)
    """
    
    def __init__(self, tc_id, title, status="Not Run", priority="P1"):
        self.tc_id = tc_id
        self.title = title
        self.status = status
        self.priority = priority
    
    def execute(self):
        """Simulate test case execution."""
        print(f"  ▶ Executing {self.tc_id}: {self.title}...")
        self.status = "In Progress"
        print(f"    Status: {self.status}")
    
    def mark_pass(self):
        """Mark the test case as passed."""
        self.status = "Pass"
        print(f"  ✓ {self.tc_id}: PASSED")
    
    def mark_fail(self):
        """Mark the test case as failed."""
        self.status = "Fail"
        print(f"  ✗ {self.tc_id}: FAILED")
    
    def __str__(self):
        """Human-readable string representation."""
        icon = {"Pass": "✓", "Fail": "✗", "Not Run": "○", "In Progress": "▶"}
        return f"{icon.get(self.status, '?')} [{self.tc_id}] {self.title} | {self.status} | {self.priority}"

# Create test cases
tc1 = TestCase("TC_001", "Verify Login", priority="P0")
tc2 = TestCase("TC_002", "Verify Search", priority="P1")
tc3 = TestCase("TC_003", "Verify Cart", priority="P0")

# Execute test cases
print("Before execution:")
print(f"  {tc1}")
print(f"  {tc2}")
print(f"  {tc3}")

print("\nExecuting tests:")
tc1.execute()
tc1.mark_pass()

tc2.execute()
tc2.mark_fail()

tc3.execute()
tc3.mark_pass()

print("\nAfter execution:")
print(f"  {tc1}")
print(f"  {tc2}")
print(f"  {tc3}")


# ============================================================
# PRACTICE TASK 2: BasePage → LoginPage Inheritance
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: BasePage → LoginPage (POM Pattern)")
print("=" * 60)

class BasePage:
    """
    Base page class for Page Object Model (POM) pattern.
    Contains common methods shared by all pages.
    """
    
    def __init__(self, driver_name="Chrome"):
        self.driver_name = driver_name
        self.current_url = None
        print(f"  BasePage initialized with {driver_name}")
    
    def open_url(self, url):
        """Navigate to a URL."""
        self.current_url = url
        print(f"  → Navigating to: {url}")
    
    def get_title(self):
        """Get the page title."""
        title = f"Page at {self.current_url}"
        print(f"  → Page title: {title}")
        return title
    
    def click_element(self, locator):
        """Click on an element using a locator."""
        print(f"  → Clicking element: {locator}")


class LoginPage(BasePage):
    """
    Login page class — inherits from BasePage.
    Adds login-specific functionality.
    """
    
    LOGIN_URL = "https://boodmo.com/login"
    
    def __init__(self, driver_name="Chrome"):
        super().__init__(driver_name)  # Initialize parent class
        self.is_logged_in = False
        print(f"  LoginPage initialized")
    
    def open(self):
        """Open the login page."""
        self.open_url(self.LOGIN_URL)  # Use inherited method
    
    def enter_credentials(self, username, password):
        """Enter username and password."""
        print(f"  → Entering username: {username}")
        print(f"  → Entering password: {'*' * len(password)}")
    
    def submit_login(self):
        """Click the login button."""
        self.click_element("login-button")  # Use inherited method
        self.is_logged_in = True
        print(f"  ✓ Login submitted successfully!")
    
    def login(self, username, password):
        """Complete login flow — convenience method."""
        self.open()
        self.enter_credentials(username, password)
        self.submit_login()

# Usage
print("\n--- Using LoginPage ---")
login_page = LoginPage("Chrome")
print()
login_page.login("tayyab", "SecureP@ss123")
print()
login_page.get_title()  # Inherited method


# ============================================================
# PRACTICE TASK 3: Encapsulation — Private __password
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Encapsulation Demo")
print("=" * 60)

class SecureConfig:
    """Demonstrates encapsulation with getter/setter methods."""
    
    def __init__(self, api_key, db_password):
        self.api_key = api_key           # Public attribute
        self.__db_password = db_password  # Private attribute (hidden)
    
    def get_db_password(self):
        """Getter — returns masked password."""
        return self.__db_password[:2] + "*" * (len(self.__db_password) - 4) + self.__db_password[-2:]
    
    def set_db_password(self, old_password, new_password):
        """Setter — validates before updating."""
        if old_password != self.__db_password:
            print("  ✗ Error: Current password is incorrect!")
            return False
        if len(new_password) < 8:
            print("  ✗ Error: New password must be at least 8 characters!")
            return False
        self.__db_password = new_password
        print("  ✓ Password updated successfully!")
        return True

config = SecureConfig("API_KEY_123", "MySecureP@ss")

# Public attribute — accessible
print(f"API Key: {config.api_key}")

# Private attribute — NOT directly accessible
try:
    print(config.__db_password)
except AttributeError as e:
    print(f"Direct access failed: {e}")

# Access through getter (safe)
print(f"DB Password (masked): {config.get_db_password()}")

# Update through setter (validated)
config.set_db_password("wrong_pass", "NewPass123")     # Fails — wrong old pass
config.set_db_password("MySecureP@ss", "short")        # Fails — too short
config.set_db_password("MySecureP@ss", "NewSecure123") # Success!
print(f"Updated password: {config.get_db_password()}")


# ============================================================
# PRACTICE TASK 4: BrowserConfig with @classmethod/@staticmethod
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 4: BrowserConfig — classmethod & staticmethod")
print("=" * 60)

class BrowserConfigV2:
    """Browser configuration with class and static methods."""
    
    SUPPORTED = ["Chrome", "Firefox", "Edge", "Safari"]
    _default = "Chrome"
    
    def __init__(self, name, version="latest", headless=False):
        if not self.is_supported_browser(name):
            raise ValueError(f"Browser '{name}' is not supported!")
        self.name = name
        self.version = version
        self.headless = headless
    
    @classmethod
    def get_default_browser(cls):
        """Returns the default browser name."""
        return cls._default
    
    @classmethod
    def set_default_browser(cls, browser):
        """Changes the default browser (affects all instances)."""
        if browser in cls.SUPPORTED:
            cls._default = browser
            print(f"  Default browser changed to: {browser}")
        else:
            print(f"  Error: {browser} is not supported!")
    
    @staticmethod
    def is_supported_browser(name):
        """Check if a browser is supported (no class/instance needed)."""
        return name in BrowserConfigV2.SUPPORTED
    
    def __str__(self):
        mode = "headless" if self.headless else "headed"
        return f"Browser({self.name} v{self.version}, {mode})"

# @classmethod usage
print(f"Default browser: {BrowserConfigV2.get_default_browser()}")
BrowserConfigV2.set_default_browser("Firefox")
print(f"New default: {BrowserConfigV2.get_default_browser()}")

# @staticmethod usage
print(f"\nIs 'Chrome' supported? {BrowserConfigV2.is_supported_browser('Chrome')}")
print(f"Is 'Opera' supported?  {BrowserConfigV2.is_supported_browser('Opera')}")
print(f"Is 'Safari' supported? {BrowserConfigV2.is_supported_browser('Safari')}")

# Create instance
browser = BrowserConfigV2("Chrome", "121.0", headless=True)
print(f"\nConfig: {browser}")

# Try unsupported browser
try:
    bad = BrowserConfigV2("Opera")
except ValueError as e:
    print(f"Error: {e}")


# ============================================================
# PRACTICE TASK 5: Abstract BaseTest with Subclasses
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 5: Abstract BaseTest Class")
print("=" * 60)

class BaseTest(ABC):
    """
    Abstract base class for all tests.
    Subclasses MUST implement run_test() method.
    """
    
    def __init__(self, test_name):
        self.test_name = test_name
        self.result = None
    
    @abstractmethod
    def run_test(self):
        """Execute the test. Must be implemented by subclasses."""
        pass
    
    def setup(self):
        """Common setup — runs before each test."""
        print(f"  [SETUP] Preparing: {self.test_name}")
    
    def teardown(self):
        """Common teardown — runs after each test."""
        print(f"  [TEARDOWN] Cleaning up: {self.test_name}")
    
    def execute(self):
        """Template method — defines the test execution workflow."""
        self.setup()
        self.run_test()       # Calls the subclass implementation
        self.teardown()
        print(f"  [RESULT] {self.test_name}: {self.result}")

# Cannot instantiate abstract class:
# test = BaseTest("sample")  # TypeError!

class LoginTest(BaseTest):
    """Concrete test — tests login functionality."""
    
    def run_test(self):
        """Implementation of the abstract run_test() method."""
        print(f"  [TEST] Navigating to login page...")
        print(f"  [TEST] Entering credentials...")
        print(f"  [TEST] Clicking login button...")
        print(f"  [TEST] Verifying dashboard is displayed...")
        self.result = "PASS"

class SearchTest(BaseTest):
    """Concrete test — tests search functionality."""
    
    def run_test(self):
        """Implementation of the abstract run_test() method."""
        print(f"  [TEST] Navigating to home page...")
        print(f"  [TEST] Entering search query: 'brake pad'...")
        print(f"  [TEST] Clicking search button...")
        print(f"  [TEST] Verifying search results are displayed...")
        self.result = "PASS"

# Execute tests using the template method
print("\n--- Executing LoginTest ---")
login_test = LoginTest("Login Verification")
login_test.execute()

print("\n--- Executing SearchTest ---")
search_test = SearchTest("Search Verification")
search_test.execute()

print("\n--- All Tests Summary ---")
tests = [login_test, search_test]
for t in tests:
    icon = "✓" if t.result == "PASS" else "✗"
    print(f"  {icon} {t.test_name}: {t.result}")

print("\n--- Topic 10 Complete! ---")
