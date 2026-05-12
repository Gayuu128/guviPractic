*** Settings ***
Resource    ../resources/keywords.robot
Resource    ../variables/config.robot

*** Test Cases ***
TC3 - Add Single Product To Cart
    [Documentation]    Verify user can add a product and it appears in cart

    Open Browser To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Verify Products Page Loaded

    Add Product To Cart    add-to-cart-sauce-labs-backpack
    Open Cart
    Verify Product In Cart    Sauce Labs Backpack

    Close Browser Session


TC4 - Add Multiple Products And Checkout
    [Documentation]    Verify multiple products are added and checkout summary is correct

    Open Browser To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Verify Products Page Loaded

    Add Product To Cart    add-to-cart-sauce-labs-backpack
    Add Product To Cart    add-to-cart-sauce-labs-bike-light

    Open Cart
    Verify Product In Cart    Sauce Labs Backpack
    Verify Product In Cart    Sauce Labs Bike Light

    Proceed To Checkout
    Page Should Contain    Checkout: Your Information

    Close Browser Session