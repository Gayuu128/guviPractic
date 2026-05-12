
*** Settings ***
Resource    ../resources/keywords.robot
Resource    ../variables/config.robot

*** Test Cases ***
TC1 - Login With Valid Credentials
    [Documentation]    Verify user can login with valid credentials and lands on products page

    Open Browser To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASS}
    Verify Products Page Loaded
    Close Browser Session

TC2 - Login With Invalid Credentials
    [Documentation]    Verify error message is shown for invalid login

    Open Browser To Login Page
    Login With Credentials    ${INVALID_USER}    ${INVALID_PASS}
    Verify Login Error Message
    Close Browser Session

