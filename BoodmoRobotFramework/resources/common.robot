*** Settings ***
# ============================================================
# Common Resource File
# Contains shared setup/teardown keywords, browser management,
# and utility keywords used across all test suites
# ============================================================
Library           SeleniumLibrary
Library           Collections
Library           String
Library           OperatingSystem
Library           DateTime
Resource          ${CURDIR}${/}locators${/}locators.robot
Resource          ${CURDIR}${/}..${/}variables${/}env_common.robot

*** Keywords ***

# ============================================================
# SUITE SETUP & TEARDOWN
# ============================================================

Open Browser To Boodmo
    [Documentation]    Opens browser and navigates to Boodmo base URL.
    ...                Used as Suite Setup for UI test suites.
    Log    Environment: ${ENVIRONMENT}    console=True
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${SELENIUM_SPEED}
    Set Selenium Implicit Wait    ${IMPLICIT_WAIT}
    Set Selenium Timeout    ${TIMEOUT}

Close Browser Session
    [Documentation]    Closes all browser windows. Used as Suite Teardown.
    Run Keyword And Ignore Error    Capture Page Screenshot    ${SCREENSHOT_DIR}${/}final_state_{index}.png
    Close All Browsers

# ============================================================
# TEST SETUP & TEARDOWN
# ============================================================

Start Test
    [Documentation]    Navigates to base URL before each test.
    Go To    ${BASE_URL}
    Wait Until Page Is Loaded

End Test
    [Documentation]    Captures screenshot after each test (pass or fail).
    Run Keyword If Test Failed    Capture Page Screenshot    ${SCREENSHOT_DIR}${/}FAIL_{TEST_NAME}_{index}.png

# ============================================================
# COMMON WAIT KEYWORDS
# ============================================================

Wait Until Page Is Loaded
    [Documentation]    Waits until page body is visible (generic page load wait).
    Wait Until Element Is Visible    css=body    timeout=${TIMEOUT}

Wait And Click Element
    [Documentation]    Waits for element to be visible then clicks it.
    ...                Falls back to JavaScript click if regular click is intercepted.
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    timeout=${TIMEOUT}
    ${status}=    Run Keyword And Return Status    Click Element    ${locator}
    Run Keyword If    not ${status}    JS Click Element    ${locator}

Wait And Input Text
    [Documentation]    Waits for element to be visible then inputs text.
    ...                For Angular reactive forms, uses focus + clear + type approach.
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}    timeout=${TIMEOUT}
    Click Element    ${locator}
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}

Wait For Element Visible
    [Documentation]    Waits until the specified element is visible on page.
    [Arguments]    ${locator}    ${timeout}=${TIMEOUT}
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}

Wait For Element Not Visible
    [Documentation]    Waits until the specified element disappears.
    [Arguments]    ${locator}    ${timeout}=${TIMEOUT}
    Wait Until Element Is Not Visible    ${locator}    timeout=${timeout}

# ============================================================
# ANGULAR-SPECIFIC HELPER KEYWORDS
# ============================================================

JS Click Element
    [Documentation]    Clicks an element using JavaScript (bypasses overlays).
    [Arguments]    ${locator}
    ${element}=    Get WebElement    ${locator}
    Execute JavaScript    arguments[0].click();    ARGUMENTS    ${element}

JS Input Text
    [Documentation]    Sets input value via JavaScript with Angular event dispatch.
    ...                Useful when Angular reactive form bindings don't detect Input Text.
    [Arguments]    ${locator}    ${text}
    ${element}=    Get WebElement    ${locator}
    Execute JavaScript
    ...    var el = arguments[0];
    ...    var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    ...    nativeSetter.call(el, arguments[1]);
    ...    el.dispatchEvent(new Event('input', {bubbles: true}));
    ...    el.dispatchEvent(new Event('change', {bubbles: true}));
    ...    ARGUMENTS    ${element}    ${text}

Remove Element By Selector
    [Documentation]    Removes a DOM element by CSS selector (useful for overlays).
    [Arguments]    ${css_selector}
    Execute JavaScript
    ...    var el = document.querySelector(arguments[0]);
    ...    if (el) el.remove();
    ...    ARGUMENTS    ${css_selector}

Hide Element By Selector
    [Documentation]    Hides a DOM element by CSS selector.
    [Arguments]    ${css_selector}
    Execute JavaScript
    ...    var el = document.querySelector(arguments[0]);
    ...    if (el) el.style.display = 'none';
    ...    ARGUMENTS    ${css_selector}

Wait For Angular
    [Documentation]    Waits briefly for Angular change detection to complete.
    Sleep    1s

# ============================================================
# COMMON VERIFICATION KEYWORDS
# ============================================================

Verify Page Title Contains
    [Documentation]    Verifies the browser page title contains expected text.
    [Arguments]    ${expected_title}
    ${title}=    Get Title
    Should Contain    ${title}    ${expected_title}    ignore_case=True

Verify Element Text
    [Documentation]    Verifies an element's text matches expected value.
    [Arguments]    ${locator}    ${expected_text}
    Wait Until Element Is Visible    ${locator}    timeout=${TIMEOUT}
    ${actual_text}=    Get Text    ${locator}
    Should Contain    ${actual_text}    ${expected_text}

Verify Element Is Displayed
    [Documentation]    Verifies that the given element is visible on page.
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    timeout=${TIMEOUT}
    Element Should Be Visible    ${locator}

Verify Element Is Not Displayed
    [Documentation]    Verifies that the given element is NOT visible.
    [Arguments]    ${locator}
    Element Should Not Be Visible    ${locator}

Verify URL Contains
    [Documentation]    Verifies current URL contains the expected substring.
    [Arguments]    ${expected_url_part}
    ${current_url}=    Get Location
    Should Contain    ${current_url}    ${expected_url_part}

Get Element Count On Page
    [Documentation]    Returns the number of elements matching the locator.
    [Arguments]    ${locator}
    ${count}=    Get Element Count    ${locator}
    RETURN    ${count}

# ============================================================
# COMMON NAVIGATION KEYWORDS
# ============================================================

Navigate To URL
    [Documentation]    Navigates to the specified URL and waits for load.
    [Arguments]    ${url}
    Go To    ${url}
    Wait Until Page Is Loaded

Navigate To Login Page
    [Documentation]    Navigates to the login page.
    Navigate To URL    ${LOGIN_URL}

Navigate To Cart Page
    [Documentation]    Navigates to the cart page.
    Navigate To URL    ${CART_URL}

Navigate To Checkout Page
    [Documentation]    Navigates to the checkout page.
    Navigate To URL    ${CHECKOUT_URL}

# ============================================================
# SCREENSHOT UTILITY
# ============================================================

Take Screenshot With Name
    [Documentation]    Captures screenshot with a custom name for reporting.
    [Arguments]    ${name}
    Capture Page Screenshot    ${SCREENSHOT_DIR}${/}${name}_{index}.png
