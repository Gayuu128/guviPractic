from pages.home_page import HomePage
from playwright.sync_api import expect
from utils.test_data import TestData

# Test Case 3 : Verify visibility and clickability of the Login button.
def test_login_button(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()


    assert home.is_visible(
        home.LOGIN_BUTTON
    )

# Test Case 4 : Verify visibility and clickability of the Sign-Up button.
def test_signup_button(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()


    assert home.is_visible(
        home.SIGNUP_BUTTON
    )

# Test Case 5 : Verify navigation to the registration page.
def test_signup_navigation(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()

    home.click_signup()

    expect(page).to_have_title("HCL GUVI | Sign Up")

    assert  TestData.REGISTER_URL in page.url
