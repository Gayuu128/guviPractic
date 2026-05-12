*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To Login Page
    [Documentation]    Opens browser and navigates to application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Enter Username
    [Arguments]    ${username}
    Input Text    id:username    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    id:password    ${password}

Click Login Button
    Click Button    xpath://button[@type='submit']

Verify Login Successful
    [Documentation]    Checks dashboard element after login
    Page Should Contain Element    xpath=//button[contains(text(),'Log out')]

Logout From Application
    [Documentation]    Logs out from application
    Click Button    xpath://button[@id='logout']
    Page Should Contain Element   xpath://button[@type='submit']
    Close Browser