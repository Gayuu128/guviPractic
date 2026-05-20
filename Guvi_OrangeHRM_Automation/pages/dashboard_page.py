from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
    profile_dropdown = (By.CLASS_NAME, "oxd-userdropdown-name")
    logout_button = (By.XPATH, "//a[text()='Logout']")

    menu_items = {
        "Admin": (By.XPATH, "//span[text()='Admin']"),
        "PIM": (By.XPATH, "//span[text()='PIM']"),
        "Leave": (By.XPATH, "//span[text()='Leave']"),
        "Time": (By.XPATH, "//span[text()='Time']"),
        "Recruitment": (By.XPATH, "//span[text()='Recruitment']"),
        "My Info": (By.XPATH, "//span[text()='My Info']"),
        "Performance": (By.XPATH, "//span[text()='Performance']"),
        "Dashboard": (By.XPATH, "//span[text()='Dashboard']"),
        "Claim": (By.XPATH, "//span[text()='Claim']")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_dashboard_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.dashboard_header)
            ).is_displayed()
        except Exception:
            return False

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.profile_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    def is_menu_visible_and_clickable(self, menu_name):
        element = self.wait.until(
            EC.element_to_be_clickable(self.menu_items[menu_name])
        )
        return element.is_displayed() and element.is_enabled()

    def click_menu(self, menu_name):
        self.wait.until(
            EC.element_to_be_clickable(self.menu_items[menu_name])
        ).click()