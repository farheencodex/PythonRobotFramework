"""
test_utils.utils — Utility functions for the automation framework.

This module provides:
    - generate_test_id(): Creates unique test case IDs
    - log_result(): Logs test results to console
    - TestStatus: Enum-like class for test statuses
"""

import random
import string
from datetime import datetime


class TestStatus:
    """Enum-like class for test result statuses."""
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"
    ERROR = "ERROR"
    NOT_RUN = "NOT_RUN"
    
    @classmethod
    def all_statuses(cls):
        """Return all valid statuses."""
        return [cls.PASS, cls.FAIL, cls.SKIP, cls.ERROR, cls.NOT_RUN]
    
    @classmethod
    def is_valid(cls, status):
        """Check if a status value is valid."""
        return status in cls.all_statuses()


def generate_test_id(prefix="TC", length=4):
    """
    Generate a unique test case ID.
    
    Args:
        prefix (str): Prefix for the ID (default: 'TC')
        length (int): Number of random digits (default: 4)
    
    Returns:
        str: A unique test ID like 'TC_1234'
    
    Example:
        >>> generate_test_id()
        'TC_8374'
        >>> generate_test_id(prefix="BUG", length=6)
        'BUG_483921'
    """
    random_part = ''.join(random.choices(string.digits, k=length))
    return f"{prefix}_{random_part}"


def log_result(test_id, test_name, status, duration=None, error_msg=None):
    """
    Log a test result with formatting.
    
    Args:
        test_id (str): The test case ID
        test_name (str): The test case name/title
        status (str): Test result status (use TestStatus constants)
        duration (float): Execution duration in seconds (optional)
        error_msg (str): Error message if test failed (optional)
    
    Returns:
        dict: A dictionary containing the logged result
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Status icons
    icons = {
        TestStatus.PASS: "✓",
        TestStatus.FAIL: "✗",
        TestStatus.SKIP: "⊘",
        TestStatus.ERROR: "⚠",
        TestStatus.NOT_RUN: "○",
    }
    icon = icons.get(status, "?")
    
    # Build log message
    msg = f"  {icon} [{test_id}] {test_name} — {status}"
    if duration is not None:
        msg += f" ({duration:.2f}s)"
    print(msg)
    
    if error_msg and status in (TestStatus.FAIL, TestStatus.ERROR):
        print(f"    Error: {error_msg}")
    
    return {
        "timestamp": timestamp,
        "test_id": test_id,
        "test_name": test_name,
        "status": status,
        "duration": duration,
        "error": error_msg,
    }


def format_duration(seconds):
    """Format duration in human-readable format."""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    else:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.1f}s"


# Module-level code that runs when imported
_creation_time = datetime.now().strftime("%H:%M:%S")
