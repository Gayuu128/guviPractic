*** Settings ***
Library           SeleniumLibrary
Resource          ../resources/keywords.robot
Resource          ../variables/config.robot

*** Test Cases ***
Verify User Can Login And Logout Successfully
    [Documentation]    Test to verify login and logout functionality

    Open Browser To Login Page
    Enter Username    ${USERNAME}
    Enter Password    ${PASSWORD}
    Click Login Button
    Verify Login Successful
    Logout From Application