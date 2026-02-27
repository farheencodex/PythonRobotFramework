"""
Topic 12 — File Handling | Python for Automation Course
========================================================
File handling is ESSENTIAL for automation — reading test data from CSV/JSON,
writing reports, managing logs, reading configurations, etc.

Concepts Covered:
    1. Opening and closing files (open(), close())
    2. Reading files: read(), readline(), readlines()
    3. Writing files: write(), writelines()
    4. The 'with' statement (context manager) — auto-close!
    5. File modes: r, w, a, r+, x
    6. Working with CSV files (csv module)
    7. Working with JSON files (json module)
    8. Working with file paths (os.path)
    9. Checking file existence and properties

Practice Tasks:
    1. Read test_data.csv and display a formatted report
    2. Read config.json and access nested values
    3. Generate a test execution report (write to file)
    4. Log messages to a file with timestamps

Data Files (included in this folder):
    - test_data.csv  → Sample test case data
    - config.json    → Sample configuration data

How to Run:
    cd Topic_12_File_Handling
    python file_handling.py
"""

import os
import csv
import json
from datetime import datetime


# ============================================================
# SECTION 1: Opening and Closing Files
# ============================================================

print("=" * 60)
print("SECTION 1: Opening and Closing Files")
print("=" * 60)

# open(filename, mode) opens a file
# Modes:
#   'r'  → Read (default) — file must exist
#   'w'  → Write — creates new or OVERWRITES existing
#   'a'  → Append — creates new or adds to end of existing
#   'r+' → Read + Write — file must exist
#   'x'  → Exclusive create — fails if file exists

# --- Basic open and close (old style) ---
# Creating a sample file to work with
sample_file = "sample_output.txt"
f = open(sample_file, "w")  # Open for writing
f.write("Hello from file handling!\n")
f.write("This is line 2.\n")
f.write("This is line 3.\n")
f.close()  # MUST close the file!
print(f"  Created: {sample_file}")

# Reading the file
f = open(sample_file, "r")  # Open for reading
content = f.read()           # Read entire content
f.close()                    # MUST close!
print(f"  Content:\n{content}")

# WARNING: If you forget to close, data might not be written
# and the file handle stays open (bad for OS resources).

print()


# ============================================================
# SECTION 2: Reading Files — read(), readline(), readlines()
# ============================================================

print("=" * 60)
print("SECTION 2: Reading Files")
print("=" * 60)

# --- read() — reads ENTIRE file as one string ---
print("--- read() ---")
with open(sample_file, "r") as f:
    content = f.read()
print(f"  read(): '{content.strip()}'")

# --- readline() — reads ONE line at a time ---
print("\n--- readline() ---")
with open(sample_file, "r") as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
print(f"  Line 1: '{line1.strip()}'")
print(f"  Line 2: '{line2.strip()}'")

# --- readlines() — reads ALL lines into a LIST ---
print("\n--- readlines() ---")
with open(sample_file, "r") as f:
    lines = f.readlines()  # Returns list of strings
print(f"  readlines(): {lines}")
print(f"  Number of lines: {len(lines)}")

