
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from zenlogin import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.zenclass.in/login")
    yield driver
    driver.quit()

# Positive Test Case - Successful Login
def test_successful_login(setup):

    driver = setup
    page = LoginPage(driver)

    page.enter_username("valid_email.com")
    page.enter_password("valid_paswword")

    page.click_login()

    # Wait 10 seconds to observe
    WebDriverWait(driver, 20).until(
        lambda d: d.current_url != "https://www.zenclass.in/login"
    )

    assert "dashboard"  in driver.current_url.lower()

# Negative Test Case - Invalid Login
def test_invalid_login(setup):

    driver = setup
    page = LoginPage(driver)

    page.enter_username("invalid_user")
    page.enter_password("invalid_pass")

    page.click_login()

    WebDriverWait(driver, 20).until(
        lambda d: "login" in d.current_url.lower()
    )

    assert "login" in driver.current_url.lower()


# Validate Input Fields
def test_input_fields(setup):

    driver = setup
    page = LoginPage(driver)

    page.enter_username("valid_email.com")
    page.enter_password("valid_paswword")

    username_value = driver.find_element(
        *page.username_input
    ).get_attribute("value")

    password_value = driver.find_element(
        *page.password_input
    ).get_attribute("value")

    assert username_value == "valid_email.com"
    assert password_value == "valid_paswword"


# Validate Submit Button
def test_submit_button(setup):

    driver = setup
    page = LoginPage(driver)

    page.enter_username("valid_email.com")
    page.enter_password("valid_paswword")

    page.click_login()


    WebDriverWait(driver, 20).until(
        lambda d: d.current_url != "https://www.zenclass.in/login"
    )

    assert driver.current_url != "https://www.zenclass.in/login"


# Logout Test
def test_logout(setup):

    driver = setup
    page = LoginPage(driver)


    page.enter_username("valid_email.com")
    page.enter_password("valid_paswword")

    page.click_login()

    WebDriverWait(driver, 20).until(
        lambda d: d.current_url != "https://www.zenclass.in/login"
    )

    # Open profile menu
    page.open_profile_menu()


    # Click logout
    page.click_logout()

    WebDriverWait(driver, 20).until(
        lambda d: "login" in d.current_url.lower()
    )

    assert "login" in driver.current_url.lower()

