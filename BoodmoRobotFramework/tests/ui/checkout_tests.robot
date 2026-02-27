*** Settings ***
# ============================================================
# Checkout UI Test Suite
# Module: CHECKOUT
# Assignment 1 Test Cases: TC_103, TC_110, TC_111, TC_112
# Test Scenarios: TS_035, TS_038, TS_039
# ============================================================
Documentation     Checkout Module UI Tests for Boodmo
...               Validates checkout with saved address,
...               order summary, coupon code functionality.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}ui_keywords.robot

Suite Setup       Open Browser To Boodmo
Suite Teardown    Close Browser Session
Test Setup        Start Test
Test Teardown     End Test

Force Tags        ui    checkout
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# TC_103 | TS_035 | Verify checkout with saved address
# ----------------------------------------------------------
Verify Checkout With Saved Address
    [Documentation]    TC_103 (TS_035): Add to cart > Proceed to checkout >
    ...                Select saved address > Click Continue.
    ...                Address confirmed; user proceeds to payment step.
    [Tags]    TC_103    TS_035    smoke    P0    positive
    # Pre-condition: Login and add item to cart
    Perform Login    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Click Proceed To Checkout
    Verify Checkout Page Is Loaded
    Select Saved Address
    Take Screenshot With Name    TC_103_checkout_saved_address

# ----------------------------------------------------------
# TC_110 | TS_038 | Verify order summary at checkout
# ----------------------------------------------------------
Verify Order Summary Is Accurate At Checkout
    [Documentation]    TC_110 (TS_038): Add items to cart > Proceed to checkout.
    ...                Order summary shows items, quantities, prices, taxes, total.
    [Tags]    TC_110    TS_038    smoke    P0    functional
    Perform Login    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Click Proceed To Checkout
    Verify Checkout Page Is Loaded
    Take Screenshot With Name    TC_110_order_summary

# ----------------------------------------------------------
# TC_111 | TS_039 | Verify valid coupon code application
# ----------------------------------------------------------
Verify Valid Coupon Code Is Applied Successfully
    [Documentation]    TC_111 (TS_039): Enter valid coupon code at checkout >
    ...                Click Apply. Discount applied; updated total shown.
    [Tags]    TC_111    TS_039    regression    P0    positive
    Perform Login    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Click Proceed To Checkout
    Verify Checkout Page Is Loaded
    Apply Coupon Code    TESTCOUPON10
    Verify Coupon Applied Successfully
    Take Screenshot With Name    TC_111_coupon_applied

# ----------------------------------------------------------
# TC_112 | TS_039 | Verify invalid coupon code
# ----------------------------------------------------------
Verify Invalid Coupon Code Shows Error
    [Documentation]    TC_112 (TS_039): Enter "INVALIDCODE" > Click Apply.
    ...                Error: "Invalid or expired coupon code".
    [Tags]    TC_112    TS_039    regression    P1    negative
    Perform Login    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Click Proceed To Checkout
    Verify Checkout Page Is Loaded
    Apply Coupon Code    INVALIDCODE
    Verify Coupon Error Message
    Take Screenshot With Name    TC_112_invalid_coupon
