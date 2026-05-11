from zen_login import LoginPage


# Successful Login Test
def test_successful_login(setup):

    page_driver = setup

    page = LoginPage(page_driver)

    page.enter_username("valid_email")

    page.enter_password("invalid_password")

    page.click_login()

    page_driver.wait_for_url(
        "**/dashboard",
        timeout=30000
    )

    assert "dashboard" in page_driver.url.lower()


# Unsuccessful Login Test
def test_unsuccessful_login(setup):

    page_driver = setup

    page = LoginPage(page_driver)

    page.enter_username("invalid_user")

    page.enter_password("invalid_password")

    page.click_login()

    page_driver.wait_for_url(
        "**/login",
        timeout=30000
    )

    assert "login" in page_driver.url.lower()


# Validate Username and Password Input Fields
def test_validate_input_fields(setup):

    page_driver = setup

    page = LoginPage(page_driver)

    page.enter_username("valid_email")

    page.enter_password("invalid_password")

    username_value = page_driver.locator(
        page.username_input
    ).input_value()

    password_value = page_driver.locator(
        page.password_input
    ).input_value()

    assert username_value == "valid_email"

    assert password_value == "invalid_password"


# Validate Submit Button
def test_validate_submit_button(setup):

    page_driver = setup

    page = LoginPage(page_driver)

    page.enter_username("valid_email")

    page.enter_password("invalid_password")

    page.click_login()

    page_driver.wait_for_url(
        "**/dashboard",
        timeout=30000
    )

    assert "dashboard" in page_driver.url.lower()


# Validate Logout Functionality
def test_logout_functionality(setup):

    page_driver = setup

    page = LoginPage(page_driver)

    page.enter_username("valid_email")

    page.enter_password("invalid_password")

    page.click_login()
    page.close_popup()

    page_driver.wait_for_url(
        "**/dashboard",
        timeout=30000
    )


    page.open_profile_menu()

    page.click_logout()

    page_driver.wait_for_url(
        "**/login",
        timeout=30000
    )

    assert "login" in page_driver.url.lower()