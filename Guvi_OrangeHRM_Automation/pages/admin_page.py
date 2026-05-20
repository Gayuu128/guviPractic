from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    add_button = (By.XPATH, "//button[contains(.,'Add')]")
    username_search = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    search_button = (By.XPATH, "//button[@type='submit']")
    result_record = (By.XPATH, "//div[@class='oxd-table-card']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add_user(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def search_user(self, username):
        field = self.wait.until(
            EC.visibility_of_element_located(self.username_search)
        )
        field.clear()
        field.send_keys(username)

        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def is_user_found(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.result_record)
            ).is_displayed()
        except Exception:
            return False