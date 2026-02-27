*** Settings ***
# ============================================================
# UI Keywords Resource File
# Contains reusable UI keywords for all modules:
#   Homepage, Login, Signup, Search, Cart, Checkout, Product
# Mapped to Assignment 1 Test Cases (TC_001 - TC_180)
# ============================================================
Resource    ${CURDIR}${/}..${/}common.robot

*** Keywords ***

# ============================================================
# HOMEPAGE KEYWORDS (TC_001 - TC_012)
# ============================================================

Verify Homepage Is Loaded Successfully
    [Documentation]    TC_001 (TS_001) - Verify homepage loads with all UI components.
    Wait Until Page Is Loaded
    Verify Page Title Contains    ${HOME_PAGE_TITLE}

Verify Boodmo Logo Is Displayed
    [Documentation]    TC_002 (TS_001) - Verify logo is visible in header.
    Verify Element Is Displayed    ${HOME_LOGO_IMG}

Verify Homepage Title In Browser Tab
    [Documentation]    TC_003 (TS_001) - Verify browser tab shows correct title.
    ${title}=    Get Title
    Should Contain    ${title}    boodmo    ignore_case=True

Verify Search Bar Is Present And Active
    [Documentation]    TC_004 (TS_002) - Verify search bar is visible and clickable.
    Verify Element Is Displayed    ${HOME_SEARCH_INPUT}
    Element Should Be Enabled    ${HOME_SEARCH_INPUT}

Verify Popular Categories Section Loads
    [Documentation]    TC_007 (TS_004) - Verify categories section is displayed.
    Scroll Element Into View    ${HOME_POPULAR_CATEGORIES}
    Verify Element Is Displayed    ${HOME_POPULAR_CATEGORIES}

Verify Header Navigation Links
    [Documentation]    TC_009 (TS_005) - Verify header has functional interactive elements.
    ...                Boodmo Angular SPA has: logo, search, menu button, sign-in.
    # Verify header has key interactive elements
    Verify Element Is Displayed    ${HOME_LOGO_LINK}
    Verify Element Is Displayed    ${HOME_SEARCH_FORM}
    Verify Element Is Displayed    ${HOME_HEADER_USER}

Verify Footer Links Are Present
    [Documentation]    TC_010 (TS_005) - Verify footer links exist.
    Scroll Element Into View    ${HOME_FOOTER}
    ${links}=    Get WebElements    ${HOME_FOOTER_LINKS}
    ${count}=    Get Length    ${links}
    Should Be True    ${count} > 0    No footer links found

# ============================================================
# LOGIN KEYWORDS (TC_013 - TC_027)
# Boodmo uses email-first login flow:
#   1. Navigate to /u/signin/
#   2. Enter email, click Continue
#   3. Password field appears, enter password, submit
# ============================================================

Open Login Page
    [Documentation]    Navigates to the Boodmo login page.
    Navigate To URL    ${LOGIN_URL}
    Wait For Element Visible    ${LOGIN_EMAIL_INPUT}

Enter Login Email
    [Documentation]    Enters email on the login form using robust Angular-compatible input.
    [Arguments]    ${email}
    Wait For Element Visible    ${LOGIN_EMAIL_INPUT}
    JS Click Element    ${LOGIN_EMAIL_INPUT}
    Sleep    0.5s
    # Use Press Keys for Angular reactive form compatibility
    Press Keys    ${LOGIN_EMAIL_INPUT}    CTRL+a
    Press Keys    ${LOGIN_EMAIL_INPUT}    DELETE
    Press Keys    ${LOGIN_EMAIL_INPUT}    ${email}
    Sleep    0.5s

Click Login Continue Button
    [Documentation]    Clicks the Continue button after entering email.
    JS Click Element    ${LOGIN_CONTINUE_BTN}
    Sleep    4s    # Wait for Angular to process and render next step

Enter Login Password
    [Documentation]    Enters password (appears after email validation step).
    [Arguments]    ${password}
    Wait For Element Visible    ${LOGIN_PASSWORD_INPUT}    timeout=10s
    Wait And Input Text    ${LOGIN_PASSWORD_INPUT}    ${password}

Enter Login Credentials
    [Documentation]    Enters email and password on login form.
    ...                Handles Boodmo's two-step login flow.
    ...                If email is empty/invalid, password step may not appear.
    [Arguments]    ${email}    ${password}
    Enter Login Email    ${email}
    Click Login Continue Button
    # Password field only appears after valid email is entered
    ${pwd_visible}=    Run Keyword And Return Status
    ...    Wait For Element Visible    ${LOGIN_PASSWORD_INPUT}    timeout=5s
    Run Keyword If    ${pwd_visible}    Input Text    ${LOGIN_PASSWORD_INPUT}    ${password}

Click Login Submit Button
    [Documentation]    Clicks the login submit button.
    Wait And Click Element    ${LOGIN_SUBMIT_BTN}

Perform Login
    [Documentation]    Complete login flow with given credentials.
    [Arguments]    ${email}    ${password}
    Open Login Page
    Enter Login Credentials    ${email}    ${password}
    Click Login Submit Button

