*** Settings ***
# ============================================================
# Login UI Test Suite
# Module: LOGIN
# Assignment 1 Test Cases: TC_013, TC_014, TC_015, TC_016,
#                          TC_017, TC_018, TC_019, TC_020, TC_023
# Test Scenarios: TS_006, TS_007, TS_008
# ============================================================
Documentation     Login Module UI Tests for Boodmo
...               Validates valid/invalid login, empty fields,
...               forgot password, password masking.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}ui_keywords.robot

Suite Setup       Open Browser To Boodmo
Suite Teardown    Close Browser Session
Test Setup        Start Test
Test Teardown     End Test

Force Tags        ui    login
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# TC_013 | TS_006 | Verify login with valid credentials
# ----------------------------------------------------------
Verify Successful Login With Valid Credentials
    [Documentation]    TC_013 (TS_006): Click Login > Enter registered email >
    ...                Enter correct password > Click Submit.
    ...                User is logged in and redirected to homepage/dashboard.
    [Tags]    TC_013    TS_006    smoke    P0    positive
    Perform Login    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verify Login Successful
    Take Screenshot With Name    TC_013_login_success

# ----------------------------------------------------------
# TC_014 | TS_007 | Verify login with invalid password
# ----------------------------------------------------------
Verify Login Fails With Invalid Password
    [Documentation]    TC_014 (TS_007): Click Login > Enter registered email >
    ...                Enter wrong password > Click Submit.
    ...                Error message: "Invalid credentials. Please try again".
    [Tags]    TC_014    TS_007    smoke    P0    negative
    Perform Login    ${VALID_USERNAME}    ${INVALID_PASSWORD}
    Verify Login Error Message Displayed
    Take Screenshot With Name    TC_014_login_invalid_pwd

# ----------------------------------------------------------
# TC_015 | TS_007 | Verify login with unregistered email
# ----------------------------------------------------------
Verify Login Fails With Unregistered Email
    [Documentation]    TC_015 (TS_007): Click Login > Enter unregistered email >
    ...                Enter any password > Click Submit.
    ...                Error message indicating account not found.
    [Tags]    TC_015    TS_007    smoke    P0    negative
    Perform Login    ${UNREGISTERED_EMAIL}    ${VALID_PASSWORD}
    Verify Login Error Message Displayed
    Take Screenshot With Name    TC_015_login_unregistered

# ----------------------------------------------------------
# TC_016 | TS_007 | Verify login with empty email field
# ----------------------------------------------------------
Verify Login Fails With Empty Email Field
    [Documentation]    TC_016 (TS_007): Click Login > Leave email blank >
    ...                Click Continue. Validation error: "This field is required".
    [Tags]    TC_016    TS_007    regression    P1    validation
    Open Login Page
    Click Login Continue Button
    Verify Login Error Message Displayed
    Take Screenshot With Name    TC_016_login_empty_email

# ----------------------------------------------------------
# TC_017 | TS_007 | Verify login with empty password field
# ----------------------------------------------------------
Verify Login Fails With Empty Password Field
    [Documentation]    TC_017 (TS_007): Click Login > Enter email >
    ...                Click Continue > Leave password blank > Click Submit.
    ...                Validation error: "Password is required".
    [Tags]    TC_017    TS_007    regression    P1    validation
    Open Login Page
    Enter Login Email    ${VALID_USERNAME}
    Click Login Continue Button
    Click Login Submit Button
    Take Screenshot With Name    TC_017_login_empty_pwd

# ----------------------------------------------------------
# TC_018 | TS_007 | Verify login with both fields empty
# ----------------------------------------------------------
Verify Login Fails With Both Fields Empty
    [Documentation]    TC_018 (TS_007): Click Login > Leave email empty >
    ...                Click Continue. Validation error shown for email field.
    [Tags]    TC_018    TS_007    regression    P1    validation
    Open Login Page
    Click Login Continue Button
    Verify Login Error Message Displayed
    Take Screenshot With Name    TC_018_login_both_empty

# ----------------------------------------------------------
# TC_019 | TS_007 | Verify login with invalid email format
# ----------------------------------------------------------
Verify Login Fails With Invalid Email Format
    [Documentation]    TC_019 (TS_007): Click Login > Enter "testuser" in email >
    ...                Click Continue. Validation error: "Please enter a valid email address".
    [Tags]    TC_019    TS_007    regression    P1    validation
    Open Login Page
    Enter Login Email    testuser
    Click Login Continue Button
    Verify Login Error Message Displayed
    Take Screenshot With Name    TC_019_login_invalid_email

# ----------------------------------------------------------
# TC_020 | TS_008 | Verify Forgot Password link is present
# ----------------------------------------------------------
Verify Forgot Password Link Is Visible
    [Documentation]    TC_020 (TS_008): Open Login > Enter valid email > Click Continue.
    ...                "Forgot Password?" link is visible on the password step.
    [Tags]    TC_020    TS_008    regression    P1    ui_check
    Open Login Page
    Enter Login Email    ${REGISTERED_TEST_EMAIL}
    Click Login Continue Button
    Verify Forgot Password Link Is Present
    Take Screenshot With Name    TC_020_forgot_pwd_link

# ----------------------------------------------------------
# TC_023 | TS_007 | Verify password is masked (not visible)
# ----------------------------------------------------------
Verify Password Field Is Masked On Login Page
    [Documentation]    TC_023 (TS_007): Open Login > Enter valid email > Click Continue.
    ...                Password field type is 'password' (characters masked).
    [Tags]    TC_023    TS_007    regression    P1    security
    Open Login Page
    Enter Login Email    ${REGISTERED_TEST_EMAIL}
    Click Login Continue Button
    Verify Password Field Is Masked
    Take Screenshot With Name    TC_023_password_masked
