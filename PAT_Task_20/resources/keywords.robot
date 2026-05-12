*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To Login Page
    [Documentation]    Opens Sauce Demo login page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Login With Credentials
    [Arguments]    ${username}    ${password}
    [Documentation]    Enters username and password and logs in
    Input Text    id:user-name    ${username}
    Input Text    id:password     ${password}
    Click Button   id:login-button

Verify Products Page Loaded
    [Documentation]    Verifies user is on products page
    Page Should Contain    Products

Verify Login Error Message
    [Documentation]    Checks invalid login error
    Page Should Contain Element    css:h3[data-test='error']

Add Product To Cart
    [Arguments]    ${product_id}
    Click Button    id:${product_id}

Open Cart
    Click Element    css:a.shopping_cart_link

Verify Product In Cart
    [Arguments]    ${product_name}
    Page Should Contain    ${product_name}

Proceed To Checkout
    Click Button    id:checkout

Close Browser Session
    Close Browser