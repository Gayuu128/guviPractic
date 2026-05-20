from pages.login_page import LoginPage

# Test Case 2 : Attempt to login using incorrect username and password
def test_invalid_login(setup):

    driver = setup
    login = LoginPage(driver)

    login.login("wrong_user", "wrong_password")

    error = login.get_error_message()

    assert "epic sadface" in error.lower()