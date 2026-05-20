from pages.login_page import LoginPage

#Test-Case-7 : Verify Forgot Password link functionality
def test_forgot_password_link(setup):

    driver = setup

    login_page = LoginPage(driver)

    login_page.click_forgot_password()

    login_page.reset_password("Admin")

    assert "login" in driver.current_url