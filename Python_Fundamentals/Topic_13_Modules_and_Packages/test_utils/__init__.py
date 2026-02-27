"""
test_utils package — Custom utility module for automation.
Demonstrates how packages work in Python.

A package is a FOLDER containing:
    1. __init__.py (makes it a package)
    2. Module files (.py files)
"""

# When someone does: from test_utils import utils
# or: from test_utils.utils import generate_test_id
# This __init__.py runs first.

# You can import and re-export things here for convenience:
from .utils import generate_test_id, log_result, TestStatus

# Package-level variables
PACKAGE_NAME = "test_utils"
VERSION = "1.0.0"

print(f"  [__init__.py] test_utils package loaded (v{VERSION})")
