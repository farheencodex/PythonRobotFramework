# ============================================================
# Production Environment Variables (Python format)
# Used with: robot --variablefile variables/env_production.py
# ============================================================

# ---------- Production URLs ----------
BASE_URL = "https://boodmo.com"
API_BASE_URL = "https://boodmo.com/api"
LOGIN_URL = f"{BASE_URL}/u/signin/"
SIGNUP_URL = f"{BASE_URL}/u/signup/"
CART_URL = f"{BASE_URL}/cart/"
CHECKOUT_URL = f"{BASE_URL}/checkout/"
PROFILE_URL = f"{BASE_URL}/u/profile/"
ORDERS_URL = f"{BASE_URL}/u/orders/"
CATALOG_URL = f"{BASE_URL}/catalog/"

# ---------- Production Credentials ----------
# NOTE: Use dedicated test account for production
VALID_USERNAME = "prod_testuser@boodmo.com"
VALID_PASSWORD = "ProdPass@123"
INVALID_PASSWORD = "WrongPass@000"
UNREGISTERED_EMAIL = "nonexistent_user_xyz@boodmo.com"

# ---------- Production API Config ----------
API_AUTH_TOKEN = "prod-bearer-token-placeholder"
API_SESSION_ALIAS = "boodmo_prod_session"

# ---------- Environment Identifier ----------
ENVIRONMENT = "PRODUCTION"
