*** Settings ***
# ============================================================
# Common Environment Variables
# Shared across all environments (staging, qa, production)
# These values remain constant regardless of environment
# ============================================================
# Usage: Included via --variablefile or Resource import
# ============================================================

*** Variables ***
# ---------- Browser Configuration ----------
${BROWSER}                  chrome
${IMPLICIT_WAIT}            10s
${TIMEOUT}                  15s
${SELENIUM_SPEED}           0.2s
${DOWNLOAD_DIR}             ${CURDIR}${/}..${/}..${/}results${/}downloads

# ---------- Retry Configuration ----------
${RETRY_COUNT}              3x
${RETRY_INTERVAL}           2s

# ---------- API Configuration ----------
${API_TIMEOUT}              30
${API_RETRY}                3
${CONTENT_TYPE_JSON}        application/json
${CONTENT_TYPE_FORM}        application/x-www-form-urlencoded

# ---------- Test Data: Search Keywords ----------
${SEARCH_KEYWORD_VALID}         brake pad
${SEARCH_KEYWORD_OEM}           8616047000
${SEARCH_KEYWORD_EMPTY}         ${EMPTY}
${SEARCH_KEYWORD_SPECIAL}       @@##$%
${SEARCH_KEYWORD_NO_RESULT}     xyznonexistentpart123

# ---------- Test Data: Login Test Email ----------
# Email known to trigger "registered" flow on Boodmo login
${REGISTERED_TEST_EMAIL}        test@example.com

# ---------- Test Data: Vehicle Search ----------
${VEHICLE_MAKE}             Maruti
${VEHICLE_MODEL}            Swift
${VEHICLE_YEAR}             2020

# ---------- Screenshot Configuration ----------
${SCREENSHOT_DIR}           ${CURDIR}${/}..${/}..${/}results${/}screenshots
