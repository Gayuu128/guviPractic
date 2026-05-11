
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators (Update based on your Zen Portal)
    username_input = (By.XPATH, "//input[@id=':r1:']")
    password_input = (By.XPATH, "//input[@id=':r2:']")
    login_button = (By.XPATH, "//button[@type='submit']")
    logout_button = (By.XPATH, "//div[text()='Log out']")
    profile_icon = (By.XPATH, "//p[contains(@class,'avatar-profile-name')]")

    # Actions
    def enter_username(self, username):

        username_field = self.wait.until(
            EC.presence_of_element_located(self.username_input)
        )

        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.presence_of_element_located(self.password_input)
        )

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):

        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )

        # Scroll to button
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            login_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

    def is_login_successful(self):

        try:

            WebDriverWait(self.driver, 20).until(
                EC.url_changes("https://www.zenclass.in/login")
            )

            return True

        except:
            return False

    def open_profile_menu(self):

        profile = self.wait.until(
            EC.element_to_be_clickable(self.profile_icon)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            profile
        )

    def click_logout(self):

        logout_btn = self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_btn
        )