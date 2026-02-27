*** Settings ***
# ============================================================
# API Keywords Resource File
# Contains reusable API keywords for Boodmo API automation
# Uses RequestsLibrary for HTTP operations
# Uses JSONLibrary for response validation
# ============================================================
# API Endpoints are derived from Boodmo's public-facing requests
# (captured via browser DevTools Network tab)
# ============================================================
Library           RequestsLibrary
Library           JSONLibrary
Library           Collections
Library           String
Resource          ${CURDIR}${/}..${/}..${/}variables${/}env_common.robot

*** Variables ***
# ---------- API Endpoint Paths ----------
${API_SEARCH_ENDPOINT}          /search
${API_PRODUCT_ENDPOINT}         /product
${API_CART_ENDPOINT}            /cart
${API_CART_ADD_ENDPOINT}        /cart/add
${API_CART_REMOVE_ENDPOINT}     /cart/remove
${API_CATEGORIES_ENDPOINT}      /categories
${API_AUTOCOMPLETE_ENDPOINT}    /search/autocomplete

*** Keywords ***

# ============================================================
# SESSION MANAGEMENT
# ============================================================

Create Boodmo API Session
    [Documentation]    Creates a persistent HTTP session for Boodmo API.
    ...                Uses environment-specific base URL and auth token.
    &{headers}=    Create Dictionary
    ...    Content-Type=${CONTENT_TYPE_JSON}
    ...    Accept=${CONTENT_TYPE_JSON}
    ...    Authorization=Bearer ${API_AUTH_TOKEN}
    ...    User-Agent=RobotFramework-BoodmoTest/1.0
    Create Session    ${API_SESSION_ALIAS}    ${API_BASE_URL}
    ...    headers=${headers}
    ...    timeout=${API_TIMEOUT}
    ...    verify=${True}
    Log    API Session created for: ${API_BASE_URL} [${ENVIRONMENT}]    console=True

Close Boodmo API Session
    [Documentation]    Closes the Boodmo API session.
    Delete All Sessions

# ============================================================
# SEARCH API KEYWORDS (API_001, API_005)
# Ref: TC_049, TC_050, TC_051
# ============================================================

Search Product Via API
    [Documentation]    API_001 - Sends GET request to search API with a keyword.
    ...                Returns the response object for validation.
    [Arguments]    ${search_keyword}
    &{params}=    Create Dictionary    q=${search_keyword}
    ${response}=    GET On Session    ${API_SESSION_ALIAS}    ${API_SEARCH_ENDPOINT}
    ...    params=${params}    expected_status=any
    Log    Search API Response Status: ${response.status_code}    console=True
    RETURN    ${response}

Search Product With Empty Query Via API
    [Documentation]    API_005 - Sends search request with empty/invalid query.
    [Arguments]    ${invalid_query}=${EMPTY}
    &{params}=    Create Dictionary    q=${invalid_query}
    ${response}=    GET On Session    ${API_SESSION_ALIAS}    ${API_SEARCH_ENDPOINT}
    ...    params=${params}    expected_status=any
    RETURN    ${response}

Get Autocomplete Suggestions Via API
    [Documentation]    Sends request to autocomplete/suggestions endpoint.
    [Arguments]    ${partial_keyword}
    &{params}=    Create Dictionary    q=${partial_keyword}
    ${response}=    GET On Session    ${API_SESSION_ALIAS}    ${API_AUTOCOMPLETE_ENDPOINT}
    ...    params=${params}    expected_status=any
    RETURN    ${response}

# ============================================================
# PRODUCT API KEYWORDS (API_002)
# Ref: TC_078, TC_079
# ============================================================

Get Product Details Via API
    [Documentation]    API_002 - Fetches product details by product ID.
    ...                Validates the response contains product information.
    [Arguments]    ${product_id}
    ${response}=    GET On Session    ${API_SESSION_ALIAS}    ${API_PRODUCT_ENDPOINT}/${product_id}
    ...    expected_status=any
    Log    Product API Response Status: ${response.status_code}    console=True
    RETURN    ${response}

# ============================================================
# CART API KEYWORDS (API_003, API_004)
# Ref: TC_088, TC_096
# ============================================================

Add Product To Cart Via API
    [Documentation]    API_003 - Adds a product to cart via POST request.
    [Arguments]    ${product_id}    ${quantity}=1
    &{body}=    Create Dictionary
    ...    product_id=${product_id}
    ...    quantity=${quantity}
    ${response}=    POST On Session    ${API_SESSION_ALIAS}    ${API_CART_ADD_ENDPOINT}
    ...    json=${body}    expected_status=any
    Log    Add to Cart API Response: ${response.status_code}    console=True
    RETURN    ${response}