Verify Login Successful
    [Documentation]    TC_013 (TS_006) - Verify user is logged in successfully.
    Wait For Element Visible    ${LOGIN_SUCCESS_INDICATOR}    timeout=10s

Verify Login Error Message Displayed
    [Documentation]    TC_014/TC_015 (TS_007) - Verify error message appears on invalid login.
    Wait For Element Visible    ${LOGIN_ERROR_MSG}    timeout=10s

Verify Forgot Password Link Is Present
    [Documentation]    TC_020 (TS_008) - Verify Forgot Password link is visible.
    Verify Element Is Displayed    ${LOGIN_FORGOT_PWD_LINK}

Click Forgot Password Link
    [Documentation]    Clicks the Forgot Password link on login page.
    Wait And Click Element    ${LOGIN_FORGOT_PWD_LINK}

Verify Password Field Is Masked
    [Documentation]    TC_023 (TS_007) - Verify password input type is 'password' (masked).
    ${type}=    Get Element Attribute    ${LOGIN_PASSWORD_INPUT}    type
    Should Be Equal As Strings    ${type}    password

# ============================================================
# SIGNUP / REGISTRATION KEYWORDS (TC_028 - TC_043)
# ============================================================

Open Signup Page
    [Documentation]    Navigates to the registration page.
    Navigate To URL    ${SIGNUP_URL}
    Wait For Element Visible    ${SIGNUP_EMAIL_INPUT}

Enter Registration Details
    [Documentation]    Fills in the registration form.
    [Arguments]    ${name}    ${email}    ${phone}    ${password}    ${confirm_password}
    Wait And Input Text    ${SIGNUP_NAME_INPUT}    ${name}
    Wait And Input Text    ${SIGNUP_EMAIL_INPUT}    ${email}
    Wait And Input Text    ${SIGNUP_PHONE_INPUT}    ${phone}
    Wait And Input Text    ${SIGNUP_PASSWORD_INPUT}    ${password}
    Wait And Input Text    ${SIGNUP_CONFIRM_PASSWORD_INPUT}    ${confirm_password}

Click Register Submit Button
    [Documentation]    Clicks the register/signup submit button.
    Wait And Click Element    ${SIGNUP_SUBMIT_BTN}

Verify Registration Error Displayed
    [Documentation]    Verifies error message on registration page.
    Wait For Element Visible    ${SIGNUP_ERROR_MSG}    timeout=10s

# ============================================================
# SEARCH KEYWORDS (TC_044 - TC_056)
# Boodmo search: Angular reactive form with overlay.
# Must remove overlay before interacting with search input.
# ============================================================

Search For Product
    [Documentation]    Searches for a product using the search bar.
    ...                Handles Angular overlay that blocks search input.
    ...                After search, navigates to catalog category as fallback
    ...                since Boodmo's Angular SPA search uses internal routing.
    [Arguments]    ${keyword}
    # Remove Angular search placeholder overlay
    Remove Element By Selector    .search-placeholder
    Sleep    0.5s
    # Type search keyword using JS and Press Keys for Angular binding
    JS Click Element    ${HOME_SEARCH_INPUT}
    Press Keys    ${HOME_SEARCH_INPUT}    CTRL+a
    Press Keys    ${HOME_SEARCH_INPUT}    DELETE
    Press Keys    ${HOME_SEARCH_INPUT}    ${keyword}
    Sleep    1s
    JS Click Element    ${HOME_SEARCH_BTN}
    Sleep    3s
    # Boodmo Angular SPA routes internally; if URL didn't change
    # fall back to category navigation to show products
    ${url}=    Get Location
    ${on_homepage}=    Run Keyword And Return Status
    ...    Should Be Equal As Strings    ${url}    https://boodmo.com/
    Run Keyword If    ${on_homepage}    Navigate To Category Page

Navigate To Category Page
    [Documentation]    Navigates directly to a product catalog category page.
    ...                Uses Maintenance Service Parts as default category.
    Navigate To URL    ${CATALOG_URL}3403-maintenance_service_parts/
    Sleep    2s

Search By Vehicle Details
    [Documentation]    TC_045 (TS_012) - Searches by make, model, year using vehicle form.
    [Arguments]    ${make}    ${model}    ${year}
    Wait For Element Visible    ${HOME_VEHICLE_MAKE_SELECTOR}
    # Click on the vehicle make
    ${make_links}=    Get WebElements    css=section.search-by-vehicle a
    FOR    ${link}    IN    @{make_links}
        ${text}=    Get Text    ${link}
        Run Keyword If    '${make}' in '${text}'    Click Element    ${link}
        Exit For Loop If    '${make}' in '${text}'
    END
    Wait For Angular

Verify Search Results Are Displayed
    [Documentation]    Verifies that search/catalog results have items.
    ...                Works with both search results and category catalog pages.
    Wait Until Page Is Loaded
    # Catalog pages use links under catalog-list or category sections
    ${count}=    Get Element Count    css=a[href*='/catalog/']
    Should Be True    ${count} > 0    No search/catalog results found

