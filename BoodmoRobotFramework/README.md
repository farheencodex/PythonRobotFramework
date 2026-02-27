# Boodmo Robot Framework - Automation Suite

## Project Description

A complete **Python Robot Framework** automation suite for [Boodmo](https://boodmo.com) — India's leading auto parts e-commerce platform. This framework covers both **UI Automation** (using SeleniumLibrary) and **API Automation** (using RequestsLibrary) with environment-based execution, comprehensive tagging, and full test case traceability.

### Key Features
- **Environment-based execution** — Run against Staging, QA, or Production with a single flag
- **Tag-driven selective execution** — Run by type (ui/api), suite (smoke/regression), module (login/search/cart), or priority (P0/P1/P2)
- **Test case traceability** — Every automated test maps to Assignment 1 test case IDs via `mapping/testcase_mapping.csv`
- **Reusable keywords** — Separate keyword libraries for UI and API operations
- **Centralized locators** — All web element locators in a single resource file
- **Auto-generated reports** — HTML reports and logs per environment

---

## Project Structure

```
BoodmoRobotFramework/
│
├── tests/                              # All test suites
│   ├── ui/                             # UI test suites
│   │   ├── homepage_tests.robot        # TC_001-TC_010 (7 tests)
│   │   ├── login_tests.robot           # TC_013-TC_023 (9 tests)
│   │   ├── search_tests.robot          # TC_044-TC_077 (8 tests)
│   │   ├── cart_tests.robot            # TC_088-TC_100 (6 tests)
│   │   └── checkout_tests.robot        # TC_103-TC_112 (4 tests)
│   └── api/                            # API test suites
│       ├── search_api_tests.robot      # API_001, API_005, API_006 (6 tests)
│       ├── product_api_tests.robot     # API_002, API_006 (4 tests)
│       └── cart_api_tests.robot        # API_003, API_004, API_006 (6 tests)
│
├── resources/                          # Shared resources
│   ├── keywords/
│   │   ├── ui_keywords.robot           # Reusable UI keywords
│   │   └── api_keywords.robot          # Reusable API keywords
│   ├── locators/
│   │   └── locators.robot              # All web element locators
│   └── common.robot                    # Setup/teardown, wait utilities
│
├── variables/                          # Environment-specific variables
│   ├── env_common.robot                # Shared config (browser, timeout, test data)
│   ├── env_staging.py                  # Staging environment URLs & credentials
│   ├── env_qa.py                       # QA environment URLs & credentials
│   └── env_production.py               # Production environment URLs & credentials
│
├── mapping/                            # Test case traceability
│   └── testcase_mapping.csv            # TC_ID ↔ Robot file/test name mapping
│
├── results/                            # Auto-generated reports (gitignored)
│
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

---

## Prerequisites

- **Python** 3.8 or higher
- **pip** (Python package manager)
- **Google Chrome** browser (or update `${BROWSER}` variable)
- **ChromeDriver** (auto-managed by webdriver-manager)

---

## Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd BoodmoRobotFramework

# 2. Create virtual environment (recommended)
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify Robot Framework is installed
robot --version
```

---

## How to Run Tests

### Run Full Suite (by Environment)

```bash
# Run ALL tests on Staging
robot --variablefile variables/env_staging.py --outputdir results/staging tests/

# Run ALL tests on QA
robot --variablefile variables/env_qa.py --outputdir results/qa tests/

# Run ALL tests on Production
robot --variablefile variables/env_production.py --outputdir results/production tests/
```

### Run by Type (UI / API)

```bash
# Run only UI tests
robot --variablefile variables/env_staging.py --include ui --outputdir results/staging tests/

# Run only API tests
robot --variablefile variables/env_staging.py --include api --outputdir results/staging tests/
```

### Run by Suite (Smoke / Regression)

```bash
# Run only Smoke tests
robot --variablefile variables/env_staging.py --include smoke --outputdir results/staging tests/

# Run only Regression tests
robot --variablefile variables/env_staging.py --include regression --outputdir results/staging tests/
```

### Run by Module

```bash
# Run only Login tests
robot --variablefile variables/env_staging.py --include login --outputdir results/staging tests/

# Run only Search tests (UI + API)
robot --variablefile variables/env_staging.py --include search --outputdir results/staging tests/

# Run only Cart tests (UI + API)
robot --variablefile variables/env_staging.py --include cart --outputdir results/staging tests/
```

### Run by Priority

```bash
# Run only P0 (Critical) tests
robot --variablefile variables/env_staging.py --include P0 --outputdir results/staging tests/

# Run P0 + P1 tests, exclude P2
robot --variablefile variables/env_staging.py --exclude P2 --outputdir results/staging tests/
```

### Run by Specific Test Case ID

```bash
# Run specific test case by Assignment 1 TC_ID
robot --variablefile variables/env_staging.py --include TC_013 --outputdir results tests/

# Run specific API test case
robot --variablefile variables/env_staging.py --include API_001 --outputdir results tests/
```

### Combined Tag Execution

```bash
# Run Smoke + Login tests only
robot --variablefile variables/env_staging.py --include smokeANDlogin --outputdir results tests/

# Run P0 API tests only
robot --variablefile variables/env_staging.py --include P0ANDapi --outputdir results tests/

# Run Smoke UI tests, exclude checkout
robot --variablefile variables/env_staging.py --include smokeANDui --exclude checkout --outputdir results tests/
```

---

## Test Case Mapping

The file `mapping/testcase_mapping.csv` provides full traceability between Assignment 1 test cases and the Robot Framework implementation.

| Column | Description |
|--------|-------------|
| `TC_ID` | Test case ID from Assignment 1 (e.g., TC_001, API_001) |
| `Scenario_ID` | Test scenario ID from Assignment 1 (e.g., TS_001) |
| `Test_Case_Title` | Human-readable test case title |
| `Module` | Feature module (Homepage, Login, Search, Cart, etc.) |
| `Robot_File` | Relative path to the `.robot` test file |
| `Robot_Test_Name` | Exact test case name in the `.robot` file |
| `Type` | UI or API |
| `Tags` | All tags applied to the test case |

**Total Automated:**
- **34 UI test cases** across 5 modules (Homepage, Login, Search, Cart, Checkout)
- **16 API test cases** across 3 endpoints (Search, Product, Cart)
- **50 total automated test scenarios** mapped to Assignment 1

---

## Tagging Strategy

| Tag Category | Values | Usage |
|-------------|--------|-------|
| **Type** | `ui`, `api` | `--include ui` or `--include api` |
| **Suite** | `smoke`, `regression` | `--include smoke` |
| **Module** | `homepage`, `login`, `search`, `cart`, `checkout`, `product` | `--include login` |
| **Priority** | `P0`, `P1`, `P2` | `--include P0` |
| **TC ID** | `TC_001`, `TC_013`, `API_001`, etc. | `--include TC_013` |
| **Scenario ID** | `TS_001`, `TS_006`, etc. | `--include TS_006` |
| **Test Type** | `positive`, `negative`, `validation`, `security`, `functional` | `--include negative` |

---

## Environment Configuration

| Environment | Variable File | Base URL |
|------------|---------------|----------|
| Staging | `variables/env_staging.py` | https://staging.boodmo.com |
| QA | `variables/env_qa.py` | https://qa.boodmo.com |
| Production | `variables/env_production.py` | https://boodmo.com |

**No hardcoded URLs or credentials in test files.** Everything is driven by environment variable files via `--variablefile` flag.

---

## Reports

After execution, Robot Framework auto-generates:
- `report.html` — Summary report with pass/fail statistics
- `log.html` — Detailed execution log with screenshots
- `output.xml` — Machine-readable output for CI/CD integration

Reports are organized by environment:
```
results/
├── staging/
│   ├── report.html
│   ├── log.html
│   └── output.xml
├── qa/
└── production/
```

---

## Known Issues / Assumptions

1. **Locators** — CSS selectors are based on common patterns. Actual Boodmo selectors may differ and need to be updated using browser DevTools.
2. **API Endpoints** — API paths (`/search`, `/product/{id}`, `/cart/add`) are assumed based on typical e-commerce patterns. Capture actual endpoints from browser Network tab.
3. **Credentials** — Placeholder test credentials are used. Replace with actual test account credentials per environment.
4. **Product IDs** — Sample product IDs (12345) need to be replaced with actual Boodmo product IDs.
5. **WebDriver** — ChromeDriver is managed automatically via `webdriver-manager`. Ensure Chrome browser version is compatible.

---

## Author

Assignment for Python Robot Framework Implementation  
Target: Boodmo (https://boodmo.com)  
Date: February 2026
