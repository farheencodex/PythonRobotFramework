*** Settings ***
# ============================================================
# Locators File - All Web Element Locators
# Centralized locator management for Boodmo UI automation
# NO hardcoded locators in test files - all locators defined here
# ============================================================
# Naming Convention: MODULE_ELEMENT_TYPE
# e.g., HOME_LOGO_IMG, LOGIN_EMAIL_INPUT, CART_REMOVE_BTN
# ============================================================
# NOTE: Boodmo is an Angular SPA. Selectors use Angular-specific
# attributes like formcontrolname, ng-star-inserted, etc.
# ============================================================

*** Variables ***

# ========================================
# HOMEPAGE LOCATORS
# Ref: TC_001 - TC_012
# ========================================
${HOME_LOGO_IMG}                    css=img.header-logo__images
${HOME_LOGO_LINK}                   css=a.header-logo
${HOME_SEARCH_INPUT}                css=input.search-form__filed__control
${HOME_SEARCH_BTN}                  css=button.search-form__button__search
${HOME_SEARCH_FORM}                 css=form.search-form
${HOME_SEARCH_OVERLAY}              css=div.search-placeholder__body
${HOME_BANNER_SLIDER}               css=div.home-slider
${HOME_POPULAR_CATEGORIES}          css=section.search-by-category
${HOME_CATEGORY_LINKS}              css=section.search-by-category a
${HOME_CATALOG_LIST}                css=div.catalog-list
${HOME_HEADER_USER}                 css=div.header__user
${HOME_SIGN_IN_BTN}                 css=span.btn-border
${HOME_HEADER_MENU_BTN}             css=span.header-button-menu
${HOME_FOOTER}                      css=footer
${HOME_FOOTER_LINKS}                css=footer a
${HOME_FOOTER_NAV}                  css=ul.footer-nav__menu
${HOME_NUMBER_PLATE_INPUT}          css=input.number-plate__control
${HOME_VEHICLE_MAKE_SELECTOR}       css=div.search-vehicle-form
${HOME_PAGE_TITLE}                  boodmo

# ========================================
# LOGIN PAGE LOCATORS (/u/signin/)
# Ref: TC_013 - TC_027
# Boodmo uses email-first login:
#   Step 1: Enter email + click Continue
#   Step 2: Enter password (appears after email validation)
# ========================================
${LOGIN_BTN_HEADER}                 css=span.btn-border
${LOGIN_PAGE_CONTAINER}             css=div.authorization
${LOGIN_FORM_CONTAINER}             css=ngx-signin-form.authorization__form
${LOGIN_TITLE}                      css=h3.signin-form__title
${LOGIN_EMAIL_DESC}                 css=div.signin-email__desc
${LOGIN_EMAIL_INPUT}                css=input[formcontrolname='username']
${LOGIN_CONTINUE_BTN}              css=button.btn.btn-block
${LOGIN_PASSWORD_INPUT}             css=input[formcontrolname='password']
${LOGIN_SUBMIT_BTN}                 css=button.btn.btn-block
${LOGIN_ERROR_MSG}                  css=div.form-error
${LOGIN_FORGOT_PWD_LINK}            css=span.signin-email__link
${LOGIN_SHOW_PWD_TOGGLE}            css=button.toggle-password
${LOGIN_SUCCESS_INDICATOR}          css=div.header__user span.user-name
${LOGIN_INFO_TITLE}                 css=p.authorization__info__title
${LOGIN_INFO_DESC}                  css=p.authorization__info__desc

# ========================================
# SIGNUP / REGISTRATION LOCATORS
# Ref: TC_028 - TC_043
# ========================================
${SIGNUP_LINK}                      css=a[href*='signup']
${SIGNUP_NAME_INPUT}                css=input[formcontrolname='name']
${SIGNUP_EMAIL_INPUT}               css=input[formcontrolname='email']
${SIGNUP_PHONE_INPUT}               css=input[formcontrolname='phone']
${SIGNUP_PASSWORD_INPUT}            css=input[formcontrolname='password']
${SIGNUP_CONFIRM_PASSWORD_INPUT}    css=input[formcontrolname='confirmPassword']
${SIGNUP_SUBMIT_BTN}                css=button[type='submit']
${SIGNUP_ERROR_MSG}                 css=ngx-form-control-error
${SIGNUP_SUCCESS_MSG}               css=div.success-message

