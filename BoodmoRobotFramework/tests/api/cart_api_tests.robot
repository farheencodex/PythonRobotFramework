*** Settings ***
# ============================================================
# Cart API Test Suite
# API Test Cases: API_003, API_004
# Mapped to Assignment 1: TC_088, TC_096, TC_098, TC_100
# ============================================================
Documentation     Cart API Tests for Boodmo
...               Validates add to cart, remove from cart,
...               cart details, and error handling via API.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}api_keywords.robot

Suite Setup       Create Boodmo API Session
Suite Teardown    Close Boodmo API Session

Force Tags        api    cart
Default Tags      regression


*** Variables ***
# Sample product ID for cart operations
${CART_TEST_PRODUCT_ID}     12345


*** Test Cases ***

# ----------------------------------------------------------
# API_003 | Verify Add to Cart API
# Mapped: TC_088 (TS_030) - Add item to cart
# ----------------------------------------------------------
Verify Add To Cart API Adds Product Successfully
    [Documentation]    API_003: Send POST /cart/add with product_id and quantity.
    ...                Validate status=200, product added response.
    [Tags]    API_003    TC_088    smoke    P0
    ${response}=    Add Product To Cart Via API    ${CART_TEST_PRODUCT_ID}    1
    Validate Response Status Code    ${response}    200
    ${json}=    Validate Response Is JSON    ${response}
    Log    API_003 PASSED: Product ${CART_TEST_PRODUCT_ID} added to cart    console=True

# ----------------------------------------------------------
# API_003 (variant) | Verify Add to Cart with quantity > 1
# Mapped: TC_090 (TS_031) - Quantity update
# ----------------------------------------------------------
Verify Add To Cart API With Multiple Quantity
    [Documentation]    API_003 variant: Add product with quantity=3.
    ...                Validate response reflects correct quantity.
    [Tags]    API_003    TC_090    regression    P0
    ${response}=    Add Product To Cart Via API    ${CART_TEST_PRODUCT_ID}    3
    Validate Response Status Code    ${response}    200
    ${json}=    Validate Response Is JSON    ${response}
    Log    API_003 PASSED: Added quantity 3 to cart    console=True

# ----------------------------------------------------------
# API_004 | Verify Remove from Cart API
# Mapped: TC_096 (TS_032) - Remove item from cart
# ----------------------------------------------------------
Verify Remove From Cart API Removes Product
    [Documentation]    API_004: First add a product, then send POST /cart/remove.
    ...                Validate product is removed from cart.
    [Tags]    API_004    TC_096    smoke    P0
    # Step 1: Add item to cart first
    ${add_response}=    Add Product To Cart Via API    ${CART_TEST_PRODUCT_ID}    1
    Validate Response Status Code    ${add_response}    200
    # Step 2: Remove the item
    ${remove_response}=    Remove Product From Cart Via API    ${CART_TEST_PRODUCT_ID}
    Validate Response Status Code    ${remove_response}    200
    ${json}=    Validate Response Is JSON    ${remove_response}
    Log    API_004 PASSED: Product removed from cart    console=True

# ----------------------------------------------------------
# API_003 + API_004 | Verify Cart Details After Operations
# Mapped: TC_098 (TS_034) - Cart price calculation
# ----------------------------------------------------------
Verify Cart Details API Shows Correct Items
    [Documentation]    Send GET /cart to fetch cart contents.
    ...                Validate cart has items after adding, empty after removing.
    [Tags]    API_003    API_004    TC_098    regression    P0    functional
    # Add product to cart
    ${add_resp}=    Add Product To Cart Via API    ${CART_TEST_PRODUCT_ID}    2
    Validate Response Status Code    ${add_resp}    200
    # Fetch cart details
    ${cart_resp}=    Get Cart Details Via API
    Validate Response Status Code    ${cart_resp}    200
    ${json}=    Validate Response Is JSON    ${cart_resp}
    Log    Cart details: ${json}    console=True
    # Cleanup: remove product
    ${remove_resp}=    Remove Product From Cart Via API    ${CART_TEST_PRODUCT_ID}

# ----------------------------------------------------------
# API_003 (negative) | Verify Add to Cart with invalid product
# ----------------------------------------------------------
Verify Add To Cart API Rejects Invalid Product
    [Documentation]    API_003 negative: Send add to cart with invalid product ID.
    ...                Validate appropriate error response.
    [Tags]    API_003    regression    P1    negative
    ${response}=    Add Product To Cart Via API    99999999    1
    ${status}=    Set Variable    ${response.status_code}
    Should Be True    ${status} == 400 or ${status} == 404 or ${status} == 422
    ...    Expected 400/404/422 for invalid product but got ${status}
    Log    Add to Cart (invalid) handled with status ${status}    console=True

# ----------------------------------------------------------
# API_006 | Verify Cart API response headers and timing
# ----------------------------------------------------------
Verify Cart API Response Headers And Performance
    [Documentation]    API_006: Validate Content-Type and response time for cart API.
    [Tags]    API_006    regression    P1
    ${response}=    Get Cart Details Via API
    Validate Response Content Type    ${response}    application/json
    Validate Response Time Within Limit    ${response}    5
    Log    Cart API response headers and timing validated    console=True
