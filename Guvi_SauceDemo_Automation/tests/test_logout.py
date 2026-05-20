from pages.login_page import LoginPage
from pages.menu_page import MenuPage

# Test Case 3 : Verify that user can successfully logout after login
def test_logout_functionality(setup):

    driver = setup
    login = LoginPage(driver)
    menu = MenuPage(driver)

    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    menu.logout()

    assert login.is_login_page_displayed()