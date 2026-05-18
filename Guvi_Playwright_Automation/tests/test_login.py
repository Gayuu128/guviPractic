from pages.login_page import LoginPage

from utils.test_data import TestData

# Test Case 6 : Verify login functionality with valid credentials.
def test_valid_login(browser_setup):


    page=browser_setup

    page.goto(
        "https://www.guvi.in/sign-in/"
    )


    login=LoginPage(page)

    login.login(
        TestData.VALID_EMAIL,
        TestData.VALID_PASSWORD
    )

    page.wait_for_selector(login.COURSES)

    assert login.is_visible(
        login.COURSES
     or
        "Courses" in page.title())


# Test Case 7 : Verify login functionality with invalid credentials.
def test_invalid_login(browser_setup):


    page=browser_setup

    page.goto(
        "https://www.guvi.in/sign-in/"
    )

    login=LoginPage(page)

    login.login(
        TestData.INVALID_EMAIL,
        TestData.INVALID_PASSWORD
    )

    assert page.title() == "HCL GUVI | Login"
