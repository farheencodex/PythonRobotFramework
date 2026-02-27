*** Settings ***
# ============================================================
# Homepage UI Test Suite
# Module: HOMEPAGE
# Assignment 1 Test Cases: TC_001, TC_002, TC_003, TC_004,
#                          TC_007, TC_009, TC_010
# Test Scenarios: TS_001, TS_002, TS_004, TS_005
# ============================================================
Documentation     Homepage UI Tests for Boodmo (https://boodmo.com)
...               Validates homepage load, logo, title, search bar,
...               categories, header nav, and footer links.
...               Environment: ${ENVIRONMENT}

Resource          ${CURDIR}${/}..${/}..${/}resources${/}keywords${/}ui_keywords.robot

Suite Setup       Open Browser To Boodmo
Suite Teardown    Close Browser Session
Test Setup        Start Test
Test Teardown     End Test

Force Tags        ui    homepage
Default Tags      regression


*** Test Cases ***

# ----------------------------------------------------------
# TC_001 | TS_001 | Verify homepage loads successfully
# ----------------------------------------------------------
Verify Homepage Loads Successfully
    [Documentation]    TC_001 (TS_001): Open browser, navigate to boodmo.com.
    ...                Homepage loads within 5 seconds with all UI components visible.
    [Tags]    TC_001    TS_001    smoke    P0    functional
    Verify Homepage Is Loaded Successfully
    Take Screenshot With Name    TC_001_homepage_loaded

# ----------------------------------------------------------
# TC_002 | TS_001 | Verify logo is displayed on homepage
# ----------------------------------------------------------
Verify Boodmo Logo Is Visible On Homepage
    [Documentation]    TC_002 (TS_001): Open homepage.
    ...                Boodmo logo is visible in the header.
    [Tags]    TC_002    TS_001    regression    P1    ui_check
    Verify Boodmo Logo Is Displayed
    Take Screenshot With Name    TC_002_logo_visible

# ----------------------------------------------------------
# TC_003 | TS_001 | Verify homepage title in browser tab
# ----------------------------------------------------------
Verify Homepage Title In Browser Tab
    [Documentation]    TC_003 (TS_001): Open homepage.
    ...                Browser tab shows correct title containing "boodmo".
    [Tags]    TC_003    TS_001    regression    P2    ui_check
    Verify Homepage Title In Browser Tab
    Take Screenshot With Name    TC_003_page_title

# ----------------------------------------------------------
# TC_004 | TS_002 | Verify search bar is present and active
# ----------------------------------------------------------
Verify Search Bar Is Present And Clickable
    [Documentation]    TC_004 (TS_002): Open homepage. Observe search bar.
    ...                Search bar is visible with placeholder text and is clickable.
    [Tags]    TC_004    TS_002    smoke    P0    functional
    Verify Search Bar Is Present And Active
    Take Screenshot With Name    TC_004_search_bar

# ----------------------------------------------------------
# TC_007 | TS_004 | Verify "Popular Categories" section loads
# ----------------------------------------------------------
Verify Popular Categories Section Is Displayed
    [Documentation]    TC_007 (TS_004): Open homepage, scroll to categories section.
    ...                Categories like Engine, Brakes, Filters etc. are displayed.
    [Tags]    TC_007    TS_004    regression    P1    functional
    Verify Popular Categories Section Loads
    Take Screenshot With Name    TC_007_categories

# ----------------------------------------------------------
# TC_009 | TS_005 | Verify all header navigation links work
# ----------------------------------------------------------
Verify Header Navigation Links Are Functional
    [Documentation]    TC_009 (TS_005): Open homepage, click each nav link.
    ...                All links navigate to the respective pages without 404 errors.
    [Tags]    TC_009    TS_005    regression    P1    functional
    Verify Header Navigation Links
    Take Screenshot With Name    TC_009_header_nav

# ----------------------------------------------------------
# TC_010 | TS_005 | Verify footer links are not broken
# ----------------------------------------------------------
Verify Footer Links Are Not Broken
    [Documentation]    TC_010 (TS_005): Open homepage, scroll to footer,
    ...                click each footer link. All footer links navigate correctly.
    [Tags]    TC_010    TS_005    regression    P1    functional
    Verify Footer Links Are Present
    Take Screenshot With Name    TC_010_footer_links
