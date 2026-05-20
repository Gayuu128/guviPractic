from pages.login_page import LoginPage

from pages.dashboard_page import DashboardPage

from utils.test_data import TestData

# Test Case 10 : Validate logout functionality.
def test_logout(browser_setup):


    page=browser_setup

    page.goto(
        "https://www.guvi.in/sign-in/"
    )

    login=LoginPage(page)

    login.login(
        TestData.VALID_EMAIL,
        TestData.VALID_PASSWORD
    )


    dashboard=DashboardPage(page)

    dashboard.logout()
    page.wait_for_selector(dashboard.LOGIN_BUTTON)


    assert dashboard.is_visible(
        dashboard.LOGIN_BUTTON
    )