# ========================================
# SEARCH RESULTS LOCATORS
# Ref: TC_044 - TC_056
# Boodmo search: type in search bar, submit form.
# Results page may show catalog items or product cards.
# ========================================
${SEARCH_VEHICLE_FORM}              css=form.search-vehicle-form
${SEARCH_MAKE_DROPDOWN}             css=div.search-vehicle-form select
${SEARCH_NUMBER_PLATE_INPUT}        css=input[formcontrolname='number']
${SEARCH_RESULTS_CONTAINER}         css=div.catalog-list
${SEARCH_RESULT_ITEMS}              css=div.catalog-list a
${SEARCH_NO_RESULTS_MSG}            css=div.not-found
${SEARCH_AUTOCOMPLETE_DROPDOWN}     css=div[class*='autocomplete']
${SEARCH_AUTOCOMPLETE_ITEMS}        css=div[class*='autocomplete'] a

# ========================================
# FILTER & SORTING LOCATORS
# Ref: TC_057 - TC_070
# ========================================
${FILTER_SIDEBAR}                   css=div[class*='filter']
${FILTER_BRAND_OPTIONS}             css=div[class*='filter'] input[type='checkbox']
${FILTER_PRICE_MIN_INPUT}           css=input[formcontrolname='priceFrom']
${FILTER_PRICE_MAX_INPUT}           css=input[formcontrolname='priceTo']
${FILTER_APPLY_BTN}                 css=button[class*='filter']
${FILTER_CLEAR_ALL_BTN}             css=button[class*='reset']
${SORT_DROPDOWN}                    css=select[class*='sort']

# ========================================
# PRODUCT DETAIL PAGE LOCATORS
# Ref: TC_078 - TC_087
# ========================================
${PDP_PRODUCT_NAME}                 css=h1[class*='product']
${PDP_PRODUCT_PRICE}                css=span[class*='price']
${PDP_PRODUCT_BRAND}                css=span[class*='brand']
${PDP_PART_NUMBER}                  css=span[class*='part-number']
${PDP_ADD_TO_CART_BTN}              css=button[class*='add-to-cart']
${PDP_PRODUCT_IMAGE}                css=img[class*='product']
${PDP_COMPATIBILITY_CHECK}          css=div[class*='compatibility']
${PDP_ALTERNATE_PARTS}              css=div[class*='alternate']
${PDP_SELLER_INFO}                  css=div[class*='seller']
${PDP_BREADCRUMB}                   css=div[class*='breadcrumb']
${PDP_OUT_OF_STOCK_LABEL}           css=div[class*='out-of-stock']

# ========================================
# CART PAGE LOCATORS
# Ref: TC_088 - TC_102
# ========================================
${CART_ICON}                        css=a[href*='cart']
${CART_ITEM_COUNT}                  css=span[class*='cart-count']
${CART_ITEMS_LIST}                  css=div[class*='cart-item']
${CART_ITEM_QTY_INCREASE}          css=button[class*='qty-plus']
${CART_ITEM_QTY_DECREASE}          css=button[class*='qty-minus']
${CART_ITEM_QTY_INPUT}             css=input[class*='quantity']
${CART_REMOVE_ITEM_BTN}            css=button[class*='remove']
${CART_TOTAL_PRICE}                css=div[class*='total']
${CART_SHIPPING_CHARGES}           css=div[class*='shipping']
${CART_EMPTY_MSG}                  css=div[class*='empty-cart']
${CART_CONTINUE_SHOPPING_LINK}     css=a[class*='continue-shopping']
${CART_PROCEED_CHECKOUT_BTN}       css=button[class*='checkout']

# ========================================
# CHECKOUT PAGE LOCATORS
# Ref: TC_103 - TC_115
# ========================================
${CHECKOUT_SAVED_ADDRESS}           css=div[class*='address-card']
${CHECKOUT_ADD_NEW_ADDRESS_BTN}     css=button[class*='new-address']
${CHECKOUT_ADDRESS_NAME}            css=input[formcontrolname='name']
${CHECKOUT_ADDRESS_LINE1}           css=input[formcontrolname='address']
${CHECKOUT_ADDRESS_CITY}            css=input[formcontrolname='city']
${CHECKOUT_ADDRESS_STATE}           css=input[formcontrolname='state']
${CHECKOUT_ADDRESS_PINCODE}         css=input[formcontrolname='pincode']
${CHECKOUT_ADDRESS_PHONE}           css=input[formcontrolname='phone']
${CHECKOUT_CONTINUE_BTN}            css=button[class*='continue']
${CHECKOUT_ORDER_SUMMARY}           css=div[class*='order-summary']
${CHECKOUT_COUPON_INPUT}            css=input[formcontrolname='coupon']
${CHECKOUT_APPLY_COUPON_BTN}        css=button[class*='apply-coupon']
${CHECKOUT_REMOVE_COUPON_BTN}       css=button[class*='remove-coupon']
${CHECKOUT_COUPON_ERROR_MSG}        css=div[class*='coupon-error']
${CHECKOUT_COUPON_SUCCESS_MSG}      css=div[class*='coupon-success']
