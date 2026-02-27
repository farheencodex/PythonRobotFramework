# ============================================================
# Staging Environment Variables (Python format)
# Used with: robot --variablefile variables/env_staging.py
# ============================================================

# ---------- Staging URLs ----------
BASE_URL = "https://staging.boodmo.com"
API_BASE_URL = "https://staging.boodmo.com/api"
LOGIN_URL = f"{BASE_URL}/u/signin/"
SIGNUP_URL = f"{BASE_URL}/u/signup/"
CART_URL = f"{BASE_URL}/cart/"
CHECKOUT_URL = f"{BASE_URL}/checkout/"
PROFILE_URL = f"{BASE_URL}/u/profile/"
ORDERS_URL = f"{BASE_URL}/u/orders/"
CATALOG_URL = f"{BASE_URL}/catalog/"

# ---------- Staging Credentials ----------
VALID_USERNAME = "staging_testuser@boodmo.com"
VALID_PASSWORD = "StagingPass@123"
INVALID_PASSWORD = "WrongPass@000"
UNREGISTERED_EMAIL = "nonexistent_user_xyz@boodmo.com"

# ---------- Staging API Config ----------
API_AUTH_TOKEN = "staging-bearer-token-placeholder"
API_SESSION_ALIAS = "boodmo_staging_session"

# ---------- Environment Identifier ----------
ENVIRONMENT = "STAGING"