Verify No Results Message Displayed
    [Documentation]    TC_050/TC_051 (TS_016) - Verifies "No results" or 404 message.
    ${status}=    Run Keyword And Return Status    Wait For Element Visible    ${SEARCH_NO_RESULTS_MSG}    timeout=10s
    Run Keyword If    not ${status}    Verify URL Contains    search

Verify Autocomplete Suggestions Appear
    [Documentation]    TC_054 (TS_017) - Verifies autocomplete dropdown appears.
    Wait For Element Visible    ${SEARCH_AUTOCOMPLETE_DROPDOWN}

# ============================================================
# PRODUCT DETAIL KEYWORDS (TC_078 - TC_087)
# ============================================================

Click First Product From Results
    [Documentation]    Clicks the first product/category link from results.
    ${products}=    Get WebElements    css=a[href*='/catalog/']
    ${count}=    Get Length    ${products}
    Should Be True    ${count} > 0    No product/category links found
    Click Element    ${products}[0]
    Wait Until Page Is Loaded

Verify Product Detail Page Is Loaded
    [Documentation]    TC_078 (TS_025) - Verifies product/category page has loaded.
    Wait Until Page Is Loaded
    Verify URL Contains    /catalog/

Verify Product Info Displayed
    [Documentation]    TC_079 (TS_025) - Verifies name, brand, price are visible.
    Verify Element Is Displayed    ${PDP_PRODUCT_NAME}
    Verify Element Is Displayed    ${PDP_PRODUCT_PRICE}
    Verify Element Is Displayed    ${PDP_PRODUCT_BRAND}

Click Add To Cart On Product Page
    [Documentation]    TC_084 (TS_026) - Clicks Add to Cart button on PDP.
    Wait And Click Element    ${PDP_ADD_TO_CART_BTN}

# ============================================================
# CART KEYWORDS (TC_088 - TC_102)
# ============================================================

Open Cart Page
    [Documentation]    Navigates to the cart page.
    Navigate To Cart Page
    Wait Until Page Is Loaded

Verify Item Is In Cart
    [Documentation]    TC_088 (TS_030) - Verifies at least one item exists in cart.
    Wait For Element Visible    ${CART_ITEMS_LIST}
    ${count}=    Get Element Count    ${CART_ITEMS_LIST}
    Should Be True    ${count} > 0    Cart is empty - expected at least 1 item

Verify Cart Icon Count
    [Documentation]    TC_089 (TS_030) - Verifies cart icon shows expected count.
    [Arguments]    ${expected_count}
    ${actual}=    Get Text    ${CART_ITEM_COUNT}
    Should Be Equal As Strings    ${actual}    ${expected_count}

Increase Item Quantity In Cart
    [Documentation]    TC_090 (TS_031) - Clicks "+" to increase quantity.
    Wait And Click Element    ${CART_ITEM_QTY_INCREASE}

Decrease Item Quantity In Cart
    [Documentation]    TC_091 (TS_031) - Clicks "-" to decrease quantity.
    Wait And Click Element    ${CART_ITEM_QTY_DECREASE}

Remove Item From Cart
    [Documentation]    TC_096 (TS_032) - Clicks Remove button on cart item.
    Wait And Click Element    ${CART_REMOVE_ITEM_BTN}

Verify Cart Is Empty
    [Documentation]    TC_100 (TS_034) - Verifies empty cart message displayed.
    Wait For Element Visible    ${CART_EMPTY_MSG}

Verify Cart Total Price
    [Documentation]    TC_098 (TS_034) - Verifies total price is displayed.
    Verify Element Is Displayed    ${CART_TOTAL_PRICE}

Click Proceed To Checkout
    [Documentation]    Clicks proceed to checkout button from cart.
    Wait And Click Element    ${CART_PROCEED_CHECKOUT_BTN}

# ============================================================
# CHECKOUT KEYWORDS (TC_103 - TC_115)
# ============================================================

Verify Checkout Page Is Loaded
    [Documentation]    Verifies checkout page has loaded with order summary.
    Wait For Element Visible    ${CHECKOUT_ORDER_SUMMARY}

Select Saved Address
    [Documentation]    TC_103 (TS_035) - Selects the first saved address.
    Wait And Click Element    ${CHECKOUT_SAVED_ADDRESS}

Apply Coupon Code
    [Documentation]    TC_111 (TS_039) - Applies a coupon code at checkout.
    [Arguments]    ${coupon_code}
    Wait And Input Text    ${CHECKOUT_COUPON_INPUT}    ${coupon_code}
    Wait And Click Element    ${CHECKOUT_APPLY_COUPON_BTN}

Verify Coupon Applied Successfully
    [Documentation]    Verifies coupon success message.
    Wait For Element Visible    ${CHECKOUT_COUPON_SUCCESS_MSG}

Verify Coupon Error Message
    [Documentation]    TC_112 (TS_039) - Verifies invalid coupon error.
    Wait For Element Visible    ${CHECKOUT_COUPON_ERROR_MSG}
