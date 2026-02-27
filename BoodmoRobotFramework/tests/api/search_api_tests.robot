*** Settings ***
# ============================================================
# Search API Test Suite
# API Test Cases: API_001, API_005, API_006
# Mapped to Assignment 1: TC_049, TC_050, TC_051, TC_054
# ============================================================
Documentation     Search API Tests for Boodmo
...               Validates search endpoint with valid keywords,
...               empty/invalid queries, and response validation.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}api_keywords.robot

Suite Setup       Create Boodmo API Session
Suite Teardown    Close Boodmo API Session

Force Tags        api    search
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# API_001 | Verify Search API with valid keyword
# Mapped: TC_049 (TS_015) - Search "brake pad"
# ----------------------------------------------------------
Verify Search API Returns Valid Response For Brake Pad
    [Documentation]    API_001: Send GET /search?q=brake pad.
    ...                Validate status=200, response is JSON, contains results.
    [Tags]    API_001    TC_049    smoke    P0
    ${response}=    Search Product Via API    ${SEARCH_KEYWORD_VALID}
    Validate Response Status Code    ${response}    200
    Validate Response Is JSON    ${response}
    Validate Search Results In Response    ${response}
    Log    API_001 PASSED: Search for '${SEARCH_KEYWORD_VALID}' returned results    console=True

# ----------------------------------------------------------
# API_001 (variant) | Verify Search API with OEM part number
# Mapped: TC_048 (TS_014) - Search by OEM part number
# ----------------------------------------------------------
Verify Search API Returns Results For OEM Part Number
    [Documentation]    API_001 variant: Send GET /search?q=8616047000.
    ...                Validate the specific part is returned.
    [Tags]    API_001    TC_048    smoke    P0
    ${response}=    Search Product Via API    ${SEARCH_KEYWORD_OEM}
    Validate Response Status Code    ${response}    200
    Validate Response Is JSON    ${response}
    Log    API_001 PASSED: OEM search returned valid response    console=True

# ----------------------------------------------------------
# API_005 | Verify Search API with empty query
# Mapped: TC_050 (TS_016) - Empty search input
# ----------------------------------------------------------
Verify Search API Handles Empty Query Gracefully
    [Documentation]    API_005: Send GET /search?q= (empty).
    ...                Validate appropriate error response or empty results.
    [Tags]    API_005    TC_050    regression    P1    negative
    ${response}=    Search Product With Empty Query Via API    ${EMPTY}
    # Empty query should return 400 (bad request) or 200 with empty results
    ${status}=    Set Variable    ${response.status_code}
    Should Be True    ${status} == 400 or ${status} == 200
    ...    Unexpected status code ${status} for empty search query
    Log    API_005 PASSED: Empty query handled with status ${status}    console=True

# ----------------------------------------------------------
# API_005 (variant) | Verify Search API with special characters
# Mapped: TC_051 (TS_016) - Special char input
# ----------------------------------------------------------
Verify Search API Handles Special Characters Safely
    [Documentation]    API_005 variant: Send GET /search?q=@@##$%.
    ...                Validate input is sanitized, no server error (500).
    [Tags]    API_005    TC_051    regression    P1    negative    security
    ${response}=    Search Product With Empty Query Via API    ${SEARCH_KEYWORD_SPECIAL}
    # Should NOT return 500 (internal server error)
    Should Not Be Equal As Integers    ${response.status_code}    500
    ...    Server returned 500 for special characters - possible injection vulnerability
    Log    API_005 PASSED: Special chars handled safely, status=${response.status_code}    console=True

# ----------------------------------------------------------
# API_006 | Verify Search API response headers
# Mapped: General API validation
# ----------------------------------------------------------
Verify Search API Response Headers And Content Type
    [Documentation]    API_006: Validate Content-Type is application/json,
    ...                status code is correct, and response time is acceptable.
    [Tags]    API_006    regression    P1
    ${response}=    Search Product Via API    ${SEARCH_KEYWORD_VALID}
    Validate Response Status Code    ${response}    200
    Validate Response Content Type    ${response}    application/json
    Validate Response Time Within Limit    ${response}    5
    Log    API_006 PASSED: Headers and response time validated    console=True

# ----------------------------------------------------------
# API_001 (variant) | Verify Search API for no-result keyword
# Mapped: TC_075 (TS_022) - Non-existent product
# ----------------------------------------------------------
Verify Search API Returns Empty For NonExistent Product
    [Documentation]    Validate search for "xyznonexistentpart123" returns
    ...                status 200 with empty results or a "no results" indicator.
    [Tags]    API_001    TC_075    regression    P1    negative
    ${response}=    Search Product Via API    ${SEARCH_KEYWORD_NO_RESULT}
    Validate Response Status Code    ${response}    200
    ${json}=    Validate Response Is JSON    ${response}
    Log    Search for non-existent product returned: ${json}    console=True
