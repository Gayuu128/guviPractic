from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    forgot_password_link = (By.XPATH, "//p[contains(@class,'orangehrm-login-forgot-header')]")
    reset_username = (By.NAME, "username")
    reset_button = (By.XPATH, "//button[@type='submit']")
    cancel_button = (By.XPATH, "//button[contains(.,'Cancel')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        field = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_error_message_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.error_message)
            ).is_displayed()
        except Exception:
            return False

    def are_login_fields_visible(self):
        return (
            self.driver.find_element(*self.username_input).is_displayed()
            and self.driver.find_element(*self.password_input).is_displayed()
        )

    def click_forgot_password(self):
        self.wait.until(
            EC.element_to_be_clickable(self.forgot_password_link)
        ).click()

    def reset_password(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.reset_username)
        ).send_keys(username)

        self.wait.until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()


    def is_reset_success_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.reset_success_message)
            ).is_displayed()
        except Exception:
            return False