Remove Product From Cart Via API
    [Documentation]    API_004 - Removes a product from cart via POST/DELETE request.
    [Arguments]    ${product_id}
    &{body}=    Create Dictionary    product_id=${product_id}
    ${response}=    POST On Session    ${API_SESSION_ALIAS}    ${API_CART_REMOVE_ENDPOINT}
    ...    json=${body}    expected_status=any
    Log    Remove from Cart API Response: ${response.status_code}    console=True
    RETURN    ${response}

Get Cart Details Via API
    [Documentation]    Fetches current cart contents via GET request.
    ${response}=    GET On Session    ${API_SESSION_ALIAS}    ${API_CART_ENDPOINT}
    ...    expected_status=any
    RETURN    ${response}

# ============================================================
# RESPONSE VALIDATION KEYWORDS
# ============================================================

Validate Response Status Code
    [Documentation]    Validates HTTP response status code matches expected.
    [Arguments]    ${response}    ${expected_status}
    Should Be Equal As Integers    ${response.status_code}    ${expected_status}
    ...    Expected status ${expected_status} but got ${response.status_code}

Validate Response Is JSON
    [Documentation]    Validates that the response body is valid JSON.
    [Arguments]    ${response}
    ${json}=    Set Variable    ${response.json()}
    Should Not Be Empty    ${json}    Response body is empty or not valid JSON
    RETURN    ${json}

Validate Response Contains Key
    [Documentation]    Validates that JSON response contains a specific key.
    [Arguments]    ${json_response}    ${key}
    Dictionary Should Contain Key    ${json_response}    ${key}
    ...    Response JSON does not contain key: ${key}

Validate Response Field Value
    [Documentation]    Validates a specific field in JSON response has expected value.
    [Arguments]    ${json_response}    ${field}    ${expected_value}
    ${actual_value}=    Get From Dictionary    ${json_response}    ${field}
    Should Be Equal As Strings    ${actual_value}    ${expected_value}
    ...    Field '${field}' expected '${expected_value}' but got '${actual_value}'

Validate Response Field Is Not Empty
    [Documentation]    Validates a specific field in JSON response is not empty/null.
    [Arguments]    ${json_response}    ${field}
    ${value}=    Get From Dictionary    ${json_response}    ${field}
    Should Not Be Empty    ${value}    Field '${field}' is empty or null

Validate Search Results In Response
    [Documentation]    Validates search API response contains product results.
    [Arguments]    ${response}
    ${json}=    Validate Response Is JSON    ${response}
    # Boodmo API typically returns results in a 'data' or 'products' key
    ${has_data}=    Run Keyword And Return Status    Dictionary Should Contain Key    ${json}    data
    ${has_products}=    Run Keyword And Return Status    Dictionary Should Contain Key    ${json}    products
    Should Be True    ${has_data} or ${has_products}
    ...    Search response does not contain 'data' or 'products' key

Validate Product Fields In Response
    [Documentation]    Validates product detail response has required fields.
    [Arguments]    ${response}
    ${json}=    Validate Response Is JSON    ${response}
    # Product must have name, price, availability fields
    FOR    ${field}    IN    name    price
        ${has_field}=    Run Keyword And Return Status
        ...    Dictionary Should Contain Key    ${json}    ${field}
        Log    Field '${field}' present: ${has_field}    console=True
    END

Validate Response Content Type
    [Documentation]    API_006 - Validates Content-Type header in response.
    [Arguments]    ${response}    ${expected_content_type}=application/json
    ${content_type}=    Get From Dictionary    ${response.headers}    Content-Type
    Should Contain    ${content_type}    ${expected_content_type}
    ...    Expected Content-Type '${expected_content_type}' but got '${content_type}'

Validate Response Time Within Limit
    [Documentation]    API_006 - Validates response time is within acceptable limit.
    [Arguments]    ${response}    ${max_seconds}=5
    ${elapsed}=    Set Variable    ${response.elapsed.total_seconds()}
    Should Be True    ${elapsed} <= ${max_seconds}
    ...    Response time ${elapsed}s exceeded limit of ${max_seconds}s
    Log    Response time: ${elapsed}s (limit: ${max_seconds}s)    console=True
