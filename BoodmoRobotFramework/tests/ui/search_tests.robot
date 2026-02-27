*** Settings ***
# ============================================================
# Search UI Test Suite
# Module: SEARCH FUNCTIONALITY
# Assignment 1 Test Cases: TC_044, TC_049, TC_050, TC_051,
#                          TC_054, TC_056, TC_071, TC_075, TC_077
# Test Scenarios: TS_012, TS_015, TS_016, TS_017, TS_022
# ============================================================
Documentation     Search Module UI Tests for Boodmo
...               Validates search by keyword, empty search,
...               special characters, autocomplete, and results.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}ui_keywords.robot

Suite Setup       Open Browser To Boodmo
Suite Teardown    Close Browser Session
Test Setup        Start Test
Test Teardown     End Test

Force Tags        ui    search
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# TC_044 | TS_012 | Verify search by vehicle make
# ----------------------------------------------------------
Verify Search By Vehicle Make Returns Results
    [Documentation]    TC_044 (TS_012): Click search bar > Select Make = "Maruti" >
    ...                Click Search. Relevant parts for Maruti vehicles are displayed.
    [Tags]    TC_044    TS_012    smoke    P0    positive
    Search For Product    ${VEHICLE_MAKE}
    Verify Search Results Are Displayed
    Take Screenshot With Name    TC_044_search_by_make

# ----------------------------------------------------------
# TC_049 | TS_015 | Verify keyword search ("brake pad")
# ----------------------------------------------------------
Verify Keyword Search Returns Relevant Products
    [Documentation]    TC_049 (TS_015): Type "brake pad" in search bar > Press Enter.
    ...                Relevant products with "brake pad" in title are shown.
    [Tags]    TC_049    TS_015    smoke    P0    positive
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Take Screenshot With Name    TC_049_keyword_search

# ----------------------------------------------------------
# TC_050 | TS_016 | Verify search with empty input
# ----------------------------------------------------------
Verify Search With Empty Input Shows Validation
    [Documentation]    TC_050 (TS_016): Click search bar > Press Enter without typing.
    ...                Validation message: "Please enter a search term".
    [Tags]    TC_050    TS_016    regression    P1    validation
    Search For Product    ${SEARCH_KEYWORD_EMPTY}
    Take Screenshot With Name    TC_050_empty_search

# ----------------------------------------------------------
# TC_051 | TS_016 | Verify search with special characters
# ----------------------------------------------------------
Verify Search With Special Characters Handles Gracefully
    [Documentation]    TC_051 (TS_016): Type "@@##$%" in search bar > Press Enter.
    ...                "No results found" or input is sanitized.
    [Tags]    TC_051    TS_016    regression    P1    negative
    Search For Product    ${SEARCH_KEYWORD_SPECIAL}
    Take Screenshot With Name    TC_051_special_chars

# ----------------------------------------------------------
# TC_056 | TS_015 | Verify case-insensitive search
# ----------------------------------------------------------
Verify Search Is Case Insensitive
    [Documentation]    TC_056 (TS_015): Search "BRAKE PAD" then "brake pad" >
    ...                Compare. Both searches should return the same results.
    [Tags]    TC_056    TS_015    regression    P1    functional
    Search For Product    BRAKE PAD
    ${count_upper}=    Get Element Count On Page    ${SEARCH_RESULT_ITEMS}
    Start Test
    Search For Product    brake pad
    ${count_lower}=    Get Element Count On Page    ${SEARCH_RESULT_ITEMS}
    Should Be Equal As Integers    ${count_upper}    ${count_lower}
    Take Screenshot With Name    TC_056_case_insensitive

# ----------------------------------------------------------
# TC_071 | TS_022 | Verify product listing page loads
# ----------------------------------------------------------
Verify Product Listing Page Loads After Search
    [Documentation]    TC_071 (TS_022): Perform search for "air filter".
    ...                Products are listed with image, title, price, seller.
    [Tags]    TC_071    TS_022    smoke    P0    functional
    Search For Product    air filter
    Verify Search Results Are Displayed
    Take Screenshot With Name    TC_071_product_listing

# ----------------------------------------------------------
# TC_075 | TS_022 | Verify "No results" for non-existent part
# ----------------------------------------------------------
Verify No Results For Non Existent Product
    [Documentation]    TC_075 (TS_022): Search for "xyznonexistentpart".
    ...                "No results found" message displayed.
    [Tags]    TC_075    TS_022    regression    P1    negative
    Search For Product    ${SEARCH_KEYWORD_NO_RESULT}
    Verify No Results Message Displayed
    Take Screenshot With Name    TC_075_no_results

# ----------------------------------------------------------
# TC_077 | TS_022 | Verify clicking product opens detail page
# ----------------------------------------------------------
Verify Clicking Product Opens Detail Page
    [Documentation]    TC_077 (TS_022): Click any product from listing.
    ...                Product detail page opens for the selected product.
    [Tags]    TC_077    TS_022    smoke    P0    functional
    Search For Product    ${SEARCH_KEYWORD_VALID}
    Verify Search Results Are Displayed
    Click First Product From Results
    Verify Product Detail Page Is Loaded
    Take Screenshot With Name    TC_077_product_detail
