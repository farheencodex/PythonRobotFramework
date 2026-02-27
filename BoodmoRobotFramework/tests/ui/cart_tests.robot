*** Settings ***
# ============================================================
# Cart UI Test Suite
# Module: CART
# Assignment 1 Test Cases: TC_088, TC_090, TC_091, TC_096,
#                          TC_098, TC_100
# Test Scenarios: TS_030, TS_031, TS_032, TS_034
# ============================================================
Documentation     Cart Module UI Tests for Boodmo
...               Validates add to cart, quantity change,
...               item removal, price calculation, empty cart.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}ui_keywords.robot

Suite Setup       Open Browser To Boodmo
Suite Teardown    Close Browser Session
Test Setup        Start Test
Test Teardown     End Test

Force Tags        ui    cart
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# TC_088 | TS_030 | Verify item added to cart
# ----------------------------------------------------------
Verify Item Is Added To Cart Successfully
    [Documentation]    TC_088 (TS_030): Add a product from product detail >
    ...                Click Cart icon. Cart opens with the added item.
    [Tags]    TC_088    TS_030    smoke    P0    positive
    # Step 1: Search and go to a product
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Verify Product Detail Page Is Loaded
    # Step 2: Add to cart
    Click Add To Cart On Product Page
    # Step 3: Verify in cart
    Open Cart Page
    Verify Item Is In Cart
    Take Screenshot With Name    TC_088_item_added_to_cart

# ----------------------------------------------------------
# TC_090 | TS_031 | Verify quantity increase in cart
# ----------------------------------------------------------
Verify Quantity Increase In Cart Updates Price
    [Documentation]    TC_090 (TS_031): Open cart > Click "+" on any item.
    ...                Quantity increases by 1; price updates accordingly.
    [Tags]    TC_090    TS_031    smoke    P0    positive
    # Pre-condition: Add item to cart first
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Verify Item Is In Cart
    # Increase quantity
    Increase Item Quantity In Cart
    Verify Cart Total Price
    Take Screenshot With Name    TC_090_qty_increase

# ----------------------------------------------------------
# TC_091 | TS_031 | Verify quantity decrease in cart
# ----------------------------------------------------------
Verify Quantity Decrease In Cart Updates Price
    [Documentation]    TC_091 (TS_031): Open cart > Click "–" on any item.
    ...                Quantity decreases by 1; price updates.
    [Tags]    TC_091    TS_031    smoke    P0    positive
    # Pre-condition: Item in cart with qty > 1
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Increase Item Quantity In Cart
    # Now decrease
    Decrease Item Quantity In Cart
    Verify Cart Total Price
    Take Screenshot With Name    TC_091_qty_decrease

# ----------------------------------------------------------
# TC_096 | TS_032 | Verify item removal from cart
# ----------------------------------------------------------
Verify Item Removal From Cart
    [Documentation]    TC_096 (TS_032): Open cart > Click "Remove" on an item.
    ...                Item is removed; cart updates.
    [Tags]    TC_096    TS_032    smoke    P0    positive
    # Pre-condition: Add item first
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Verify Item Is In Cart
    # Remove item
    Remove Item From Cart
    Take Screenshot With Name    TC_096_item_removed

# ----------------------------------------------------------
# TC_098 | TS_034 | Verify price calculation in cart
# ----------------------------------------------------------
Verify Cart Shows Correct Price Calculation
    [Documentation]    TC_098 (TS_034): Add items to cart > Open cart.
    ...                Total price displayed correctly.
    [Tags]    TC_098    TS_034    regression    P0    functional
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Click Add To Cart On Product Page
    Open Cart Page
    Verify Cart Total Price
    Take Screenshot With Name    TC_098_price_calculation

# ----------------------------------------------------------
# TC_100 | TS_034 | Verify "Empty Cart" state
# ----------------------------------------------------------
Verify Empty Cart State Shows Message
    [Documentation]    TC_100 (TS_034): Remove all items from cart.
    ...                Empty cart message shown: "Your cart is empty."
    [Tags]    TC_100    TS_034    regression    P2    negative
    Open Cart Page
    Verify Cart Is Empty
    Take Screenshot With Name    TC_100_empty_cart
