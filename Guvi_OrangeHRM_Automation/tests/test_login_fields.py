from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Test-Case-3 : Validate presence of login fields
def test_login_fields_visible(setup):

    driver = setup

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    login_page = LoginPage(driver)

    assert login_page.are_login_fields_visible()