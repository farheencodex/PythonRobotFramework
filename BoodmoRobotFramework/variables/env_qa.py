# ============================================================
# QA Environment Variables (Python format)
# Used with: robot --variablefile variables/env_qa.py
# ============================================================

# ---------- QA URLs ----------
BASE_URL = "https://qa.boodmo.com"
API_BASE_URL = "https://qa.boodmo.com/api"
LOGIN_URL = f"{BASE_URL}/u/signin/"
SIGNUP_URL = f"{BASE_URL}/u/signup/"
CART_URL = f"{BASE_URL}/cart/"
CHECKOUT_URL = f"{BASE_URL}/checkout/"
PROFILE_URL = f"{BASE_URL}/u/profile/"
ORDERS_URL = f"{BASE_URL}/u/orders/"
CATALOG_URL = f"{BASE_URL}/catalog/"

# ---------- QA Credentials ----------
VALID_USERNAME = "qa_testuser@boodmo.com"
VALID_PASSWORD = "QAPass@123"
INVALID_PASSWORD = "WrongPass@000"
UNREGISTERED_EMAIL = "nonexistent_user_xyz@boodmo.com"

# ---------- QA API Config ----------
API_AUTH_TOKEN = "qa-bearer-token-placeholder"
API_SESSION_ALIAS = "boodmo_qa_session"

# ---------- Environment Identifier ----------
ENVIRONMENT = "QA"
