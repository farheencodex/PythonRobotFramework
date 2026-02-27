"""
base_page.py — BasePage class for Page Object Model (POM)
==========================================================
The BasePage contains common methods shared by ALL page objects.
Every page class (LoginPage, SearchPage, etc.) inherits from BasePage.

In a real Selenium framework, this would use:
    - self.driver (WebDriver instance)
    - WebDriverWait for explicit waits
    - ActionChains for complex interactions
    
This is a SIMULATED version for learning — no Selenium required.
See the comments for what real Selenium code would look like.
"""

import logging

# Set up logger for the pages module
logger = logging.getLogger("pages.base_page")


class BasePage:
    """
    Base class for all page objects.
    
    Contains common methods that every page needs:
    - Navigation (open URL)
    - Element interaction (click, type, get text)
    - Waiting mechanisms
    - Screenshot capture
    
    Real Selenium Usage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
    """
    
    def __init__(self, driver_name="MockDriver"):
        """
        Initialize BasePage.
        
        In real Selenium:
            self.driver = driver
            self.wait = WebDriverWait(driver, timeout)
        """
        self.driver_name = driver_name
        self.current_url = None
        self.page_title = "Untitled"
        logger.info(f"BasePage initialized with {driver_name}")
    
    def open_url(self, url):
        """
        Navigate to a URL.
        
        Real Selenium:
            self.driver.get(url)
        """
        self.current_url = url
        logger.info(f"Navigating to: {url}")
        print(f"    [BasePage] Navigated to: {url}")
        return self
    
    def get_title(self):
        """
        Get the page title.
        
        Real Selenium:
            return self.driver.title
        """
        title = f"Page Title - {self.current_url}"
        logger.info(f"Page title: {title}")
        return title
    
    def find_element(self, locator):
        """
        Find an element on the page.
        
        Real Selenium:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        
        Args:
            locator (str): Element locator (CSS selector, XPath, etc.)
        """
        logger.debug(f"Finding element: {locator}")
        print(f"    [BasePage] Found element: {locator}")
        return f"Element({locator})"
    
    def click(self, locator):
        """
        Click on an element.
        
        Real Selenium:
            element = self.find_element(locator)
            element.click()
        """
        print(f"    [BasePage] Clicked: {locator}")
        logger.info(f"Clicked element: {locator}")
    
    def type_text(self, locator, text):
        """
        Type text into an input element.
        
        Real Selenium:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        """
        masked = text if "password" not in locator.lower() else "*" * len(text)
        print(f"    [BasePage] Typed '{masked}' into {locator}")
        logger.info(f"Typed text into: {locator}")
    
    def get_text(self, locator):
        """
        Get text from an element.
        
        Real Selenium:
            element = self.find_element(locator)
            return element.text
        """
        text = f"MockText({locator})"
        logger.debug(f"Got text from {locator}: {text}")
        return text
    
    def is_element_displayed(self, locator):
        """
        Check if an element is visible.
        
        Real Selenium:
            try:
                element = self.find_element(locator)
                return element.is_displayed()
            except NoSuchElementException:
                return False
        """
        logger.debug(f"Checking if {locator} is displayed")
        return True  # Mock always returns True
    
    def take_screenshot(self, filename):
        """
        Take a screenshot.
        
        Real Selenium:
            self.driver.save_screenshot(filename)
        """
        print(f"    [BasePage] Screenshot saved: {filename}")
        logger.info(f"Screenshot: {filename}")
    
    def close_browser(self):
        """
        Close the browser.
        
        Real Selenium:
            self.driver.quit()
        """
        print(f"    [BasePage] Browser closed: {self.driver_name}")
        logger.info(f"Browser closed")