# --- Iterating over lines (most Pythonic) ---
print("\n--- Iterating over file ---")
with open(sample_file, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

print()


# ============================================================
# SECTION 3: Writing Files — write(), writelines()
# ============================================================

print("=" * 60)
print("SECTION 3: Writing Files")
print("=" * 60)

# --- write() — writes a string (no automatic newline) ---
print("--- write() ---")
with open("test_results.txt", "w") as f:
    f.write("Test Execution Report\n")
    f.write("=" * 30 + "\n")
    f.write("TC_001: Login Test — PASS\n")
    f.write("TC_002: Search Test — FAIL\n")
    f.write("TC_003: Cart Test — PASS\n")
print("  Created: test_results.txt")

# --- writelines() — writes a LIST of strings ---
print("\n--- writelines() ---")
log_entries = [
    "2024-01-15 10:00:00 | INFO  | Test suite started\n",
    "2024-01-15 10:00:05 | INFO  | Browser launched\n",
    "2024-01-15 10:00:10 | INFO  | Login page opened\n",
    "2024-01-15 10:00:15 | ERROR | Login failed\n",
    "2024-01-15 10:00:20 | INFO  | Browser closed\n",
]
with open("test_log.txt", "w") as f:
    f.writelines(log_entries)  # Writes all at once (no separator added)
print("  Created: test_log.txt")

# --- Appending to a file ---
print("\n--- Append mode ('a') ---")
with open("test_log.txt", "a") as f:
    f.write("2024-01-15 10:01:00 | INFO  | Retry attempt 1\n")
    f.write("2024-01-15 10:01:05 | INFO  | Login successful\n")
print("  Appended 2 entries to test_log.txt")

# Verify
with open("test_log.txt", "r") as f:
    print(f"  Total lines: {len(f.readlines())}")

print()


# ============================================================
# SECTION 4: The 'with' Statement (Context Manager)
# ============================================================

print("=" * 60)
print("SECTION 4: Context Manager (with statement)")
print("=" * 60)

# The 'with' statement automatically:
# 1. Opens the file
# 2. Gives you the file handle
# 3. AUTOMATICALLY closes the file when the block ends
# 4. Handles exceptions — file gets closed even if error occurs!

# ALWAYS use 'with' for file operations!

# --- with statement benefits ---
print("--- with statement ---")

# Without 'with' (BAD pattern):
# f = open("file.txt")
# content = f.read()
# f.close()  # Easy to forget!

# With 'with' (GOOD pattern):
with open(sample_file, "r") as f:
    content = f.read()
    print(f"  File is open: {not f.closed}")
# After 'with' block ends, file is automatically closed
print(f"  File is closed: {f.closed}")

# --- Multiple files with 'with' ---
print("\n--- Multiple files ---")
with open("test_results.txt", "r") as source, \
     open("results_copy.txt", "w") as dest:
    data = source.read()
    dest.write(data)
    print(f"  Copied {len(data)} chars from test_results.txt to results_copy.txt")

print()


# ============================================================
# SECTION 5: Working with CSV Files
# ============================================================

print("=" * 60)
print("SECTION 5: CSV Files")
print("=" * 60)

# CSV = Comma-Separated Values
# Very common for test data, reports, and data-driven testing.

# Get the directory of the current script for relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "test_data.csv")

# --- Reading CSV with csv.reader ---
print("--- Reading CSV (csv.reader) ---")
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # First row is the header
    print(f"  Header: {header}")
    print(f"  Data:")
    for row in reader:
        print(f"    {row}")

# --- Reading CSV with csv.DictReader (recommended!) ---
print("\n--- Reading CSV (csv.DictReader) ---")
with open(csv_path, "r") as f:
    reader = csv.DictReader(f)  # Each row is a dictionary
    test_cases = list(reader)

# Access data by column name (much cleaner!)
print(f"  Loaded {len(test_cases)} test cases:")
for tc in test_cases:
    icon = {"Pass": "✓", "Fail": "✗", "Not Run": "○"}.get(tc["Status"], "?")
    print(f"    {icon} [{tc['TC_ID']}] {tc['Title']} — {tc['Status']} ({tc['Priority']})")

# --- Writing CSV ---
print("\n--- Writing CSV ---")
report_data = [
    {"TC_ID": "TC_001", "Result": "Pass", "Duration": "2.5s"},
    {"TC_ID": "TC_002", "Result": "Fail", "Duration": "5.1s"},
    {"TC_ID": "TC_003", "Result": "Pass", "Duration": "1.8s"},
]

output_csv = os.path.join(script_dir, "report_output.csv")
with open(output_csv, "w", newline="") as f:
    fieldnames = ["TC_ID", "Result", "Duration"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(report_data)
print(f"  Written: report_output.csv ({len(report_data)} rows)")

print()


# ============================================================
# SECTION 6: Working with JSON Files
# ============================================================

print("=" * 60)
print("SECTION 6: JSON Files")
print("=" * 60)

# JSON = JavaScript Object Notation
# Standard format for API responses, configs, test data

json_path = os.path.join(script_dir, "config.json")

# --- Reading JSON ---
print("--- Reading JSON ---")
with open(json_path, "r") as f:
    config = json.load(f)  # Parse JSON into Python dict

print(f"  Project: {config['project']}")
print(f"  Environment: {config['environment']}")
print(f"  Base URL: {config['base_url']}")
print(f"  Browser: {config['browser']}")
print(f"  Timeout: {config['timeout']}s")

# Accessing nested JSON values
print(f"\n  Admin user: {config['credentials']['admin']['username']}")
print(f"\n  Test Suites:")
for suite in config["test_suites"]:
    print(f"    - {suite['name']} ({suite['priority']}): {suite['test_count']} tests")

# --- Writing JSON ---
print("\n--- Writing JSON ---")
test_results = {
    "run_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "environment": "staging",
    "total_tests": 10,
    "passed": 6,
    "failed": 2,
    "not_run": 2,
    "pass_rate": "60%",
    "tests": [
        {"id": "TC_001", "status": "Pass", "duration": 2.5},
        {"id": "TC_002", "status": "Fail", "duration": 5.1, "error": "Element not found"},
    ]
}

output_json = os.path.join(script_dir, "results_output.json")
with open(output_json, "w") as f:
    json.dump(test_results, f, indent=4)  # indent=4 for pretty printing
print(f"  Written: results_output.json")

# --- json.dumps() for strings (not files) ---
json_string = json.dumps(test_results, indent=2)
print(f"\n  JSON as string (first 100 chars): {json_string[:100]}...")

print()


# ============================================================
# SECTION 7: File Paths (os.path)
# ============================================================

print("=" * 60)
print("SECTION 7: File Paths (os.path)")
print("=" * 60)

# os.path provides utilities for working with file paths

# --- Common os.path operations ---
filepath = os.path.abspath(__file__)
print(f"  Current file: {filepath}")
print(f"  Directory:    {os.path.dirname(filepath)}")
print(f"  Filename:     {os.path.basename(filepath)}")
print(f"  File exists:  {os.path.exists(filepath)}")
print(f"  Is file:      {os.path.isfile(filepath)}")
print(f"  Is directory: {os.path.isdir(filepath)}")
print(f"  File size:    {os.path.getsize(filepath)} bytes")

# --- Joining paths (cross-platform!) ---
print("\n--- Path joining ---")
project_root = os.path.dirname(script_dir)  # Go up one level
reports_dir = os.path.join(project_root, "reports")
print(f"  Project root: {project_root}")
print(f"  Reports dir:  {reports_dir}")

# --- Splitting path and extension ---
name, ext = os.path.splitext("test_data.csv")
print(f"\n  splitext('test_data.csv'): name='{name}', ext='{ext}'")

# Always use os.path.join() instead of string concatenation for paths!
# Good: os.path.join("folder", "file.txt")
# Bad:  "folder" + "/" + "file.txt"  (breaks on Windows!)

print()


# ============================================================
# SECTION 8: Checking File Properties
# ============================================================

print("=" * 60)
print("SECTION 8: File Properties")
print("=" * 60)

# --- Check if files/directories exist ---
files_to_check = [
    csv_path,
    json_path,
    "nonexistent_file.txt",
    script_dir,
]

for path in files_to_check:
    name = os.path.basename(path) or path
    exists = os.path.exists(path)
    if exists:
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(f"  ✓ FILE   {name:30s} ({size} bytes)")
        elif os.path.isdir(path):
            print(f"  ✓ DIR    {name}")
    else:
        print(f"  ✗ MISSING {name}")

# --- List files in a directory ---
print(f"\n--- Files in script directory ---")
for item in sorted(os.listdir(script_dir)):
    full_path = os.path.join(script_dir, item)
    icon = "📁" if os.path.isdir(full_path) else "📄"
    print(f"  {icon} {item}")

print()


# ============================================================
# PRACTICE TASK 1: Read CSV & Display Formatted Report
# ============================================================

print("=" * 60)
print("PRACTICE TASK 1: Formatted CSV Report")
print("=" * 60)

def display_csv_report(csv_file):
    """Read test_data.csv and display a nicely formatted report."""
    
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        test_cases = list(reader)
    
    # Count statistics
    total = len(test_cases)
    passed = sum(1 for tc in test_cases if tc["Status"] == "Pass")
    failed = sum(1 for tc in test_cases if tc["Status"] == "Fail")
    not_run = sum(1 for tc in test_cases if tc["Status"] == "Not Run")
    
    # Group by module
    modules = {}
    for tc in test_cases:
        module = tc["Module"]
        if module not in modules:
            modules[module] = []
        modules[module].append(tc)
    
    # Print report
    print(f"\n  {'=' * 55}")
    print(f"  {'TEST EXECUTION REPORT':^55}")
    print(f"  {'=' * 55}")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Total: {total} | Pass: {passed} | Fail: {failed} | Not Run: {not_run}")
    pass_rate = (passed / total * 100) if total > 0 else 0
    print(f"  Pass Rate: {pass_rate:.1f}%")
    print(f"  {'-' * 55}")
    
    for module, tcs in modules.items():
        print(f"\n  [{module}]")
        for tc in tcs:
            icon = {"Pass": "✓", "Fail": "✗", "Not Run": "○"}[tc["Status"]]
            print(f"    {icon} {tc['TC_ID']:8s} {tc['Title']:40s} {tc['Priority']}")
    
    print(f"\n  {'=' * 55}")

display_csv_report(csv_path)


# ============================================================
# PRACTICE TASK 2: Read JSON Config & Access Nested Values
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 2: JSON Config Reader")
print("=" * 60)

def read_config(json_file):
    """Read config.json and display all settings."""
    
    with open(json_file, "r") as f:
        config = json.load(f)
    
    print(f"\n  === Configuration Settings ===")
    print(f"  Project:     {config['project']}")
    print(f"  Version:     {config['version']}")
    print(f"  Environment: {config['environment']}")
    print(f"  Base URL:    {config['base_url']}")
    print(f"  Browser:     {config['browser']}")
    print(f"  Headless:    {config['headless']}")
    print(f"  Timeout:     {config['timeout']}s")
    
    print(f"\n  === Credentials ===")
    for role, creds in config["credentials"].items():
        print(f"  {role.upper():10s} user: {creds['username']}")
    
    print(f"\n  === Test Suites ===")
    total_tests = 0
    for suite in config["test_suites"]:
        total_tests += suite["test_count"]
        print(f"    {suite['name']:15s} ({suite['priority']}): {suite['test_count']:3d} tests")
    print(f"    {'TOTAL':15s}       : {total_tests:3d} tests")
    
    return config

config = read_config(json_path)


# ============================================================
# PRACTICE TASK 3: Generate Test Execution Report (Write)
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE TASK 3: Generate Execution Report")
print("=" * 60)

def generate_report(csv_file, output_file):
    """Read CSV test data and generate a formatted text report."""
    
    # Read test data
    with open(csv_file, "r") as f:
        test_cases = list(csv.DictReader(f))
    
    # Calculate stats
    total = len(test_cases)
    passed = sum(1 for tc in test_cases if tc["Status"] == "Pass")
    failed = sum(1 for tc in test_cases if tc["Status"] == "Fail")
    not_run = sum(1 for tc in test_cases if tc["Status"] == "Not Run")
    pass_rate = (passed / total * 100) if total > 0 else 0
    
    # Write report
    with open(output_file, "w") as f:
        f.write("=" * 60 + "\n")
        f.write(f"{'TEST EXECUTION REPORT':^60}\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"Date:      {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total:     {total}\n")
        f.write(f"Passed:    {passed}\n")
        f.write(f"Failed:    {failed}\n")
        f.write(f"Not Run:   {not_run}\n")
        f.write(f"Pass Rate: {pass_rate:.1f}%\n")
        f.write("\n" + "-" * 60 + "\n\n")
        
        # Detailed results
        f.write(f"{'TC_ID':<10} {'Title':<35} {'Status':<10} {'Priority'}\n")
        f.write("-" * 60 + "\n")
        for tc in test_cases:
            f.write(f"{tc['TC_ID']:<10} {tc['Title']:<35} {tc['Status']:<10} {tc['Priority']}\n")
        
        f.write("\n" + "=" * 60 + "\n")
        f.write("Report generated by Python Automation Framework\n")
    
    print(f"  ✓ Report generated: {output_file}")
    print(f"  Stats: {total} total, {passed} pass, {failed} fail, {not_run} not run")
    print(f"  Pass Rate: {pass_rate:.1f}%")

report_path = os.path.join(script_dir, "execution_report.txt")
generate_report(csv_path, report_path)

# Show the generated report
print(f"\n  --- Generated Report Content ---")
with open(report_path, "r") as f:
    print(f.read())


# ============================================================
# PRACTICE TASK 4: Log Messages to File with Timestamps
# ============================================================

print("=" * 60)
print("PRACTICE TASK 4: File Logger")
print("=" * 60)

class FileLogger:
    """A simple file logger that writes timestamped messages."""
    
    LOG_LEVELS = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    
    def __init__(self, log_file, min_level="DEBUG"):
        self.log_file = log_file
        self.min_level = min_level
        # Create/clear the log file
        with open(self.log_file, "w") as f:
            f.write(f"{'='*60}\n")
            f.write(f"Log started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n\n")
    
    def _should_log(self, level):
        """Check if this level should be logged."""
        return self.LOG_LEVELS.get(level, 0) >= self.LOG_LEVELS.get(self.min_level, 0)
    
    def log(self, level, message):
        """Write a log entry to the file."""
        if not self._should_log(level):
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {level:<8} | {message}\n"
        with open(self.log_file, "a") as f:
            f.write(entry)
        print(f"  {entry.strip()}")
    
    def debug(self, message):
        self.log("DEBUG", message)
    
    def info(self, message):
        self.log("INFO", message)
    
    def warning(self, message):
        self.log("WARNING", message)
    
    def error(self, message):
        self.log("ERROR", message)
    
    def critical(self, message):
        self.log("CRITICAL", message)

# Usage
log_path = os.path.join(script_dir, "automation.log")
logger = FileLogger(log_path, min_level="INFO")

# Simulate a test execution
logger.info("Test suite started")
logger.info("Browser: Chrome v121.0")
logger.info("Environment: staging")
logger.debug("This won't appear (below INFO level)")  # Filtered out
logger.info("Navigating to login page...")
logger.info("Entering credentials...")
logger.warning("Login button took 5s to appear (slow)")
logger.info("Login successful!")
logger.info("Navigating to search page...")
logger.error("Search button not found — NoSuchElementException")
logger.critical("Test aborted due to critical failure!")
logger.info("Browser closed")
logger.info("Test suite completed")

# Show the log file
print(f"\n  --- Log File Content ---")
with open(log_path, "r") as f:
    print(f.read())

# --- Cleanup generated files ---
print("--- Cleaning up generated files ---")
cleanup_files = ["sample_output.txt", "test_results.txt", "test_log.txt", "results_copy.txt"]
for fname in cleanup_files:
    path = os.path.join(script_dir, fname)
    if os.path.exists(path):
        os.remove(path)
        print(f"  Removed: {fname}")
    else:
        # File might be in CWD if script was run from elsewhere
        if os.path.exists(fname):
            os.remove(fname)
            print(f"  Removed: {fname} (from CWD)")

print("\n--- Topic 12 Complete! ---")
