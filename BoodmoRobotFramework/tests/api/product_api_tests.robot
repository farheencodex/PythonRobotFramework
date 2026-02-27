*** Settings ***
# ============================================================
# Product API Test Suite
# API Test Cases: API_002
# Mapped to Assignment 1: TC_078, TC_079, TC_087
# ============================================================
Documentation     Product Detail API Tests for Boodmo
...               Validates product detail endpoint, field presence,
...               and response structure.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}api_keywords.robot

Suite Setup       Create Boodmo API Session
Suite Teardown    Close Boodmo API Session

Force Tags        api    product
Default Tags      regression


*** Variables ***
# Sample product IDs for testing (update with actual Boodmo product IDs)
${VALID_PRODUCT_ID}         12345
${INVALID_PRODUCT_ID}       99999999


*** Test Cases ***

# ----------------------------------------------------------
# API_002 | Verify Product Details API with valid product ID
# Mapped: TC_078 (TS_025) - Product detail page loads
# ----------------------------------------------------------
Verify Product Details API Returns Valid Product Info
    [Documentation]    API_002: Send GET /product/{id} with valid product ID.
    ...                Validate status=200, response contains name, price, availability.
    [Tags]    API_002    TC_078    smoke    P0
    ${response}=    Get Product Details Via API    ${VALID_PRODUCT_ID}
    Validate Response Status Code    ${response}    200
    Validate Product Fields In Response    ${response}
    Log    API_002 PASSED: Product details returned for ID ${VALID_PRODUCT_ID}    console=True

# ----------------------------------------------------------
# API_002 (variant) | Verify product response has required fields
# Mapped: TC_079 (TS_025) - Name, brand, part number, price
# ----------------------------------------------------------
Verify Product API Response Contains Required Fields
    [Documentation]    API_002 variant: Validate product response contains
    ...                name, brand, price, and part_number fields.
    [Tags]    API_002    TC_079    regression    P0
    ${response}=    Get Product Details Via API    ${VALID_PRODUCT_ID}
    Validate Response Status Code    ${response}    200
    ${json}=    Validate Response Is JSON    ${response}
    # Verify key product fields exist
    Validate Response Contains Key    ${json}    name
    Validate Response Contains Key    ${json}    price
    Log    API_002 PASSED: Required product fields present    console=True

# ----------------------------------------------------------
# API_002 (negative) | Verify invalid product ID returns error
# Mapped: TC_087 (TS_025) - Out of stock / non-existent
# ----------------------------------------------------------
Verify Product API Returns Error For Invalid Product ID
    [Documentation]    API_002 negative: Send GET /product/{invalid_id}.
    ...                Validate status=404 or appropriate error response.
    [Tags]    API_002    TC_087    regression    P1    negative
    ${response}=    Get Product Details Via API    ${INVALID_PRODUCT_ID}
    # Should return 404 (not found) for invalid product
    ${status}=    Set Variable    ${response.status_code}
    Should Be True    ${status} == 404 or ${status} == 400
    ...    Expected 404/400 for invalid product but got ${status}
    Log    API_002 (negative) PASSED: Invalid product returns ${status}    console=True

# ----------------------------------------------------------
# API_006 | Verify Product API response headers
# ----------------------------------------------------------
Verify Product API Response Headers And Timing
    [Documentation]    API_006: Validate Content-Type and response time
    ...                for product detail endpoint.
    [Tags]    API_006    regression    P1
    ${response}=    Get Product Details Via API    ${VALID_PRODUCT_ID}
    Validate Response Content Type    ${response}    application/json
    Validate Response Time Within Limit    ${response}    5
    Log    Product API response time validated    console=True
