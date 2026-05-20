import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "success"),
    ("problem_user", "secret_sauce", "success"),
    ("performance_glitch_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "fail"),
])

# Test Case 1 : Verify successful login with valid credentials
def test_login_with_predefined_users(setup, username, password, expected):

    driver = setup
    login = LoginPage(driver)

    login.login(username, password)

    if expected == "success":
        assert "inventory" in driver.current_url
    else:
        assert "locked out" in login.get_error_message().lower()